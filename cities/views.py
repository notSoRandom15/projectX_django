from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, TemplateView
from .models import City

class HomePageView(TemplateView):
    template_name = 'webapp/search-home.html'

class SearchResultsView(ListView):
    model = City
    template_name = 'webapp/search_results.html'

    def get_queryset(self):  
        query = self.request.GET.get("q")
        object_list = City.objects.filter(
            Q(name__icontains=query) | Q(state__icontains=query)
        )
        return object_list
    