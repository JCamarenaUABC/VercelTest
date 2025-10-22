#from flask import Flask, jsonify
#import sqlite3
import os
import requests
from flask import Flask, jsonify, request, render_template
import pyodbc
from bs4 import BeautifulSoup
#from flask_cors import CORS  #INSTALAR
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)  


@app.route("/hello", methods=['GET'])
def hello():
    return jsonify({"mensaje": "Hello JFCM"}) 

if __name__ == '__main__':
    app.run(debug=True)