# AI-Powered E-Commerce Search Engine for Cars

This project is a full-stack AI-powered search engine for cars, built with FastAPI for the backend, Next.js for the frontend, and Dockerized for easy deployment. The backend leverages a pre-trained NLP model to provide semantic search capabilities.

## Features

- **AI-Powered Search**: Search for cars using natural language queries.
- **FastAPI Backend**: RESTful API for handling car data and search.
- **Next.js Frontend**: User-friendly interface for accessing the search engine.
- **PostgreSQL Database**: Stores car details efficiently.
- **Dockerized Setup**: Simplified deployment and scaling.

## Prerequisites

Make sure you have the following installed:

- Docker
- Docker Compose
- Python 3.12
- Node.js 18+

## Project Structure

## Setup Instructions

Follow these steps to set up and run the project locally:

1. **Clone the Repository**
    ```bash
    git clone git@github.com:rochdikhalid/ai-powered-ecommerce-search-engine.git
    cd ai-powered-ecommerce-search-engine
    ```

2. **Configure Environment Variables**

   Create a `.env` file in the backend and frontend directories if needed, and add necessary configurations such as `DATABASE_URL`.

3. **Build and Start Services**

   Run the following command to build and start the containers:
    ```bash
    docker-compose up --build
    ```

4. **Access the Application**
   - **Frontend**: Open `http://localhost:3000`
   - **Backend**: Open `http://localhost:8000/docs` for API documentation

## Backend

### Key Features

- **API Documentation**: Auto-generated Swagger UI available at `/docs`.
- **AI Search**: NLP-based semantic search for car queries.
- **Database**: PostgreSQL integration for storing and retrieving car details.

### Backend Directory Structure

```bash
.
├── backend/          # FastAPI backend
│   ├── src/          # Backend source code
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/         # Next.js frontend
│   ├── pages/        # Frontend pages
│   ├── components/   # Reusable components
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## Frontend

### Key Features

- **Responsive Design**: Built with Next.js and styled for a seamless user experience.
- **Search Interface**: Intuitive UI for entering search queries and viewing results.

### Frontend Directory Structure

```bash
frontend/
├── pages/            # Next.js pages
├── components/       # Reusable components
├── public/           # Static assets
├── package.json      # Node.js dependencies
└── Dockerfile        # Frontend Dockerfile
```

## Database

### Setup

The database is a PostgreSQL instance running in a Docker container. Data is populated using the `load_data.py` script.

### Running the Data Loader

```bash
docker exec -it <backend-container-id> python /app/load_data.py