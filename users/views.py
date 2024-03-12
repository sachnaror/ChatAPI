from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import MyUser as User
from .serializers import UserSerializer


@api_view(['GET'])
def user_list(request, ):
    users = User.objects.all().order_by('username')
    serializer = UserSerializer(instance=users, many=True)
    return Response(serializer.data)
