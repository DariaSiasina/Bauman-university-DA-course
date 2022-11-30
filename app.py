import pickle
import flask
from flask import Flask
from flask import render_template, request
from sklearn import svm

app = Flask(__name__, template_folder='.')
@app.route('/', methods = ['POST', 'GET'])
@app.route('/index', methods = ['POST', 'GET'])

def main():
    if flask.request.method == 'GET':
        return render_template('main.html')

    if flask.request.method == 'POST':
        # load model
        load_model1 = pickle.load(open('svm1.pkl', 'rb'))
        load_model2 = pickle.load(open('svm2.pkl', 'rb'))

            
        IW = float(flask.request.form['IW'])
        IF = float(flask.request.form['IF'])
        VW = float(flask.request.form['VW'])
        FP = float(flask.request.form['FP'])

        y_pred_Depth = load_model1.predict([[IW, IF, VW, FP]])
        y_pred_Width = load_model2.predict([[IW, IF, VW, FP]])

        return render_template('main.html', result_depth = y_pred_Depth, result_width = y_pred_Width)


if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)