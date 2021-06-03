from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from .serializers import *
from .models import Bio, CustomUser

User = get_user_model()

class UserRegistrationAPIView(generics.CreateAPIView):
    """
    Endpoint for user registration.

    """

    permission_classes = (permissions.AllowAny, )
    serializer_class = UserSerializer
    queryset = User.objects.all()

# class UserLoginAPIView(views.APIView):
#     """
#     Endpoint for user login. Returns authentication token on success.

#     """

#     permission_classes = (permissions.AllowAny, )
#     serializer_class = serializers.UserLoginSerializer
#     def post(self, request):
#     	try:
# 	        serializer = self.serializer_class(data=request.data)
# 	        if serializer.is_valid(raise_exception=True):
# 	            obj, created = Token.objects.get_or_create(user=user)
# 	            return Response({'status': True, 'token': obj.key, 'message': 'you are successfully logged in!'})
# 	        return Response({'status': False, 'message': 'Please Enter valid login details!'})
#     	except Exception as e:
#     		print("Error:", e)
#     		return Response({'status': False ,'message': "something went wrong"})


class AuthenticateUser(views.APIView):
    def post(self, request):
        try:
            data = request.data
            password = data.get('password')
            username = data.get('username')
            email = data.get('email')
            if email:
            	username = User.objects.get(email=email).username
            print("details::",username)
            user = authenticate(username=username, password=password)
            print("user::",user)
            # if user.is_superuser:
                # user_type = "1"
            # else:
            if user:
                # user_type = "0"
                user_id = User.objects.get(username=username).id
                authenticated_userid = {user_id}
                obj, created = Token.objects.get_or_create(user=user)
                # return Response({'status': True,'token': obj.key,'user_id': user_id, 'message': 'you are successfully logged in!'})
                return Response({'status': True,'token': obj.key,'user_id': user_id, 'message': 'you are successfully logged in!'})
            else:
                return Response({'status': False, 'message': 'Please Enter valid login details!'})
        except Exception as e:
            print("Error:", e)
            return Response({'status': False ,'message': "something went wrong"})


class AuthenticateEmail(views.APIView):
    def post(self, request):
        try:
            email = request.data.get('email')
            email_exists = User.objects.filter(email=email)
            if email_exists:
                return Response({'status': True})
            else:
                return Response({'status': False})
        except Exception as e:
            print("Error", e)
            return Response({'status': False,'message': "something went wrong"})


class BioDetails(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            bio_details = Bio.objects.all()
            serializer = BioSerializer(bio_details, many=True)
            return Response({'status': True, 'bio_details': serializer.data})
        except Exception as e:
            print("Error:", e)
            return Response({'status': False ,'message': "something went wrong"})

    def post(self, request):
    	try:
	        serializer = BioSerializer(data=request.data)
	        if serializer.is_valid(raise_exception=True):
	        	serializer.save()	        	
	        	return Response({'status': True, 'message': 'your details are successfully saved!'})
	       	return Response({'status': False, 'message': 'Please Enter valid details!'})
    	except Exception as e:
    		print("Error:", e)
    		return Response({'status': False ,'message': "something went wrong"})

    # def put(self, request, pk):
        # try:
            # save_bio = get_object_or_404(Bio.objects.all(), pk=pk)
        #     serializer = BioSerializer(instance=save_bio, data=request.data, partial=True)
        #     if serializer.is_valid(raise_exception=True):
        #         article_saved = serializer.save()
        #         return Response({'status': True, 'message': 'your details are successfully updated!'})
        # except Exception as e:
        #     print("Error:", e)
        #     return Response({'status': False ,'message': "something went wrong"})

# class UpdateBioDetails(generics.UpdateAPIView):
#     queryset = Bio.objects.all()
#     serializer_class = BioSerializer
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

class UpdateUserDetails(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    # lookup_field = 'pk'
    serializer_class = UserSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]