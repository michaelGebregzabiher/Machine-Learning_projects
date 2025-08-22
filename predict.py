import pickle
import uvicorn
from fastapi import FastAPI
from typing import Dict, Any

app = FastAPI(title="churn_prediction")

#load the pipeline
with open("churn_model.pkl", "rb") as f_in:
    pipeline = pickle.load(f_in) #Reads the file and deserializes it back into Python objects.

def predict_single(customer): 
    # Predict the probability of churn for a single customer
    result = pipeline.predict_proba(customer)[0, 1]
    return float(result)

@app.post("/predict") #POST request because we are sending data to the server to process.
def predict(customer: Dict[str, Any]):       #tell fastapi what the input data type and its value(expectations)
    churn = predict_single(customer)
    return {
        "churn_probability": churn,
        "churn": bool(churn >= 0.5)
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)
# # Then predict a new customer probability of churn:
# churn_proba = pipeline.predict_proba(customer_new)[0, 1]
# churn_proba

