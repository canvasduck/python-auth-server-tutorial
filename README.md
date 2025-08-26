# Python Supabase Server

A simple Python server built with FastAPI that uses Supabase for authentication and data storage.

## Features

- User registration and authentication using Supabase Auth
- JWT token-based authorization
- CRUD operations for user data
- Row Level Security (RLS) for data isolation
- RESTful API endpoints
- Automatic API documentation with FastAPI

## Prerequisites

- Python 3.8+
- A Supabase project (free at [supabase.com](https://supabase.com))

## Setup

### 1. Clone or download this project

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up Supabase

1. Create a new project at [supabase.com](https://supabase.com)
2. Go to Settings > API to get your project URL and anon key
3. Go to SQL Editor and run the contents of `database_schema.sql` to create the required tables

### 4. Environment Configuration

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` and add your Supabase credentials:
```
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key
SECRET_KEY=your-secret-key-for-jwt
```

### 5. Run the server

```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The server will start on `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- Interactive API docs: `http://localhost:8000/docs`
- Alternative API docs: `http://localhost:8000/redoc`

## API Endpoints

### Authentication

- `POST /auth/register` - Register a new user
- `POST /auth/login` - Login user
- `POST /auth/logout` - Logout user (requires authentication)
- `GET /auth/me` - Get current user info (requires authentication)

### Data Management

All data endpoints require authentication (Bearer token in Authorization header):

- `POST /data` - Create a new data item
- `GET /data` - Get all data items for the current user
- `GET /data/{item_id}` - Get a specific data item
- `PUT /data/{item_id}` - Update a data item
- `DELETE /data/{item_id}` - Delete a data item

### Health Checks

- `GET /` - Root endpoint
- `GET /health` - Health check endpoint

## Usage Examples

### Register a user

```bash
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "password123",
    "full_name": "John Doe"
  }'
```

### Login

```bash
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "password123"
  }'
```

### Create data item (requires auth token)

```bash
curl -X POST "http://localhost:8000/data" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -d '{
    "title": "My First Item",
    "content": "This is some content",
    "metadata": {"category": "example"}
  }'
```

### Get all data items (requires auth token)

```bash
curl -X GET "http://localhost:8000/data" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

## Project Structure

```
.
├── main.py              # FastAPI application and routes
├── config.py            # Supabase configuration
├── auth.py              # Authentication service
├── data_service.py      # Data storage service
├── models.py            # Pydantic models
├── database_schema.sql  # Database schema for Supabase
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variables template
└── README.md           # This file
```

## Security Features

- JWT token-based authentication via Supabase Auth
- Row Level Security (RLS) ensures users can only access their own data
- Password hashing handled by Supabase
- CORS middleware for cross-origin requests
- Input validation using Pydantic models

## Development

For development, you can run the server with auto-reload:

```bash
uvicorn main:app --reload
```

## Deployment

For production deployment:

1. Set appropriate CORS origins in `main.py`
2. Use a production WSGI server like Gunicorn
3. Set strong secret keys in environment variables
4. Consider using a reverse proxy like Nginx

Example production command:
```bash
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License.