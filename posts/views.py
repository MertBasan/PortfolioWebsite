from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import ProjectInfo

# Create your views here.

def main(request):
    return render(request, 'index.html')

# views.py


def delete_project(request, pk):
    project = get_object_or_404(ProjectInfo, pk=pk)
    project.delete()
    return JsonResponse({'message': 'Project deleted successfully'}, status=204)
