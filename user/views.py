

import logging

from .models import NotesUser
from .serializers import LoginSerializer
from .serializers import NotesUserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate

logging.basicConfig(filename="views.log", filemode="w")


class UserRegistration(APIView):
    """
    class based views for User registration
    """

    def post(self, request):
        """
        this method is created for inserting the data
        :param request: format of the request
        :return: Response
        """
        serializer = NotesUserSerializer(data=request.data)

        if serializer.is_valid():
            NotesUser.objects.create_user(username=serializer.data.get('username'),
                                          password=serializer.data.get('password'),
                                          email=serializer.data.get('email'),
                                          first_name=serializer.data.get('first_name'),
                                          last_name=serializer.data.get('last_name'),
                                          mobile=serializer.data.get('mobile'),
                                          age=serializer.data.get('age'))
            return Response({'msg': 'Registration Successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


