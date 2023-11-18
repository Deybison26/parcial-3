from django.shortcuts import redirect, render
from django.http import HttpRequest

from django.views.generic import TemplateView
# Create your views here.

from.models import BDprincipal
from.forms import PrincipalForm


class PruebaView(TemplateView):
    template_name = "paginaPrincipal.html"



def listaView(request):
    list = BDprincipal.objects.all()
    data = {
        'list':list
    }
    return render(request,'listado.html',data)


def createView(request):
    model = PrincipalForm(request.POST)
    if model.is_valid():
        model.save()
        model = BDprincipal()
        return redirect('listarTabla')
    return render(request, 'Formulario.html',{"form": model})

class FormularioActualizar(HttpRequest):
    def modificarView(request,id):
        modificarT = BDprincipal.objects.filter(id=id).first()
        form = PrincipalForm(instance=modificarT)
        
        return render(request,"modificarTabla.html",{"form":form, 'modificarT':modificarT})
    
    def actualizarView(request,id):
        modificarTa = BDprincipal.objects.get(id=id)
        form = PrincipalForm(request.POST, instance=modificarTa)

        if form.is_valid():
            form.save()
        list = BDprincipal.objects.all()
        data = {
            'list':list
        }
        return render(request,'listado.html',data)
    
    def deleteView(request,id):
        list = BDprincipal.objects.get(id=id)
        list.delete()
        list = BDprincipal.objects.all()
        data = {
            'list':list
        }
        return render(request, 'listado.html',data)
    
            




        
                
            
            
           




