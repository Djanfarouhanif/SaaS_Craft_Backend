from django.shortcuts import render, redirect
from .models import Article, Comment



def index(request):
    article = Article.objects.all()

    context = {
        "articles":article
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
