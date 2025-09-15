# Django REST API Project with Celery, Redis, PostgreSQL, and Swagger

This is a sample backend system built with Django and Docker, featuring:

- **Django REST Framework (DRF)**: Build RESTful APIs for user registration, authentication, and other endpoints.
- **Celery + Redis**: Handle background tasks asynchronously, e.g., sending welcome emails after registration.
- **PostgreSQL**: Reliable relational database for storing user data.
- **Swagger / drf-yasg**: API documentation with an interactive Swagger UI.
- **Automated Test Cases**: Unit and integration tests for models, views, and API endpoints.

---

## Tech Stack

- **Backend**: Django 5.x, Django REST Framework
- **Database**: PostgreSQL
- **Task Queue**: Celery
- **Message Broker**: Redis
- **API Documentation**: Swagger (drf-yasg)
- **Testing**: pytest / Django TestCase
- **Containerization**: Docker & Docker Compose


---

## How to Run

### Clone the repository

```bash
git clone https://github.com/solmaz-sahmani/BlogAPI.git
cd BlogAPI
```
---

### Build and run with Docker

```bash
docker-compose up --build
```

Visit: http://localhost:8000

---
## Access Swagger UI
```bash
http://127.0.0.1:8000/swagger/
```
---
## Project Structure
```bash

BlogAPI/
├── backend
├── compose.yml
├── Dockerfile
├── README.md
├── requirements.txt
└── scripts
```
