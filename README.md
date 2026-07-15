# Student Marks Prediction - End-to-End ML Deployment

## Project Overview

Student Marks Prediction is an end-to-end Machine Learning deployment project that predicts student marks based on input features.

The project covers the complete ML lifecycle including dataset storage, model training, deployment on Amazon SageMaker, API integration using AWS Lambda and API Gateway, API testing, and Docker-based application deployment.

The objective of this project is to build and deploy a production-ready Machine Learning prediction system using AWS cloud services.

---

# Architecture Workflow

```
Student Dataset
       |
       ↓
Amazon S3
       |
       ↓
Amazon SageMaker
       |
       ↓
Model Training
       |
       ↓
inference.py
       |
       ↓
SageMaker Endpoint
       |
       ↓
AWS Lambda
       |
       ↓
API Gateway
       |
       ↓
Prediction API URL
       |
       ↓
Postman Testing
       |
       ↓
Docker Frontend + Backend Deployment
```

---

# Project Workflow

## 1. Dataset Preparation

* Created an Amazon S3 bucket for storing project data.
* Uploaded the student marks dataset into S3.
* Created a separate `model` folder for storing model-related files and deployment artifacts.

### S3 Folder Structure

```
S3 Bucket
│
├── dataset/
│      └── student_marks.csv
│
└── model/
       └── model joblib

```

---

# 2. Model Training using Amazon SageMaker

* Configured Amazon SageMaker environment.
* Loaded the student marks dataset from Amazon S3.
* Performed required data preprocessing.
* Trained the Machine Learning model.
* Generated the trained model artifact.

The trained model was prepared for deployment using SageMaker inference architecture.

---

# 3. SageMaker Model Deployment

After model training, the model was deployed on Amazon SageMaker.

Created an `inference.py` file responsible for handling prediction requests.

### inference.py Responsibilities

* Loading the trained model.
* Receiving input data from API requests.
* Performing prediction.
* Returning model output.

### Inference Flow

```
Input Data
     |
     ↓
inference.py
     |
     ↓
Trained ML Model
     |
     ↓
Predicted Student Marks
```

A real-time SageMaker Endpoint was created successfully for serving predictions.

---

# 4. SageMaker Endpoint Creation

* Created SageMaker Model.
* Configured deployment settings.
* Created a real-time endpoint.
* Verified endpoint status after deployment.

The endpoint provides real-time prediction capability for incoming student data.

---

# 5. AWS Lambda Integration

An AWS Lambda function was created to communicate with the SageMaker Endpoint.

Lambda acts as a serverless middleware between API Gateway and SageMaker.

### Request Flow

```
Client Request
      |
      ↓
API Gateway
      |
      ↓
AWS Lambda
      |
      ↓
SageMaker Endpoint
      |
      ↓
Prediction Response
```

---

# 6. API Gateway Integration

Amazon API Gateway was configured to expose the ML model as a REST API.

Steps performed:

* Created REST API.
* Created `/predict` POST endpoint.
* Connected API Gateway with Lambda.
* Deployed API stage.
* Generated public API URL.

Example Endpoint:

```
POST /predict
```

---

# 7. API Testing using Postman

The deployed API was tested using Postman.

### Sample Request

```json
{
    "feature_1": "value",
    "feature_2": "value"
}
```

### Sample Response

```json
{
    "prediction": "Student Predicted Marks"
}
```

Postman testing confirmed successful communication between API Gateway, Lambda, and SageMaker Endpoint.

---

# 8. Docker Deployment

After successful API testing, the application was containerized using Docker.

Implemented:

* Dockerized backend application.
* Connected frontend and backend services.
* Ran the complete application using Docker containers.

### Docker Architecture

```
Frontend Container
        |
        ↓
Backend Container
        |
        ↓
API Gateway
        |
        ↓
AWS Lambda
        |
        ↓
SageMaker Endpoint
```

---

# Final System Architecture

```
                    User
                     |
                     ↓
                 Frontend
                     |
                     ↓
                 Backend API
                     |
                     ↓
              Amazon API Gateway
                     |
                     ↓
                AWS Lambda
                     |
                     ↓
          Amazon SageMaker Endpoint
                     |
                     ↓
            Student Marks ML Model
                     |
                     ↓
             Predicted Marks Output
```



## SageMaker Endpoint

(Add SageMaker endpoint screenshot here)

---

## API Gateway Configuration

(Add API Gateway screenshot here)

---

## Postman API Testing

(Add successful API response screenshot here)

---

## Docker Deployment

(Add Docker running containers screenshot here)

---

# Key Learnings

* Built an end-to-end Machine Learning deployment pipeline.
* Learned Amazon SageMaker model deployment.
* Created real-time ML inference endpoint.
* Integrated SageMaker with AWS Lambda.
* Developed REST API using API Gateway.
* Tested cloud ML APIs using Postman.
* Containerized applications using Docker.
* Understood complete ML model production workflow.

---

# Future Improvements

* Add CI/CD pipeline using GitHub Actions.
* Add model monitoring using Amazon CloudWatch.
* Implement automated model retraining pipeline.
* Deploy frontend and backend on cloud infrastructure.

```
```
