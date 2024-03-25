from django.db import models

class ProjectInfo(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    github = models.URLField()
    image = models.FileField(blank=True)  
    show = models.BooleanField(default=False)

    def __str__(self):
        return self.name

