import os
import sys
import requests

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib


app = FastAPI(title="FastAPI MLOps Service")

# Setup CORS middleware so your HTML file can communicate with the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)






# ==========================
# API Gateway URL
# ==========================

API_GATEWAY_URL = "https:///satge-details/api-gateway-path/predict"

# ==========================
# Request Model
# ==========================

class Student(BaseModel):
    maths: float
    english: float

from fastapi.responses import FileResponse

@app.get("/")
def home():
    return FileResponse("index.html")
@app.post("/predict")
def predict(student: Student):

    payload = student.model_dump()

    try:

        response = requests.post(
            API_GATEWAY_URL,
            json=payload,
            headers={
                "Content-Type": "application/json"
            },
            timeout=30
        )

        response.raise_for_status()

        prediction = response.json()

        return {
            "status": "success",
            "prediction": prediction
        }

    except requests.exceptions.HTTPError as e:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.text
        )

    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )



if __name__ == "__main__":
    import uvicorn
    # Run using uvicorn server instead of native flask development server
    uvicorn.run(app, host='0.0.0.0', port=5000)