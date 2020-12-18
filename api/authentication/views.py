from rest_framework import generics, status
from rest_framework.response import Response

from .serializer import UserProfileSerializer, LoginSerializer


class RegisterView(generics.GenericAPIView):
    serializer_class = UserProfileSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            return Response(
                {'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'error':'email/password incorrect'}, status=status.HTTP_400_BAD_REQUEST)
