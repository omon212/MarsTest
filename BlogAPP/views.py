from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import NewsModel
from .serializers import NewsSerializer
from drf_yasg.utils import swagger_auto_schema

#create post delete put patch for model NewsModel

class NewsView(APIView):
    @swagger_auto_schema(
        operation_description="Get all news",
        responses={200: NewsSerializer(many=True)}
    )

    def get(self,request):
        news = NewsModel.objects.all()
        serializer = NewsSerializer(news,many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a news",
        request_body=NewsSerializer,
        responses={201: NewsSerializer}
    )
    def post(self,request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

