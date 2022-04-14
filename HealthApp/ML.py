import joblib

def Predict(Sugar,Pressure,BMI,Pedigree,Age):
    model = joblib.load('Diabetes_jlib')
    x = model.predict([[Sugar,Pressure,BMI,Pedigree,Age]])
    return x
