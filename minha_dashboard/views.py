from calendar import month_abbr
from distutils.log import error
from re import template
from django.shortcuts import render, redirect
from datetime import date, datetime
from .models import nc_financeiro, lista, disponibilidade, promocoes, tempo, avaliacao, lista, lojas
import pandas as pd
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib import messages
import numpy as np
from datetime import date, timedelta
from django.core.serializers import serialize
import math
from django.contrib.auth.decorators import login_required

#yesterday = date.today() - timedelta(days=1)
today = date.today()

today0 = today.strftime('%Y-%m-%d')
today1 = today.strftime('%d/%m/%Y')
last_5days = today - timedelta(5) 
last_5days = last_5days.strftime('%Y-%m-%d')
month_current = today.month

def login_user(request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuário e senha inválido. Por favor tentar novamente.')
    
    return redirect('/login/')

@login_required
def home(request):

    name_loja = ""
    
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        name_loja = request.POST.get('name-loja')

        if start_date != "" and end_date != "" and name_loja != "" and name_loja != None:
            item = nc_financeiro.objects.values().filter(data__range = [start_date, end_date], cliente = request.user, restaurante = name_loja) 

        elif name_loja != "" and name_loja != None:
            item = nc_financeiro.objects.values().filter(cliente = request.user, restaurante = name_loja, mes = month_current)

        elif start_date != "" and end_date != "":
            item = nc_financeiro.objects.values().filter(data__range = [start_date, end_date], cliente = request.user)

    else:
        item = nc_financeiro.objects.values().filter(cliente = request.user, mes = month_current)
    
    try:
        df=pd.DataFrame(item)
        df['nps_medio'] = df['nps_medio'].replace(np.nan,0)
        df['cancelamento_pelo_restaurante'] = df['cancelamento_pelo_restaurante'].replace(np.nan,0)
        df['cancelamento_pelo_cliente'] = df['cancelamento_pelo_cliente'].replace(np.nan,0)
    except:
        item = nc_financeiro.objects.values().filter(cliente = request.user, mes = month_current)

    df=pd.DataFrame(item)

    df['cancelamento_pelo_restaurante'] = df['cancelamento_pelo_restaurante'].replace(np.nan,0)
    df['cancelamento_pelo_cliente'] = df['cancelamento_pelo_cliente'].replace(np.nan,0)
    
    df['cancelamento_pelo_restaurante'] = df['cancelamento_pelo_restaurante'].astype(float)
    df['faturamento_real'] = df['faturamento_real'].astype(float)
    df['nps_medio'] = df['nps_medio'].astype(float)
    df['numero_de_comentarios'] = df['numero_de_comentarios'].astype(float)
    df['numero_de_avaliacoes'] = df['numero_de_avaliacoes'].astype(float)
        
    ###LISTAS##

##tabela promocao

    if name_loja == None:
        lista1 = promocoes.objects.filter(cliente = request.user, data = today0)
    elif name_loja != "":
        lista1 = promocoes.objects.filter(loja = name_loja, cliente = request.user, data = today0)
    else:
        lista1 = promocoes.objects.filter(cliente = request.user, data = today0)
        
##tabela tempos
    

    if name_loja == None:
        lista2 = tempo.objects.filter(cliente = request.user, data = today0)
    elif name_loja != "":
        lista2 = tempo.objects.filter(loja = name_loja, cliente = request.user, data = today0)
    else:
        lista2 = tempo.objects.filter(cliente = request.user, data = today0)

##tabela avaliações

    if name_loja == None:
        lista3 = avaliacao.objects.filter(cliente = request.user, data_da_avaliação__range = [last_5days, today0])
    elif name_loja != "":
        lista3 = avaliacao.objects.filter(cliente = request.user, loja = name_loja, data_da_avaliação__range = [last_5days, today0])
    else:
        lista3 = avaliacao.objects.filter(cliente = request.user, data_da_avaliação__range = [last_5days, today0])

##tabela listas


    if name_loja == None:
        lista4 = lista.objects.filter(cliente = request.user, data = today0
        )
    if name_loja != "":
        lista4 = lista.objects.filter(loja = name_loja, cliente = request.user, data = today0)
    else:
        lista4 = lista.objects.filter(cliente = request.user, data = today0)

##tabela disponibilidade

    if name_loja == None:
        lista0 = disponibilidade.objects.filter(cliente= request.user, data = today0)
    if name_loja != "":
        lista0 = disponibilidade.objects.filter(loja = name_loja, cliente= request.user, data = today0)
    else:
        lista0 = disponibilidade.objects.filter(cliente= request.user, data = today0)

    ###INCENTIVOS_CARD###

    if name_loja == None:
        incentivo_loja = df['incentivo_loja'].sum()
        incentivo_ifood = df['incentivo_ifood'].sum()

    elif name_loja != "":
        incentivo_loja = df[df['restaurante'] == name_loja]
        incentivo_loja = incentivo_loja['incentivo_loja'].sum() 

        incentivo_ifood = df[df['restaurante'] == name_loja]
        incentivo_ifood = incentivo_ifood['incentivo_ifood'].sum() 
    
    else:
        incentivo_loja = df['incentivo_loja'].sum()
        incentivo_ifood = df['incentivo_ifood'].sum()

    incentivo_loja = round(incentivo_loja,2)
    incentivo_ifood = round(incentivo_ifood,2)

    incentivo_loja = '{0:,}'.format(incentivo_loja)
    incentivo_loja = incentivo_loja.replace(',','.')

    fim = incentivo_loja[-3:].replace('.',',')
    inicio = incentivo_loja[:len(incentivo_loja)-3]
    
    incentivo_loja = inicio + fim

    incentivo_ifood = '{0:,}'.format(incentivo_ifood)
    incentivo_ifood = incentivo_ifood.replace(',','.')

    fim = incentivo_ifood[-3:].replace('.',',')
    inicio = incentivo_ifood[:len(incentivo_ifood)-3]
    
    incentivo_ifood = inicio + fim

    ###CANCELAMENTOS_CARD###

    if name_loja == None:
        canc_cliente = df['cancelamento_pelo_cliente'].sum()
        canc_restaurante = df['cancelamento_pelo_restaurante'].sum()

    elif name_loja != "":
        canc_cliente = df[df['restaurante'] == name_loja]
        canc_cliente = canc_cliente['cancelamento_pelo_cliente'].sum() 

        canc_restaurante = df[df['restaurante'] == name_loja]
        canc_restaurante = canc_restaurante['cancelamento_pelo_restaurante'].sum() 
    
    else:
        canc_cliente = df['cancelamento_pelo_cliente'].sum()
        canc_restaurante = df['cancelamento_pelo_restaurante'].sum()


    canc_cliente = round(canc_cliente,2)
    canc_restaurante = round(canc_restaurante,2)

    canc_cliente = '{0:,}'.format(canc_cliente)
    canc_cliente = canc_cliente.replace(',','.')

    fim = canc_cliente[-3:].replace('.',',')
    inicio = canc_cliente[:len(canc_cliente)-3]
    
    canc_cliente = inicio + fim

    canc_restaurante = '{0:,}'.format(canc_restaurante)
    canc_restaurante = canc_restaurante.replace(',','.')

    fim = canc_restaurante[-3:].replace('.',',')
    inicio = canc_restaurante[:len(canc_restaurante)-3]
    
    canc_restaurante = inicio + fim
    
    ###FATURAMENTO_CARD###

    if name_loja == None:
        faturamento_card = df['faturamento_bruto'].sum()

    elif name_loja != "":
        faturamento_card = df[df['restaurante'] == name_loja]
        faturamento_card = faturamento_card['faturamento_bruto'].sum()

    else:
        faturamento_card = df['faturamento_bruto'].sum()
    
    faturamento_card = round(faturamento_card,2)

    faturamento_card = '{0:,}'.format(faturamento_card)
    faturamento_card = faturamento_card.replace(',','.')

    fim = faturamento_card[-3:].replace('.',',')
    inicio = faturamento_card[:len(faturamento_card)-3]

    faturamento_card = inicio + fim

    ###TICKET_MEDIO_CARD###

    if name_loja == None:
        ticket_card = df['ticket_medio'].mean()

    elif name_loja != "":
        ticket_card = df[df['restaurante'] == name_loja]
        ticket_card = ticket_card['ticket_medio'].mean()
    
    else:
        ticket_card = df['ticket_medio'].mean()

    ###TOTAL_PEDIDOS_CARD###

    if name_loja == None:
        num_pedidos = df['numero_de_pedidos'].sum()
    
    elif name_loja != "":
        num_pedidos = df[df['restaurante'] == name_loja]
        num_pedidos = num_pedidos['numero_de_pedidos'].sum() 
    
    else:
        num_pedidos = df['numero_de_pedidos'].sum()

    num_pedidos = '{0:,}'.format(round(num_pedidos))
    num_pedidos = num_pedidos.replace(',','.')

    ###CANCELAMENTOS_MES_GRÁFICO###

    cancelamento = df.groupby(by=['data'], dropna=False).sum()
    
    cancelamento = cancelamento[['cancelamento_pelo_cliente', 'cancelamento_pelo_restaurante']]

    cancelamento = cancelamento.replace(np.nan,0)
    cancelamento = cancelamento.reset_index()

    cancelamento['data'] = pd.to_datetime(cancelamento['data'])
    cancelamento['data'] = cancelamento['data'].dt.strftime('%Y-%m-%d')

    cancelamento_cliente = cancelamento['cancelamento_pelo_cliente'].tolist()
    cancelamento_loja = cancelamento['cancelamento_pelo_restaurante'].tolist()
    labels_cancelamentos = cancelamento['data'].tolist()

    ###INCENTIVOS_GRÁFICO###
    
    incentivo = df.groupby(by=['data'], dropna=False).sum()

    incentivo = incentivo[['incentivo_loja', 'incentivo_ifood']]

    incentivo = incentivo.replace(np.nan,0)
    incentivo = incentivo.reset_index()

    incentivo['data'] = pd.to_datetime(incentivo['data'])
    incentivo['data'] = incentivo['data'].dt.strftime('%Y-%m-%d')

    i_loja = incentivo['incentivo_loja'].tolist()
    i_ifood = incentivo['incentivo_ifood'].tolist()
    labels_incentivo = incentivo['data'].tolist()

    ###FATURAMENTO_BRUTO_GRÁFICO###

    group_faturamento = df.groupby(by=['data'], dropna=False).sum()
    group_taxa = df.groupby(by=['data'], dropna=False).mean()

    group_faturamento = group_faturamento[['faturamento_bruto']]
    group_taxa = group_taxa[['taxa_efetiva']]

    fatxtaxa = pd.merge(group_faturamento, 
                group_taxa, 
                on ='data', 
                how ='right')

    fatxtaxa = fatxtaxa.replace(np.nan,0)
    fatxtaxa = fatxtaxa.reset_index()

    fatxtaxa['data'] = pd.to_datetime(fatxtaxa['data'])
    fatxtaxa['data'] = fatxtaxa['data'].dt.strftime('%Y-%m-%d')

    fat_bruto = fatxtaxa['faturamento_bruto'].tolist()
    taxa_efetiva = fatxtaxa['taxa_efetiva'].tolist()
    labels_fat = fatxtaxa['data'].tolist()

    ###PEDIDOS_TICKET_MEDIO_GRÁFICO###

    group_numero_ped = df.groupby(by=['data'], dropna=False).sum()
    group_tm = df.groupby(by=['data'], dropna=False).mean()

    group_numero_ped = group_numero_ped[['numero_de_pedidos']]
    group_tm = group_tm[['ticket_medio']]

    numeroxtm = pd.merge(group_numero_ped, 
                group_tm, 
                on ='data', 
                how ='right')

    numeroxtm = numeroxtm.replace(np.nan,0)
    numeroxtm = numeroxtm.reset_index()

    numeroxtm['data'] = pd.to_datetime(numeroxtm['data'])
    numeroxtm['data'] = numeroxtm['data'].dt.strftime('%Y-%m-%d')

    numero_pedidos = numeroxtm['numero_de_pedidos'].tolist()
    tm = numeroxtm['ticket_medio'].tolist()
    labels_pedidos_tm = numeroxtm['data'].tolist()

    ###FATURAMENTO_DIA_GRÁFICO###

    fat_dia = df.groupby(by=['data'], dropna=False).mean()
    fat_dia = fat_dia[['faturamento_bruto']]
    fat_dia.reset_index(inplace=True)
    fat_dia = fat_dia.replace(np.nan, '')

    fat_dia['data'] = pd.to_datetime(fat_dia['data'])
    fat_dia['data'] = fat_dia['data'].dt.strftime('%Y-%m-%d')

    fat_dia1 = fat_dia['faturamento_bruto'].tolist()
    labels_fat_dia = fat_dia['data'].tolist()

    ###NPS_CARD###
    
    df['nps_medio'] = df['nps_medio'].replace(np.nan,0)

    if name_loja == None:
        nps_card = df[df['nps_medio'] != 0].mean()
        
    elif name_loja != "":
        nps_card = df[df['restaurante'] == name_loja]
        nps_card = nps_card[nps_card['nps_medio'] != 0].mean()

    else:
        nps_card = df[df['nps_medio'] != 0].mean()

    nps_card = nps_card.nps_medio

    if math.isnan(float(nps_card)):
        nps_card = 0
    
    ###NPS_DIA_GRÁFICO###

    df['nps_medio'] = df['nps_medio'].replace(np.nan,0)
    df2 = df.groupby(by=['data'], dropna=False).mean()
    df2 = df2[['nps_medio']]
    df2.reset_index(inplace=True)

    df2['data'] = pd.to_datetime(df2['data'])
    df2['data'] = df2['data'].dt.strftime('%Y-%m-%d')

    nps_dia = df2['nps_medio'].tolist()
    labels_nps = df2['data'].tolist()
        
    ###PEDIDOS_DIA_GRÁFICO###

    pedido_dia = df.groupby(by=['data'], dropna=False).sum()

    pedido_dia = pedido_dia[['numero_de_pedidos']]
    pedido_dia.reset_index(inplace=True)
    pedido_dia = pedido_dia.replace(np.nan, '')

    pedido_dia['data'] = pd.to_datetime(pedido_dia['data'])
    pedido_dia['data'] = pedido_dia['data'].dt.strftime('%Y-%m-%d')

    pedido_dia1 = pedido_dia['numero_de_pedidos'].tolist()
    labels_pedidos_dia = pedido_dia['data'].tolist()

    ##LISTAS_LOJA_DROP_DOWN##
    item_lista   = lojas.objects.values().filter(cliente = request.user)

    ## DICIONÁRIO COM VALORES ##

    context={

        ###INCENTIVOS_CARD###

        'incentivo_loja':incentivo_loja,
        'incentivo_ifood':incentivo_ifood,

        ###CANCELAMENTOS_CARD###

        'canc_restaurante':canc_restaurante,
        'canc_cliente':canc_cliente,

        ##LISTAS_LOJA_DROP_DOWN##

        'item_lista':item_lista,

        ###FATURAMENTO_DIA_GRÁFICO###

        'fat_dia1':fat_dia1,
        'labels_fat_dia':labels_fat_dia,

        ###FATURAMENTO_DIA_GRÁFICO###

        'pedido_dia1':pedido_dia1,
        'labels_pedidos_dia':labels_pedidos_dia,
        
        ###PEDIDOS_TICKET_MEDIO_GRÁFICO###

        'numero_pedidos':numero_pedidos,
        'tm':tm,
        'labels_pedidos_tm':labels_pedidos_tm,

        ##FATURAMENTO_GRÁFICO##

        'fat_bruto':fat_bruto,
        'taxa_efetiva':taxa_efetiva,
        'labels_fat':labels_fat,

        ###INCENTIVOS_GRÁFICO###

        'i_loja':i_loja,
        'i_ifood':i_ifood,
        'labels_incentivo': labels_incentivo,

        ###CANCELAMENTOS_MES_GRÁFICO###

        'cancelamento_cliente':cancelamento_cliente,
        'cancelamento_loja':cancelamento_loja,
        'labels_cancelamentos':labels_cancelamentos,

        ###TICKET_MEDIO_CARD###

        'ticket_card':round(ticket_card,2),

        ###NUMERO_PEDIDOS_CARD###

        'num_pedidos': num_pedidos,

        ##NPS_DIA_GRÁFICO## 

        'nps_dia_labels': labels_nps,
        'nps_dia_dados': nps_dia,

        ##FATURAMENTO_CARD##

        'faturamento_card':faturamento_card,

        ##NPS_CARD##

        'nps_card': round(nps_card,2),

        #LISTAS#

        'lista0' : lista0,
        'lista1': lista1,
        'lista2': lista2,
        'lista3': lista3,
        'lista4': lista4,

        #NOME_LOJA#

        'nome_loja': name_loja, 
    }

    return render(request, 'home.html', context)