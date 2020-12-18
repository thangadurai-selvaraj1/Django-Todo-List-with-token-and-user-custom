from django.urls import path

from .views import TaskList, TaskDetailView

urlpatterns = [
    path('', TaskList.as_view()),
    path('<int:id>', TaskDetailView.as_view()),
]
