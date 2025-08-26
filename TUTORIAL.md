# Building Your First Python Authentication Server: A Complete Beginner's Guide

## Table of Contents
1. [Introduction: What We're Building](#introduction-what-were-building)
2. [Key Programming Concepts Explained](#key-programming-concepts-explained)
3. [Prerequisites and Environment Setup](#prerequisites-and-environment-setup)
4. [Setting Up Supabase (Your Database)](#setting-up-supabase-your-database)
5. [Project Structure Overview](#project-structure-overview)
6. [Step-by-Step Implementation](#step-by-step-implementation)
7. [Testing Your Application](#testing-your-application)
8. [Understanding the Code in Detail](#understanding-the-code-in-detail)
9. [Common Issues and Troubleshooting](#common-issues-and-troubleshooting)
10. [Next Steps and Learning Resources](#next-steps-and-learning-resources)

---

## Introduction: What We're Building

By the end of this tutorial, you'll have built a simple **authentication server** – a program that can:

- Register new users with email and password
- Log users in and out securely
- Store user data safely in a database
- Protect user information so only they can access it
- Provide an interface for other applications to use

---

## Key Programming Concepts Explained

Before we start coding, let's go over key concepts we'll be working with. Don't worry if these seem complex. We'll see them in action throughout the tutorial.

### 1. API (Application Programming Interface)

**Simple Explanation:** An API is like a waiter at a restaurant. Just as a waiter takes your order (request) to the kitchen and brings back your food (response), an API takes requests from applications and returns the requested information. It provides a standardized and predictable interface so other people know how to interact with the system.

**Real Example:** When you open a weather app, it doesn't store weather data itself. Instead, it asks (makes a request to) a weather API: "What's the weather in New York?" The API responds with the current weather data.

**In Our Project:** Our server will be an API that other applications can ask: "Register this new user" or "Get this user's data."

### 2. RESTful API

**Simple Explanation:** REST is a set of rules for building APIs, like having good table manners. It makes APIs predictable and easy to use.

**The Rules:**
- Use standard HTTP methods: GET (read), POST (create), PUT (update), DELETE (remove)
- Use clear, descriptive URLs like `/users` or `/data/123`
- Return consistent response formats

**Example:**
- `GET /users/123` → "Get information about user 123"
- `POST /users` → "Create a new user"
- `DELETE /users/123` → "Delete user 123"

### 3. JWT (JSON Web Token)

**Simple Explanation:** A JWT is like a special wristband you get at an amusement park. Once you show your ticket (login), you get a wristband that proves you paid. You can then use this wristband to access rides without showing your ticket again. A JWT stands for JSON Web Token and is an encrypted string of data that contains information about the user's session authorization.

**How It Works:**
1. User logs in with email/password
2. Server verifies credentials and gives them a JWT
3. User includes this JWT with future requests
4. Server checks the JWT to confirm who they are

**Security Benefit:** The server doesn't need to remember who's logged in – the JWT contains all necessary information and can't be faked.

### 4. RLS (Row Level Security)

**Simple Explanation:** Imagine a filing cabinet where each person can only open drawers with their name on them. RLS is like having automatic locks that ensure users can only access their own data. In our tutorial, Supabase will be handling RLS automatically.

**Example:** If User A and User B both store notes in our database, RLS ensures that User A can never see User B's notes, even if there's a bug in our code.

### 5. Database

**Simple Explanation:** A database is like a super-organized digital filing cabinet that can instantly find, store, and organize information.

**In Our Project:** We'll use Supabase, which provides:
- **Storage:** Keeps our data safe and organized
- **Authentication:** Handles user registration and login
- **Security:** Ensures data protection

### 6. Environment Variables

**Simple Explanation:** These are secret configuration values that your program needs but shouldn't be shared publicly (like passwords or API keys).

**Example:** Instead of writing your database password directly in your code (where anyone could see it), you store it in an environment variable that only your program can access.

---

## Prerequisites and Environment Setup

### What You Need

1. **A Computer:** Windows, Mac, or Linux
2. **Basic Computer Skills:** Ability to create folders, download files, and copy/paste
3. **Internet Connection:** For downloading tools and accessing Supabase
4. **Patience and Curiosity:** Programming involves trial and error – that's normal!

### Step 1: Install Python

Python is the programming language we'll use. It's like the foundation of our house.

#### For Windows:
1. Go to [python.org/downloads](https://python.org/downloads)
2. Download Python 3.11 or newer
3. **Important:** During installation, check "Add Python to PATH"

#### For Mac:
1. Go to [python.org/downloads](https://python.org/downloads)
2. Download Python 3.11 or newer
3. Run the installer

#### For Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3 python3-pip
```

#### Verify Installation:
Open your command prompt (Windows) or terminal (Mac/Linux) and type:
```bash
python --version
```
You should see something like "Python 3.11.x"

**🖼️ Screenshot Marker: Terminal showing successful Python version output**

### Step 2: Install a Code Editor

We recommend **Visual Studio Code** (VS Code) – it's free and beginner-friendly.

1. Go to [code.visualstudio.com](https://code.visualstudio.com)
2. Download and install for your operating system
3. Open VS Code

**🖼️ Screenshot Marker: VS Code welcome screen**

### Step 3: Install Useful VS Code Extensions

Extensions add helpful features to VS Code. Install these by:
1. Clicking the Extensions icon (puzzle piece) in VS Code
2. Searching for each extension name
3. Clicking "Install"

**Recommended Extensions:**
- **Python** (by Microsoft) – Adds Python support
- **Python Debugger** (by Microsoft) – Helps find and fix errors

**🖼️ Screenshot Marker: VS Code Extensions panel with Python extension highlighted**

### Step 4: Create Your Project Folder

1. Create a new folder on your computer called `python-auth-server`
2. Open VS Code
3. Click "File" → "Open Folder"
4. Select your `python-auth-server` folder

**🖼️ Screenshot Marker: VS Code with empty project folder open**

---

## Setting Up Supabase (Your Database)

Supabase is like a powerful, pre-built backend service that handles database management and user authentication for us. Instead of building these complex systems from scratch, we can use Supabase's services.

### Step 1: Create a Supabase Account

1. Go to [supabase.com](https://supabase.com)
2. Click "Start your project"
3. Sign up with your email or GitHub account

**🖼️ Screenshot Marker: Supabase homepage with "Start your project" button**

### Step 2: Create a New Project

1. Once logged in, click "New Project"
2. Fill in the details:
   - **Name:** "Python Auth Server"
   - **Database Password:** Create a strong password (save this!)
   - **Region:** Choose the closest to your location
3. Click "Create new project"

**🖼️ Screenshot Marker: Supabase new project creation form**

**Important:** Project creation takes 2-3 minutes. You'll see a progress indicator.

### Step 3: Get Your Project Credentials

Once your project is ready:

1. Go to "Settings" (gear icon) in the left sidebar
2. Click "API" 
3. You'll see two important values:
   - **Project URL** (looks like: `https://abc123.supabase.co`)
   - **anon public key** (a long string starting with `eyJ`)

**🖼️ Screenshot Marker: Supabase API settings page showing Project URL and anon key**

**Keep these safe – we'll need them soon!**

### Step 4: Set Up Your Database Schema

A database schema is like a blueprint that tells the database how to organize your data.

1. In Supabase, click "SQL Editor" in the left sidebar
2. Click "New query"
3. Copy and paste this SQL code:

```sql
-- This file contains the SQL schema to create in your Supabase database

-- Enable Row Level Security (RLS) if not already enabled
-- This is usually done automatically in Supabase

-- Create the user_data table
CREATE TABLE IF NOT EXISTS public.user_data (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    metadata JSONB,
    user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create an index on user_id for better query performance
CREATE INDEX IF NOT EXISTS idx_user_data_user_id ON public.user_data(user_id);

-- Create an index on created_at for ordering
CREATE INDEX IF NOT EXISTS idx_user_data_created_at ON public.user_data(created_at);

-- Enable Row Level Security on the user_data table
ALTER TABLE public.user_data ENABLE ROW LEVEL SECURITY;

-- Create RLS policies to ensure users can only access their own data
CREATE POLICY "Users can view their own data" ON public.user_data
    FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "Users can insert their own data" ON public.user_data
    FOR INSERT WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can update their own data" ON public.user_data
    FOR UPDATE USING (auth.uid() = user_id);

CREATE POLICY "Users can delete their own data" ON public.user_data
    FOR DELETE USING (auth.uid() = user_id);

-- Create a function to automatically update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Create a trigger to automatically update the updated_at column
CREATE TRIGGER update_user_data_updated_at BEFORE UPDATE ON public.user_data
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
```

4. Click "Run" to execute the SQL

**🖼️ Screenshot Marker: Supabase SQL Editor with the schema code and "Run" button**

**What This Code Does:**
- Creates a table called `user_data` to store user information
- Sets up Row Level Security so users can only access their own data
- Creates automatic timestamps for when data is created and updated
- Adds performance optimizations (indexes)

You should see "Success. No rows returned" – this means it worked!

---

## Project Structure Overview

Let's understand how our project is organized. Think of it like organizing a house – each file has a specific purpose and location.

```
python-auth-server/
├── main.py              # The "front door" - handles incoming requests
├── config.py            # Configuration and settings
├── auth.py              # Handles user registration and login
├── data_service.py      # Manages user data storage
├── models.py            # Defines data structures (like forms)
├── database_schema.sql  # Database blueprint (already used in Supabase)
├── requirements.txt     # List of tools (libraries) we need
├── .env                 # Secret configuration (passwords, keys)
├── .env.example         # Template for .env file
└── .gitignore          # Tells Git what files to ignore
```

### File Purposes Explained

**main.py** - The Main Application
- Like the front desk of a hotel
- Receives all incoming requests
- Decides where to send each request (registration, login, data storage)
- Sends back responses

**auth.py** - Authentication Service
- Like a security guard
- Checks if users are who they say they are
- Creates and validates JWT tokens
- Handles registration and login logic

**data_service.py** - Data Management
- Like a filing clerk
- Stores, retrieves, updates, and deletes user data
- Ensures users can only access their own information

**models.py** - Data Structures
- Like forms or templates
- Defines what information we expect (email format, required fields)
- Ensures data consistency and validation

**config.py** - Configuration
- Like a settings panel
- Connects to Supabase
- Manages environment variables
- Sets up database connections

---

## Step-by-Step Implementation

Now we'll build our application file by file. We'll start with the foundation and work our way up.

### Step 1: Set Up Environment Variables

Environment variables store sensitive information like passwords and API keys.

1. In VS Code, create a new file called `.env`
2. Add your Supabase credentials:

```env
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_KEY=your-anon-key-here
SECRET_KEY=your-secret-key-for-jwt-signing
```

**Replace the values with:**
- `SUPABASE_URL`: Your Project URL from Supabase
- `SUPABASE_KEY`: Your anon public key from Supabase  
- `SECRET_KEY`: Any random string (like `my-super-secret-key-12345`)

**🖼️ Screenshot Marker: VS Code showing .env file with placeholder values**

### Step 2: Create Environment Template

Create `.env.example` to show others what environment variables are needed (without revealing your secrets):

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
SECRET_KEY=your_secret_key_for_jwt
```

### Step 3: Create Requirements File

Create `requirements.txt` to list all the Python libraries we need:

```txt
fastapi==0.104.1
uvicorn==0.24.0
supabase==2.1.0
python-dotenv==1.0.0
pydantic>=2.10.0
python-multipart==0.0.6
```

**What Each Library Does:**
- **fastapi**: The web framework (like the foundation of our API)
- **uvicorn**: The web server (like the engine that runs our API)
- **supabase**: Connects to our Supabase database
- **python-dotenv**: Reads environment variables from .env file
- **pydantic**: Validates data and creates models
- **python-multipart**: Handles form data in requests

### Step 4: Install Dependencies

Open your terminal in VS Code (Terminal → New Terminal) and run:

```bash
pip install -r requirements.txt
```

This downloads and installs all the libraries we need.

**🖼️ Screenshot Marker: Terminal showing pip install progress**

### Step 5: Create Configuration File

Create `config.py`:

```python
import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

# Supabase configuration
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret-key")

# Create Supabase client
def get_supabase_client() -> Client:
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError("SUPABASE_URL and SUPABASE_KEY must be set in environment variables")
    
    return create_client(SUPABASE_URL, SUPABASE_KEY)

# Initialize client
supabase: Client = get_supabase_client()
```

**What This Code Does:**
1. Loads our secret environment variables
2. Creates a connection to our Supabase database
3. Provides this connection to other parts of our application

### Step 6: Create Data Models

Create `models.py`:

```python
from pydantic import BaseModel, EmailStr
from typing import Optional, Dict, Any
from datetime import datetime

class UserRegister(BaseModel):
    email: EmailStr
    password: str
    full_name: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: str
    email: str
    full_name: Optional[str] = None
    created_at: datetime

class DataItem(BaseModel):
    title: str
    content: str
    metadata: Optional[Dict[str, Any]] = None

class DataItemResponse(BaseModel):
    id: str
    title: str
    content: str
    metadata: Optional[Dict[str, Any]] = None
    user_id: str
    created_at: datetime
    updated_at: datetime

class DataItemUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

class AuthResponse(BaseModel):
    access_token: str
    user: UserResponse
```

**What These Models Do:**

**UserRegister**: Defines what information we need to register a new user
- Email (validated format)
- Password
- Optional full name

**UserLogin**: What we need for login
- Email and password only

**DataItem**: Structure for user data
- Title and content (required)
- Optional metadata for extra information

**Models are like digital forms** - they ensure we get the right information in the right format.

### Step 7: Create Authentication Service

Create `auth.py`:

```python
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
```

**What This Service Does:**
1. **Registration**: Creates new user accounts
2. **Login**: Validates credentials and returns JWT tokens
3. **Authentication**: Verifies JWT tokens to identify users
4. **Security**: Uses Supabase's built-in security features

### Step 8: Create Data Service

Create `data_service.py`:

```python
from fastapi import HTTPException, status
from config import supabase
from models import DataItem, DataItemResponse, DataItemUpdate
from typing import List, Optional
from datetime import datetime

class DataService:
    def __init__(self):
        self.supabase = supabase
        self.table_name = "user_data"

    async def create_item(self, item: DataItem, user_id: str) -> DataItemResponse:
        """Create a new data item for the user"""
        try:
            data = {
                "title": item.title,
                "content": item.content,
                "metadata": item.metadata,
                "user_id": user_id
            }
            
            result = self.supabase.table(self.table_name).insert(data).execute()
            
            if not result.data:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Failed to create item"
                )
            
            created_item = result.data[0]
            return DataItemResponse(
                id=created_item["id"],
                title=created_item["title"],
                content=created_item["content"],
                metadata=created_item["metadata"],
                user_id=created_item["user_id"],
                created_at=datetime.fromisoformat(created_item["created_at"].replace('Z', '+00:00')),
                updated_at=datetime.fromisoformat(created_item["updated_at"].replace('Z', '+00:00'))
            )
            
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed to create item: {str(e)}"
            )

    async def get_user_items(self, user_id: str, limit: int = 100, offset: int = 0) -> List[DataItemResponse]:
        """Get all items for a specific user"""
        try:
            result = self.supabase.table(self.table_name)\
                .select("*")\
                .eq("user_id", user_id)\
                .order("created_at", desc=True)\
                .limit(limit)\
                .offset(offset)\
                .execute()
            
            items = []
            for item in result.data:
                items.append(DataItemResponse(
                    id=item["id"],
                    title=item["title"],
                    content=item["content"],
                    metadata=item["metadata"],
                    user_id=item["user_id"],
                    created_at=datetime.fromisoformat(item["created_at"].replace('Z', '+00:00')),
                    updated_at=datetime.fromisoformat(item["updated_at"].replace('Z', '+00:00'))
                ))
            
            return items
            
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed to fetch items: {str(e)}"
            )

    async def get_item_by_id(self, item_id: str, user_id: str) -> DataItemResponse:
        """Get a specific item by ID for the user"""
        try:
            result = self.supabase.table(self.table_name)\
                .select("*")\
                .eq("id", item_id)\
                .eq("user_id", user_id)\
                .execute()
            
            if not result.data:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Item not found"
                )
            
            item = result.data[0]
            return DataItemResponse(
                id=item["id"],
                title=item["title"],
                content=item["content"],
                metadata=item["metadata"],
                user_id=item["user_id"],
                created_at=datetime.fromisoformat(item["created_at"].replace('Z', '+00:00')),
                updated_at=datetime.fromisoformat(item["updated_at"].replace('Z', '+00:00'))
            )
            
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed to fetch item: {str(e)}"
            )

    async def update_item(self, item_id: str, item_update: DataItemUpdate, user_id: str) -> DataItemResponse:
        """Update a specific item"""
        try:
            # Build update data excluding None values
            update_data = {}
            if item_update.title is not None:
                update_data["title"] = item_update.title
            if item_update.content is not None:
                update_data["content"] = item_update.content
            if item_update.metadata is not None:
                update_data["metadata"] = item_update.metadata
            
            if not update_data:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="No fields to update"
                )
            
            result = self.supabase.table(self.table_name)\
                .update(update_data)\
                .eq("id", item_id)\
                .eq("user_id", user_id)\
                .execute()
            
            if not result.data:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Item not found or not authorized"
                )
            
            updated_item = result.data[0]
            return DataItemResponse(
                id=updated_item["id"],
                title=updated_item["title"],
                content=updated_item["content"],
                metadata=updated_item["metadata"],
                user_id=updated_item["user_id"],
                created_at=datetime.fromisoformat(updated_item["created_at"].replace('Z', '+00:00')),
                updated_at=datetime.fromisoformat(updated_item["updated_at"].replace('Z', '+00:00'))
            )
            
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed to update item: {str(e)}"
            )

    async def delete_item(self, item_id: str, user_id: str) -> dict:
        """Delete a specific item"""
        try:
            result = self.supabase.table(self.table_name)\
                .delete()\
                .eq("id", item_id)\
                .eq("user_id", user_id)\
                .execute()
            
            if not result.data:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Item not found or not authorized"
                )
            
            return {"message": "Item deleted successfully"}
            
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed to delete item: {str(e)}"
            )

# Create data service instance
data_service = DataService()
```

**What This Service Does:**
1. **Create**: Adds new data items to the database
2. **Read**: Retrieves user's data (all items or specific item)
3. **Update**: Modifies existing data items
4. **Delete**: Removes data items
5. **Security**: Ensures users can only access their own data

### Step 9: Create Main Application

Create `main.py`:

```python
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
```

**What This Main File Does:**

1. **Sets Up the Web Server**: Creates a FastAPI application that can receive web requests
2. **Handles CORS**: Allows other websites/apps to use our API (Cross-Origin Resource Sharing)
3. **Defines Routes**: Maps URLs to specific functions (like `/auth/login` calls the login function)
4. **Adds Security**: Requires authentication for protected endpoints
5. **Error Handling**: Provides clear error messages when things go wrong

**API Endpoints Explained:**

**Health Checks:**
- `GET /` - Simple test to see if server is running
- `GET /health` - More detailed health status

**Authentication:**
- `POST /auth/register` - Create new user account
- `POST /auth/login` - Log in existing user
- `POST /auth/logout` - Log out current user
- `GET /auth/me` - Get current user's information

**Data Management:**
- `POST /data` - Create new data item
- `GET /data` - Get all user's data items
- `GET /data/{id}` - Get specific data item
- `PUT /data/{id}` - Update data item
- `DELETE /data/{id}` - Delete data item

### Step 10: Create Git Ignore File

Create `.gitignore` to tell Git which files to ignore:

```
# Environment variables
.env

# Python cache
__pycache__/
*.pyc
*.pyo
*.pyd
.Python

# Virtual environment
venv/
env/
ENV/

# IDE files
.vscode/settings.json
.idea/

# OS files
.DS_Store
Thumbs.db

# Logs
*.log
```

**Why We Ignore These Files:**
- `.env` contains secrets that shouldn't be shared
- Cache files are automatically generated
- IDE and OS files are personal preferences

---

## Testing Your Application

Now comes the exciting part – testing your creation! We'll start the server and test each feature.

### Step 1: Start Your Server

1. Open terminal in VS Code
2. Make sure you're in your project folder
3. Run the server:

```bash
python main.py
```

You should see output like:
```
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

**🖼️ Screenshot Marker: Terminal showing successful server startup**

### Step 2: Test Server Health

Open your web browser and go to:
```
http://localhost:8000
```

You should see:
```json
{"message": "Python Supabase Server is running!"}
```

**🖼️ Screenshot Marker: Browser showing the JSON response**

### Step 3: Explore the Interactive Documentation

FastAPI automatically creates interactive documentation. Go to:
```
http://localhost:8000/docs
```

This page shows all your API endpoints and lets you test them directly!

**🖼️ Screenshot Marker: FastAPI Swagger UI documentation page**

### Step 4: Test User Registration

In the documentation page:

1. Click on `POST /auth/register`
2. Click "Try it out"
3. Fill in the example data:
```json
{
  "email": "test@example.com",
  "password": "password123",
  "full_name": "Test User"
}
```
4. Click "Execute"

**Expected Response:**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "user": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "email": "test@example.com",
    "full_name": "Test User",
    "created_at": "2024-01-01T12:00:00Z"
  }
}
```

**🖼️ Screenshot Marker: Successful registration response in Swagger UI**

**Important:** Save the `access_token` – you'll need it for the next tests!

### Step 5: Test User Login

1. Click on `POST /auth/login`
2. Click "Try it out"
3. Use the same credentials:
```json
{
  "email": "test@example.com",
  "password": "password123"
}
```
4. Click "Execute"

You should get the same response format with a new access token.

### Step 6: Test Protected Endpoints

For endpoints that require authentication, you need to add your token:

1. At the top of the docs page, click the "Authorize" button
2. Enter: `Bearer YOUR_ACCESS_TOKEN_HERE`
3. Click "Authorize"

**🖼️ Screenshot Marker: Authorization dialog in Swagger UI**

Now test the protected endpoints:

#### Test Get Current User:
1. Click `GET /auth/me`
2. Click "Try it out" → "Execute"

#### Test Create Data Item:
1. Click `POST /data`
2. Click "Try it out"
3. Enter test data:
```json
{
  "title": "My First Note",
  "content": "This is my first data item!",
  "metadata": {"category": "test", "priority": "high"}
}
```
4. Click "Execute"

#### Test Get All Data Items:
1. Click `GET /data`
2. Click "Try it out" → "Execute"

You should see your created data item in the response!

### Step 7: Test with Command Line (Optional Advanced)

If you want to test like a professional developer, use curl commands:

#### Register:
```bash
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test2@example.com",
    "password": "password123",
    "full_name": "Test User 2"
  }'
```

#### Login:
```bash
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test2@example.com",
    "password": "password123"
  }'
```

#### Create Data (replace TOKEN with your actual token):
```bash
curl -X POST "http://localhost:8000/data" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer TOKEN" \
  -d '{
    "title": "Command Line Note",
    "content": "Created from terminal!",
    "metadata": {"source": "curl"}
  }'
```

---

## Understanding the Code in Detail

Now that your application works, let's dive deeper into how it all fits together.

### How Authentication Works

#### 1. User Registration Flow:
```
User provides email/password
    ↓
Server validates data format
    ↓
Supabase creates user account
    ↓
Supabase returns JWT token
    ↓
Server sends token to user
```

#### 2. Login Flow:
```
User provides email/password
    ↓
Server sends credentials to Supabase
    ↓
Supabase verifies credentials
    ↓
Supabase returns JWT token
    ↓
Server sends token to user
```

#### 3. Accessing Protected Data:
```
User sends request with JWT token
    ↓
Server validates token with Supabase
    ↓
Server extracts user ID from token
    ↓
Server allows access to user's data only
```

### How Row Level Security Works

When you create, read, update, or delete data, Supabase automatically:

1. **Checks the JWT token** to identify the user
2. **Applies RLS policies** we defined in the database schema
3. **Only shows/modifies data** where `user_id` matches the authenticated user

This means even if there's a bug in our code, users can never access each other's data!

### Understanding the Database Structure

Our `user_data` table has these columns:

- **id**: Unique identifier for each data item (UUID)
- **title**: User-provided title (text, required)
- **content**: User-provided content (text, required)
- **metadata**: Optional extra information (JSON)
- **user_id**: Links data to specific user (UUID, required)
- **created_at**: When item was created (timestamp, automatic)
- **updated_at**: When item was last modified (timestamp, automatic)

### How the API Routes Work

Each route in `main.py` follows this pattern:

1. **Receive Request**: FastAPI captures the incoming HTTP request
2. **Validate Data**: Pydantic models ensure data format is correct
3. **Authenticate User**: `Depends(get_current_user)` verifies the JWT token
4. **Process Request**: Call appropriate service function
5. **Return Response**: Send back JSON response

Example for creating data:
```python
@app.post("/data", response_model=DataItemResponse)
async def create_data_item(
    item: DataItem,                           # Validate incoming data
    current_user: dict = Depends(get_current_user)  # Authenticate user
):
    return await data_service.create_item(item, current_user["id"])  # Process & respond
```

### Error Handling Strategy

Our application handles errors at multiple levels:

1. **Validation Errors**: Pydantic catches invalid data formats
2. **Authentication Errors**: JWT verification failures
3. **Database Errors**: Connection or query problems
4. **Business Logic Errors**: Custom validation (like "item not found")

Each error returns a clear message and appropriate HTTP status code.

---

## Common Issues and Troubleshooting

### Issue 1: "SUPABASE_URL and SUPABASE_KEY must be set"

**Problem**: Environment variables aren't loading

**Solutions:**
1. Check that `.env` file exists in your project root
2. Verify the file contains your actual Supabase credentials
3. Make sure there are no extra spaces around the `=` signs
4. Restart your server after changing `.env`

**🖼️ Screenshot Marker: VS Code file explorer showing .env file location**

### Issue 2: "Module not found" errors

**Problem**: Python can't find required libraries

**Solutions:**
1. Make sure you ran `pip install -r requirements.txt`
2. Verify you're in the correct directory
3. If using virtual environment, make sure it's activated
4. Try running: `pip list` to see installed packages

### Issue 3: "Invalid credentials" on login

**Problem**: User authentication failing

**Solutions:**
1. Double-check email and password spelling
2. Make sure you registered the user first
3. Check Supabase dashboard to see if user exists
4. Verify Supabase URL and key are correct

### Issue 4: "Failed to create item" for data operations

**Problem**: Database operations failing

**Solutions:**
1. Verify you ran the database schema SQL in Supabase
2. Check that RLS policies are created correctly
3. Make sure you're sending a valid JWT token
4. Check Supabase logs for detailed error messages

### Issue 5: Server won't start on port 8000

**Problem**: Port already in use

**Solutions:**
1. Kill any existing Python processes
2. Change port in `main.py`: `uvicorn.run(..., port=8001)`
3. On Mac/Linux: `lsof -ti:8000 | xargs kill -9`
4. On Windows: Use Task Manager to end Python processes

### Issue 6: CORS errors in browser

**Problem**: Browser blocking API requests

**Solutions:**
1. Our code already includes CORS middleware
2. For production, update `allow_origins` to specific domains
3. Make sure requests include proper headers

### Debugging Tips

#### 1. Check Server Logs
Always look at your terminal where the server is running – it shows detailed error messages.

#### 2. Use the Interactive Docs
`http://localhost:8000/docs` is your best friend for testing API endpoints.

#### 3. Check Supabase Dashboard
Log into your Supabase project to:
- View user accounts in Authentication
- Check data in Table Editor
- Read error logs in Logs section

#### 4. Verify Environment Variables
Add a print statement in `config.py` to check if variables load:
```python
print(f"Supabase URL: {SUPABASE_URL}")
print(f"Supabase Key: {SUPABASE_KEY[:20]}...")  # Only first 20 chars for security
```

---

## Next Steps and Learning Resources

Congratulations! You've built a complete, production-ready authentication server. Here's what you can do next:

### Immediate Next Steps

#### 1. Build a Frontend
Create a simple web interface for your API:
- **HTML/CSS/JavaScript**: Basic web pages that call your API
- **React**: Modern frontend framework
- **Vue.js**: Beginner-friendly alternative to React

#### 2. Add Features
Enhance your server with:
- **Email verification**: Require users to verify their email addresses
- **Password reset**: Let users reset forgotten passwords
- **User profiles**: Add profile pictures and additional user information
- **File uploads**: Allow users to upload images or documents

#### 3. Deploy to Production
Put your server online:
- **Heroku**: Beginner-friendly hosting platform
- **Vercel**: Great for full-stack applications
- **Railway**: Modern hosting with simple deployment
- **DigitalOcean**: More control over server configuration

### Learning Resources

#### Python & FastAPI
- **Official FastAPI Tutorial**: [fastapi.tiangolo.com/tutorial](https://fastapi.tiangolo.com/tutorial)
- **Python.org Beginner's Guide**: [python.org/about/gettingstarted](https://python.org/about/gettingstarted)
- **Automate the Boring Stuff with Python**: Free online book

#### Web Development Concepts
- **MDN Web Docs**: [developer.mozilla.org](https://developer.mozilla.org) - Best web development resource
- **HTTP Status Codes**: Understanding 200, 404, 500, etc.
- **REST API Design**: Best practices for API development

#### Database & Backend
- **SQL Tutorial**: [w3schools.com/sql](https://w3schools.com/sql)
- **Database Design**: Understanding relationships and normalization
- **Supabase Documentation**: [supabase.com/docs](https://supabase.com/docs)

#### Security
- **OWASP Top 10**: Common web security vulnerabilities
- **JWT.io**: Deep dive into JSON Web Tokens
- **Authentication vs Authorization**: Understanding the difference

### Project Ideas to Practice

#### Beginner Projects
1. **Personal Note-Taking App**: Expand your current project with categories and search
2. **Todo List API**: Users can create, organize, and track tasks
3. **Simple Blog Platform**: Users can write and publish articles

#### Intermediate Projects
1. **Social Media API**: Users can follow each other and share posts
2. **E-commerce Backend**: Products, shopping carts, and orders
3. **Event Management System**: Create and manage events with RSVPs

#### Advanced Projects
1. **Multi-tenant SaaS**: Multiple organizations with isolated data
2. **Real-time Chat Application**: WebSocket integration
3. **Microservices Architecture**: Split functionality into multiple services

### Programming Career Paths

Your authentication server touches on several career paths:

#### Backend Developer
Focus on server-side logic, databases, and APIs. Technologies to learn:
- **Languages**: Python, Node.js, Java, Go
- **Databases**: PostgreSQL, MongoDB, Redis
- **Cloud Services**: AWS, Google Cloud, Azure

#### Full-Stack Developer
Work on both frontend and backend. Add these skills:
- **Frontend**: React, Vue.js, Angular
- **Mobile**: React Native, Flutter
- **DevOps**: Docker, Kubernetes, CI/CD

#### DevOps Engineer
Focus on deployment and infrastructure:
- **Containerization**: Docker, Kubernetes
- **Cloud Platforms**: AWS, GCP, Azure
- **Monitoring**: Prometheus, Grafana, ELK Stack

#### Security Engineer
Specialize in application security:
- **Penetration Testing**: Finding vulnerabilities
- **Compliance**: GDPR, SOC2, HIPAA
- **Security Tools**: Vulnerability scanners, SIEM systems

### Contributing to Open Source

Now that you understand how applications work, consider contributing to open source projects:

1. **Start Small**: Fix typos in documentation
2. **Report Bugs**: Help projects by reporting issues you find
3. **Add Features**: Once comfortable, contribute new functionality
4. **Create Your Own**: Open source your own projects

### Final Thoughts

You've accomplished something significant! You've built a real application that:
- Handles user authentication securely
- Stores data with proper access controls
- Provides a clean API interface
- Follows industry best practices
- Could be used as the foundation for a startup

The concepts you've learned – APIs, databases, authentication, security – are fundamental to almost all modern software development. Whether you become a web developer, mobile app developer, or work in any other tech role, these skills will serve you well.

Remember: every expert was once a beginner. Keep building, keep learning, and don't be afraid to tackle bigger challenges. The programming community is welcoming and always ready to help those who are learning.

**Happy coding!** 🚀

---

### Additional Resources and References

#### Documentation Links
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [Supabase Documentation](https://supabase.com/docs)
- [Python Documentation](https://docs.python.org/3/)
- [Pydantic Documentation](https://docs.pydantic.dev)

#### Community and Support
- [FastAPI GitHub Discussions](https://github.com/tiangolo/fastapi/discussions)
- [Supabase Discord Community](https://discord.supabase.com)
- [Python Discord](https://discord.gg/python)
- [Stack Overflow](https://stackoverflow.com) - For specific programming questions

#### Books for Further Learning
- "Python Crash Course" by Eric Matthes
- "Clean Code" by Robert C. Martin
- "Designing Data-Intensive Applications" by Martin Kleppmann
- "The Pragmatic Programmer" by Andrew Hunt and David Thomas

Remember: The journey of learning programming is a marathon, not a sprint. Take it one step at a time, celebrate small victories, and keep building!