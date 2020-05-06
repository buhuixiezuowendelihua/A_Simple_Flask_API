import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
from sklearn.externals import joblib

app = Flask(__name__)
model = joblib.load('E:/Flask_Sklearn/model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    file = request.files['file']
    data = pd.read_csv(file)
    #这里可以添加数据处理内容
    prediction = np.round(model.predict(data), 2)


    data["predict"] = pd.DataFrame(prediction)

    return render_template('index.html', data=data.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(debug=True)