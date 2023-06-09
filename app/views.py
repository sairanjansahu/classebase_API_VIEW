from django.shortcuts import render
from rest_framework.views import APIView
from app.models import *
from app.serializers import *
from rest_framework.response import Response


# Create your views here.

class Productjsd(APIView):
    def get(self,request):
        pqs=Product.objects.all()
        pqjd=Product_serializers(pqs,many=True)
        return Response(pqjd.data)

    def post(self,request):
        pmsd=Product_serializers(data=request.data)
        if pmsd.is_valid():
            spo=pmsd.save()
            return Response({'message':'product is created'})
        else:
            return Response({'failed':'product is not created'})

    def put(self,request):
        id=request.data['id']
        po=Product.objects.get(id=id)
        upd=Product_serializers(po,data=request.data)
        if upd.is_valid():
            upd.save()
            return Response({'message':'product is created'})
        else:
            return Response({'failed':'product is not created'})


