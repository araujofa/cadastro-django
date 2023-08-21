from django.shortcuts import render
from .models import Usuarios

# Create your views here.
def index(request):
    return render(request,'cadastro/index.html')

def sucesso(request):
    usuario = Usuarios()

    if request.method == 'POST':
        usuario.nome = request.POST.get('nome')
        usuario.email = request.POST.get('email')
        usuario.senha = request.POST.get('senha')
    else:
        return False
         
    usuario.save()

    usuarios = {
        'usuarios': Usuarios.objects.all().delete()
    }

    return render(request, 'cadastro/sucesso.html', usuarios)