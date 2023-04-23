from django.shortcuts import render
from django.http import HttpResponse
from EntregaTres.models import Publicacion, Perfil, Mensajes
from EntregaTres.forms import PublicacionForm, BuscarPublicacionesForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

def SobreMi(request):
    return render(request, "EntregaTres/sobre_mi.html")

class Inicio(ListView):
    model = Publicacion
    template_name = 'EntregaTres/Inicio.html'

class CategoriaAlien(ListView):  
    model = Publicacion
    context_object_name = "publicaciones"
    template_name = 'EntregaTres/Publicaciones/Categorias/Alienigenas.html'

    def get_queryset(self):
        return Publicacion.objects.filter(Topico__icontains="Alienigenas")

class CategoriaReptiliano(ListView):  
    model = Publicacion
    context_object_name = "publicaciones"
    template_name = 'EntregaTres/Publicaciones/Categorias/Reptilianos.html'

    def get_queryset(self):
        return Publicacion.objects.filter(Topico__icontains="Reptilianos")

class CategoriaTeorias(ListView):  
    model = Publicacion
    context_object_name = "publicaciones"
    template_name = 'EntregaTres/Publicaciones/Categorias/Teorias.html'

    def get_queryset(self):
        return Publicacion.objects.filter(Topico__icontains="Teorias")

class BuscarPublicaciones(ListView):  
    model = Publicacion
    context_object_name = "publicaciones"
    template_name = 'EntregaTres/Publicaciones/publicacion_list.html'


    def get_queryset(self):
        f = BuscarPublicacionesForm(self.request.GET)
        if f.is_valid():
            return Publicacion.objects.filter(Titulo__icontains=f.data["criterio_nombre"]).all()
        return Publicacion.objects.all()
    
class FiltrarPublicacion(DetailView):
    model = Publicacion

class PublicacionActualizar(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Publicacion
    success_url = reverse_lazy('Publicaciones')
    fields = '__all__'
    template_name = 'EntregaTres/Publicaciones/Publicaciones.html'
    context_object_name = "publicaciones"
    
    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return Publicacion.objects.filter(Autor=user_id, id=post_id).exists()

    def handle_no_permission(self):
        return render(self.request, "EntregaTres/No_Encontrado.html")

class PublicacionBorrar(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Publicacion
    success_url = reverse_lazy("Publicaciones")
    template_name = 'EntregaTres/Publicaciones/publicacion_borrar.html'

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return Publicacion.objects.filter(Autor=user_id, id=post_id).exists()

    def handle_no_permission(self):
        return render(self.request, "EntregaTres/No_Encontrado.html")

class Crear_Publicacion(LoginRequiredMixin, CreateView):
    model = Publicacion
    success_url = reverse_lazy('Publicaciones')
    fields = ['Titulo','Topico','Descripccion_Posteo','Imagen']
    template_name = 'EntregaTres/Publicaciones/Publicaciones.html'

    def form_valid(self,form):
        form.instance.Autor = self.request.user
        return super().form_valid(form)

class PublicacionDetalles(DetailView):
    model = Publicacion
    template_name = 'EntregaTres/Publicaciones/publicacion_detalles.html'

class Sistema_Usuarios(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/Inscribirse.html'
    success_url = reverse_lazy('Inicio')

class Login(LoginView):
    next_page = reverse_lazy('Inicio')

class Logout(LogoutView):
    template_name = 'registration/logout.html'

class Perfil(ListView):
    model = Perfil
    fields = '__all__'
    success_url = reverse_lazy('Inicio')
    context_object_name = "perfil"
    template_name = 'EntregaTres/Perfil/mi_perfil.html'
    
class CrearMensaje(CreateView):
    model = Mensajes
    fields = '__all__'
    template_name = 'EntregaTres/Mensajeria/mensaje-crear.html'
    success_url = reverse_lazy('mensaje-recibidos')

class VerMensajes(LoginRequiredMixin,UserPassesTestMixin,ListView):
    model = Mensajes
    template_name = 'EntregaTres/Mensajeria/mensaje-ver.html'
    context_object_name = "mensajes"

    def test_func(self):
        user_id = self.request.user.id
        mensaje_id = self.kwargs.get('pk')
        return Mensajes.objects.filter(destinatario=user_id).exists()

    def handle_no_permission(self):
        return render(self.request, "EntregaTres/No_Encontrado.html")

    def get_queryset(self):
        return Mensajes.objects.filter(destinatario=self.request.user.id).all()

class MensajeDetalle(UserPassesTestMixin,DetailView):
    model = Mensajes
    template_name = 'EntregaTres/Mensajeria/mensaje-detalles.html'

    def test_func(self):
        user_id = self.request.user.id
        mensaje_id = self.kwargs.get('pk')
        return Mensajes.objects.filter(destinatario=user_id).exists()

    def handle_no_permission(self):
        return render(self.request, "EntregaTres/No_Encontrado.html")

class BorrarMensajes(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Mensajes
    template_name = 'EntregaTres/Mensajeria/mensaje-borrar.html'
    success_url = reverse_lazy('mensaje-recibidos')

    def test_func(self):
        user_id = self.request.user.id
        mensaje_id = self.kwargs.get('pk')
        return Mensajes.objects.filter(destinatario=user_id).exists()

    def handle_no_permission(self):
        return render(self.request, "EntregaTres/No_Encontrado.html")