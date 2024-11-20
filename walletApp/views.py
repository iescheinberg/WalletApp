from django.shortcuts import render

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
    return render(request, 'login.html')