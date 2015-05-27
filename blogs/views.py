from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import RequestContext
from models import Blogs, Categories
from django.http import Http404
from django.contrib.sitemaps import Sitemap
import datetime
# Create your views here.

def index(request):

    blogs = Blogs.objects.all().filter(publish=True)[:3]
    categories = Categories.objects.all()
    page_title = 'Home'
    meta_keywords = 'kd Johar, kd, johar, KDJOHAR, KD JOHAR, KD, Karan, Karandeep Singh Johar, Karandeep Singh'
    meta_description = 'A site by Kd Johar, devoted to his Learning in programming.'
    no = blogs.count()


    return render_to_response('index.html', locals(), context_instance = RequestContext(request))

def blogs(request):

    blogs = Blogs.objects.all().filter(publish=True)
    categories = Categories.objects.all()
    page_title = 'all blogs'
    title = 'blogs'
    recent_blogs = Blogs.objects.filter(publish=True)[:5]
    meta_keywords = 'Technical blogs,programming blogs, programming'
    meta_description = 'The technical Blogs by Kd Johar'
    no = blogs.count()


    return render_to_response('allblogs.html', locals(), context_instance = RequestContext(request))


def category_view(request, slug):
    categories = Categories.objects.all()
    category = get_object_or_404(Categories, slug=slug)
    recent_blogs = Blogs.objects.filter(publish=True)[:5]
    page_title = 'category'+'-'+category.name
    title = category.name
    meta_keywords = category.name
    meta_description = 'Blogs related to '+category.name
    blogs = Blogs.objects.filter(category=category).filter(publish=True)
    no = blogs.count()

    return render_to_response('category.html', locals(), context_instance = RequestContext(request))

def blog_view(request, slug):
    categories = Categories.objects.all()
    recent_blogs = Blogs.objects.filter(publish=True)[:5]
    blog = get_object_or_404(Blogs, slug=slug)
    page_title = 'blog'+'|'+ ' '+ blog.title

    if blog.publish == True:
        pass
    else:
        raise Http404


    return render_to_response('blog.html', locals(), context_instance = RequestContext(request))

def handler404(request):

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
def contact(request):

    blogs = Blogs.objects.all().filter(publish=True)[:3]
    categories = Categories.objects.all()
    page_title = 'Contact'
    meta_keywords = 'Contact Kd johar'

    meta_description = 'Contact Kd Johar'
    no = blogs.count()
    return render_to_response('contact.html', locals(), context_instance = RequestContext(request))

class blog_sitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return Blogs.objects.filter(publish=True)

    def lastmod(self, obj):
        return obj.date

def io15(request):

    blogs = Blogs.objects.all().filter(publish=True)[:3]
    categories = Categories.objects.all()
    page_title = 'Google I/O 15'
    meta_keywords = 'google i/o, google i/o live streaming'
    meta_description = 'Watch google i/o15 here live streaming.'
    no = blogs.count()

    return render_to_response('io.html', locals(), context_instance = RequestContext(request))