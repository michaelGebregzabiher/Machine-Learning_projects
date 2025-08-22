import pickle
#load the pipeline
with open("churn_model.pkl", "rb") as f_in:
    pipeline = pickle.load(f_in) #Reads the file and deserializes it back into Python objects.

customer_new = {
    'gender': 'female',
    'seniorcitizen': 1,
    'partner': 'yes',
    'dependents': 'yes',
    'phoneservice': 'yes',
    'multiplelines': 'no_phone_service',
    'internetservice': 'dsl',
    'onlinesecurity': 'yes',
    'onlinebackup': 'yes',
    'deviceprotection': 'no',
    'techsupport': 'yes',
    'streamingtv': 'no',
    'streamingmovies': 'no',
    'contract': 'month-to-month',
    'paperlessbilling': 'yes',
    'paymentmethod': 'electronic_check',
    'tenure': 1,
    'monthlycharges': 29.85,
    'totalcharges': 29.85
}

# Then predict a new customer probability of churn:
churn_proba = pipeline.predict_proba(customer_new)[0, 1]
churn_proba
# Decision based on probability
print("Send email with promo" if churn_proba >= 0.5 else "Do not send an email") #note this will be done by a webservice
