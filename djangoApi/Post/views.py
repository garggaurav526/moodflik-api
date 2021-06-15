from django.shortcuts import render
from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .serializers import LikePostSerializer, DislikePostSerializer, FollowSerializer
from .models import Reactions, LikePost, DislikePost, Follow

from User.models import CustomUser

class LikePostview(views.APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request):
		try:
			post_details = LikePost.objects.all()
			paginator = PageNumberPagination()
			paginator.page_size = 10
			result_page = paginator.paginate_queryset(post_details, request)
			serializer = LikePostSerializer(result_page, many=True)
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

	def put(self, request, post_id):
		try:
			post_details = get_object_or_404(LikePost.objects.all(), pk=post_id)
			serializer = LikePostSerializer(instance=post_details, data=request.data, partial=True)
			if serializer.is_valid(raise_exception=True):
				article_saved = serializer.save()
				return Response({'status': True, 'message': 'your details are successfully updated!'})
		except Exception as e:
			print("Error:",e)
			return Response({'status': False, 'message':'something went wrong'})			

	def delete(self, request, post_id):
		try:
			post = get_object_or_404(LikePost.objects.all(), pk=post_id)
			if post:
				post.delete()
				return Response({'status':True, 'message': 'successfully deleted'})
		except Exception as e:
			print('Error:', e)
			return Response({'status':False, 'message':'something went wrong'})


class DislikePostView(views.APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request):
		try:
			dislikepost_detail = DislikePost.objects.all()
			paginator = PageNumberPagination()
			paginator.page_size = 10
			result_page = paginator.paginate_queryset(dislikepost_detail, request)
			serializer = DislikePostSerializer(result_page, many=True)
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

	def put(self, request, post_id):
		try:
			post_details = get_object_or_404(DislikePost.objects.all(), pk=post_id)
			serializer = DislikePostSerializer(instance=post_details, data=request.data, partial=True)
			if serializer.is_valid(raise_exception=True):
				article_saved = serializer.save()
				return Response({'status': True, 'message': 'your details are successfully updated!'})
		except Exception as e:
			print("Error:", e)
			return Response({'status': False ,'message': "something went wrong"})			

	def delete(self, request, post_id):
		try:
			post = get_object_or_404(DislikePost.objects.all(), pk=post_id)
			if post:
				post.delete()
				return Response({'status':True, 'message':'successfully deleted'})
		except Exception as e:
			print("Error:", e)
			return Response({'status': False ,'message': "something went wrong"})

class AddFavorite(views.APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request):
		try:
			likepost_favorites = Reactions.objects.filter(favorite=1,like_post__isnull=False,)
			dislikepost_favorites = Reactions.objects.filter(favorite=1,dislike_post__isnull=False,)
			# .exclude(user__email=users)
			likepost_list = [
			{'id':col.id, 'post_id':col.like_post_id,'user_who_added_favorite':col.users_id, 
			'content': col.like_post.content, 'photo': col.like_post.photo,
			'video':col.like_post.video, 'gif': col.like_post.gif, 'file': col.like_post.file, 
			'why_content': col.like_post.why_content, 'post_user_id': col.like_post.user_id
			} for col in likepost_favorites
			]

			dislike_post_list = [
			{'id':col.id, 'post_id':col.dislike_post_id,'user_who_added_favorite':col.users_id, 
			'content': col.dislike_post.content, 'photo': col.dislike_post.photo,
			'video':col.dislike_post.video, 'gif': col.dislike_post.gif, 'file': col.dislike_post.file, 
			'why_content': col.dislike_post.why_content, 'post_user_id': col.dislike_post.user_id
			} for col in dislikepost_favorites
			]

			paginator = PageNumberPagination()
			paginator.page_size = 20
			likepost_page = paginator.paginate_queryset(likepost_list, request)
			dislikepost_page = paginator.paginate_queryset(dislike_post_list, request)
			favorites = {'like_post': likepost_page, 'dislike_post':dislikepost_page}
			return Response({'status':True, 'favorites':favorites})
		except Exception as e:
			print("Error:", e)
			return Response({'status': False ,'message': "something went wrong"})

	def post(self, request):
		try:
			data = request.data
			favorite = 1
			users = request.user
			users = CustomUser.objects.get(email=users)
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
			users = request.user
			users = CustomUser.objects.get(email=users)
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
			users = request.user
			users = CustomUser.objects.get(email=users)
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
			users = request.user
			users = CustomUser.objects.get(email=users)
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
			users = request.user
			users = CustomUser.objects.get(email=users)			
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
			users = request.user
			users = CustomUser.objects.get(email=users)			
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
			like_filtered_posts = LikePost.objects.all()
			dislike_filtered_posts = DislikePost.objects.all()

			like_post_list = []
			dislike_post_list = []
			# saving all filtered likepost
			for post in like_filtered_posts:
				filtered_reactions = Reactions.objects.filter(like_post__id=post.id)
				like_count = filtered_reactions.filter(like=1).count()
				dislike_count = filtered_reactions.filter(dislike=1).count()
				share_count = filtered_reactions.filter(share=1).count()
				seen_count = filtered_reactions.filter(seen=1).count()
				comment_count = filtered_reactions.filter(comment=1).count()
				favorite_count = filtered_reactions.filter(favorite=1).count()
			
				like_post_list.append({
					'id':post.id , 'content': post.content, 'photo': post.photo,
					'video':post.video, 'gif': post.gif, 'file': post.file, 
					'why_content': post.why_content, 'user_id': post.user_id,
					'like':like_count, 'dislike':dislike_count,
					'share':share_count, 'seen':seen_count, 'comment':comment_count,
					'favorite':favorite_count})

			# saving all filtered dislikepost
			for post in dislike_filtered_posts:
				filtered_reactions = Reactions.objects.filter(dislike_post__id=post.id)
				like_count = filtered_reactions.filter(like=1).count()
				dislike_count = filtered_reactions.filter(dislike=1).count()
				share_count = filtered_reactions.filter(share=1).count()
				seen_count = filtered_reactions.filter(seen=1).count()
				comment_count = filtered_reactions.filter(comment=1).count()
				favorite_count = filtered_reactions.filter(favorite=1).count()
			
				dislike_post_list.append({
					'id':post.id, 'content': post.content, 'photo': post.photo,
					'video':post.video, 'gif': post.gif, 'file': post.file, 
					'why_content': post.why_content, 'user_id': post.user_id,
					'like':like_count, 'dislike':dislike_count,
					'share':share_count, 'seen':seen_count, 'comment':comment_count,
					'favorite':favorite_count})

			# Code for implemeting pagination
			paginator = PageNumberPagination()
			paginator.page_size = 20
			likepost_page = paginator.paginate_queryset(like_post_list, request)
			dislikepost_page = paginator.paginate_queryset(dislike_post_list, request)

			posts = {'like_post': likepost_page, 'dislike_post':dislikepost_page}
			return Response({'status': True, 'posts': posts})
		except Exception as e:
			msg = str(e)
			print("Error:", e)
			return Response({'status': False ,'message': msg, 'posts': []})

class FollowView(views.APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request):
		try:
			user = CustomUser.objects.get(email=request.user)
			following = Follow.objects.filter(follower=user)
			following_list = [{'following_user':col.following.id, 'user_first_name': col.following.first_name,
                    'last_name':col.following.last_name, 'username': col.following.username, 'email': col.following.email, 
                    'date_of_birth': col.following.date_of_birth, 'gender': col.following.gender} for col in following]
			follower = Follow.objects.filter(following=user)
			follower_list = [{'follower_user':col.follower.id, 'user_first_name': col.follower.first_name,
                    'last_name':col.follower.last_name, 'username': col.follower.username, 'email': col.follower.email, 
                    'date_of_birth': col.follower.date_of_birth, 'gender': col.follower.gender,} for col in following]
			Follow_list = {'following': following_list, 'follower': follower_list}
			return Response({'status': True, 'users': Follow_list})
		except Exception as e:
			print("Error:", e)
			return Response({'status': False ,'message': "something went wrong"})
	def post(self, request):
		try:
			user = CustomUser.objects.get(email=request.user)
			following_user = request.data.get('following_user')
			follow_user = CustomUser.objects.get(id=following_user)
			if user.id and follow_user:
				f = Follow(follower=user, following=follow_user)
				f.save()
				return Response({'status': True, 'message': 'your details are successfully saved!'})
		except Exception as e:
			return Response({'status': False ,'message': "something went wrong"})
			
