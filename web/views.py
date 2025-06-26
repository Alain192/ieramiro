from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistroForm
from .models import Paciente
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import TestBeckForm
from .models import BeckResultado


def inicio(request):
    return render(request, 'web/inicio.html')

def admision(request):
    return render(request, 'web/admision.html')

def niveles(request):
    return render(request, 'web/niveles.html')

def psicologia(request):
    return render(request, 'web/psicologia.html')

def login_view(request):
    return render(request, 'web/login.html')

def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password != confirm_password:
                messages.error(request, "Las contraseñas no coinciden.")
                return render(request, 'web/register.html', {'form': form})

            if User.objects.filter(username=email).exists():
                messages.error(request, "Este correo ya está registrado.")
                return render(request, 'web/register.html', {'form': form})

            # Crear usuario
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password
            )

            # Crear perfil Paciente
            Paciente.objects.create(
                user=user,
                dni=form.cleaned_data['dni'],
                genero=form.cleaned_data['genero'],
                telefono=form.cleaned_data['telefono'],
                fecha_nacimiento=form.cleaned_data['fecha_nacimiento']
            )

            messages.success(request, "Registro exitoso. Ahora puedes iniciar sesión.")
            return redirect('inicio')  # o redirige a una vista de login si prefieres

    else:
        form = RegistroForm()

    return render(request, 'web/register.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                username = User.objects.get(email=email).username
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('portada')
                else:
                    form.add_error(None, 'Correo o contraseña incorrectos.')
            except User.DoesNotExist:
                form.add_error('email', 'No existe una cuenta con ese correo.')
    return render(request, 'web/login.html', {'form': form})

@login_required
def portada(request):
    return render(request, 'web/portada.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def test_beck(request):
    return render(request, 'web/test_beck.html')

@login_required
def test_beck(request):
    if request.method == 'POST':
        form = TestBeckForm(request.POST)
        if form.is_valid():
            puntuacion = sum([int(valor) for valor in form.cleaned_data.values()])

            if puntuacion <= 13:
                nivel = "Mínimo o nulo"
            elif puntuacion <= 19:
                nivel = "Leve"
            elif puntuacion <= 28:
                nivel = "Moderado"
            else:
                nivel = "Severo"

            BeckResultado.objects.create(
                paciente=request.user,
                puntuacion=puntuacion,
                nivel=nivel
            )

            return render(request, 'web/beck_resultado.html', {
                'puntuacion': puntuacion,
                'nivel': nivel
            })
    else:
        form = TestBeckForm()

    return render(request, 'web/test_beck.html', {'form': form})


    