from django.shortcuts import render
from django.views.generic import View
from django.http.response import JsonResponse
from .models import Post

# Create your views here.

class PostListView(View):

    def get(self, request):

        posts = Post.objects.all()

        posts_dict = {'results':[],
                      'count': posts.count()}

        for post in posts:
            post_as_dict = {'text': post.text,
                            'date_added': post.date_added,
                            'date_updated': post.date_updated,
                            'user': post.user.username,
                            'tags':[]}

            for tag in post.tags.all():
                post_as_dict['tags'].append(tag.name)

            posts_dict['results'].append(post_as_dict)

        return JsonResponse(posts_dict)

    def post(self, request):
        pass

