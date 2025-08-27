from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect, render


def home_view(request):
    """Show landing page for anonymous users, redirect authenticated users"""
    if request.user.is_authenticated:
        return redirect('habit:habit-list')
    else:
        return render(request, 'home.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('habits/', include('main.urls')),
    path('', home_view, name='home'),
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)