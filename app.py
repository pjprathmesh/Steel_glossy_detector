#import requests
#import base64
#img_file='C:\\Users\PRATHMESH\Desktop\college project\SampleImages\Image5.jpg'
#with open(img_file, "rb") as image_file:
    #encoded_string = base64.b64encode(image_file.read())
#print(requests.post("http://127.0.1.1:5000/",data={"image":encoded_string}).text)

from flask import Flask,request
from flask_restful import Resource,Api
import cv2
import matplotlib.pyplot as plt
import base64
import numpy as np

app=Flask(__name__)
api=Api(app)
class Image(Resource):
    def post(self):
        return "ok done"
#         tem=request.form
        
#         with open("imageToSave.png", "wb") as fh:
#             fh.write(base64.decodebytes(bytes(tem["image"], 'utf-8') ))
            
#         img=cv2.imread("imageToSave.png",3)
#         img1=img.reshape((-1,3))
#         vectorized=np.float32(img1)

#         ret,label,center=cv2.kmeans(vectorized,3,None,(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0),10,cv2.KMEANS_PP_CENTERS)
#         print(center)
#         vector=np.sum(center,axis=1)
#         sort_vector=sorted(vector)
#         max_vector=np.where(vector==sort_vector[-1])
#         min_vector=np.where(vector==sort_vector[-2])
#         medium_vector=np.where(vector==sort_vector[-3])

#         uni=np.unique(label,return_counts=True)
#         print(uni)
#         whiteness=uni[1][max_vector][0]
#         silverness=uni[1][min_vector][0]
#         blackness=uni[1][medium_vector][0]
#         percent_whiteness=whiteness/(whiteness+silverness+blackness)*100
#         percent_silverness=silverness/(whiteness+silverness+blackness)*100
#         print("% of white",(percent_whiteness))
#         print("% of silver",(percent_silverness))
#         print("ratio w/s",percent_whiteness/percent_silverness)

#         prob=5-np.round((percent_whiteness/percent_silverness)*5)
#         if(prob<0):
#             prob=0
#             print("probablity",0)
#         elif prob>3:
#             prob=3
#             print("probablity",3)
#         else:
#             print("probablity",prob)
        
#         return {"prob":prob}
        
#         return "ok done"
api.add_resource(Image,'/')
if __name__=="__main__":
    app.run(debug=True)
