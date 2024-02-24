from django.shortcuts import render, redirect
from .models import Article, Comment



def index(request):
    article = Article.objects.all()

    context = {
        "articles":article
    }
    return render(request, 'templates.html', context)

def settings(request):
    if request.method == "POST":
        if request.FILES["article_image"]:
            image = request.FILES["article_image"]
        else:
            image = None

        title = request.POST["title"]
        post = request.POST["post"]

        artilce = Article.objects.create(title=title, post=post, image=image)
        artilce.save()
        return redirect('settings')
    else:
        return render(request, "settings.html")

        
def articleComment(request, pk):
    article = Article.objects.get(id=pk)
    if request.method=="POST":
        text = request.POST["comment"]
        
        comment = Comment.objects.create(article=article, text=text)
        comment.save()
        return redirect("/")
    else:
        return redirect("/")