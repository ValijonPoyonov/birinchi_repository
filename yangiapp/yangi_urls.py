from django.urls import path
from . import views
from .views import index_page, get_max_salary_employees, get_dependents


app_name = 'blogapp'
urlpatterns = [
path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.post_detail,
         name='post_detail'),

    # path('', list1, name='countries_list'),
    # path('', index_page, name='index_list'),
    # path('salary/<int:top>',get_max_salary_employees, name='employee-list'),
    # path('deps/<int:employee_id>', get_dependents, name='deps-list'),
]