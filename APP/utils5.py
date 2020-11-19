import json
import numpy as np
import requests
from APP.loadData import load_data
# 加载数据
import time

def predict_postural(x):
    # （？，128，9）
    data = json.dumps({"instances": x.tolist()})
    headers = {"content-type": "application/json"}
    json_response = requests.post(
        'http://42.192.128.191:8501/v1/models/model:predict',
        data=data, headers=headers)
    # print(type(json_response.text))
    # print(type(eval(json_response.text)))\
    predictions = eval(json_response.text)['predictions']
    return [np.argmax(index)+1 for index in predictions]


if __name__ == '__main__':
    x_train,y_train,x_test,y_test = load_data()
    start = time.time()
    predictions = predict_postural(x_train[:10])
    end = time.time()
    print(predictions)
    print('time:',float(end)-float(start))



