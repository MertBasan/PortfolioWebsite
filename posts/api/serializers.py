from rest_framework.serializers import ModelSerializer 
from ..models import ProjectInfo

class ProjectSerializer(ModelSerializer):
    
    class Meta:
        model = ProjectInfo
        fields = ['name', 'description', 'github', 'image']


