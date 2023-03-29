from decimal import Decimal, InvalidOperation
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from http.client import HTTPResponse
from django.http import HttpResponseRedirect
from .models import *

import datetime

from django.http import JsonResponse
from django.views import View
from django.http import HttpResponse
from string import Template
import requests
from decouple import config

from django.shortcuts import render
from django.http import JsonResponse
from decouple import config
import requests
from .models import TemperatureData

from django.shortcuts import render
from django.http import JsonResponse
from decouple import config
import requests
from .models import TemperatureData


@login_required
def dashboard(request):
    # Para acessar a o sistema é necessário o usuário estar logado
    # Caso não esteja é redirecionado a página de Signin
    # Caso esteja autenticado é redirecionado a página principal
    if not request.user.is_authenticated:
        return redirect('/login')

    contexto = {

    }

    return render(request, "spyFruit/dashboard/dashboard.html", contexto)


def relatorio_temperatura(request_staste, dados_entrada):
    info = dados_entrada.split("-")
    ano_busca = info[0]
    mes_busca = info[1]
    dia_busca = info[2]
    dataTemperatura = []
    labels = []

    # Dicionário com os horários
    timestamp = datetime.timedelta(0)
    begin = True

    dados = TemperatureData.objects.all()
    if(ano_busca):
        dados = TemperatureData.objects.filter(timestamp__year=ano_busca)
    if(mes_busca):
        dados = TemperatureData.objects.filter(timestamp__month=mes_busca)
    if(dia_busca):
        dados = TemperatureData.objects.filter(timestamp__day=dia_busca)

    for dat in dados:
        flag = -1
        if begin == False:
            labels.append(dat.timestamp.time())
            dataTemperatura.append(dat.temperature)

        else:
            begin = False
    timestamp_number = timestamp.total_seconds()
    data_json = {
        'timestamp_texto': strfdelta(timestamp, "%D days %H:%M:%S"),
        'timestamp': timestamp_number,
        'dataTemperatura': dataTemperatura[::1],
        'labels': labels[::1]
    }
    return JsonResponse(data_json)


class DeltaTemplate(Template):
    delimiter = "%"


def strfdelta(tdelta, fmt):
    d = {"D": tdelta.days}
    d["H"], rem = divmod(tdelta.seconds, 3600)
    d["M"], d["S"] = divmod(rem, 60)
    t = DeltaTemplate(fmt)
    return t.substitute(**d)


def save_data(request):

    # Obtém a chave API e o ID do canal do arquivo .env
    api_key = config('API_KEY')
    channel = config('CHANNEL_ID')
    # Cria a url para obter os dados do canal no ThingSpeak
    url = f'https://api.thingspeak.com/channels/{channel}/feeds.json?api_key={api_key}'
    # Faz a requisição para a API do ThingSpeak
    response = requests.get(url)
    json_data = response.text
    data = json.loads(json_data)
    # Percorre todos os feeds retornados pelo ThingSpeak
    for feed in data['feeds']:
        try:
            timestamp = feed['created_at']
            temperature = Decimal(feed['field1'])
            #temperature = feed['field1']
            # Usado get_or_create para verificar de acordo com o timestamp se já existe um dado de temperatura adicionado ao banco
            # caso não exista é adicionado
            obj, created = TemperatureData.objects.get_or_create(
                timestamp=timestamp,
                defaults={'temperature': temperature}
            )
            # Se não existir será criado
            if not created:
                obj.temperature = temperature
                obj.save()
        except (ValueError, InvalidOperation):
            print('Valor de temperatura inválido')
    return JsonResponse({'status': 'ok'})
