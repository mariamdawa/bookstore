from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from django.contrib.auth.models import User



# @api_view(['GET'])
# def index(request):
#     pass
#     books = User.objects.all()
#     serializer = UserSerializer(instance=books, many=True)
#     return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def api_signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success":True,
            "message": "User Has been created"
        },status=status.HTTP_201_CREATED)
    return Response(data={
        "success":False,
        "errors": serializer.errors
    },status=status.HTTP_400_BAD_REQUEST)