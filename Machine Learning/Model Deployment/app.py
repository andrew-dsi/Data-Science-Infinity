
# import the required packages
from flask import Flask, render_template, request
import joblib
import pandas as pd

# instantiate the web-app
app = Flask(__name__)

# load our model pipeline object
model = joblib.load("model.joblib")

# outline the homepage or "default" page
# when a user visits this page, the home function will be run
@app.route("/")
def home():
    return render_template("index.html")

# outline the prediction page
# when a user visits the /predict page, the predict function will be run
@app.route('/predict', methods=['POST'])
def predict():
    
    # get input variables from form
    age = request.form.get('age')
    gender = request.form.get('gender')
    credit_score = request.form.get('credit_score')
    new_data = pd.DataFrame({"age" : [age], "gender" : [gender], "credit_score" : [credit_score]})
    
    # apply model pipeline to the input data and extract probability prediction
    pred_proba = model.predict_proba(new_data)[0][1]
    
    # render the page using result.html and include the predicted probability
    return render_template("result.html", prediction_text = f"{pred_proba:.0%}")
    
if __name__ == "__main__":
    app.run(debug=True)