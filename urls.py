from django.urls import path

from.import views

urlpatterns = [
    path('principal/', views.PruebaView.as_view()),
    path('formulario/', views.createView, name='formulario'),
    path('listarTabla/', views.listaView, name='listarTabla'),
    path('modificarTabla/<id>/',views.FormularioActualizar.modificarView, name='modificarTabla'),
    path('actualizar/<id>/',views.FormularioActualizar.actualizarView,name='actualizar'),
    path('eliminarTable/<id>/',views.FormularioActualizar.deleteView, name='eliminarTable')
]