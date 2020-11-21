from flask import Flask, request
import numpy as np
import joblib

app = Flask(__name__)

@app.route('/home')
def Fn1():
    main = open('main.html').read()
    return main

@app.route('/about')
def Fn2():
    return 'About 1'

@app.route('/predict')
def predictFn():
	model = joblib.load('model.joblib')

	data = [int(request.args.get('rnd')),int(request.args.get('adm')),int(request.args.get('mkt'))]

	res = model.predict(np.array(data).reshape(1,-1))

	return str(res[0])