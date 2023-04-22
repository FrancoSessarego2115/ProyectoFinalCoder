from django.contrib import admin
from django.urls import path
from EntregaTres.views import (PaginaPrincipal, Inicio, Crear_Publicacion, BuscarPublicaciones,
                                FiltrarPublicacion, Sistema_Usuarios, Login, Logout, PublicacionDetalles, PublicacionActualizar,
                                PublicacionBorrar
)
from django.conf import settings
from django.conf.urls.static import static         


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PaginaPrincipal),
    path('inicio/', Inicio, name="Inicio"),
    path('publicaciones', BuscarPublicaciones.as_view(),name="Publicaciones"),     
    path('publicaciones/crear', Crear_Publicacion.as_view(),name="Publicaciones-crear"),     
    path('publicaciones/<pk>', FiltrarPublicacion.as_view(), name="publicaciones-todo"),
    path('publicacion/<pk>/detalle', PublicacionDetalles.as_view(), name="publicacion-detalle"),
    path('publicacion/<pk>/actualizar', PublicacionActualizar.as_view(), name="publicacion-actualizar"),
    path('publicacion/<pk>/borrar', PublicacionBorrar.as_view(), name="publicacion-borrar"),
    path('Registrarse/', Sistema_Usuarios.as_view(), name="Registrarse"),
    path('Ingresar/', Login.as_view(), name="Ingresar"),
    path('Salir/', Logout.as_view(), name="Salir"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)