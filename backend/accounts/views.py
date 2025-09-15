from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .tasks import send_welcome_email

User = get_user_model()

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = make_password(request.POST["password"])
        user = User.objects.create(username=username, email=email, password=password)

        send_welcome_email.delay(user.email)

        return render(request, "register_success.html")

    return render(request, "register.html")