# Security Advisory API

## Overview
A containerized Flask application for searching and retrieving GitHub Security Advisory (GHSA) information. This API provides access to security advisories stored as JSON files in a structured format.

## Features
- RESTful API endpoint to retrieve security advisories by GHSA ID
- Cross-Origin Resource Sharing (CORS) enabled
- JSON response format
- Containerized for easy deployment

## Prerequisites
- Docker

## Installation and Setup

### Using Docker
1. Clone the repository:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Build the Docker image:
   ```
   docker build -t software-sec .
   ```

3. Run the container:
   ```
   docker run -p 5000:5000 software-sec
   ```
   This maps port 5000 from the container to port 5000 on your host machine.

## API Usage

### Retrieving an Advisory
```
GET /api/advisories/<ghsa_id>
```

#### Example
```
curl http://localhost:5000/api/advisories/GHSA-jp4x-w63m-7wgm
```

#### Response
- **Success**: Returns the JSON data for the requested advisory
- **Not Found**: Returns a 404 status with an error message
- **Bad Request**: Returns a 400 status if GHSA ID is missing

## Project Structure
- `backend.py`: Main Flask application
- `process-info.py`: Script for processing advisory data
- `requirements.txt`: Python dependencies
- `entrypoint.sh`: Container entrypoint script
- `linear_advisories/`: Directory containing JSON files for each advisory

