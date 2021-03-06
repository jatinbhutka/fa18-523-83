from flask import Flask, request
import json
import pandas as pd
import pickle
from xgboost import XGBClassifier

app = Flask(__name__) #create the Flask app

 

 

@app.route('/')

def welcome_page():

    print('Credit Scoring Algorithm')
             

              

              

@app.route('/json-get-results', methods=['POST']) #GET requests will be blocked

def json_get_results():

    req_data = request.get_json()
 
    df = pd.DataFrame.from_dict(req_data, orient='columns')

    y=df['SeriousDlqin2yrs']

    x=df[['RevolvingUtilizationOfUnsecuredLines','age','MonthlyIncome','NumberOfDependents','TotalNumberofTimesPastDue']]

    df_result=pd.DataFrame()
    df_result['ID']=df['Unnamed: 0']

    with open('src/docker/xgboost_model.pkl','rb') as f:
    	model = pickle.load(f)
    
    y_predict=model.predict(x)

    y_predict_df=pd.DataFrame(y_predict)

    df_result['SeriousDlqin2yrs']=y_predict_df

    data= df_result.to_json(orient='records')
    with open('data/processed/results.json', 'w') as fp:
        	fp.write(data + '\n')

    return 'JSON returned'

if __name__ == '__main__':

    app.run(host="0.0.0.0", port=80)



















