from django.shortcuts import render
from .models import Portfolio

def index(request):
    active_portfolios = Portfolio.objects.filter(is_active=True)

    return render(request, 'portfolio_app/index.html', {'active_portfolios': active_portfolios})

from django.views.generic import ListView, DetailView
from .models import Student

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