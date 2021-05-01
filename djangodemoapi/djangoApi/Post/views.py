from django.shortcuts import render
from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from .serializers import LikePostSerializer, DislikePostSerializer

class CreateLikePost(views.APIView):
	permission_classes = (permissions.AllowAny, )
	serializer_class = LikePostSerializer
	def post(self, request):
		try:
			serializer = self.serializer_class(data=request.data)
			if serializer.is_valid(raise_exception=True):
				# serializer.save()
				return Response({'status': True, 'message': 'your details are successfully saved!'})
		except Exception as e:
			print("Error:", e)
			return Response({'status': False})

class CreateDislikePost(views.APIView):
	permission_classes = (permissions.AllowAny, )
	serializer_class = DislikePostSerializer
	def post(self, request):
		try:
			serializer = self.serializer_class(data=request.data)
			if serializer.is_valid(raise_exception=True):
				# print("1:::::::::::::", serializer.data)
				serializer.save()
				return Response({'status': True, 'message': 'your details are successfully saved!'})
		except Exception as e:
			print("Error:", e)
			return Response({'status': False})			