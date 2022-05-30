""" Views file for the blogs """

from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Post
from .forms import CommentForm, BlogForm


def index(request):
    """ home page view """

    return render(request, 'index.html')


class PostList(generic.ListView):
    """ blog page view """

    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog_page.html'
    paginate_by = 6


def profile(request):
    """ profile page view """
    return render(request, 'profile.html')


def publish(request):
    """ Publish a blog if authenticated user """
    if request.method == 'POST':
        blog_form = BlogForm(request.POST, request.FILES)

        if blog_form.is_valid():
            form = blog_form.save(commit=False)
            form.author = User.objects.get(username=request.user.username)
            form.slug = form.title.replace(" ", "-")
            messages.success(
                request, 'Your blog has been submitted for approval'
            )
            form.save()
        return redirect('my_blogs')

    blog_form = BlogForm()
    context = {'blog_form': blog_form}
    return render(
        request,
        'publish.html', context
    )


def my_blogs(request):
    """ authenticated user can view their own blogs """

    logged_in_user = request.user
    logged_in_user_posts = Post.objects.filter(author=logged_in_user)
    return render(request, 'my_blogs.html', {'posts': logged_in_user_posts})


def edit_post(request, post_id):
    """ users that are authenticated can edit their own blog """
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        blog_form = BlogForm(request.POST, instance=post)
        if blog_form.is_valid():
            form = blog_form.save(commit=False)
            form.approved = False
            messages.success(
                request,
                'Updated blog has been successfully submitted for approval'
            )
            form.save()
            return redirect('my_blogs')
    blog_form = BlogForm(instance=post)
    context = {'blog_form': blog_form}
    return render(request, 'edit_blog.html', context)


def delete_post(request, post_id):
    """ Authenticated users can delete their own blogs"""
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    messages.success(request, 'Blog deleted!')
    return redirect('my_blogs')


class BlogDetail(View):
    """ View for the complete post"""

    def get(self, request, slug, *args, **kwargs):
        """ Get post information """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
             
        return render(
            request,
            "blog_details.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """ posting comments """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            messages.success(
                request, "Your comment has been submitted, awaiting approval")
            comment.save()
        else:
            comment_form = CommentForm()
                
        return render(
            request,
            "blog_details.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class BlogLike(View):
    """ user to like/unlike blogs"""

    def post(self, request, slug):
        """ function for like/unlike"""

        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('blog_details', args=[slug]))
