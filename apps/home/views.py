# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import PessoaForm
import json as j
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
#@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@csrf_exempt
#@login_required(login_url="/login/")
def pages(request):
    
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        print(request)
        print(load_template)
        print(request.method)
        context['segment'] = load_template
        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        
        if load_template == 'chat.html':
            if request.method == 'POST':
                print('Entrou no post')
                form = PessoaForm(request.POST)
                
                if form.is_valid():  # Corrigido de 'formulario' para 'form'
                    formulario = PessoaForm()
                    msg = form.cleaned_data['mensagem']
                    print(msg)
                    context = {'formulario': formulario} # Corrigido de 'formulario' para 'form'
                    html_template = loader.get_template('home/' + load_template)
                    return HttpResponse(html_template.render(context, request))
            
            if request.method == 'GET':
                print('Entrou no get')
                formulario = PessoaForm()
                print(formulario)
                context = {'formulario': formulario}  # Adiciona o formulário ao contexto
                html_template = loader.get_template('home/' + load_template)
                return HttpResponse(html_template.render(context, request))
            
        if load_template == 'teste.html':
            if request.method == 'POST':
                html_template = loader.get_template('home/' + load_template)
                return HttpResponse(html_template.render(context, request))
            
            if request.method == 'GET':
                html_template = loader.get_template('home/' + load_template)
                return HttpResponse(html_template.render(context, request))
            
        if load_template == 'webhook': 
            print('oi')   
            if request.method == 'POST':
                print('entrou no webhook')
                data = j.loads(request.body)
                print(data)
                # Faça algo com os dados recebidos, por exemplo, salve no banco de dados
                # e retorne uma resposta adequada

            return j.JsonResponse({'status': 'success'})

                
        print('Deu ruim')
        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
    

@csrf_exempt
def webhook_receiver(request):
    print('oi')
    if request.method == 'POST':
        print('entrou no webhook')
        data = j.loads(request.body)
        # Faça algo com os dados recebidos, por exemplo, salve no banco de dados
        # e retorne uma resposta adequada

        return j.JsonResponse({'status': 'success'})

    return j.JsonResponse({'status': 'error', 'message': 'Método não permitido'}, status=405)




