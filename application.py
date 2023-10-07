# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 09:20:54 2023

@author: nilay
"""


from flask import  Flask, render_template,request
from flask import Flask, render_template, request
from src.pipeline.predict_pipeline import CustomData,PredictPipeline
application=Flask(__name__)
app=application

#route
@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict_price():
    data=CustomData(
        km=float(request.form['km']),
        oprice=float(request.form['oprice']),
        year=int(request.form['year']),
        fuel_type=request.form['fuel_type'],
        transmission=request.form['transmission']
    )

    df=data.get_data_as_dataframe()

    predictPipeline=PredictPipeline()
    result=predictPipeline.model_prediction(df)
    return render_template('index.html',prediction_value=result[0])



if __name__ =='__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0' ,port=8080)
    



    