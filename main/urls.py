from django.urls import path
from . import views


app_name = 'habit'

urlpatterns = [
    path('', views.HabitListView.as_view(), name='habit-list'),
    path('create/', views.HabitCreateView.as_view(), name='habit-create'),
    path('<int:pk>/update/', views.HabitUpdateView.as_view(), name='habit-update'),
    path('<int:pk>/delete/', views.HabitDeleteView.as_view(), name='habit-delete'),
    path('<int:habit_id>/toggle/', views.ToggleHabitView.as_view(), name='toggle-habit'),

    # Category URLs
    path('category/create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),
]