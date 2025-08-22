# Decision based on probability
import requests

customer = {
  "gender": "female",
  "seniorcitizen": 1,
  "partner": "yes",
  "dependents": "yes",
  "phoneservice": "yes",
  "multiplelines": "no_phone_service",
  "internetservice": "dsl",
  "onlinesecurity": "yes",
  "onlinebackup": "yes",
  "deviceprotection": "no",
  "techsupport": "yes",
  "streamingtv": "no",
  "streamingmovies": "no",
  "contract": "month-to-month",
  "paperlessbilling": "yes",
  "paymentmethod": "electronic_check",
  "tenure": 1,
  "monthlycharges": 29.85,
  "totalcharges": 29.85
}

url = "http://localhost:9696/predict"
response = requests.post(url, json=customer)
churn_proba = response.json()
print("Churn Probability:", churn_proba)

if churn_proba["churn_probability"] >= 0.5:
    print("Send email with promo")
else:
    print("Do not send an email") #note this will be done by a webservice