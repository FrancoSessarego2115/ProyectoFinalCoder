from django.contrib import admin
from django.urls import path
from EntregaTres.views import (Inicio, Crear_Publicacion, BuscarPublicaciones,
                                FiltrarPublicacion, Sistema_Usuarios, Login, Logout, PublicacionDetalles, PublicacionActualizar,
                                PublicacionBorrar, CrearMensaje, VerMensajes, BorrarMensajes, MensajeDetalle,
                                CategoriaAlien, CategoriaReptiliano, CategoriaTeorias, SobreMi, Perfil, 
)
from django.conf import settings
from django.conf.urls.static import static         


urlpatterns = [
    path('admin/', admin.site.urls),
    path('SobreMi', SobreMi, name="SobreMi"),
    path('', Inicio.as_view(), name="Inicio"),
    path('publicaciones', BuscarPublicaciones.as_view(),name="Publicaciones"),     
    path('publicaciones/crear', Crear_Publicacion.as_view(),name="Publicaciones-crear"),     
    path('publicaciones/<pk>', FiltrarPublicacion.as_view(), name="publicaciones-todo"),
    path('publicacion/<pk>/detalle', PublicacionDetalles.as_view(), name="publicacion-detalle"),
    path('publicacion/<pk>/actualizar', PublicacionActualizar.as_view(), name="publicacion-actualizar"),
    path('publicacion/<pk>/borrar', PublicacionBorrar.as_view(), name="publicacion-borrar"),
    path('publicaciones/categoria/Alienigenas', CategoriaAlien.as_view(),name="Categoria-Alienigenas"),
    path('publicaciones/categoria/Reptilianos', CategoriaReptiliano.as_view(),name="Categoria-Reptilianos"),
    path('publicaciones/categoria/Teorias', CategoriaTeorias.as_view(),name="Categoria-Teorias"),
    path('Registrarse/', Sistema_Usuarios.as_view(), name="Registrarse"),
    path('Ingresar/', Login.as_view(), name="Ingresar"),
    path('Salir/', Logout.as_view(), name="Salir"),
    path('perfil', Perfil.as_view(), name="perfil"),
    path('mensaje/enviar', CrearMensaje.as_view(),name="mensaje-enviar"),   
    path('mensaje/recibidos', VerMensajes.as_view(),name="mensaje-recibidos"),   
    path('mensaje/<pk>/detalle', MensajeDetalle.as_view(),name="mensaje-detalle"),     
    path('mensaje/<pk>/borrar', BorrarMensajes.as_view(),name="mensaje-borrar"),     
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)