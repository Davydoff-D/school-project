from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'learning_materials'

urlpatterns = [
    path('', views.index, name='index'),
    path('materials', views.materials, name='materials'),
    path('materials/<int:material_id>/', views.materials_detail, name='material_detail'),
    path('materials/<int:material_id>/tasks/', views.tasks, name='tasks'),
    path('materials/<int:material_id>/answers/<int:question_id>/<int:answermodel_id>/', views.answers, name='answers'),
    path('materials/<int:material_id>/tasks/<int:question_id>/', views.tasks_detail, name='tasks_detail'),
]
