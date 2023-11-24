
# import libraries
import sys
import pandas as pd
import joblib

# Load our model pipeline object
model = joblib.load("model.joblib")

def predict(age: int, gender: str, credit_score: int):
    
    # specify input limits
    age_bounds = list(range(18, 121))
    gender_options = ['M', 'F']
    credit_score_bounds = list(range(0, 1001))
    
    # Apply limits
    if age not in age_bounds:
        raise ValueError("Age must be a whole number between 18 and 120")
        
    if gender not in gender_options:
        raise ValueError("Gender must be either M or F")
        
    if credit_score not in credit_score_bounds:
        raise ValueError("Credit Score must be a whole number between 0 and 1000")
         
    # Compile data together for prediction     
    new_data = pd.DataFrame({"age" : [age], "gender" : [gender], "credit_score" : [credit_score]})
    
    # Make prediction & extract probability of positive class
    pred_proba = model.predict_proba(new_data)[0][1] 
    
    return(f"Based on these customer attributes, our model predicts a purchase probability of {pred_proba:.0%}")

if len(sys.argv) != 4:
    print("Usage: script.py <age> <gender> <credit_score>")
    sys.exit(1)

try:
    # Convert arguments and handle any conversion errors
    age = int(sys.argv[1])
    gender = sys.argv[2].upper()  # Convert gender to uppercase to match the gender options
    credit_score = int(sys.argv[3])

    # Call the predict function with the converted arguments
    prediction = predict(age, gender, credit_score)
    print(prediction)

except ValueError as e:
    print(f"Input error: {e}")
    sys.exit(1)






