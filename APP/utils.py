import tensorflow as tf

# import numpy as np
# import cv2
import sys

from tensorflow.python.framework import tensor_util
from APP.loadData import load_data
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2_grpc
from grpc.beta import implementations


# 加载数据
x_train,y_train,x_test,y_test = load_data()


# # 利用grpc 进行连接


channel = implementations.insecure_channel("42.192.128.191", 8500) #服务器IP地址
stub = prediction_service_pb2_grpc.PredictionServiceStub(channel._channel)
request = predict_pb2.PredictRequest()
# 模型的名称
request.model_spec.name = "har"
# 签名的名称
request.model_spec.signature_name = tf.compat.v1.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY
# request.model_spec.signature_name = "serving_default"
# 每次只支持传入一条数据进行预测，传入数据时要注意数据格式和模型定义时的格式一致
print(request.inputs)
request.inputs['input_1'].CopyFrom(tf.make_tensor_proto(x_test[0],dtype=tf.float32))

# response返回的是protobuff的格式
response = stub.Classify.future(request)
# print(response)
# 这里的a就是模型的返回结果，是tensorProto格式
a = response.result()
# .outputs["scores"]

#tensorflow 2.0弃用
# b = tf.MakeNdarray(a)
print(a)
print(a.shape)
# if b[0][0]>b[0][1]:
#     print(0)
# else:
#     print(1)
