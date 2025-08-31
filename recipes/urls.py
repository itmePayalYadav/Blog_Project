from django.urls import path
from .views import (
    recipe_list_view,
    recipe_create_view,
    recipe_detail_view,
    recipe_update_view,
    recipe_detail_hx_view,
    recipe_update_hx_view
)

urlpatterns = [
    # List & Create
    path("", recipe_list_view, name="recipe-list"),  
    path("create/", recipe_create_view, name="recipe-create"),

    # HTMX detail & ingredient URLs (specific first)
    path("hx/<slug:slug>/ingredient/<int:id>/edit/", recipe_update_hx_view, name="recipe-update-hx"),
    path("hx/<slug:slug>/ingredient/view/", recipe_update_hx_view, name="recipe-update-new-hx"),  
    path("hx/<slug:slug>/", recipe_detail_hx_view, name="recipe-detail-hx"),  

    # Regular detail & update URLs (more general)
    path("<int:id>/edit/", recipe_update_view, name="recipe-update"),  
    path("<slug:slug>/", recipe_detail_view, name="recipe-detail"),  
]
