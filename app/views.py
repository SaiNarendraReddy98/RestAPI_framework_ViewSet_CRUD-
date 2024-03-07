from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from app.models import *
from app.serializers import *

# Create your views here.

class ProductCrud(ViewSet):
    def list(self,request):
        PD = Product.objects.all()
        JDO = ProductModelSerializer(PD,many=True)
        return Response(JDO.data)
    
    def create(self,request):
        JD = request.data
        JDO = ProductModelSerializer(data=JD)
        if JDO.is_valid():
            JDO.save()
            return Response({'Created':'Data Created Successfully'})
        else:
            return Response({'error':'Invalid Data'})
    
    def retrieve(self,request,pk):
        PD = Product.objects.get(pk=pk)
        JDO = ProductModelSerializer(PD)
        return Response(JDO.data)
    
    def update(self,request,pk):
        PD = Product.objects.get(pk=pk)
        JD = request.data
        JDO = ProductModelSerializer(PD,data=JD)
        if JDO.is_valid():
            JDO.save()
            return Response({'Update':'Data updated successfully'})
        else:
            return Response({'error':'Data invalid'})
        
    def partial_update(self,request,pk):
        PD = Product.objects.get(pk=pk)
        JD = request.data
        JDO = ProductModelSerializer(PD,data=JD,partial=True)
        if JDO.is_valid():
            JDO.save()
            return Response({'Updated':'Data Updated Successfully'})
        else:
            return Response({'error':'Invalid data'})
        
    def destory(self,request,pk):
        Product.objects.get(pk=pk).delete()
        return Response({'Deleted':'Data Deleted Successfully'})
        
