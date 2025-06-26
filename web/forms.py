from django import forms
from django.contrib.auth.models import User
from .models import Paciente
from django import forms


class RegistroForm(forms.Form):
    dni = forms.CharField(max_length=8, label="DNI")
    email = forms.EmailField(label="Correo electrónico")
    genero = forms.ChoiceField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')])
    telefono = forms.CharField(max_length=15)
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirmar contraseña")

    def clean_dni(self):
        dni = self.cleaned_data['dni']
        if Paciente.objects.filter(dni=dni).exists():
            raise forms.ValidationError("Este DNI ya está registrado.")
        return dni

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo ya está registrado.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")
        if password != confirm:
            self.add_error('confirm_password', "Las contraseñas no coinciden.")
            
# web/forms.py
class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico', widget=forms.EmailInput(attrs={
        'placeholder': 'Correo electrónico'
    }))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={
        'placeholder': 'Contraseña'
    }))


#Formulario
opciones = [
    "No me siento triste",
    "Me siento triste",
    "Me siento todo el tiempo triste y no puedo evitarlo",
    "Estoy tan triste o soy tan infeliz que no puedo soportarlo",
]
class TestBeckForm(forms.Form):
    PREGUNTAS = [
        "1. Tristeza",
        "2. Pesimismo",
        "3. Fracaso",
        "4. Pérdida de placer",
        "5. Sentimientos de culpa",
        "6. Sentimientos de castigo",
        "7. Disconformidad con uno mismo",
        "8. Autocrítica",
        "9. Pensamientos o deseos suicidas",
        "10. Llanto",
        "11. Agitación",
        "12. Pérdida de interés",
        "13. Indecisión",
        "14. Desvalorización",
        "15. Pérdida de energía",
        "16. Cambios en los patrones de sueño",
        "17. Irritabilidad",
        "18. Cambios en el apetito",
        "19. Dificultad de concentración",
        "20. Cansancio o fatiga",
        "21. Pérdida de interés en el sexo",
    ]

    for i, pregunta in enumerate(PREGUNTAS, 1):
        choices = [(j, opciones[j]) for j in range(len(opciones))]
        locals()[f"pregunta_{i}"] = forms.ChoiceField(
            label=pregunta,
            choices=choices,
            widget=forms.RadioSelect,
        )

    
