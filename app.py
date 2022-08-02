import numpy as np
import joblib
from flask import Flask, request, jsonify, render_template
from pandas import array
import os

#create flask app
app =  Flask(__name__)

# load the model from joblib
churn_model = joblib.load('pipe_model.joblib', 'r+')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods  = ["POST"])
def predict():
           
    Months_Inactive_12_mon = int(request.form['Months_Inactive_12_mon'])
    Credit_Limit = float(request.form['Credit_Limit'])
    Total_Revolving_Bal = float(request.form['Total_Revolving_Bal'])
    Total_Trans_Amt = float(request.form['Total_Trans_Amt'])
    Avg_Utilization_Ratio = float(request.form['Avg_Utilization_Ratio'])

    array = np.array([[Months_Inactive_12_mon, Credit_Limit, Total_Revolving_Bal,
                            Total_Trans_Amt, Avg_Utilization_Ratio]])

    prediction = churn_model.predict(array)

    return render_template('result.html', prediction_text_ = "This customer is belongs to cluster : {}".format(prediction[0]))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", threaded=True, port=port)