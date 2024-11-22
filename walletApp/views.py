from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_django

def mi_pagina_inicio(request):
    lista_usuarios = [
        {'nombre': 'Lucas', 'apellido': 'Ibañez'},
        {'nombre': 'Federico', 'apellido': 'Aguirre'},
        {'nombre': 'Raul', 'apellido': 'Rolon'}
    ]
    contexto = {
        "todos_los_usuarios": lista_usuarios,
        "usuario_autenticado": "Lucas Ibañez"
    }
    return render(request, 'mi_pagina_inicio.html', contexto)



def login(request):
    username = ""
    
    if request.method == 'POST':
        username = request.POST.get('username', default = None)
        password = request.POST.get('password', default = None)
        
        usuario = authenticate(username=username, password=password)
        
        if usuario:
            login_django(request, usuario)
            print(f'Login successful, {usuario}')
            return redirect('inicio')
        else:
            print('Login failed')
        
    ctx = {
        "username": username,
    }
    return render(request, 'login.html', ctx)