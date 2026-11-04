from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name = 'index'),
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),
    path('portfolios/<int:pk>/', views.PortfolioDetailView.as_view(), name='portfolio_detail'),
]