from django.shortcuts import render
from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .serializers import LikePostSerializer, DislikePostSerializer, FollowSerializer
from .models import LikePostReactions, DisLikePostReactions, LikePost, DislikePost, Follow

from User.models import CustomUser, Bio

class LikePostview(views.APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request):
		try:
			post_details = LikePost.objects.all()
			paginator = PageNumberPagination()
			paginator.page_size = 20
			result_page = paginator.paginate_queryset(post_details, request)
			serializer = LikePostSerializer(result_page, many=True)
			return Response({'status':True, 'post_details':serializer.data})
		except Exception as e:
			print("Error:", e)
			return Response({'status': False ,'message': "something went wrong"})

	def post(self, request):

		try:

			bio = Bio.objects.get(user__email=request.user)

			# changing the data into its mutable state
			# _mutable = request.data._mutable
			try:
				request.data._mutable = True
			except:
				pass
			data = request.data
			data['bio'] = bio.id
			# request.data._mutable = _mutable

			serializer = LikePostSerializer(data=data)
			if serializer.is_valid(raise_exception=True):
				serializer.save()
				return Response({'status': True, 'message': 'your details are successfully saved!'})
		except Exception as e:
			print("Error:", e)
			return Response({'status': False ,'message': "something went wrong"})

	def put(self, request, post_id):
		try:
			bio = Bio.objects.get(user__email=request.user)
			post_details = LikePost.objects.get(pk=post_id)

			if post_details:
				post_details.bio = bio
				post_details.content = request.data.get('content')
				post_details.photo = request.data.get('photo')
				post_details.video = request.data.get('video')
				post_details.gif = request.data.get('gif')
				post_details.file = request.data.get('file')
				post_details.why_content = request.data.get('why_content')
				post_details.save()

				print("11111111111111111", post_details)
				serializer = LikePostSerializer(post_details)
				return Response({'status': True, 'updated_data':serializer.data})
			else:
				return Response({'status':False,'message':'please enter valid post id!'})
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
			print("Error:", e)
			return Response({'status': False ,'message': "something went wrong"})

	def post(self, request):
		try:
			bio = Bio.objects.get(user__email=request.user)

			# changing the data into its mutable state
			# _mutable = request.data._mutable
			try:
				request.data._mutable = True
			except:
				pass
			request.data['bio'] = bio.id
			# request.data._mutable = _mutable

			serializer = DislikePostSerializer(data=request.data)
			if serializer.is_valid(raise_exception=True):
				serializer.save()
				return Response({'status': True, 'message': 'your details are successfully saved!'})
		except Exception as e:
			print("Error:", e)
			return Response({'status': False ,'message': "something went wrong"})

	def put(self, request, post_id):
		try:
			bio = Bio.objects.get(user__email=request.user)
			post_details = DislikePost.objects.get(pk=post_id)

			if post_details:
				post_details.bio = bio
				post_details.content = request.data.get('content')
				post_details.photo = request.data.get('photo')
				post_details.video = request.data.get('video')
				post_details.gif = request.data.get('gif')
				post_details.file = request.data.get('file')
				post_details.why_content = request.data.get('why_content')
				post_details.save()

				serializer = DislikePostSerializer(post_details)
				return Response({'status': True, 'updated_data':serializer.data})
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
			like_filtered_posts = LikePost.objects.order_by('-created_date')
			likepost_reactions = []
			for post in like_filtered_posts:
				filtered_reactions = LikePostReactions.objects.filter(like_post__id=post.id)
				favorites = filtered_reactions.filter(favorite=1).values_list('bios__user_id',flat=True)
				like = filtered_reactions.filter(like=1).values_list('bios__user_id',flat=True)
				dislike = filtered_reactions.filter(dislike=1).values_list('bios__user_id',flat=True)
				share = filtered_reactions.filter(share=1).values_list('bios__user_id',flat=True)
				seen = filtered_reactions.filter(seen=1).values_list('bios__user_id',flat=True)
				comment = filtered_reactions.filter(comment__isnull=False).values_list('bios__user_id',flat=True)
				if filtered_reactions.filter(favorite=1):
					likepost_reactions.append({'post_id':post.id,'why_content':post.why_content,'file':post.file,'gif':post.gif,'video':post.video,'photo':post.photo,'content':post.content,'user_id':post.bio.user.id, 'username':post.bio.user.username,
						'first_name':post.bio.user.first_name,'last_name':post.bio.user.last_name,
						 'favorites':favorites, 'like':like,'profile_image':post.bio.photo_url,
						'dislike':dislike, 'share':share, 'seen':seen, 
						'comment':comment,'created_at':post.created_at,'updated_at':post.updated_at})
			paginator = PageNumberPagination()
			paginator.page_size = 20
			likepost_page = paginator.paginate_queryset(likepost_reactions, request)
			favorites = likepost_page
			# grouper(2, likepost_reactions)
			# print(likepost_page)
			return Response({'status':True, 'favorites':favorites})
		except Exception as e:
			print("Error:", e)
			return Response({'status': False ,'message': "something went wrong"})

	def post(self, request):
		try:
			data = request.data
			favorite = 1
			like = 0
			dislike = 0
			share = 0
			seen = 0
			comment = None
			users = request.user
			users = Bio.objects.get(user__email=users)
			if data.get('like_post_id'):
				like_post = data.get('like_post_id')
				like_post = LikePost.objects.get(id=like_post)
				if like_post:
					favorite_exist = LikePostReactions.objects.filter(bios=users,
					 favorite=favorite,
					 like_post=like_post,
					 )
					if not favorite_exist:
						r = LikePostReactions(like=like, dislike=dislike, share=share, seen=seen, comment=comment,
						 bios=users, like_post=like_post, favorite=favorite)
						r.save()
						return Response({'status': True})
					else:
						return Response({'status': False, 'message':'Added Already to favorites'})
				else:
					return Response({'status':False, 'message':'please check the like_post id!'})
			if data.get('dislike_post_id'):
				dislike_post = data.get('dislike_post_id')
				dislike_post = DislikePost.objects.get(id=dislike_post)
				if dislike_post:
					favorite_exist = DisLikePostReactions.objects.filter(bios=users,
					 favorite=favorite,
					 dislike_post=dislike_post,
					 )
					if not favorite_exist:
						r = DisLikePostReactions(like=like, dislike=dislike, share=share, seen=seen, comment=comment,
						 bios=users, dislike_post=dislike_post, favorite=favorite)
						r.save()
						return Response({'status': True})
					else:
						return Response({'status': False, 'message':'Added Already to favorites'})
				else:
					return Response({'status':False, 'message':'please check the dislike_post id!'})
			return Response({'status': False,'message': 'Please pass likepost or dislikepost!'})
		except Exception as e:
			print("Error:", e)
			return Response({'status': False ,'message': "something went wrong"})

# import itertools
#
# def grouper(n, iterable, fillvalue=None):
#     "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
#     args = [iter(iterable)] * n
#     return itertools.zip_longest(fillvalue=fillvalue, *args)

class DislikeFav(views.APIView):
	def get(self,request):
		dislike_filtered_posts = DislikePost.objects.order_by('-created_date')
		dislikepost_reactions = []
		for post in dislike_filtered_posts:
			filtered_reactions = DisLikePostReactions.objects.filter(dislike_post__id=post.id, )
			favorites = filtered_reactions.filter(favorite=1).values_list('bios__user_id', flat=True)
			like = filtered_reactions.filter(like=1).values_list('bios__user_id', flat=True)
			dislike = filtered_reactions.filter(dislike=1).values_list('bios__user_id', flat=True)
			share = filtered_reactions.filter(share=1).values_list('bios__user_id', flat=True)
			seen = filtered_reactions.filter(seen=1).values_list('bios__user_id', flat=True)
			comment = filtered_reactions.filter(comment__isnull=False).values_list('bios__user_id', flat=True)
			if filtered_reactions.filter(favorite=1):
				dislikepost_reactions.append(
					{'post_id': post.id,'why_content':post.why_content,'file':post.file,'gif':post.gif,'video':post.video,'photo':post.photo,'content':post.content, 'user_id': post.bio.user.id, 'username': post.bio.user.username,
					 'first_name': post.bio.user.first_name, 'last_name': post.bio.user.last_name,
					 'favorites': favorites, 'like': like, 'profile_image': post.bio.photo_url,
					 'dislike': dislike, 'share': share, 'seen': seen,
					 'comment': comment,'created_at':post.created_at,'updated_at':post.updated_at})

		paginator = PageNumberPagination()
		paginator.page_size = 20
		dislikepost_page = paginator.paginate_queryset(dislikepost_reactions, request)
		# dislikepost_page = grouper(20,dislikepost_reactions)
		favorites = dislikepost_page
		return Response({'status': True, 'favorites': favorites})


class AddLike(views.APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request,likepost_id, dislikepost_id):
		try:
			like_reactions = []
			dislike_reactions = []
			
			# sending the data of likeposts
			if likepost_id!=0:
				filtered_reactions = LikePostReactions.objects.filter(
					like_post__id=likepost_id, like=1)
				like_reactions = [{'user_id':reactions.bios.user.id, 'user_email':reactions.bios.user.email,
				'username':reactions.bios.user.username,'profile_photo':reactions.bios.photo_url,
				'cover_photo':reactions.bios.cover_photo_url,'like':reactions.like,
				} for reactions in filtered_reactions]

			# sending the data of dislikeposts
			if dislikepost_id!=0:
				filtered_reactions = DisLikePostReactions.objects.filter(
					dislike_post__id=dislikepost_id, like=1)
				dislike_reactions = [{'user_id':reactions.bios.user.id, 'user_email':reactions.bios.user.email,
				'username':reactions.bios.user.username,'profile_photo':reactions.bios.photo_url,
				'cover_photo':reactions.bios.cover_photo_url, 'like':reactions.like,
				} for reactions in filtered_reactions]

			# Code for pagination
			paginator = PageNumberPagination()
			paginator.page_size = 20
			likepost_page = paginator.paginate_queryset(like_reactions, request)
			dislikepost_page = paginator.paginate_queryset(dislike_reactions, request)
			dislikes = {'like_post': likepost_page, 'dislike_post':dislikepost_page}
			return Response({'status':True, 'dislikes':dislikes})
		except Exception as e:
			print("Error:", e)
			return Response({'status': False ,'message': "something went wrong"})

	def post(self, request):
		try:
			data = request.data
			like = 1
			favorite = 0
			dislike = 0
			share = 0
			seen = 0
			comment = None
			users = request.user
			users = Bio.objects.get(user__email=users)

			if data.get('like_post_id'):
				if LikePostReactions.objects.filter(bios=users.id,
					like_post__id=data.get('like_post_id'), dislike=1).exists():
					return Response({'status':False})
				like_post = data.get('like_post_id')
				like_post = LikePost.objects.get(id=like_post)
				like_exists = LikePostReactions.objects.filter(bios=users,
					like_post=like_post,
					like=like,
				)
				if not like_exists:
					r = LikePostReactions(like=like, dislike=dislike, share=share, seen=seen, comment=comment,
					 bios=users, like_post=like_post, favorite=favorite)
					r.save()
					return Response({'status': True})
				else:
					return Response({'status': False, 'message':'Added Already to favorites'})
			if data.get('dislike_post_id'):
				if DisLikePostReactions.objects.filter(bios=users.id,
					like_post__id=data.get('dislike_post_id'), dislike=1).exists():
					return Response({'status':False})
				dislike_post = data.get('dislike_post_id')
				dislike_post = DislikePost.objects.get(id=dislike_post)
				like_exists = DisLikePostReactions.objects.filter(bios=users,
					dislike_post=dislike_post,
					like=like,
				)
				if not like_exists:
					r = DisLikePostReactions(dislike=dislike, share=share, seen=seen, comment=comment,
					 bios=users, dislike_post=dislike_post, favorite=favorite, like=like)
					r.save()
					return Response({'status': True})
				else:
					return Response({'status': False, 'message':'you have already liked the post!'})
			return Response({'status': False,'message': 'Please pass likepost or dislikepost!'})
		except Exception as e:
			print("Error:", e)
			return Response({'status': False ,'message': "something went wrong"})

class AddDislike(views.APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request,likepost_id, dislikepost_id):
		try:
			like_reactions = []
			dislike_reactions = []
			# sending the data of likeposts
			if likepost_id!=0:
				filtered_reactions = LikePostReactions.objects.filter(
					like_post__id=likepost_id, dislike=1)
				like_reactions = [{'user_id':reactions.bios.user.id, 'user_email':reactions.bios.user.email,
				'username':reactions.bios.user.username,'profile_photo':reactions.bios.photo_url,
				'cover_photo':reactions.bios.cover_photo_url,'dislike':reactions.dislike,
				} for reactions in filtered_reactions]

			# sending the data of dislikeposts
			if dislikepost_id!=0:
				filtered_reactions = DisLikePostReactions.objects.filter(
					dislike_post__id=dislikepost_id, dislike=1)
				dislike_reactions = [{'user_id':reactions.bios.user.id, 'user_email':reactions.bios.user.email,
				'username':reactions.bios.user.username,'profile_photo':reactions.bios.photo_url,
				'cover_photo':reactions.bios.cover_photo_url, 'dislike':reactions.dislike,
				} for reactions in filtered_reactions]

			# Code for pagination
			paginator = PageNumberPagination()
			paginator.page_size = 20
			likepost_page = paginator.paginate_queryset(like_reactions, request)
			dislikepost_page = paginator.paginate_queryset(dislike_reactions, request)
			dislikes = {'like_post': likepost_page, 'dislike_post':dislikepost_page}
			return Response({'status':True, 'dislikes':dislikes})
		except Exception as e:
			print("Error:", e)
			return Response({'status': False ,'message': "something went wrong"})

	def post(self, request):
		try:
			data = request.data
			dislike = 1
			favorite = 0
			like = 0
			share = 0
			seen = 0
			comment = None
			users = request.user
			users = Bio.objects.get(user__email=users)

			if data.get('like_post_id'):
				# if data.get('like_post_id'):
				if LikePostReactions.objects.filter(bios=users.id,
						like_post__id=data.get('like_post_id'), like=1).exists():
					return Response({'status': False})
				like_post = data.get('like_post_id')
				like_post = LikePost.objects.get(id=like_post)
				dislike_exists = LikePostReactions.objects.filter(bios=users,
					like_post=like_post,
					dislike=dislike,
				)
				if not dislike_exists:
					r = LikePostReactions(dislike=dislike, share=share, seen=seen, comment=comment,
					 bios=users, like_post=like_post, favorite=favorite, like=like)
					r.save()
					return Response({'status': True})
				else:
					return Response({'status': False, 'message':'you have already liked the post!'})
			if data.get('dislike_post_id'):
				if DisLikePostReactions.objects.filter(bios=users.id,
					like_post__id=data.get('dislike_post_id'), like=1).exists():
					return Response({'status':False})
				dislike_post = data.get('dislike_post_id')
				dislike_post = DislikePost.objects.get(id=dislike_post)
				dislike_exists = DisLikePostReactions.objects.filter(bios=users,
					dislike_post=dislike_post,
					dislike=dislike,
				)				
				if not dislike_exists:
					r = DisLikePostReactions(dislike=dislike, share=share, seen=seen, comment=comment,
					 bios=users, dislike_post=dislike_post, favorite=favorite, like=like)
					r.save()
					return Response({'status': True})
				else:
					return Response({'status': False, 'message':'you have already liked the post!'})			
			return Response({'status': False,'message': 'Please pass likepost or dislikepost!'})
		except Exception as e:
			print("Error:", e)
			return Response({'status': False ,'message': "something went wrong"})

class AddShare(views.APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request,likepost_id, dislikepost_id):
		try:
			like_reactions = []
			dislike_reactions = []
			# sending the data of likeposts
			if likepost_id!=0:
				filtered_reactions = LikePostReactions.objects.filter(
					like_post__id=likepost_id, share=1)
				like_reactions = [{'user_id':reactions.bios.user.id, 'user_email':reactions.bios.user.email,
				'username':reactions.bios.user.username,'profile_photo':reactions.bios.photo_url,
				'cover_photo':reactions.bios.cover_photo_url,'share':reactions.share,
				} for reactions in filtered_reactions]

			# sending the data of dislikeposts
			if dislikepost_id!=0:
				filtered_reactions = DisLikePostReactions.objects.filter(
					dislike_post__id=dislikepost_id, share=1)
				dislike_reactions = [{'user_id':reactions.bios.user.id, 'user_email':reactions.bios.user.email,
				'username':reactions.bios.user.username,'profile_photo':reactions.bios.photo_url,
				'cover_photo':reactions.bios.cover_photo_url, 'share':reactions.share,
				} for reactions in filtered_reactions]

			# Code for pagination
			paginator = PageNumberPagination()
			paginator.page_size = 20
			likepost_page = paginator.paginate_queryset(like_reactions, request)
			dislikepost_page = paginator.paginate_queryset(dislike_reactions, request)
			shares = {'like_post': likepost_page, 'dislike_post':dislikepost_page}
			return Response({'status':True, 'shares':shares})		
		except Exception as e:
			print("Error:", e)
			return Response({'status': False ,'message': "something went wrong"})	
	def post(self, request):
		try:
			data = request.data
			share = 1
			favorite = 0
			dislike = 0
			like = 0
			seen = 0
			comment = None
			users = request.user
			users = Bio.objects.get(user__email=users)

			if data.get('like_post_id'):
				like_post = data.get('like_post_id')
				like_post = LikePost.objects.get(id=like_post)
				share_exists = LikePostReactions.objects.filter(bios=users,
					like_post=like_post,
					share=share,
				)
				if not share_exists:
					r = LikePostReactions(dislike=dislike, share=share, seen=seen, comment=comment,
					 bios=users, like_post=like_post, favorite=favorite, like=like)
					r.save()
					return Response({'status': True})
				else:
					return Response({'status': False, 'message':'you have already liked the post!'})
			if data.get('dislike_post_id'):
				dislike_post = data.get('dislike_post_id')
				dislike_post = DislikePost.objects.get(id=dislike_post)
				share_exists = DisLikePostReactions.objects.filter(bios=users,
					dislike_post=dislike_post,
					share=share,
				)
				if not share_exists:
					r = DisLikePostReactions(dislike=dislike, share=share, seen=seen, comment=comment,
					 bios=users, dislike_post=dislike_post, favorite=favorite, like=like)
					r.save()
					return Response({'status': True})
				else:
					return Response({'status': False, 'message':'you have already liked the post!'})
			return Response({'status': False,'message': 'Please pass likepost or dislikepost!'})
		except Exception as e:
			print("Error:", e)
			return Response({'status': False ,'message': "something went wrong"})

class AddSeen(views.APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request,likepost_id, dislikepost_id):
		try:
			like_reactions = []
			dislike_reactions = []
			# sending the data of likeposts
			if likepost_id!=0:
				filtered_reactions = LikePostReactions.objects.filter(
					like_post__id=likepost_id, seen=1)
				like_reactions = [{'user_id':reactions.bios.user.id, 'user_email':reactions.bios.user.email,
				'username':reactions.bios.user.username,'profile_photo':reactions.bios.photo_url,
				'cover_photo':reactions.bios.cover_photo_url,'seen':reactions.seen,
				} for reactions in filtered_reactions]

			# sending the data of dislikeposts
			if dislikepost_id!=0:
				filtered_reactions = DisLikePostReactions.objects.filter(
					dislike_post__id=dislikepost_id, seen=1)
				dislike_reactions = [{'user_id':reactions.bios.user.id, 'user_email':reactions.bios.user.email,
				'username':reactions.bios.user.username,'profile_photo':reactions.bios.photo_url,
				'cover_photo':reactions.bios.cover_photo_url, 'seen':reactions.seen,
				} for reactions in filtered_reactions]

			# Code for pagination
			paginator = PageNumberPagination()
			paginator.page_size = 20
			likepost_page = paginator.paginate_queryset(like_reactions, request)
			dislikepost_page = paginator.paginate_queryset(dislike_reactions, request)
			seens = {'like_post': likepost_page, 'dislike_post':dislikepost_page}
			return Response({'status':True, 'seens':seens})
		except Exception as e:
			print("Error:", e)
			return Response({'status': False ,'message': "something went wrong"})
	def post(self, request):
		try:
			data = request.data
			seen = 1
			favorite = 0
			dislike = 0
			share = 0
			like = 0
			comment = None
			users = request.user
			users = Bio.objects.get(user__email=users)

			if data.get('like_post_id'):
				like_post = data.get('like_post_id')
				like_post = LikePost.objects.get(id=like_post)
				seen_exists = LikePostReactions.objects.filter(bios=users,
					like_post=like_post,
					seen=seen,
				)
				if not seen_exists:
					r = LikePostReactions(dislike=dislike, share=share, seen=seen, comment=comment,
					 bios=users, like_post=like_post, favorite=favorite,like=like)
					r.save()
					return Response({'status': True})
				else:
					return Response({'status': False, 'message':'you have already liked the post!'})
			if data.get('dislike_post_id'):
				dislike_post = data.get('dislike_post_id')
				dislike_post = DislikePost.objects.get(id=dislike_post)
				seen_exists = DisLikePostReactions.objects.filter(bios=users,
					dislike_post=dislike_post,
					seen=seen,
				)
				if not seen_exists:
					r = DisLikePostReactions(dislike=dislike, share=share, seen=seen, comment=comment,
					 bios=users, dislike_post=dislike_post, favorite=favorite, like=like)
					r.save()
					return Response({'status': True})
				else:
					return Response({'status': False, 'message':'you have already liked the post!'})				
			return Response({'status': False,'message': 'Please pass likepost or dislikepost!'})
		except Exception as e:
			print("Error:", e)
			return Response({'status': False ,'message': "something went wrong"})

class AddComment(views.APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request,likepost_id, dislikepost_id):
		try:
			like_reactions = []
			dislike_reactions = []
			# sending the data of likeposts
			if likepost_id!=0:
				filtered_reactions = LikePostReactions.objects.filter(
					like_post__id=likepost_id, comment__isnull=False)
				like_reactions = [{'user_id':reactions.bios.user.id, 'user_email':reactions.bios.user.email,
				'username':reactions.bios.user.username,'profile_photo':reactions.bios.photo_url,
				'cover_photo':reactions.bios.cover_photo_url,'comment':reactions.comment,
				} for reactions in filtered_reactions]

			# sending the data of dislikeposts
			if dislikepost_id!=0:
				filtered_reactions = DisLikePostReactions.objects.filter(
					dislike_post__id=dislikepost_id, comment__isnull=False)
				dislike_reactions = [{'user_id':reactions.bios.user.id, 'user_email':reactions.bios.user.email,
				'username':reactions.bios.user.username,'profile_photo':reactions.bios.photo_url,
				'cover_photo':reactions.bios.cover_photo_url, 'comment':reactions.comment,
				} for reactions in filtered_reactions]

			# Code for pagination
			paginator = PageNumberPagination()
			paginator.page_size = 20
			likepost_page = paginator.paginate_queryset(like_reactions, request)
			dislikepost_page = paginator.paginate_queryset(dislike_reactions, request)
			comments = {'like_post': likepost_page, 'dislike_post':dislikepost_page}
			return Response({'status':True, 'comments':comments})
		except Exception as e:
			print("Error:", e)
			return Response({'status': False ,'message': "something went wrong"})

	def post(self, request):
		try:
			data = request.data
			comment = data.get('comment')
			favorite = 0
			dislike = 0
			share = 0
			like = 0
			seen = 0
			users = request.user
			users = Bio.objects.get(user__email=users)

			if data.get('like_post_id'):
				like_post = data.get('like_post_id')
				like_post = LikePost.objects.get(id=like_post)
				# comment_exists = LikePostReactions.objects.filter(users=users,
				# 	like_post=like_post,
				# 	comment=comment,
				# )

				if comment:
					r = LikePostReactions(dislike=dislike, share=share,
					 seen=seen, comment=comment, bios=users, 
					 like_post=like_post, favorite=favorite, like=like)
					r.save()
					return Response({'status': True})
				else:
					return Response({'status': False, 'message':'Please comment!'})
			if data.get('dislike_post_id'):
				dislike_post = data.get('dislike_post_id')
				dislike_post = DislikePost.objects.get(id=dislike_post)
				# comment_exists = DisLikePostReactions.objects.filter(users=users,
				# 	dislike_post=dislike_post,
				# 	comment=comment,
				# )
				if comment:
					r = DisLikePostReactions(dislike=dislike, share=share,
					 seen=seen, comment=comment,bios=users, like=like,
					 dislike_post=dislike_post, favorite=favorite)
					r.save()
					return Response({'status': True})
				else:
					return Response({'status': False, 'message':'you have already liked the post!'})			
			return Response({'status': True})
		except Exception as e:
			print("Error:", e)
			return Response({'status': False ,'message': "something went wrong"})

class Home(views.APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request):
		try:
			like_filtered_posts = LikePost.objects.order_by('-created_date')
			likepost_reactions = []
			for post in like_filtered_posts:
				filtered_reactions = LikePostReactions.objects.filter(like_post__id=post.id)
				favorites = filtered_reactions.filter(favorite=1).values_list('bios__user_id',flat=True)
				like = filtered_reactions.filter(like=1).values_list('bios__user_id',flat=True)
				dislike = filtered_reactions.filter(dislike=1).values_list('bios__user_id',flat=True)
				share = filtered_reactions.filter(share=1).values_list('bios__user_id',flat=True)
				seen = filtered_reactions.filter(seen=1).values_list('bios__user_id',flat=True)
				comment = filtered_reactions.filter(comment__isnull=False).values_list('bios__user_id',flat=True)
				likepost_reactions.append({'post_id':post.id,'why_content':post.why_content,'file':post.file,'gif':post.gif,'video':post.video,'photo':post.photo,'content':post.content,'user_id':post.bio.user.id, 'username':post.bio.user.username,
					'first_name':post.bio.user.first_name,'last_name':post.bio.user.last_name,
					 'favorites':favorites, 'like':like,'profile_image':post.bio.photo_url,
					'dislike':dislike, 'share':share, 'seen':seen, 
					'comment':comment,'created_at':post.created_at,'updated_at':post.updated_at})
			# print(likepost_reactions)
			# Code for implemeting pagination
			paginator = PageNumberPagination()
			paginator.page_size = 20
			likepost_page = paginator.paginate_queryset(likepost_reactions, request)


			posts = likepost_page#, 'dislike_post':dislikepost_page}
			# posts = {'like_post': 'like_post_list'}
			return Response({'status': True, 'posts': posts})
		except Exception as e:
			msg = str(e)
			print("Error:", e)
			return Response({'status': False ,'message': msg, 'posts': []})


class HomeDislikePosts(views.APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self,request):

		dislike_filtered_posts = DislikePost.objects.order_by('-created_date')
		dislikepost_reactions = []
		for post in dislike_filtered_posts:
			filtered_reactions = DisLikePostReactions.objects.filter(dislike_post__id=post.id)
			favorites = filtered_reactions.filter(favorite=1).values_list('bios__user_id', flat=True)
			like = filtered_reactions.filter(like=1).values_list('bios__user_id', flat=True)
			dislike = filtered_reactions.filter(dislike=1).values_list('bios__user_id', flat=True)
			share = filtered_reactions.filter(share=1).values_list('bios__user_id', flat=True)
			seen = filtered_reactions.filter(seen=1).values_list('bios__user_id', flat=True)
			comment = filtered_reactions.filter(comment__isnull=False).values_list('bios__user_id', flat=True)
			dislikepost_reactions.append(
				{'post_id': post.id, 'why_content': post.why_content, 'file': post.file, 'gif': post.gif,
				 'video': post.video, 'photo': post.photo, 'content': post.content, 'user_id': post.bio.user.id,
				 'username': post.bio.user.username,'first_name': post.bio.user.first_name, 'last_name': post.bio.user.last_name,
				 'favorites': favorites, 'like': like, 'profile_image': post.bio.photo_url,
				 'dislike': dislike, 'share': share, 'seen': seen,
				 'comment': comment, 'created_at': post.created_at, 'updated_at': post.updated_at})
		# print(dislikepost_reactions)
		paginator = PageNumberPagination()
		paginator.page_size = 20
		dislikepost_page = paginator.paginate_queryset(dislikepost_reactions, request)
		posts = dislikepost_page
		# posts = {'like_post': 'like_post_list'}
		return Response({'status': True, 'posts': posts})


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
			


class CommentsAPI(views.APIView):
	def get(self,request,id):

		reactions = LikePostReactions.objects.filter(like_post__id=id)
		dreactions = DisLikePostReactions.objects.filter(dislike_post__id=id)
		reaction_details = []
		for reaction in reactions:
			if reaction.comment:
				jx = {}
				usr = Bio.objects.filter(id=reaction.bios.id).values('id','user__username','user__first_name','user__last_name','photo_url','cover_photo_url')[0]
				jx.update(usr)
				jx.update({'comment':reaction.comment,'created_at':reaction.created_at})

				reaction_details.append(jx)
		# reaction_details = []
		for reaction in dreactions:
			if reaction.comment:
				jx = {}
				usr = Bio.objects.filter(id=reaction.bios.id).values('id', 'user__username', 'user__first_name',
																	 'user__last_name', 'photo_url', 'cover_photo_url')[0]
				jx.update(usr)
				jx.update({'comment': reaction.comment,'created_at':reaction.created_at})

				reaction_details.append(jx)
		# print(reaction_details)
		result = sorted(reaction_details, key=lambda x: x['created_at'])
		return Response(result[::-1])
