from django.shortcuts import render, redirect
from datetime import date
from .models import ToDo

# Create your views here.
def main(request):
    if request.method == "POST":
        task = request.POST.get("task_input")
        if task: 
            ToDo.objects.create(title=task)
        

        return redirect(request.path)

    cnt_time = date.today()
    return render(request, "main/index.html", { 'cnt_time': cnt_time })

