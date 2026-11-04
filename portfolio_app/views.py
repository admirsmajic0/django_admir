from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Student, Portfolio, Project

def index(request):
    active_portfolios = Portfolio.objects.filter(is_active=True)

    return render(request, 'portfolio_app/index.html', {'active_portfolios': active_portfolios})

class StudentListView(ListView):
    model = Student
    template_name = 'portfolio_app/student_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'portfolio_app/student_detail.html'
    context_object_name = 'student'

class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio_app/portfolio_detail.html'
    context_object_name = 'portfolio'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portfolio_app/projects_detail.html'
    context_object_name = 'project'