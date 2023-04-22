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

def PaginaPrincipal(request):
    return render(request, 'EntregaTres/PaginaPrincipal.html')

def Inicio(request):
    return render(request, 'EntregaTres/Inicio.html')


class BuscarPublicaciones(ListView):  
    model = Publicacion
    context_object_name = "publicaciones"

    def get_queryset(self):
        f = BuscarPublicacionesForm(self.request.GET)
        if f.is_valid():
            return Publicacion.objects.filter(Titulo__icontains=f.data["criterio_nombre"]).all()
        return Publicacion.objects.all()
    

class FiltrarPublicacion(DetailView):
    model = Publicacion

class Sistema_Usuarios(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/Inscribirse.html'
    success_url = reverse_lazy('Inicio')

class Login(LoginView):
    next_page = reverse_lazy('Inicio')

class Logout(LogoutView):
    template_name = 'registration/logout.html'

class PublicacionDetalles(DetailView):
    model = Publicacion
    template_name = 'EntregaTres/publicacion_detalles.html'

class Crear_Publicacion(LoginRequiredMixin, CreateView):
    model = Publicacion
    success_url = reverse_lazy('Publicaciones')
    fields = ['Titulo','Categoria','Descripccion_Posteo','Imagen']
    template_name = 'EntregaTres/Publicaciones.html'

    def form_valid(self,form):
        form.instance.Autor = self.request.user
        return super().form_valid(form)

class PublicacionActualizar(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Publicacion
    success_url = reverse_lazy('Publicaciones')
    fields = '__all__'
    template_name = 'EntregaTres/Publicaciones.html'
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
    template_name = 'EntregaTres/publicacion_borrar.html'

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return Publicacion.objects.filter(Autor=user_id, id=post_id).exists()

    def handle_no_permission(self):
        return render(self.request, "EntregaTres/No_Encontrado.html")

class PerfilActualizar(UpdateView):
    model = Perfil
    fields = '__all__'
    success_url = reverse_lazy('Inicio')
    template_name = 'EntregaTres/Perfil/perfil.html'
    
class CrearMensaje(CreateView):
    model = Mensajes
    fields = '__all__'
    template_name = 'EntregaTres/mensajes.html'
    success_url = reverse_lazy('Inicio')

class VerMensajes(LoginRequiredMixin,ListView):
    model = Mensajes
    template_name = 'EntregaTres/ver-mensajes.html'
    context_object_name = "mensajes"

    def get_queryset(self):
        return Mensajes.objects.filter(destinatario=self.request.user.id).all()

class BorrarMensajes(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Mensajes
    template_name = 'EntregaTres/borrar-mensajes.html'
    success_url = reverse_lazy('mensaje-recibidos')

    def test_func(self):
        user_id = self.request.user.id
        mensaje_id = self.kwargs.get('pk')
        return Publicacion.objects.filter(destinatario=user.id).exists()

    def handle_no_permission(self):
        return render(self.request, "EntregaTres/No_Encontrado.html")