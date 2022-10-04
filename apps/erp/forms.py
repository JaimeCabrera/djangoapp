from django.forms import ModelForm

from apps.erp.models import Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
