# CI/CD Mini-Project with Jenkins

This is a Flask application configured for CI/CD testing with Jenkins on Windows OS.

## Project Structure

```
test-flask/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── Jenkinsfile           # Jenkins pipeline configuration
├── templates/
│   └── index.html        # HTML template
└── tests/
    └── test_app.py       # Unit tests
```

## Features

- **Flask Web Application**: Simple web app with health check endpoint
- **Jenkins Pipeline**: Complete CI/CD pipeline with build, test, and deploy stages
- **Docker Support**: Containerized application for consistent deployment
- **Unit Tests**: Comprehensive test suite with health checks
- **Windows Compatibility**: Configured specifically for Jenkins on Windows OS

## Jenkins Pipeline Stages

1. **Cleanup Previous Build**: Removes any existing containers
2. **Prepare Environment**: Sets up Python virtual environment and installs dependencies
3. **Run Tests**: Executes unit tests to ensure code quality
4. **Build Docker Image**: Creates Docker image for the application
5. **Deploy Application**: Runs the containerized application and performs health checks

## Local Development

1. Create virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate virtual environment:
   ```bash
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run tests:
   ```bash
   python -m unittest discover -s tests
   ```

5. Start the application:
   ```bash
   python app.py
   ```

## Docker Deployment

1. Build the image:
   ```bash
   docker build -t test-flask .
   ```

2. Run the container:
   ```bash
   docker run -d -p 5000:5000 test-flask
   ```

3. Access the application at `http://localhost:5000`

## Jenkins Setup

1. Create a new Jenkins pipeline job
2. Configure the job to use this repository
3. Set the pipeline script to use the `Jenkinsfile`
4. Ensure Docker is installed and accessible on the Jenkins agent
5. Run the pipeline

## Health Check

The application includes a health check endpoint at `/health` that returns:
```json
{
  "status": "healthy",
  "message": "Flask app is running"
}
```

This endpoint is used by the Jenkins pipeline to verify successful deployment.

