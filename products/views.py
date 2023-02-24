from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET', 'POST'])
def products_list(request):
    if request.method == "GET":
        products = Product.objects.all()
        serialzer = ProductSerializer(products,many=True)
        return Response(serialzer.data, status=status.HTTP_200_OK)
    

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        






    # if request.method == 'GET':
    #     product = Product.objects.all()
    #     serializer = ProductSerializer(product, many = True)
    #     return Response(serializer.data)
    # elif request.method == 'POST':
    #     pass
    



# Create your views here.
