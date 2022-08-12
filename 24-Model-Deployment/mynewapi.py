from flask import Flask,request,jsonify
import joblib
import pandas as pd
#Create Flask app
app=Flask(__name__)
#Connect post Api call-->predict function
@app.route('/predict',methods=['POST'])#http://localhost:5000/predict
def predict():
    #GET JSON Request
    feat_data=request.json
    #Convert to pandas df(matches column names)
    df=pd.DataFrame(feat_data)
    df=df.reindex(columns=col_names)
    #Predict json
    prediction=list(model.predict(df))
    return jsonify({'prediction':str(prediction)})#Prediction
#load model and setup column names
if __name__=='__main__':
    model=joblib.load('final_model.pkl')
    col_names=joblib.load('column_names.pkl')
    app.run(debug=True)