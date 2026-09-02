# Python Flask REST API

A simple REST API built with Flask for managing items.

## Features

- CRUD operations for items
- Health check endpoint
- JSON responses
- Dockerized application
- Production-ready with Gunicorn

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Welcome message |
| GET | /health | Health check |
| GET | /api/items | Get all items |
| POST | /api/items | Create new item |
| GET | /api/items/:id | Get item by ID |
| PUT | /api/items/:id | Update item |
| DELETE | /api/items/:id | Delete item |

## Local Development

### Prerequisites
- Python 3.11+
- pip

### Setup

```bash
cd python_rest_api

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

The API will be available at `http://localhost:5000`

## Docker

### Build Image

```bash
docker build -t flask-rest-api:latest .
```

### Run Container

```bash
docker run -p 5000:5000 flask-rest-api:latest
```

## Usage Examples

### Create Item
```bash
curl -X POST http://localhost:5000/api/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Item 1", "description": "First item"}'
```

### Get All Items
```bash
curl http://localhost:5000/api/items
```

### Get Item by ID
```bash
curl http://localhost:5000/api/items/1
```

### Update Item
```bash
curl -X PUT http://localhost:5000/api/items/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated Item", "description": "Updated description"}'
```

### Delete Item
```bash
curl -X DELETE http://localhost:5000/api/items/1
```

### Health Check
```bash
curl http://localhost:5000/health
```

## CI/CD

The project includes a GitHub Actions workflow that:
- Builds the Docker image
- Runs security scans
- Pushes to Docker Hub (on main branch)
- Supports multi-platform builds (amd64, arm64)

## Environment Variables

- `PORT` - Port to run the application (default: 5000)

## Production Considerations

- Uses Gunicorn as WSGI server
- Runs as non-root user
- Includes health checks
- Multi-worker configuration
- Lightweight Python slim image
