from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from models import (
    UserRegister, UserLogin, AuthResponse, 
    DataItem, DataItemResponse, DataItemUpdate
)
from auth import auth_service, get_current_user
from data_service import data_service
from typing import List
import uvicorn

# Create FastAPI app
app = FastAPI(
    title="Python Supabase Server",
    description="A simple Python server with Supabase authentication and data storage",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/")
async def root():
    return {"message": "Python Supabase Server is running!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "python-supabase-server"}

# Authentication endpoints
@app.post("/auth/register", response_model=AuthResponse)
async def register(user_data: UserRegister):
    """Register a new user"""
    return await auth_service.register_user(user_data)

@app.post("/auth/login", response_model=AuthResponse)
async def login(user_data: UserLogin):
    """Login user"""
    return await auth_service.login_user(user_data)

@app.post("/auth/logout")
async def logout(current_user: dict = Depends(get_current_user)):
    """Logout user"""
    return await auth_service.logout_user("")

@app.get("/auth/me")
async def get_me(current_user: dict = Depends(get_current_user)):
    """Get current user information"""
    return current_user

# Data storage endpoints
@app.post("/data", response_model=DataItemResponse)
async def create_data_item(
    item: DataItem, 
    current_user: dict = Depends(get_current_user)
):
    """Create a new data item"""
    return await data_service.create_item(item, current_user["id"])

@app.get("/data", response_model=List[DataItemResponse])
async def get_data_items(
    limit: int = Query(default=100, ge=1, le=1000),
    offset: int = Query(default=0, ge=0),
    current_user: dict = Depends(get_current_user)
):
    """Get all data items for the current user"""
    return await data_service.get_user_items(current_user["id"], limit, offset)

@app.get("/data/{item_id}", response_model=DataItemResponse)
async def get_data_item(
    item_id: str,
    current_user: dict = Depends(get_current_user)
):
    """Get a specific data item by ID"""
    return await data_service.get_item_by_id(item_id, current_user["id"])

@app.put("/data/{item_id}", response_model=DataItemResponse)
async def update_data_item(
    item_id: str,
    item_update: DataItemUpdate,
    current_user: dict = Depends(get_current_user)
):
    """Update a specific data item"""
    return await data_service.update_item(item_id, item_update, current_user["id"])

@app.delete("/data/{item_id}")
async def delete_data_item(
    item_id: str,
    current_user: dict = Depends(get_current_user)
):
    """Delete a specific data item"""
    return await data_service.delete_item(item_id, current_user["id"])

# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {
        "error": True,
        "message": exc.detail,
        "status_code": exc.status_code
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )