from django.urls import path
from django.views.generic import TemplateView

from forum.views import ElasticSearchView, SimpleSearchView

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html')),
    path('elastic_search/', ElasticSearchView.as_view(), name='elastic_search'),
    path('simple_search/', SimpleSearchView.as_view(), name='simple_search')
]
