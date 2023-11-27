from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TaskCreationForm, TagCreationForm
from todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    ordering = ["is_completed", "-created_at"]


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreationForm
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskCreationForm
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")


def change_status(request: HttpRequest, pk: int) -> HttpResponse:
    task = Task.objects.get(id=pk)
    task.is_completed = not task.is_completed
    task.save()
    return HttpResponseRedirect(reverse_lazy("todo:task-list"))


class TagListView(generic.ListView):
    model = Tag
    ordering = ["name"]


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagCreationForm
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagCreationForm
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
