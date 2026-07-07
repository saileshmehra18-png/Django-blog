from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from . models import Blog,Category



def post_by_category(request, category_id):
    post = Blog.objects.filter(category=category_id,status='Published')
    try:
        category = Category.objects.get(pk=category_id)
    except:
        # redirect user to home if category does not existt
        return redirect('home')
    # use the 404 when you want to show the 404 error page if the category dosen't exists
    # category = get_object_or_404(Category, pk=category_id)
    context = {
        'post':post,
        'category':category
    }
    return render(request, 'post_by_category.html', context)