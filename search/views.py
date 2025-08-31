from django.shortcuts import render
from articles.models import Article
from recipes.models import Recipe

SEARCH_TYPE_MAPPING = {
    'articles': Article,
    'article': Article,
    'recipe': Recipe,
    'recipes': Recipe,
}

def search_view(request):
    query = request.GET.get('q')
    search_type = request.GET.get('type')

    Klass = SEARCH_TYPE_MAPPING.get(search_type, Recipe)

    qs = Klass.objects.search(query=query)

    context = {"queryset": qs}
    template = "result-view.html"

    if request.htmx:
        context['queryset'] = qs[:5]  
        template = "result-view.html"

    return render(request, template, context)