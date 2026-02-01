# Serverless Task Automation Platform

## Project Overview

The Serverless Task Automation Platform is a lightweight event-driven system that enables users to automate tasks using triggers such as time-based schedules and API events. The platform simplifies workflow automation by allowing users to create rule-based triggers and actions without managing complex infrastructure.

## Branching Strategy

This project follows GitHub Flow.  
The main branch contains stable production-ready code. Feature branches such as `feature-rule-engine` are created for new functionality and merged into the main branch after testing.

## Local Development Tools

- Git
- Docker Desktop
- Python
- VS Code

## Quick Start – Local Development

Follow the steps below to run the Serverless Task Automation Platform locally using Docker.

### Prerequisites

Ensure the following tools are installed:

- Git
- Docker Desktop
- Web Browser

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
cd serverless-task-automation-platform
```

### Step 2: Build Docker Image

```bash
docker build -t automation-app backend/
```

### Step 3: Run Docker Container

```bash
docker run -p 5000:5000 automation-app
```

### Step 4: Access Application

Open your browser and navigate to: http://localhost:5000

### Step 5: Stop the Application

To stop the running container, press: CTRL + C
