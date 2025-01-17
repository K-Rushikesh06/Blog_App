from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Blogs, Category,Comment
from django.shortcuts import get_object_or_404
from django.db.models import Q

def posts_by_category(request,category_id):
    category = get_object_or_404(Category, pk=category_id)
    posts = Blogs.objects.filter(category=category)
    if not posts.exists():
        return HttpResponse(f"No posts found in category {category.category_name}")
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)
    
#blogs
def blogs(request,slug):
   single_post= get_object_or_404(Blogs,slug=slug,status='published')
   
   comments = Comment.objects.filter(blog = single_post)
   
   context={
    'single_post':single_post,
    'comments':comments
   }
   return render(request,'blogs.html',context)

   #search Functionality
def search(request):
    keyword=request.GET.get('keyword')

    blogs = Blogs.objects.filter(
    Q(title__icontains=keyword) |
    Q(short_description__icontains=keyword) |
    Q(blog_body__icontains=keyword),
    status='published'
)
    content={
        'blogs':blogs,
        'keyword':keyword
    }
  
    return render(request,'search.html',content)

