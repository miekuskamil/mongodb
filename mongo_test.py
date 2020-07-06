#! /usr/bin/python3
# -*- coding: utf-8 -*-

import pymongo
from flask import Flask, render_template
from flask import request

'''
    Script to interrogate MongoDB, provide front-end Flask
    interface Jinja2 template engine renderer
'''

__author__ = "Kamil Miekus"
__copyright__ = "Copyright 2020, Author Org"
__credits__ = ["Kamil Miekus"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Kamil Miekus"
__email__ = "miekus@yahoo.co.uk"
__status__ = "Development"


#sample dict
mydict = {"name": "James", "address": "Most"}

#connect
client = pymongo.MongoClient('mongodb://192.168.0.3:27017/')

#create db
mydb = client["aci"]

#create collection
mycol = mydb["vrf"]

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

#-------------------------------#
#-------------------------------#
#-------------------------------#

@app.route('/')
def student():
    return render_template('student.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form.to_dict()
        mycol.insert_one(result)
    return render_template("result.html", result=result)

@app.route('/show')
def all_items():
    documents = mycol.find()
    response = []
    for document in documents:
        #document['_id'] = str(document['_id'])
        #document['name'] = str(document['name'])
        #document['address'] = str(document['address'])
        response.append(document)
    return render_template('base.html', pages=response)

if __name__ == '__main__':
    app.run(host='192.168.0.19')
