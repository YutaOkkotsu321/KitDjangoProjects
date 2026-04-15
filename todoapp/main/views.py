from django.shortcuts import render, redirect
from datetime import date
from .models import ToDo
from django.http import JsonResponse

# Create your views here.
def main(request):
    if request.method == "POST":
        task = request.POST.get("task_input")
        if task: 
            ToDo.objects.create(title=task)
        return redirect(request.path)
   
    cnt_time = date.today()
    filter_by = request.GET.get('filter', 'all')
    if filter_by == "pending":
        all_todos = ToDo.objects.filter(completed=False)
    elif filter_by == "completed":
        all_todos = ToDo.objects.filter(completed=True)
    else:
        all_todos = ToDo.objects.all()
    return render(request, "main/index.html", { 'cnt_time': cnt_time, 'all_todos': all_todos })

def toggle_todo(request, pk):
    if request.method == "POST":
        todo = ToDo.objects.get(pk=pk)
        todo.completed = not todo.completed
        todo.save()
        return JsonResponse({'completed': todo.completed})