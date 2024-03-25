from rest_framework.viewsets import ModelViewSet
from ..models import ProjectInfo
from .serializers import ProjectSerializer

class ProjectViewSet(ModelViewSet):

    queryset = ProjectInfo.objects.all()
    serializer_class = ProjectSerializer