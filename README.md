# Serverless Task Automation Platform

## Project Overview

The Serverless Task Automation Platform is a lightweight event-driven system that enables users to automate tasks using triggers such as time-based schedules and API events. The platform simplifies workflow automation by allowing users to create rule-based triggers and actions without managing complex infrastructure.

---

## Problem It Solves

Many automation platforms are expensive, complex, or designed for enterprise use. Students and small developers need a simple, free, and easy-to-use automation solution to automate repetitive tasks, schedule workflows, and monitor execution status efficiently.

---

## Target Users (Personas)

### Student Developer

- Needs simple automation for academic projects
- Has limited cloud experience
- Prefers free and open-source tools

### Small Team Developer

- Automates repetitive development tasks
- Requires monitoring and execution logs
- Needs lightweight deployment

---

## Vision Statement

To provide a simple, scalable, and free automation platform that enables users to build event-driven workflows efficiently with minimal setup and high reliability.

---

## Key Features / Goals

- Rule-based automation creation
- Time-based and API-based triggers
- Automatic task execution
- Execution logging and monitoring
- Web-based user interface
- Docker-based deployment

---

## Success Metrics

- Successful creation and execution of automation rules
- Task execution success rate above 90%
- Stable system performance during testing
- Positive user feedback on usability

---

## Assumptions & Constraints

### Assumptions

- Users have access to the internet
- Users understand basic automation concepts
- Docker is available for local development

### Constraints

- Only free and open-source technologies are used
- Limited development timeline
- Academic project environment

---

## Branching Strategy

This project follows GitHub Flow.  
The main branch contains stable production-ready code. Feature branches such as `feature-rule-engine` are created for new functionality and merged into the main branch after testing.

---

## Local Development Tools

- Git
- Docker Desktop
- Python
- VS Code

## 🚀 Quick Start – Local Development

Follow the steps below to run the Serverless Task Automation Platform locally using Docker.

### Prerequisites

Ensure the following tools are installed:

- Git
- Docker Desktop
- Web Browser

---

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
