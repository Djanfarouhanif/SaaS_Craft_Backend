from django.shortcuts import render, redirect
from .models import Article, Comment, Profile
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages


def index(request):

    
    article = Article.objects.all()
    users =  request.user.username

    user_current = False
    if users:
        user_current = True
   
    context = {
        "articles":article,
        "user_current":user_current
        
    }
    return render(request, 'index.html', context)

def settings(request):
    if request.method == "POST":
        if request.FILES["image"]:
            image = request.FILES["image"]
        else:
            image = None

        title = request.POST["title"]
        post = request.POST["post"]


        artilce = Article.objects.create(title=title, post=post, post_image=image)
        artilce.save()
        return redirect('settings')
    else:
        return render(request, "settings.html")

def article_post(request, pk):
    article = Article.objects.get(id=pk)
    comments = Comment.objects.filter(article=article)

    return render(request, 'post.html', {"article": article,"comments": comments})

def articleComment(request, pk):
    article = Article.objects.get(id=pk)
    if request.method=="POST":
        text = request.POST["comment"]
        
        comment = Comment.objects.create(article=article, text=text)
        comment.save()
        return redirect("/article_post/"+ pk)
    else:
        return redirect("article_post")

def signup(request):
    if request.user in User.objects.all():
        return redirect("index")
    else:
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST["password2"]

            if User.objects.filter(username=username).exists():
                messages.info(request, "username exists alredy")
                return redirect("signup")
            
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email is alredy use')
                return redirect("signup")
            if password == password2:
                new_user = User.objects.create_user(username=username, email=email, password=password)
                new_user.save()

                # login directly for user
                
                new_user_login = authenticate(username=username, password=password)
                user_login = login(request, new_user_login)

                new_profile = Profile.objects.create(user=new_user)
                new_profile.save()
                return redirect("index")
            else:
                messages.error(request, "password no matching ")
                return redirect("signup")


    return render(request, 'signup.html')

# Correct this part of code
def signin(request):
    if request.user in User.objects.all():
        return redirect('index')
    else:
       
        if request.method == 'POST':
            username = request.POST["username"]
            password = request.POST['password']

            user = authenticate(username = username, password = password)
            
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                messages.error(request, "Username or Password Not matching ")
                return redirect('signin')

    return render(request, 'login.html')


def Logout(request):
    logout(request)
    return redirect('signin')