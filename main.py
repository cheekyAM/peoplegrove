import numpy as np
from fastapi import FastAPI, Form
import pandas as pd
from starlette.responses import HTMLResponse
import pickle
from pydantic import BaseModel

#lets keep our data format fixed
class people(BaseModel):
    mentee_major:list
    mentee_help_topics:list
    mentee_experitse:list
    mentor_major:list
    mentor_help_topics:list
    mentor_experitse:list


# cleaning, processing, transforming the data
#our code from finalgrove functions like process, rare_insert,count_dict etc will come here

app = FastAPI()

# import model pickle file here
pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)

#write our test pipeline, eg. 
def my_pipeline(data): #pipeline
  #process and transform in required format for prediction
  return X


@app.get('/') #basic get view
def basic_view():
    return {"WELCOME": "GO TO /docs route, or /post or send post request to /predict "}

#this api on post of data will give the prediction
@app.post('/predict') #exposing a prediction functionality to make prediction on json data
def predict(data:people): #input is data of dictionary containing the values for the fields of people class
    data=data.dict()
    mentee_major=data[mentee_major]
    mentee_help_topics=data[mentee_help_topics]
    mentee_experitse=data[mentee_experitse]
    mentor_major=data[mentor_major]
    mentor_help_topics=data[mentor_help_topics]
    mentor_experitse=data[mentor_experitse]
    X = my_pipeline([mentee_major,mentee_help_topics,mentee_experitse,mentor_major,mentor_help_topics,mentor_experitse]) #cleaning and preprocessing of the sample
    prediction = classifier.predict(X) #making predictions
    
    return { 
        'prediction':prediction
    }

if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)