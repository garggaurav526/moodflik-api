from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.conf import settings


from .serializers import *
from .models import CustomUser, Bio, Block, PostSettings, Contact, ShareBioSettings, ShowLikeDisLikeSettings

User = get_user_model()

class UserRegistrationAPIView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = UserSerializer
    queryset = User.objects.all()

class ContactAPIView(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            contacts = Contact.objects.all()
            serializer = ContactSerializer(contacts, many=True)
            return Response({'status': True, 'contact_us': serializer.data})
        except Exception as e:
            print("Error:", e)
            return Response({'status': False ,'message': "something went wrong"})

    def post(self, request):
        try:
            serializer = ContactSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()       
                return Response({'status': True, 'message': 'your details are successfully saved!'})
            return Response({'status': False, 'message': 'Please Enter valid details!'})
        except Exception as e:
            print("Error:", e)
            return Response({'status': False ,'message': "something went wrong"})

class UserView(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, user_id):
        try:
            user_detail = Bio.objects.filter(user=user_id)
            user_details = [{'user_id':user.user.id, 'username':user.user.username,
            'email':user.user.email,'profile_image':user.photo_url, 'cover_image':user.cover_photo_url
            } for user in user_detail]
            return Response({'status': True, 'users': user_details})
        except Exception as e:
            print("Error:", e)
            return Response({'status': False ,'message': "something went wrong"})    

class AuthenticateUser(views.APIView):
    def post(self, request):
        try:
            data = request.data
            password = data.get('password')
            username = data.get('username')
            email = data.get('email')
            if email:
            	username = User.objects.get(email=email).username
            user = authenticate(username=username, password=password)
            if user:
                user_id = User.objects.get(username=username).id
                authenticated_userid = {user_id}
                obj, created = Token.objects.get_or_create(user=user)
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

class PasswordReset(views.APIView):
    def post(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            email_exists = User.objects.filter(email=email)
            if email_exists:
                if len(password) > getattr(settings, 'PASSWORD_MIN_LENGTH', 8):
                    u = CustomUser.objects.get(email=email)
                    u.set_password(password)
                    u.save()
                    return Response({'status': True, 'message':'password updated successfully!'})
                else:
                    return Response({'status':False, 'message':'password should be 8 characters long'})
            else:
                return Response({'status': False, 'message':'please enter valid email'})
        except Exception as e:
            print("Error", e)
            return Response({'status': False,'message': "something went wrong"})

class BioDetails(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            user = CustomUser.objects.get(email=request.user)
            bio = Bio.objects.filter(user=user)
            bio_details = [{'bio_id':col.id, 'user_id':col.user.id, 
                'username': col.user.username, 'email': col.user.email, 'profile_photo':col.photo_url,
                'phone_number':col.phone_number, 'country':col.country, 'city':col.city,
                'website':col.website, 'me':col.me, 'like':col.like, 'dislike': col.dislike,
                'cover_photo_url':col.cover_photo_url} for col in bio]
            return Response({'status': True, 'bio_details': bio_details})
        except Exception as e:
            print("Error:", e)
            return Response({'status': False ,'message': "something went wrong"})

    def post(self, request):
    	try:
            bio = Bio.objects.filter(user_id=request.data.get('user'))
            user = CustomUser.objects.get(id = request.data.get('user'))
            if not bio:
                serializer = BioSerializer(data=request.data)
                serializer.context["user"] = user.id
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response({'status': True, 'message': 'your details are successfully saved!'})
                else:
                    return({'status':False, 'message':'please enter valid details!'})
            else:
                return Response({'status': False, 'message': 'Profile already exists!'})
    	except Exception as e:
    		print("Error:", e)
    		return Response({'status': False ,'message': "something went wrong"})

    def put(self, request, bio_id):
        try:
            save_bio = get_object_or_404(Bio.objects.all(), pk=user_id)
            serializer = BioSerializer(instance=save_bio, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                article_saved = serializer.save()
                return Response({'status': True, 'message': 'your details are successfully updated!'})
        except Exception as e:
            print("Error:", e)
            return Response({'status': False ,'message': "something went wrong"})

    def delete(self, request, bio_id):
        try:
            bio = get_object_or_404(Bio.objects.all(), pk=bio_id)
            if bio:
                bio.delete()
                return Response({'status': True, 'message': 'your details are successfully deleted!'})
        except Exception as e:
            print("Error:", e)
            return Response({'status': False ,'message': "something went wrong"})

class PrivacySetting(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            user = CustomUser.objects.get(email=request.user)
            settings = PostSettings.objects.filter(user__email=user)
            print(user, settings)
            if user and settings:
                for setting in settings:
                    if setting.privacy_settings==0:
                        return Response({'status':True, 'setting':'Default'})
                    if setting.privacy_settings==1:
                        return Response({'status':True, 'setting':'Anyone'})
                    if setting.privacy_settings==2:
                        return Response({'status':True, 'setting':'OnlyFollowers'})
                    if setting.privacy_settings==3:
                        return Response({'status':True, 'setting':'OnlyFollowing'})
            else:
                return Response({'status':False, 'message': 'enter valid details!'})
        except Exception as e:
            print("Error:", e)
            return Response({'status': False ,'message': "something went wrong"})

    def post(self, request):
        try:
            user = CustomUser.objects.get(email=request.user)
            privacy_settings = request.data.get('privacy_settings')
            settings = PostSettings.objects.filter(user=user)
            if int(privacy_settings) < 4:
                if not settings:
                    p = PostSettings(user=user, privacy_settings=privacy_settings)
                    p.save()
                    return Response({'status': True, 'message': 'your details are successfully saved!'})
                elif settings:
                    PostSettings.objects.filter(user=user).update(privacy_settings=privacy_settings)
                    return Response({'status': True, 'message': 'your details are successfully saved!'})
            else:
                return Response({'status':False, 'message': 'please enter valid settings!'})    
        except Exception as e:
            print("Error:", e)
            return Response({'status': False ,'message': "something went wrong"})

class BioSetting(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            user = CustomUser.objects.get(email=request.user)
            settings = ShareBioSettings.objects.filter(user=user)
            if user and settings:
                for setting in settings:
                    if setting.setting==0:
                        return Response({'status':True, 'setting':'Default'})
                    if setting.setting==1:
                        return Response({'status':True, 'setting':'Anyone'})
                    if setting.setting==2:
                        return Response({'status':True, 'setting':'OnlyFollowers'})
                    if setting.setting==3:
                        return Response({'status':True, 'setting':'OnlyFollowing'})
            else:
                return Response({'status':False, 'message': 'enter valid details!'})
        except Exception as e:
            print("Error:", e)
            return Response({'status': False ,'message': "something went wrong"})

    def post(self, request):
        try:
            user = CustomUser.objects.get(email=request.user)
            privacy_settings = request.data.get('privacy_settings')
            settings = ShareBioSettings.objects.filter(user=user)
            if int(privacy_settings) < 4:
                if not settings:
                    p = ShareBioSettings(user=user, setting=privacy_settings)
                    p.save()
                    return Response({'status': True, 'message': 'your details are successfully saved!'})
                elif settings:
                    ShareBioSettings.objects.filter(user=user).update(setting=privacy_settings)
                    return Response({'status': True, 'message': 'your details are successfully saved!'})
            else:
                return Response({'status':False, 'message': 'please enter valid settings!'})    
        except Exception as e:
            print("Error:", e)
            return Response({'status': False ,'message': "something went wrong"})

class ShowingFiguresSettings(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            user = CustomUser.objects.get(email=request.user)
            settings = ShowLikeDisLikeSettings.objects.filter(user=user)
            if user and settings:
                for setting in settings:
                    if setting.setting==0:
                        return Response({'status':True, 'setting':'Show_Posts'})
                    if setting.setting==1:
                        return Response({'status':True, 'setting':'Not_Showing'})
            else:
                return Response({'status':False, 'message': 'enter valid details!'})
        except Exception as e:
            print("Error:", e)
            return Response({'status': False ,'message': "something went wrong"})

    def post(self, request):
        try:
            user = CustomUser.objects.get(email=request.user)
            privacy_settings = request.data.get('privacy_settings')
            settings = ShowLikeDisLikeSettings.objects.filter(user=user)
            if int(privacy_settings) == 0 or int(privacy_settings)==1:
                if not settings:
                    p = ShowLikeDisLikeSettings(user=user, setting=privacy_settings)
                    p.save()
                    return Response({'status': True, 'message': 'your details are successfully saved!'})
                elif settings:
                    ShowLikeDisLikeSettings.objects.filter(user=user).update(setting=privacy_settings)
                    return Response({'status': True, 'message': 'your details are successfully saved!'})
            else:
                return Response({'status':False, 'message': 'please enter valid settings!'})    
        except Exception as e:
            print("Error:", e)
            return Response({'status': False ,'message': "something went wrong"})

class BlockUsers(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            # user = CustomUser.objects.get(email=request.user)
            blocked_users = Block.objects.filter(user__email=request.user)
            print("11111")            
            profiles = Bio.objects.filter(user=blocked_users.blocked_user.id)
            block_user_list = []
            for block_user in blocked_users:
                filtered_users = Bio.objects.filter(user_id=block_user.blocked_user.id)

                block_user_list.append({'block_id':block_user.id, 'block_user_id': block_user.blocked_user.id,
                'blockuser_username': block_user.blocked_user.username,'blockuser_firstname': block_user.blocked_user.first_name,
                'blockuser_photo_url':filtered_users.photo_url, 'photo': post.photo,})               
            return Response({'status': True, 'blocked_user': block_user_list})
        except Exception as e:
            raise e
    def post(self, request):
        try:
            user = CustomUser.objects.get(email=request.user)
            block_user = request.data.get('blocked_user')
            blocked_user = CustomUser.objects.get(id=block_user)
            # print("3333", user)
            if user.id and blocked_user:
                print(type(user.id), type(blocked_user.id))
                b = Block(user=user, blocked_user=blocked_user)
                b.save()
            return Response({'status': True, 'message': 'your details are successfully saved!'})
        except Exception as e:
            print("Error:", e)
            return Response({'status': False ,'message': "something went wrong"})

    def delete(self, request, blockeduser_id):
        try:
            user = CustomUser.objects.get(email=request.user)
            block_user = get_object_or_404(Block.objects.filter(user=user,blocked_user=blockeduser_id))
            if block_user:
                block_user.delete()
                return Response({'status': True, 'message': 'your details are successfully deleted!'})
            else:
                return Response({'status': False, 'message': 'Please enter valid blocked_user!'})
        except Exception as e:
            print("Error:", e)
            return Response({'status': False ,'message': "something went wrong"})            