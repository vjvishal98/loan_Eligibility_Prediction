#importing  libraries
import numpy as np
from flask import Flask, render_template,request
import pickle

#Initialize the flask App
app = Flask(__name__)

#importing the model
model = pickle.load(open('svmp.pkl', 'rb'))

#default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')

#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    #Getting the values from index.html
    int_features = [x for x in request.form.values()]

    #converting the values in 2D array
    final_features = [np.array(int_features)]

    #prdicting the output
    prediction = model.predict(final_features)

    if prediction == 1:
        prediction = 'The applicant is eligible for loan'
    else:
        prediction = "The applicant is not eligible for loan"

    return render_template('index.html', pred=prediction)

if __name__ == "__main__":
    app.run(debug=True)