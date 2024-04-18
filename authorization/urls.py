from django.urls import path

from authorization.views import logout_view, login_view, register_view
urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),  # This should match the URL pattern in config.urls
    path('register/', register_view, name='register'),
]
