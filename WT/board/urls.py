from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  # ... your existing URL patterns ...

                  path('', views.home, name='home'),
                  path('create/', views.create, name='create'),
                  path('update/<id>', views.update, name='update'),
                  path('delete/<id>', views.delete, name='delete'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
