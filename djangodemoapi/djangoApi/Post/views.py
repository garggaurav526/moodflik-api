from django.shortcuts import render
from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import LikePostSerializer, DislikePostSerializer
from .models import Reactions, LikePost, DislikePost

from User.models import CustomUser

class LikePostview(views.APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request):
		try:
			post_details = LikePost.objects.all()
			serializer = LikePostSerializer(post_details, many=True)
			return Response({'status':True, 'post_details':serializer.data})
		except Exception as e:
			print("Error:", e)
			return Response({'status': False ,'message': "something went wrong"})

	def post(self, request):
		try:
			serializer = LikePostSerializer(data=request.data)
			if serializer.is_valid(raise_exception=True):
				serializer.save()
				return Response({'status': True, 'message': 'your details are successfully saved!'})
		except Exception as e:
			print("Error:", e)
			return Response({'status': False ,'message': "something went wrong"})

class DislikePostView(views.APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request):
		try:
			dislikepost_detail = DislikePost.objects.all()
			serializer = DislikePostSerializer(dislikepost_detail, many=True)
			return Response({'status':True, 'dislikepost_details':serializer.data})
		except Exception as e:
			raise e
	def post(self, request):
		try:
			serializer = DislikePostSerializer(data=request.data)
			if serializer.is_valid(raise_exception=True):
				serializer.save()
				return Response({'status': True, 'message': 'your details are successfully saved!'})
		except Exception as e:
			print("Error:", e)
			return Response({'status': False ,'message': "something went wrong"})

class AddFavorite(views.APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	def post(self, request):
		try:
			data = request.data
			favorite = 1
			users = int(data.get('users_id'))
			users = CustomUser.objects.get(id=users)
			if data.get('like_post_id'):
				like_post = data.get('like_post_id')
				like_post = LikePost.objects.get(id=like_post)
				favorite_exist = Reactions.objects.filter(users=users,
				 favorite=favorite,
				 like_post=like_post,
				 )
			else:
				like_post = None
			if data.get('dislike_post_id'):
				dislike_post = data.get('dislike_post_id')
				dislike_post = DislikePost.objects.get(id=dislike_post)
				favorite_exist = Reactions.objects.filter(users=users,
				 favorite=favorite,
				 dislike_post=dislike_post,
				 )
			else:
				dislike_post = None
			like = 0
			dislike = 0
			share = 0
			seen = 0
			comment = 0

			if not favorite_exist:
				r = Reactions(like=like, dislike=dislike, share=share, seen=seen, comment=comment,
				 users=users, like_post=like_post, dislike_post=dislike_post, favorite=favorite)
				r.save()
				return Response({'status': True})
			else:
				return Response({'status': False,'message': 'Already added this post to favorites!'})
		except Exception as e:
			print("Error:", e)
			return Response({'status': False ,'message': "something went wrong"})

class AddLike(views.APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	def post(self, request):
		try:
			data = request.data
			like = 1
			users = int(data.get('users_id'))
			users = CustomUser.objects.get(id=users)
			print("1111111111111:",like)
			if data.get('like_post_id'):
				like_post = data.get('like_post_id')
				like_post = LikePost.objects.get(id=like_post)
				like_exists = Reactions.objects.filter(users=users,
					like_post=like_post,
					like=like,
				)
			else:
				like_post = None
			if data.get('dislike_post_id'):
				dislike_post = data.get('dislike_post_id')
				dislike_post = DislikePost.objects.get(id=dislike_post)
				like_exists = Reactions.objects.filter(users=users,
					dislike_post=dislike_post,
					like=like,
				)
			else:
				dislike_post = None
			favorite = 0
			dislike = 0
			share = 0
			seen = 0
			comment = 0

			if not like_exists:
				r = Reactions(like=like, dislike=dislike, share=share, seen=seen, comment=comment,
				 users=users, like_post=like_post, dislike_post=dislike_post, favorite=favorite)
				r.save()
			else:
				return Response({'status': False,'message': 'Already added this post to likes!'})				
			return Response({'status': True})
		except Exception as e:
			print("Error:", e)
			return Response({'status': False ,'message': "something went wrong"})

class AddDislike(views.APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	def post(self, request):
		try:
			data = request.data
			dislike = 1
			users = int(data.get('users_id'))
			users = CustomUser.objects.get(id=users)
			if data.get('like_post_id'):
				like_post = data.get('like_post_id')
				like_post = LikePost.objects.get(id=like_post)
				dislike_exists = Reactions.objects.filter(users=users,
					like_post=like_post,
					dislike=dislike,
				)
			else:
				like_post = None
			if data.get('dislike_post_id'):
				dislike_post = data.get('dislike_post_id')
				dislike_post = DislikePost.objects.get(id=dislike_post)
				dislike_exists = Reactions.objects.filter(users=users,
					dislike_post=dislike_post,
					dislike=dislike,
				)				
			else:
				dislike_post = None
			favorite = 0
			like = 0
			share = 0
			seen = 0
			comment = 0

			if not dislike_exists:
				r = Reactions(like=like, dislike=dislike, share=share, seen=seen, comment=comment,
				 users=users, like_post=like_post, dislike_post=dislike_post, favorite=favorite)
				r.save()
			else:
				return Response({'status': False,'message': 'Already added this post to dislikes!'})				
			return Response({'status': True})
		except Exception as e:
			print("Error:", e)
			return Response({'status': False ,'message': "something went wrong"})

class AddShare(views.APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	def post(self, request):
		try:
			data = request.data
			share = 1
			users = int(data.get('users_id'))
			users = CustomUser.objects.get(id=users)
			if data.get('like_post_id'):
				like_post = data.get('like_post_id')
				like_post = LikePost.objects.get(id=like_post)
				share_exists = Reactions.objects.filter(users=users,
					like_post=like_post,
					share=share,
				)
			else:
				like_post = None
			if data.get('dislike_post_id'):
				dislike_post = data.get('dislike_post_id')
				dislike_post = DislikePost.objects.get(id=dislike_post)
				share_exists = Reactions.objects.filter(users=users,
					dislike_post=dislike_post,
					share=share,
				)				
			else:
				dislike_post = None
			favorite = 0
			dislike = 0
			like = 0
			seen = 0
			comment = 0

			if not share_exists:
				r = Reactions(like=like, dislike=dislike, share=share, seen=seen, comment=comment,
				 users=users, like_post=like_post, dislike_post=dislike_post, favorite=favorite)
				r.save()
			else:
				return Response({'status': False,'message': 'Already added this post to shares!'})				
			return Response({'status': True})
		except Exception as e:
			print("Error:", e)
			return Response({'status': False ,'message': "something went wrong"})

class AddSeen(views.APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	def post(self, request):
		try:
			data = request.data
			seen = 1
			users = int(data.get('users_id'))
			users = CustomUser.objects.get(id=users)			
			if data.get('like_post_id'):
				like_post = data.get('like_post_id')
				like_post = LikePost.objects.get(id=like_post)
				seen_exists = Reactions.objects.filter(users=users,
					like_post=like_post,
					seen=seen,
				)
			else:
				like_post = None
			if data.get('dislike_post_id'):
				dislike_post = data.get('dislike_post_id')
				dislike_post = DislikePost.objects.get(id=dislike_post)
				seen_exists = Reactions.objects.filter(users=users,
					dislike_post=dislike_post,
					seen=seen,
				)
			else:
				dislike_post = None
			favorite = 0
			dislike = 0
			share = 0
			like = 0
			comment = 0

			if not seen_exists:
				r = Reactions(like=like, dislike=dislike, share=share, seen=seen, comment=comment,
				 users=users, like_post=like_post, dislike_post=dislike_post, favorite=favorite)
				r.save()
			else:
				return Response({'status': False,'message': 'Already added this post to seens!'})				

			return Response({'status': True})
		except Exception as e:
			print("Error:", e)
			return Response({'status': False ,'message': "something went wrong"})

class AddComment(views.APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	def post(self, request):
		try:
			data = request.data
			comment = 1
			users = int(data.get('users_id'))
			users = CustomUser.objects.get(id=users)			
			if data.get('like_post_id'):
				like_post = data.get('like_post_id')
				like_post = LikePost.objects.get(id=like_post)
				comment_exists = Reactions.objects.filter(users=users,
					like_post=like_post,
					comment=comment,
				)				
			else:
				like_post = None
			if data.get('dislike_post_id'):
				dislike_post = data.get('dislike_post_id')
				dislike_post = DislikePost.objects.get(id=dislike_post)
				comment_exists = Reactions.objects.filter(users=users,
					dislike_post=dislike_post,
					comment=comment,
				)				
			else:
				dislike_post = None
			favorite = 0
			dislike = 0
			share = 0
			like = 0
			seen = 0

			if not comment_exists:
				r = Reactions(like=like, dislike=dislike, share=share, seen=seen, comment=comment,
				 users=users, like_post=like_post, dislike_post=dislike_post, favorite=favorite)
				r.save()
			else:
				return Response({'status': False,'message': 'Already added this post to comments!'})				
			return Response({'status': True})
		except Exception as e:
			print("Error:", e)
			return Response({'status': False ,'message': "something went wrong"})

class Home(views.APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request):
		try:
			like_filtered_posts = LikePost.objects.exclude(user__email=request.user)
			reactions_list = []
			for post in like_filtered_posts:
				filtered_reactions = Reactions.objects.filter(like_post__id=post.id)
				like_count = filtered_reactions.filter(like=1).count()
				dislike_count = filtered_reactions.filter(dislike=1).count()
				share_count = filtered_reactions.filter(share=1).count()
				seen_count = filtered_reactions.filter(seen=1).count()
				comment_count = filtered_reactions.filter(comment=1).count()
				favorite_count = filtered_reactions.filter(favorite=1).count()
			
				reactions_list.append({
					'id':post.id, 'content': post.content, 'photo': post.photo,
					'video':post.video, 'gif': post.gif, 'file': post.file, 
					'why_content': post.why_content, 'user_id': post.user_id,
					'like':like_count, 'dislike':dislike_count,
					'share':share_count, 'seen':seen_count, 'comment':comment_count,
					'favorite':favorite_count})
			print(reactions_list)
			return Response({'status': True, 'reactions': reactions_list})
		except Exception as e:
			raise e
