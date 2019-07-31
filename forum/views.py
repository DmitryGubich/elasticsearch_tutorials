from django.shortcuts import render
from django.views import View
from elasticsearch_dsl.query import Q as elasticQ

from forum.documents import CategoryDocument
from forum.models import Category
from forum.utils import timeit

TEMPLATE_NAME = 'search.html'


class ElasticSearchView(View):
    @timeit(search_name='elastic')
    def get(self, request):
        query = request.GET.get('q')

        search_result = CategoryDocument.search().query(elasticQ('match', content=query) |
                                                        elasticQ('match', title=query))
        if not search_result.count():
            search_result = ''
        return render(request, TEMPLATE_NAME, {'search_result': search_result})


class SimpleSearchView(View):
    @timeit(search_name='simple')
    def get(self, request):
        query = request.GET.get('q')

        search_result = Category.objects.all().filter(posts__author__car__brand=query)
        return render(request, TEMPLATE_NAME, {'search_result': search_result})
