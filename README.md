# Todo List API with FastAPI

A complete, secure RESTful Todo List API with user authentication built with FastAPI and SQLite.

## 🌟 Features

- **User Authentication**: Secure registration and login with JWT tokens
- **CRUD Operations**: Full Create, Read, Update, Delete functionality for todos
- **User Isolation**: Each user can only access their own todos
- **Database**: SQLite with SQLAlchemy ORM
- **Password Security**: Bcrypt hashing for all passwords
- **Filtering**: Filter todos by completion status
- **CORS Enabled**: Ready for frontend integration

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone and setup the project:**
```bash
# Create project directory
mkdir todo_api
cd todo_api

# Create virtual environment (optional but recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Create project structure
mkdir app
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the application:**
```bash
uvicorn app.main:app --reload
```

4. **Access the API:**
   - API Base URL: http://localhost:8000
   - Interactive API Docs (Swagger UI): http://localhost:8000/docs
   - Alternative API Docs (ReDoc): http://localhost:8000/redoc

## 📚 API Documentation

### Authentication

#### Register a new user
```http
POST /register
Content-Type: application/json

{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "securepassword123"
}
```

#### Login
```http
POST /login
Content-Type: application/json

{
  "username": "john_doe",
  "password": "securepassword123"
}
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer",
  "user_id": 1
}
```

### Todo Operations (All require authentication)

#### Create a new todo
```http
POST /todos/
Authorization: Bearer <your_token>
Content-Type: application/json

{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread, fruits",
  "completed": false
}
```

#### Get all todos
```http
GET /todos/
Authorization: Bearer <your_token>
```

**Optional query parameters:**
- `skip`: Number of items to skip (default: 0)
- `limit`: Maximum number of items to return (default: 100)
- `completed`: Filter by completion status (true/false)

#### Get a specific todo
```http
GET /todos/{todo_id}
Authorization: Bearer <your_token>
```

#### Update a todo
```http
PUT /todos/{todo_id}
Authorization: Bearer <your_token>
Content-Type: application/json

{
  "title": "Updated title",
  "completed": true
}
```

#### Delete a todo
```http
DELETE /todos/{todo_id}
Authorization: Bearer <your_token>
```

### User Information

#### Get current user info
```http
GET /users/me
Authorization: Bearer <your_token>
```

## 🔐 Authentication Flow

1. **Register** a user to get credentials
2. **Login** with credentials to receive a JWT token
3. **Include token** in all subsequent requests:
   ```
   Authorization: Bearer <your_token>
   ```
4. **Tokens expire** after 30 minutes (configurable)

## 🗄️ Database Models


## 🛡️ Security Features

- **Password hashing** using bcrypt
- **JWT tokens** for stateless authentication
- **Token expiration** for enhanced security
- **SQL injection protection** via SQLAlchemy
- **Input validation** with Pydantic schemas
- **User isolation** ensuring data privacy


## 🧪 Testing

### 1. Register a user
```bash
curl -X POST "http://localhost:8000/register" \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","email":"test@example.com","password":"testpass123"}'
```

### 2. Login and save token
```bash
curl -X POST "http://localhost:8000/login" \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"testpass123"}'
```

### 3. Create a todo (replace TOKEN with actual token)
```bash
curl -X POST "http://localhost:8000/todos/" \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title":"Learn FastAPI","description":"Build more APIs"}'
```

### 4. Get all todos
```bash
curl -X GET "http://localhost:8000/todos/" \
  -H "Authorization: Bearer TOKEN"
```

## 🐛 Troubleshooting

### Common Issues

1. **"Could not validate credentials"**
   - Token might have expired (30-minute default)
   - Re-login to get a new token
   - Check that you're including the token in the Authorization header

2. **Database issues**
   - Delete `todo.db` and restart the application
   - Check SQLite permissions

3. **Import errors**
   - Ensure all files are in the correct directory structure
   - Check that virtual environment is activated
   - Verify all dependencies are installed

## 🔧 Configuration

### Environment Variables (for production)
Create a `.env` file:
```env
SECRET_KEY=your-secure-secret-key-here
DATABASE_URL=sqlite:///./todo.db
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Security Notes for Production
1. **Change SECRET_KEY** in `app/auth.py`
2. Use **environment variables** for sensitive data
3. Enable **HTTPS** for production deployment
4. Consider using **PostgreSQL** or **MySQL** for production
5. Implement **rate limiting**
6. Add **logging** and **monitoring**
7. Use **database migrations** (Alembic)

## 📈 API Response Examples

### Success Response
```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "completed": false,
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": null
}
```

### Error Responses
```json
{
  "detail": "Username already registered"
}
```

```json
{
  "detail": "Could not validate credentials"
}
```

**Happy Coding!** 🚀

For any issues or questions, please check the FastAPI documentation or open an issue in the repository.
