from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/index.html',{})

# Create your views here.
