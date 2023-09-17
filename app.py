from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
import matplotlib
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('Customer_Churn_Prediction.pkl', 'rb'))

@app.route('/', methods=['GET'])

def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        CustomerID = int(request.form['CustomerID'])
        Name = String(request.form['Name'])
        Age = int(request.form['Age'])
        Total_Usage_GB = int(request.form['Total_Usage_GB'])
        Monthly_Bill = float(request.form['Monthly_Bill'])
        Geography = request.form['Geography']
        if(Geography == 'Los_Angeles'):
            Geography_Los_Angeles = 1
            Geography_New_York = 0
            Geography_Miami = 0
            Geography_Houston = 0
            Geography_Chicago = 0
                
        elif(Geography_Germany == 'Houston'):
            Geography_Los_Angeles = 0
            Geography_New_York = 0
            Geography_Miami = 0
            Geography_Houston = 1
            Geography_Chicago = 0

        elif(Geography_Germany == 'Chicago'):
            Geography_Los_Angeles = 0
            Geography_New_York = 0
            Geography_Miami = 0
            Geography_Houston = 0
            Geography_Chicago = 1

        elif(Geography_Germany == 'Miami'):
            Geography_Los_Angeles = 0
            Geography_New_York = 0
            Geography_Miami = 1
            Geography_Houston = 0
            Geography_Chicago = 0
        
        else:
            Geography_Los_Angeles = 0
            Geography_New_York = 1
            Geography_Miami = 0
            Geography_Houston = 0
            Geography_Chicago = 0

        Gender_Male = request.form['Gender_Male']
        if(Gender_Male == 'Male'):
            Gender_Male = 1
            Gender_Female = 0
        else:
            Gender_Male = 0
            Gender_Female = 1

        prediction = model.predict([[CustomerID,Name,Age,Total_Usage_GB,Monthly_Bill,Geography,Gender_Male]])
        if prediction==1:
             return render_template('index.html',prediction_text="The Customer will leave the bank")
        else:
             return render_template('index.html',prediction_text="The Customer will not leave the bank")
                
if __name__=="__main__":
    app.run(debug=True)