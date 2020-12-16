from django.urls import path, include
from .authentication import urls as auth_url
from .todo_task import urls as todo_url

urlpatterns = [
    path('auth/', include(auth_url)),
    path('task/', include(todo_url)),
]
