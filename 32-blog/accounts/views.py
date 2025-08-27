from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

login = obtain_auth_token
User = get_user_model()

class Logout(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.user.auth_token.delete()
        return Response({'message': f"Bye {request.user.username}!"}, status=status.HTTP_204_NO_CONTENT)


class Register(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

