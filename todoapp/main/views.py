from django.shortcuts import render
from datetime import date


# Create your views here.
def main(request):
    cnt_time = date.today()
    return render(request, "main/index.html", { 'cnt_time': cnt_time })

