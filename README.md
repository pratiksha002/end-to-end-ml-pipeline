# End-to-End ML Pipeline with FastAPI & Docker

## 📌 Project Overview

This project is a complete production-style Machine Learning pipeline built using:

- Python
- Scikit-learn
- FastAPI
- Docker

The system automates the entire ML workflow including:

- Data ingestion
- Data validation
- Data cleaning
- Feature transformation
- Model training
- Artifact persistence
- Real-time inference API
- Dockerized deployment

The goal of this project is not just model training, but building a reusable ML engineering infrastructure similar to real-world production systems.

---

# 🚀 Features

## ✅ Data Pipeline
- Automated CSV ingestion
- Schema validation
- Missing value handling
- Duplicate removal

## ✅ Feature Engineering
- Numerical scaling
- Categorical encoding
- Reusable preprocessing pipeline

## ✅ Model Training
- Train/Test split
- Linear Regression training
- Model evaluation
- Metrics logging

## ✅ Artifact Management
- Save trained model
- Save preprocessing pipeline
- Persistent reusable artifacts

## ✅ FastAPI Inference Service
- REST API endpoints
- Real-time predictions
- Pydantic request validation
- Interactive Swagger UI

## ✅ Dockerized Deployment
- Fully containerized application
- Reproducible environments
- Portable deployment setup

---

# 🧠 System Architecture

```text
Raw Data
   ↓
Data Ingestion
   ↓
Data Validation
   ↓
Data Cleaning
   ↓
Feature Transformation
   ↓
Model Training
   ↓
Artifact Saving
   ↓
FastAPI Inference API
   ↓
Docker Deployment

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd end-to-end-pipeline
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the ML Pipeline

Run the complete training pipeline:

```bash
python main.py
```

This will:
- ingest data
- validate schema
- clean data
- transform features
- train model
- generate artifacts

---

# 🌐 Running FastAPI Locally

Start API server:

```bash
uvicorn app.main:app --reload
```

Open Swagger Docs:

```text
http://localhost:8000/docs
```

---

# 🧪 Sample Prediction Request

```json
{
  "age": 30,
  "department": "HR",
  "experience": 5
}
```

---

# 🐳 Docker Deployment

## Build Docker Image

```bash
docker build --no-cache -t ml-pipeline-api .
```

---

## Run Docker Container

```bash
docker run -p 8000:8000 ml-pipeline-api
```

---

## Access API

```text
http://localhost:8000/docs
```

---

# 📊 Technologies Used

| Category | Technology |
|---|---|
| Programming | Python |
| ML Library | Scikit-learn |
| API Framework | FastAPI |
| Containerization | Docker |
| Data Handling | Pandas |
| Serialization | Joblib |
| Validation | Pydantic |
| Config Management | YAML |

---

# 🧠 Key Engineering Concepts Implemented

- Modular ML pipeline architecture
- Workflow orchestration
- Feature engineering pipeline
- Artifact lifecycle management
- Real-time inference systems
- API-based ML serving
- Docker containerization
- Reproducible deployment environments

---

# 🔥 Future Improvements

- Advanced ML models (XGBoost, LightGBM)
- Cloud deployment (AWS/GCP/Azure)
- CI/CD pipelines
- Experiment tracking
- Model monitoring
- Drift detection
- Kubernetes deployment
- Database integration

---

# 📌 Learning Outcomes

This project demonstrates:
- Machine Learning Engineering
- MLOps Fundamentals
- Backend API Development
- Production Deployment Concepts
- Docker-Based Infrastructure

