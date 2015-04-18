from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import RequestContext
from models import Blogs, Categories
from django.http import Http404
# Create your views here.

def index(request):

    blogs = Blogs.objects.all().filter(publish=True)
    categories = Categories.objects.all()
    page_title = 'all blogs'
    meta_keywords = 'python, linux'
    meta_description = 'kdjohar personal blogs'
    no = blogs.count()


    return render_to_response('index.html', locals(), context_instance = RequestContext(request))

def category(request):
    page_title = 'all categories'
    categories = Categories.objects.all()
    meta_keywords = 'python, linux'
    meta_description = 'kdjohar personal blogs'

    return render_to_response('category-list.html', locals(), context_instance = RequestContext(request))

def category_view(request, slug):
    categories = Categories.objects.all()
    category = get_object_or_404(Categories, slug=slug)
    page_title = category.name
    meta_keywords = 'python, linux'
    meta_description = 'kdjohar personal blogs'
    blogs = Blogs.objects.filter(category=category).filter(publish=True)
    no = blogs.count()

    return render_to_response('category.html', locals(), context_instance = RequestContext(request))

def blog_view(request, slug):
    categories = Categories.objects.all()
    blog = get_object_or_404(Blogs, slug=slug)
    page_title = 'blog'+'|'+ ' '+ blog.title

    if blog.publish == True:
        pass
    else:
        raise Http404


    return render_to_response('blog.html', locals(), context_instance = RequestContext(request))

def error_404(request):


    categories = Categories.objects.all()
    page_title = 'Error - 404'
    return render_to_response('404.html', locals(), context_instance = RequestContext(request))

def handler404(request):
    page_title = 'Error - 404'
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request):
    page_title = 'Error - 500'
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response