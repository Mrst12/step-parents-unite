""" Views file for the blogs """

from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm


def index(request):
    """ home page view """

    return render(request, 'index.html')


class PostList(generic.ListView):
    """ blog page view """

    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog_page.html'
    paginate_by = 6


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