from django.db.models import Q as django_Q
from django.shortcuts import render
from django.views import View
from elasticsearch_dsl import Q as elastic_Q

from forum.documents import PostDocument
from forum.models import Post
from forum.utils import timeit

TEMPLATE_NAME = 'search.html'


class ElasticSearchView(View):
    @timeit(search_name='elastic')
    def get(self, request):
        query = request.GET.get('q')

        search_result = PostDocument.search().filter(elastic_Q('fuzzy', content=query) |
                                                     elastic_Q('fuzzy', title=query) |
                                                     elastic_Q('nested',
                                                               path='category',
                                                               query=elastic_Q('fuzzy', category__name=query) |
                                                                     elastic_Q('fuzzy', category__slug=query)))
        if not search_result.count():
            search_result = ''
        return render(request, TEMPLATE_NAME, {'search_result': search_result})


class SimpleSearchView(View):
    @timeit(search_name='simple')
    def get(self, request):
        query = request.GET.get('q')

        search_result = Post.objects.all().filter(django_Q(content__contains=query) |
                                                  django_Q(title__contains=query) |
                                                  django_Q(category__name__contains=query) |
                                                  django_Q(category__slug__contains=query))
        if not search_result.count():
            search_result = ''
        return render(request, TEMPLATE_NAME, {'search_result': search_result})
