from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from .models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price']


@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(data={"message": "Error"}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer.save()

    return Response(data={
        "message": "new product added successfully",
        "product": request.data
    }, status=status.HTTP_201_CREATED)



@api_view(['GET'])
def get_product(request, product_id):
    serializer = ProductSerializer(Product.objects.get(pk=product_id))
    return Response(serializer.data, status=status.HTTP_200_OK)
