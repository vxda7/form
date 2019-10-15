from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>/', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    path('<int:id>/delete/', views.delete, name="delete"),
    path('<int:id>/update/', views.update, name="update"),
    
    path('create-model-form/', views.create_model_form, name="create_model_form"),
    path('<int:id>/update-model-form/', views.update_model_form, name="update_model_form"),

    path('<int:id>/comments/create/', views.comment_create, name="comment_create"),
]