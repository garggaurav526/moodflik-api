from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate, login

from .serializers import *
from .models import Bio

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
                # obj, created = Token.objects.get_or_create(user=user)
                # return Response({'status': True,'token': obj.key,'user_id': user_id, 'message': 'you are successfully logged in!'})
                return Response({'status': True,'user_id': user_id, 'message': 'you are successfully logged in!'})
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
    permission_classes = (permissions.AllowAny, )
    serializer_class = BioSerializer
    def post(self, request):
    	try:
	        serializer = self.serializer_class(data=request.data)
	        if serializer.is_valid(raise_exception=True):
	        	serializer.save()	        	
	        	return Response({'status': True, 'message': 'your details are successfully saved!'})
	       	return Response({'status': False, 'message': 'Please Enter valid details!'})
    	except Exception as e:
    		print("Error:", e)
    		return Response({'status': False ,'message': "something went wrong"})

class UpdateDetails(generics.UpdateAPIView):
    queryset = Bio.objects.all()
    serializer_class = BioSerializer
    permission_classes = (permissions.AllowAny,)

# class UpdateDetails(views.APIView):
# 	def post(self, request):
# 		try:
# 			updated_data = {}
# 			updated_data = self.request.data.copy()
# 			updated_data['phone_number'] = request.data['phone_number']
# 			updated_data['id'] = request.data['id']
# 			updated_data['country'] = request.data['country']
# 			updated_data['city'] = request.data['city']
# 			updated_data['website'] = request.data['website']
# 			updated_data['me'] = request.data['me']
# 			updated_data['like'] = request.data['like']
# 			updated_data['dislike'] = request.data['dislike']
# 			updated_data['photo_url'] = request.data['photo_url']
# 			Bio.objects.filter(id=updated_data['id']).update(data=updated_data)
# 			print("updated_data::", updated_data)
# 			return Response({'status': True})
# 		except Exception as e:
# 			print("Error:", e)
# 			return Response({'status': False ,'message': "something went wrong"})