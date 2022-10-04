from django.urls import path

from apps.erp.views.categories.views import *

app_name = 'erp'
urlpatterns = [
    path('category/list', CategoryListView.as_view(), name='category_list'),
    path('category/add', CategoryCreateView.as_view(), name='category_add'),
    #path('category/list2', category_list, name='category_list'),
    # path('dos/', myFirstView)
]
