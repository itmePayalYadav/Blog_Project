from django import forms
from .models import Recipe, RecipeIngredient

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'directions']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter the recipe name',
                # 'hx-post':'.',
                # 'hx-trigger':'keyup changed delay:500ms',
                # 'hx-target':'#recipe-container',
                # 'hx-swap':'outerHTML'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Write a short description',
                'rows': 3,
                # 'hx-post':'.',
                # 'hx-trigger':'keyup changed delay:500ms',
                # 'hx-target':'#recipe-container',
                # 'hx-swap':'outerHTML'
            }),
            'directions': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Step-by-step cooking instructions',
                'rows': 5,
                # 'hx-post':'.',
                # 'hx-trigger':'keyup changed delay:500ms',
                # 'hx-target':'#recipe-container',
                # 'hx-swap':'outerHTML'
            }),
        }

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['name', 'quantity', 'unit']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter ingredient name'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter quantity'
            }),
            'unit': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter unit (e.g. grams, cups)'
            }),
        }
