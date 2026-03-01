from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Comment
from .comment_form import CommentForm
from django.contrib import messages

def blog_views(request):
    blogs = Blog.objects.all().order_by('-date')
    return render(request, 'blog.html', {'blogs': blogs})



def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    comments = Comment.objects.filter(blog=blog).order_by('-created_at')
    recent_blogs = Blog.objects.order_by('-date')[:4]
    categories = Blog.objects.values_list('category', flat=True).distinct()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            messages.success(request, "Your comment was posted successfully!")
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = CommentForm()

    context = {
        'blog': blog,
        'comments': comments,
        'recent_blogs': recent_blogs,
        'categories': categories,
        'form': form,
    }

    return render(request, 'detail.html', context)