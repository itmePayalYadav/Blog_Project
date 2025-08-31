from .views import home   
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls),
    path('search/', include("search.urls")),
    path('accounts/', include("accounts.urls")),
    path('recipes/', include("recipes.urls")),
    path('articles/', include("articles.urls")), 
]
