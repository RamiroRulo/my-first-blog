from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

'''def home(request):
    return HttpResponse('Hello, World!')'''



def home(request):
	#posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return  render(request, 'home.html', {})
    # Create your views here.