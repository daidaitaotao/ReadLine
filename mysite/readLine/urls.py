from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /lines/5/
    path('<int:line_number>/', views.LineDetail.as_view(), name='line_detail'),
]