from rest_framework.decorators import api_view
from rest_framework.response import Response
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
    if serializer.is_valid() == True:
     serializer.save()
    return Response(serializer.data, status=201)
   else:
    return Response(serializer.errors, status=400)