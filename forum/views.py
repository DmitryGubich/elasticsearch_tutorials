from django.shortcuts import render
from django.views import View

from forum.documents import PostDocument
from forum.models import Post

TEMPLATE_NAME = 'search.html'


class ElasticSearchView(View):

    def get(self, request):
        query = request.GET.get('q')

        search_result = PostDocument.search().filter('match_phrase', content=query)
        if not search_result.count():
            search_result = ''
        return render(request, TEMPLATE_NAME, {'search_result': search_result})


class SimpleSearchView(View):

    def get(self, request):
        query = request.GET.get('q')

        search_result = Post.objects.all().filter(content__icontains=query)
        return render(request, TEMPLATE_NAME, {'search_result': search_result})
