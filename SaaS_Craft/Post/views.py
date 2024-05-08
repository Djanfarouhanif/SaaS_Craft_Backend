from django.shortcuts import render, redirect
from .models import Article, Comment, Profile
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from Serializer.Article_serializer import ArticleSerializer
from Serializer.Comment_serializer import CommentSerializer
from Serializer.Profile_serialize import ProfileSerialiser
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def index(request):
    article = Article.objects.all()
    serializer = ArticleSerializer(article,many=True)
    users =  request.user.username
    user_current = bool(users)

    return Response(serializer.data, status=200)

@api_view(['POST'])
def settings(request):
    if request.method == "POST":
        if request.FILES.get("image"):
            image = request.FILES["image"]
        else:
            image = None

        title = request.POST["title"]
        post = request.POST["post"]

        serializer = ArticleSerializer(data={
            'title':title,
            'post':post,
            'post_image': image
        })
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
    else:
        return Response({'error': 'Only POST requests are allowed.'}, status=405)

@api_view(['GET'])
def article_post(request, pk):
    try:
        article = Article.objects.get(id=pk)
    except Articel.DoesNotExist:
        return Response({'error': 'Article not found'}, status=404)

    comments = Comment.objects.filter(article=article)
    article_serializer = ArticleSerializer(article)
    comments_serializer = CommentSerializer(comments, many=True)

    data = {
        'article':article_serializer.data,
        'comments':comments_serializer.data
    }
    return Response(data, status=200)

@api_view(['GET'])
def articleComment(request, pk):
    try:
        article = Article.objects.get(id=pk)

    except article.DoesNotExist:
        Response({'error':'Article not found'}, status=404)
    if request.method=="POST":
        text = request.POST["comment"]
        
        if text :
            
            comment = Comment.objects.create(article=article, text=text)
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status=201)
        else:
            return Resopnse({'error': 'Comment text is required'}, status=400)
    else:
        return Resopnse({'error': 'Only POST requests are allowed.'}, status=405)
        
@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        
        if username is None or email is None or password is None or password2 is None:
            return Response({"error": f'Missing required fields {username, email, password, password2}' }, status=400)
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=400)
        
        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email is already in user'}, status=400)

        if password != password2:
            print(request.user, "*********2")
            return Response({'error': 'Passwords do not match'}, status=400)

        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()

            # login directly for user
            
        new_user_login = authenticate(username=username, password=password)
        user_login = login(request, new_user_login)
        if new_user_login is not None:
            login(request, new_user_login)

            new_profile = Profile.objects.create(user=new_user)
            new_profile.save()

            return Response({'succes': 'User Created successfully'}, status=200)
            
        else:

            return Response({'error': 'Failed to authenticate user'}, status=400)


    else:
        return Response({'error': 'Only POST requests are allowed'}, status=405)

# Correct this part of code
@api_view(['POST'])
def signin(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST['password']

        user = authenticate(username = username, password = password)
        
        if user is not None:
            login(request, user)
            return Response({'succes': 'User authenticated successfully'}, status=200)
        else:
            return Response({'error': 'Username or password not matching'}, status=400)

    else:
        return Response({'error': 'Only POST requests are allowed  '}, status=405)

@api_view(['GET'])
def logout(request):
    logout(request)
    return Response({'success': 'User logged out successfully'}, status=200)