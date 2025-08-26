from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from config import supabase
from models import UserRegister, UserLogin, UserResponse, AuthResponse
from typing import Optional
import jwt
from datetime import datetime

security = HTTPBearer()

class AuthService:
    def __init__(self):
        self.supabase = supabase

    async def register_user(self, user_data: UserRegister) -> AuthResponse:
        """Register a new user with Supabase Auth"""
        try:
            # Register user with Supabase Auth
            auth_response = self.supabase.auth.sign_up({
                "email": user_data.email,
                "password": user_data.password,
                "options": {
                    "data": {
                        "full_name": user_data.full_name
                    }
                }
            })
            
            if auth_response.user is None:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Failed to create user"
                )
            
            user = UserResponse(
                id=auth_response.user.id,
                email=auth_response.user.email,
                full_name=user_data.full_name,
                created_at=datetime.fromisoformat(auth_response.user.created_at.replace('Z', '+00:00'))
            )
            
            return AuthResponse(
                access_token=auth_response.session.access_token,
                user=user
            )
            
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Registration failed: {str(e)}"
            )

    async def login_user(self, user_data: UserLogin) -> AuthResponse:
        """Login user with Supabase Auth"""
        try:
            auth_response = self.supabase.auth.sign_in_with_password({
                "email": user_data.email,
                "password": user_data.password
            })
            
            if auth_response.user is None:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid credentials"
                )
            
            user = UserResponse(
                id=auth_response.user.id,
                email=auth_response.user.email,
                full_name=auth_response.user.user_metadata.get("full_name"),
                created_at=datetime.fromisoformat(auth_response.user.created_at.replace('Z', '+00:00'))
            )
            
            return AuthResponse(
                access_token=auth_response.session.access_token,
                user=user
            )
            
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Login failed: {str(e)}"
            )

    async def logout_user(self, token: str) -> dict:
        """Logout user by invalidating the session"""
        try:
            self.supabase.auth.sign_out()
            return {"message": "Successfully logged out"}
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Logout failed: {str(e)}"
            )

    async def get_current_user(self, credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
        """Get current user from JWT token"""
        try:
            # Set the session with the provided token
            self.supabase.auth.set_session(credentials.credentials, "")
            
            # Get the current user
            user_response = self.supabase.auth.get_user()
            
            if user_response.user is None:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid or expired token"
                )
            
            return {
                "id": user_response.user.id,
                "email": user_response.user.email,
                "full_name": user_response.user.user_metadata.get("full_name"),
                "created_at": user_response.user.created_at
            }
            
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Authentication failed: {str(e)}"
            )

# Create auth service instance
auth_service = AuthService()

# Dependency to get current user
async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    return await auth_service.get_current_user(credentials)