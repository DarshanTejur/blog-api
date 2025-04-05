## Blog API

### Overview  
   This is a DevOps-enhanced version of a Blog API, featuring a FastAPI-based backend. The project is containerized using Docker for easy development and deployment.

### Features  
 
  **Backend (FastAPI):** API for user registration, authentication, and blog post CRUD operations.  
  **DevOps:** Containerized setup using Docker with Uvicorn as the ASGI server.

### Technologies  

#### Backend  
  - Python FastAPI  
  - SQLAlchemy  
  - Pydantic  
  - JWT Authentication  

#### DevOps  
  - Docker  

### Folder Structure  

blog-api/
│
├── app/                      # Main application code
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── oauth2.py
│   ├── utils.py
│   └── routers/
│       ├── auth.py
│       ├── blog.py
│       └── user.py
│
├── main.py                   # Entry point for running app
├── Dockerfile                # Dockerfile to build the image
├── pyproject.toml            # Poetry configuration and dependencies
├── uv.lock                   # Poetry lock file
└── README.md                 # Project documentation


### Step-by-Step Setup Instructions  
  You don't need to touch any internal code files — everything is already configured.


### Clone the Repo

    git clone https://github.com/DarshanTejur/blog-api.git
    cd blog-api

### Install Dependencies  

  Make sure you have:
    - Docker Desktop or Docker CLI  
    - Git  

### Build and Run Container

    docker build -t blog-api .
    docker run -d -p 8000:8000 --name blog-api-container blog-api

### Access the Application  

  - API Docs (Swagger): [http://localhost:8000/docs](http://localhost:8000/docs)  
  - Redoc Docs: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### How to Verify the API is Running  
  To confirm that the FastAPI app is active inside its container:

1. List running containers:

        docker ps

(Look for a container named `blog-api-container`)

2. Enter the container:

        docker exec -it blog-api-container /bin/sh

3. Inside the container, test the API using curl:

        curl http://localhost:8000

(You should see a JSON response or a redirect to `/docs`)

4. Exit the container:

        exit

### GitHub Repository Setup

This project was **forked** from the public repository [`chethanlreddy/blog-api`](https://github.com/chethanlreddy/blog-api) and enhanced with Docker support for DevOps learning and deployment.

#### Repository

- 📂 Repo: [`DarshanTejur/blog-api`](https://github.com/DarshanTejur/blog-api)  
- 🌐 Status: Public  
- 🔁 Forked from: [`chethanlreddy/blog-api`](https://github.com/chethanlreddy/blog-api)
