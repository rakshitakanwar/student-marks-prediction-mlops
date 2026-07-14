## Student Marks Prediction System using AWS SageMaker, Lambda & API Gateway

## Overview

This project demonstrates an end-to-end serverless machine learning deployment on AWS. A Linear Regression model is trained using Amazon SageMaker, deployed as a real-time inference endpoint, and exposed through AWS Lambda and API Gateway. A FastAPI backend communicates with the deployed endpoint, while a simple HTML frontend allows users to submit input values and receive real-time predictions.

---

## Architecture

```
HTML Frontend
       │
       ▼
    FastAPI
       │
       ▼
 API Gateway
       │
       ▼
 AWS Lambda
       │
       ▼
 SageMaker Endpoint
       │
       ▼
 ML Model (Linear Regression)
```

---

## Project Workflow

1. Created an Amazon S3 bucket to store the dataset and trained model artifacts.
2. Uploaded the dataset to the S3 bucket.
3. Trained a Linear Regression model using Amazon SageMaker.
4. Saved the trained model as `model.joblib`.
5. Compressed the model into `model.tar.gz`.
6. Uploaded both model artifacts to the S3 bucket.
7. Created and deployed a real-time SageMaker Endpoint.
8. Developed an AWS Lambda function to invoke the SageMaker endpoint.
9. Connected Lambda with Amazon API Gateway to expose a REST API.
10. Tested the deployed API successfully using Postman.
11. Developed a FastAPI backend to communicate with the API Gateway.
12. Built a simple HTML frontend for user interaction.
13. Successfully performed end-to-end prediction from the web interface.

---

## Technologies Used

* Python
* HTML, CSS, JavaScript
* FastAPI
* AWS S3
* Amazon SageMaker
* AWS Lambda
* Amazon API Gateway
* Postman
* Scikit-learn
* Joblib
* NumPy
* Pandas
* Boto3

---


## Features

* End-to-end machine learning deployment on AWS.
* Real-time prediction using a SageMaker Endpoint.
* Serverless architecture with Lambda and API Gateway.
* FastAPI backend for API integration.
* Simple HTML frontend for prediction requests.
* Successfully tested using Postman before frontend integration.

---

## API Request Example

```json
{
  "maths": 40,
  "english": 60
}
```

---

## Sample Response

```json
{
  "prediction": 52.37
}
```

---

## Future Improvements

* Add user authentication.
* Implement CI/CD using GitHub Actions.
* Containerize the application using Docker.
* Monitor inference logs using Amazon CloudWatch.
* Deploy the frontend using AWS Amplify or Amazon S3 Static Website Hosting.

---

## Author

**Rakshita Kanwar**
B.Tech (Computer Science - Artificial Intelligence)
Arya College of Engineering, Jaipur
