from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMessage
from .models import *

# Create your views here.

#! ---------- VISTAS --------------


def home(request):
    return render(request, "core/home.html")


def themes(request):
    topics = Topic.objects.all()
    subtopics = Subtopic.objects.all()
    return render(
        request, "core/themes.html", {"topics": topics, "subtopics": subtopics}
    )


def email_validation(request):
    if request.method == "POST":
        print("Obteniendo")
        print(request.POST)

        # Accede a los datos del formulario utilizando los nombres de los campos
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email_user = request.POST.get("email")
        password = request.POST.get("password")

    return render(request, "core/email_validation.html")

