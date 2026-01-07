from flask import Flask,  flash, redirect, request, render_template, make_response, url_for
import json
import sys 
#import pandas as pd

app = Flask(__name__)

#web service
##api post
@app.route("/")  #บอกว่าเรียกใช้ web ไหน
def helloworld():
    return "Hello, World!"

@app.route("/name")  #บอกว่าเรียกใช้ web ไหน
def name():
    return "Kanvara"


@app.route('/request',methods=['POST']) 
def web_service_API():

    payload = request.data.decode("utf-8")
    inmessage = json.loads(payload) # ทำ json

    print(inmessage)
    
    json_data = json.dumps({'y': 'received!'}) # ส่งกลับไปว่าได้รับเเล้ววว
    return json_data

if _name_ == "_main_":   # run code 
    app.run(host='0.0.0.0',debug=True,port=5001)#host='0.0.0.0' = run on internet ,port=5001