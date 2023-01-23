from django.shortcuts import render
from .models import Count
def increment_likes(request):
    count = Count.objects.first()
    count.likes += 1
    count.save()
    return render({'likes': count.likes})

def increment_dislikes(request):
    count = Count.objects.first()
    count.dislikes += 1
    count.save()
    return render({'dislikes': count.dislikes})
def index(request):
    count = Count.objects.first()
    return render(request, 'index.html', {'count': count})
def index(request):
    try:
        count = Count.objects.first()
    except Count.DoesNotExist:
        count = Count.objects.create()
    return render(request, 'index.html', {'count': count})


def update_count(request):
    print("Hi")
    if request.method == 'POST':
        if 'like-button' in request.POST:
            c = Count.objects.first()
            c.likes += 1
            c.save()
        elif 'dislike-button' in request.POST:
            c = Count.objects.first()
            c.dislikes += 1
            c.save()
        return render(request,'index.html', {"count":c})
    else:
        return render(request, 'index.html')
