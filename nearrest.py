from flask import Flask,jsonify,request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import json
from requests import post
import dropbox
from dropbox.exceptions import AuthError
import io

DROPBOX_ACCESS_TOKEN = 'sl.BWWqMzGPp3v4F951kZDY3Jk66Cnj2tQ4ofr0p2mGK3F92o8WM_Y1aMLoUIU4Vwyj-GZUqmsvBDp96-q7zQv6elde9xC5bDDXikSfEvUPUycuLQHeBy07bJM8hoWneEXCbnhiYayG2kXd'
file_url = 'https://www.dropbox.com/s/3x7jzgmvycr8lta/nearprojects.json?dl=0'

app = Flask(__name__)
api = Api(app)

# with open('nearprojects.json') as json_file:
#     data = json.load(json_file)

def dropbox_connect():  
    try:
        dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)
    except AuthError as e:
        print('Error connecting to Dropbox with access token: ' + str(e))
    return dbx

def read_dropbox_file():  
    dbx = dropbox_connect()  
    res = dbx.sharing_get_shared_link_file(url = file_url)
    with io.BytesIO(res[1].content) as stream:
        data = json.load(stream)
        df = pd.DataFrame(data)
    return df
    
@app.route('/', methods = ['GET','POST'])
def home():
    return 'Near APIs Endpoints'


@app.route('/Series/<name>', methods=['GET'])
def Series(name):    
    df = read_dropbox_file()
    #return {'data': list(filter(lambda x: x.get('Series', '')=='NEAR', data))}, 200  # return data and 200 OK    
    name = name.upper()
    df['Series'] = df['Series'].str.upper()
    df = df[df['Series'].str.contains(name,na= False)]    
    return jsonify({'data': df.to_dict('records')})

@app.route('/AllProjects/HasDApp', methods=['GET'])
def DApp():
    df = read_dropbox_file()
    df = df[~df['DApp Link'].isnull()] 
    return jsonify({'data': df.to_dict('records')})

@app.route('/AllProjects/<name>', methods=['GET'])
def ProjectName(name):
    df = read_dropbox_file()
    name = name.upper()
    df['ProjectName'] = df['ProjectName'].str.upper()
    df = df[df['ProjectName'].str.contains(name,na= False)]  
    return jsonify({'data': df.to_dict('records')})

@app.route('/AllProjects', methods=['GET'])
def AllProjects():    
    df = read_dropbox_file()    
    return jsonify({'data': df.to_dict('records')})

@app.route('/AllProjects/HasGrants', methods=['GET'])
def HasGrants():
    df = read_dropbox_file()
    df = df[~df['Grants'].isnull()] 
    return jsonify({'data': df.to_dict('records')})

@app.route('/Grants/<providername>', methods=['GET'])
def Grants(providername):
    df = read_dropbox_file()
    providername = providername.upper()
    df['Grants'] = df['Grants'].str.upper()
    df = df[df['Grants'].str.contains(providername,na= False)]  
    return jsonify({'data': df.to_dict('records')})

@app.route('/Category/<categoryname>', methods=['GET'])
def Category(categoryname):
    df = read_dropbox_file()
    categoryname = categoryname.upper()
    df['Category'] = df['Category'].str.upper()
    df = df[df['Category'].str.contains(categoryname,na= False)]  
    return jsonify({'data': df.to_dict('records')})

@app.route('/AllProjects/Links/<projectname>', methods=['GET'])
def GetAllLinks(projectname):
    df = read_dropbox_file()
    projectname = projectname.upper()
    df['ProjectName'] = df['ProjectName'].str.upper()
    df = df[df['ProjectName'].str.contains(projectname,na= False)]  
    filtered_df = df[['ProjectName','Website Link','Buy Link','Stake Link','DApp Link','Facebook','Twitter','Github','Telegram','Discord','Linkedin','Medium','Other Links']]
    return jsonify({'data': filtered_df.to_dict('records')})

@app.route('/AllProjects/Tokens/<projectname>', methods=['GET'])
def GetTokenDetails(projectname):
    df = read_dropbox_file()
    projectname = projectname.upper()
    df['ProjectName'] = df['ProjectName'].str.upper()
    token_df = df[df['ProjectName'].str.contains(projectname,na= False)]  
    filtered_token_df = token_df[['ProjectName','Near Token','Aurora Token','Ethereum Token','Other Tokens']]
    return jsonify({'data': filtered_token_df.to_dict('records')})

@app.route('/Projects/Create',methods = ['POST'])
def CreateProject(): 
    dbx = dropbox_connect() 
    df = read_dropbox_file()
    df_json = df.append(request.get_json(),ignore_index = True)    
    with io.StringIO() as stream:
        json.dump(df_json.to_dict('records'), stream, indent=4) # Ident param is optional
        stream.seek(0)
        dbx.files_upload(stream.read().encode(), "/nearprojects.json", mode=dropbox.files.WriteMode.overwrite)
    return "Success"


# # if __name__ == '__main__':
# #     app.run()  # run our Flask app