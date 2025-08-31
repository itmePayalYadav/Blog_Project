from django.urls import reverse
from .models import Recipe, RecipeIngredient
from django.http import HttpResponse, Http404
from .forms import RecipeForm, RecipeIngredientForm
from django.forms.models import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

@login_required
def recipe_list_view(request):
    qs = Recipe.objects.filter(user=request.user)
    context = {
        "objects":qs
    }
    return render(request, "recipes/list.html", context)

@login_required
def recipe_create_view(request):
    form = RecipeForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        if request.htmx:
            headers = {
                "HX-Push": 'recipe-list'
            }
            context = {
                "object":obj
            }
            return render(request, "recipes/partials/detail.html", context)
        return redirect('recipe-list')
    return render(request, "recipes/create.html", context) 

@login_required
def recipe_detail_view(request, slug):
    hx_url = reverse("recipe-detail", kwargs={"slug": slug})
    context = {
        "hx_url": hx_url,
    }
    return render(request, "recipes/detail.html", context) 

@login_required
def recipe_detail_hx_view(request, slug):
    try:
        obj = Recipe.objects.get(slug=slug, user=request.user)
    except:
        obj = None
    if obj is None:
        return HttpResponse("Not Found")
    context = {'object': obj}
    return render(request, "recipes/partials/detail.html", context)

@login_required
def recipe_update_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    form = RecipeForm(request.POST or None, instance=obj)
    kwargs = {'slug': obj.slug}
    new_recipe_url = reverse('recipe-update-new-hx', kwargs=kwargs)
    context = {
        "form": form,
        "object": obj,
        "new_recipe_url":new_recipe_url
    }
    if form.is_valid():
        form.save()
    if request.htmx:
        return render(request, "recipes/partials/forms.html", context)
    return render(request, "recipes/update.html", context)

@login_required
def recipe_update_hx_view(request, slug, id=None):
    if not request.htmx:
        raise Http404

    try:
        parent_obj = Recipe.objects.get(slug=slug, user=request.user)
    except Recipe.DoesNotExist:
        return HttpResponse("Not Found")

    child_obj = None
    if id is not None:
        try:
            child_obj = RecipeIngredient.objects.get(recipe=parent_obj, id=id)
        except RecipeIngredient.DoesNotExist:
            child_obj = None  

    form = RecipeIngredientForm(request.POST or None, instance=child_obj)

    kwargs = {'slug': parent_obj.slug}
    url = reverse('recipe-update-new-hx', kwargs=kwargs)
    if child_obj:
        url = child_obj.get_hx_edit_url()

    context = {
        'object': child_obj,
        'form': form,
        'url': url
    }

    if form.is_valid():
        obj = form.save(commit=False)
        print(obj)
        if child_obj is None: 
            obj.recipe = parent_obj
        obj.save()
        context['object'] = obj
        return render(request, "recipes/partials/ingredient-inline.html", context)
    return render(request, "recipes/partials/ingredient-form.html", context)

@login_required
def recipe_delete_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    if request.method == "POST":
        obj.delete()
        success_url = reverse('recipe-list')
        return redirect(success_url)
    context = {
        "object":obj,
    }
    return render(request, "recipes/delete.html", context)

@login_required
def recipe_incredient_delete_view(request, id=None):
    obj = get_object_or_404(RecipeIngredient, id=id, user=request.user)
    if request.method == "POST":
        obj.delete()
        success_url = reverse('recipe-list')
        return redirect(success_url)
    context = {
        "object":obj,
    }
    return render(request, "recipes/delete.html", context)
