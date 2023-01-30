from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import Productsserializer
from .models import Products 

@api_view(['GET', 'POST'])
def products_list(request):

   if request.method == 'GET':
    products = Products.objects.all()
    serializer = Productsserializer(products, many=True)
    return Response(serializer.data)


   elif request.method == 'POST':
    serializer = Productsserializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
   
@api_view(['GET', 'PUT', 'DELETE'])
def products_detail(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == 'GET':
     serializer = Productsserializer(product);
     return Response(serializer.data)
    elif request.method == 'PUT':
         serializer = Productsserializer(product, data=request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return Response(serializer.data)
    elif request.method == 'DELETE':
         product.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
    




# if request.method == 'GET':
#     serializer = Productsserializer(product)
# elif request.method == 'PUT':
#      serializer = Productsserializer(product, data=request.data)
#      serializer.is_valid(raise_exception=True)
#      serializer.save()
#      return Response(serializer.data)

        
   