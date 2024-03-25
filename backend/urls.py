from django.contrib import admin
from django.urls import path, include, re_path
from posts import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('posts.api.urls')),
    path('',views.main,name='home'),
    # Serve the React index.html for all other routes
    path('api/projects/<int:pk>/', views.delete_project, name='delete_project'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
