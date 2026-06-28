
# FastAPI Basics

A simple practice project to understand how REST APIs are built using FastAPI.

# Concepts covered:
- Creating a FastAPI app instance
- Defining GET, POST, PUT, DELETE endpoints
- Data validation using Pydantic BaseModel
- In-memory list as a temporary database

# Setup:
```
pip install fastapi uvicorn
uvicorn main:app --reload
```

# Endpoints:
- `GET /apis` — get all apis
- `POST /apis` — add a new api
- `PUT /apis/{id}` — update an api
- `DELETE /apis/{id}` — delete an api

![FastAPI](Screenshot (1091).png)
