from flask import Flask,jsonify
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import json

app = Flask(__name__)
api = Api(app)

with open('combineddata.json') as json_file:
    data = json.load(json_file)
    

@app.route('/Series/<name>', methods=['GET'])
def Series(name):    
    df = pd.DataFrame(data) 
    #return {'data': list(filter(lambda x: x.get('Series', '')=='NEAR', data))}, 200  # return data and 200 OK    
    name = name.upper()
    df['Series'] = df['Series'].str.upper()
    df = df[df['Series'].str.contains(name,na= False)]    
    return jsonify({'data': df.to_dict('records')})

@app.route('/AllProjects/HasDApp', methods=['GET'])
def DApp():
    df = pd.DataFrame(data)
    df = df[~df['DApp Link'].isnull()] 
    return jsonify({'data': df.to_dict('records')})

@app.route('/AllProjects/<name>', methods=['GET'])
def ProjectName(name):
    df = pd.DataFrame(data)
    name = name.upper()
    df['ProjectName'] = df['ProjectName'].str.upper()
    df = df[df['ProjectName'].str.contains(name,na= False)]  
    return jsonify({'data': df.to_dict('records')})

@app.route('/AllProjects', methods=['GET'])
def AllProjects():
    df = pd.DataFrame(data)     
    return jsonify({'data': df.to_dict('records')})

@app.route('/AllProjects/HasGrants', methods=['GET'])
def HasGrants():
    df = pd.DataFrame(data)
    df = df[~df['Grants'].isnull()] 
    return jsonify({'data': df.to_dict('records')})

@app.route('/Grants/<providername>', methods=['GET'])
def Grants(providername):
    df = pd.DataFrame(data)
    providername = providername.upper()
    df['Grants'] = df['Grants'].str.upper()
    df = df[df['Grants'].str.contains(providername,na= False)]  
    return jsonify({'data': df.to_dict('records')})

if __name__ == '__main__':
    app.run()  # run our Flask app