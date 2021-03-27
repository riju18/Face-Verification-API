from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import os
from deepface import DeepFace
import cv2

root_dir = os.path.dirname(os.path.abspath(__file__))
img_dir = os.path.join(root_dir, 'images')


class HelloAPIView(APIView):
    def get(self, request):
        data = []
        message = ''
        img_file = request.query_params.get('filename')
        if img_file:
            img_name = root_dir + '\\' + img_file
            img = cv2.imread(img_name, cv2.COLOR_BGR2RGB)
            result = DeepFace.find(img, db_path=img_dir)
            if result.shape[0] > 0:
                for i, j in zip(result['identity'], result['distance']):
                    data.append({"path": i, "matched %": str(round(j*100, 2)) + "%"})
                message = "Employee ID: xxx"
            else:
                message = "Unknown Person"

        return Response({'data': data, 'message': message})
