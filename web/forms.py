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
class TestBeckForm(forms.Form):
    PREGUNTAS_OPCIONES = [
        ("1. Tristeza", [
            (0, "No me siento triste."),
            (1, "Me siento triste gran parte del tiempo."),
            (2, "Me siento triste todo el tiempo."),
            (3, "Me siento tan triste o soy tan infeliz que no puedo soportarlo."),
        ]),
        ("2. Pesimismo", [
            (0, "No estoy desalentado respecto de mi futuro."),
            (1, "Me siento más desalentado respecto de mi futuro que lo que solía estarlo."),
            (2, "No espero que las cosas funcionen para mí."),
            (3, "Siento que no hay esperanza para mi futuro y que sólo puede empeorar."),
        ]),
        ("3. Fracaso", [
            (0, "No me siento como un fracasado."),
            (1, "He fracasado más de lo que hubiera debido."),
            (2, "Cuando miro hacia atrás, veo muchos fracasos."),
            (3, "Siento que como persona soy un fracaso total."),
        ]),
        ("4. Pérdida de Placer", [
            (0, "Obtengo tanto placer como siempre por las cosas de las que disfruto."),
            (1, "No disfruto tanto de las cosas como solía hacerlo."),
            (2, "Obtengo muy poco placer de las cosas que solía disfrutar."),
            (3, "No puedo obtener ningún placer de las cosas de las que solía disfrutar."),
        ]),
        ("5. Sentimientos de Culpa", [
            (0, "No me siento particularmente culpable."),
            (1, "Me siento culpable respecto de varias cosas que he hecho o que debería haber hecho."),
            (2, "Me siento bastante culpable la mayor parte del tiempo."),
            (3, "Me siento culpable todo el tiempo."),
        ]),
        ("6. Sentimientos de Castigo", [
            (0, "No siento que esté siendo castigado."),
            (1, "Siento que tal vez pueda ser castigado."),
            (2, "Espero ser castigado."),
            (3, "Siento que estoy siendo castigado."),
        ]),
        ("7. Disconformidad con uno mismo", [
            (0, "Siento acerca de mí lo mismo que siempre."),
            (1, "He perdido la confianza en mí mismo."),
            (2, "Estoy decepcionado conmigo mismo."),
            (3, "No me gusto a mí mismo."),
        ]),
        ("8. Autocrítica", [
            (0, "No me critico ni me culpo más de lo habitual."),
            (1, "Estoy más crítico conmigo mismo de lo que solía estarlo."),
            (2, "Me critico a mí mismo por todos mis errores."),
            (3, "Me culpo a mí mismo por todo lo malo que sucede."),
        ]),
        ("9. Pensamientos o Deseos Suicidas", [
            (0, "No tengo ningún pensamiento de matarme."),
            (1, "He tenido pensamientos de matarme, pero no lo haría."),
            (2, "Querría matarme."),
            (3, "Me mataría si tuviera la oportunidad de hacerlo."),
        ]),
        ("10. Llanto", [
            (0, "No lloro más de lo que solía hacerlo."),
            (1, "Lloro más de lo que solía hacerlo."),
            (2, "Lloro por cualquier pequeñez."),
            (3, "Siento ganas de llorar pero no puedo."),
        ]),
        # Puedes continuar así con las preguntas 11 a 21...
    ]

    # Crea dinámicamente los campos del formulario
    for index, (label, choices) in enumerate(PREGUNTAS_OPCIONES, 1):
        locals()[f"pregunta_{index}"] = forms.ChoiceField(
            label=label,
            choices=choices,
            widget=forms.RadioSelect,
        )

    
