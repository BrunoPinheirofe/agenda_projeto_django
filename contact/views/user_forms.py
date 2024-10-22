from django.contrib import messages
from django.shortcuts import redirect, render
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Usuário registrado")
            return redirect("contact:index")

    return render(request, "contact/register.html", {"form": form})


def login_view(request):
    form = AuthenticationForm(request)
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, "Logado com sucesso!")
            return redirect("contact:login")
        messages.error(request, "Login inválido")
    return render(request, "contact/index.html", {"form": form})


def logout_view(request):
    auth.logout(request)
    return redirect("contact:login")


def user_update(request):
    form = RegisterUpdateForm

    if request.method != "POST":
        return render(request, "contact/user_update.html", {"form": form})

    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(request, "contact/user_update.html", {"form": form})
    form.save()
    return redirect('contact:user_update')
