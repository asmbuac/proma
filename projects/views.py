from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Project

# Create your views here.
@login_required
def project_list(request):
    project_list = Project.objects.filter(owner=request.user)
    context = {
        "project_list": project_list,
    }
    return render(request, "projects/list.html", context)
