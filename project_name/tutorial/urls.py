from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('tutorial_list/', views.tutorial_list, name='tutorial_list'),
    
]

urlpatterns = [
    # Your existing URL patterns
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
