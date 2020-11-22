from flask import Flask, request
import numpy as np
import joblib
app = Flask(__name__)
@app.route('/home')
def Fn1():
    index = open('C:/Users/swara/Desktop/Nextup-Internship/venv/CCFD/index.html').read()
    return index
@app.route('/about')
def Fn2():
    about = open('C:/Users/swara/Desktop/Nextup-Internship/venv/CCFD/aboutus.html').read()
    return about
@app.route('/synopsis')
def Fn3():
    about = open('C:/Users/swara/Desktop/Nextup-Internship/venv/CCFD/synopsis.html').read()
    return about
@app.route('/predict')
def predictFn():
    pred = open('C:/Users/swara/Desktop/Nextup-Internship/venv/CCFD/predict.html').read()
    return pred
@app.route('/prediction')
def predictionFn():
	model = joblib.load('C:/Users/swara/Desktop/Nextup-Internship/venv/model.joblib')
	data = [
		int(request.args.get('V1')),
		int(request.args.get('V2')),
		int(request.args.get('V3')),
		int(request.args.get('V4')),
		int(request.args.get('V5')),
		int(request.args.get('V6')),
		int(request.args.get('V7')),
		int(request.args.get('V9')),
		int(request.args.get('V10')),
		int(request.args.get('V11')),
		int(request.args.get('V12')),
		int(request.args.get('V14')),
		int(request.args.get('V16')),
		int(request.args.get('V17')),
		int(request.args.get('V18')),
		int(request.args.get('V19'))
	]
	res = model.predict(np.array(data).reshape(1,-1))
	classes = ["Non-Fraud Transaction", "Fraud Transaction"]
	return classes[res[0]]