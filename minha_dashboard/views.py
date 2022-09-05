from calendar import month_abbr
from distutils.log import error
from re import template
from django.shortcuts import render, redirect
from datetime import date, datetime
from .models import metas, metas_dia, nc_financeiro, lista, disponibilidade, promocoes, tempo, avaliacao, lista, lojas
import pandas as pd
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
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

desc_last_day = today.strftime('%A')
desc_last_day = desc_last_day.lower()

last_1days = (today - timedelta(1)).strftime('%Y-%m-%d') 
current_day = (today - timedelta(1)).strftime('%Y-%m-%d') 

if today.day == 1:
    month_current = month_current - 1

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
            item10 = nc_financeiro.objects.values().filter(cliente = request.user, restaurante = name_loja, mes = month_current)

            print('1')
        elif name_loja != "" and name_loja != None:
            item = nc_financeiro.objects.values().filter(cliente = request.user, restaurante = name_loja, mes = month_current)
            item10 = nc_financeiro.objects.values().filter(cliente = request.user, restaurante = name_loja, mes = month_current)

            print('2')
        elif start_date != "" and end_date != "":
            item = nc_financeiro.objects.values().filter(data__range = [start_date, end_date], cliente = request.user)
            item10 = nc_financeiro.objects.values().filter(cliente = request.user, restaurante = name_loja, mes = month_current)

            print('3')

    else:
        item = nc_financeiro.objects.values().filter(cliente = request.user, mes = month_current)
        item10 = nc_financeiro.objects.values().filter(cliente = request.user, mes = month_current)

        print('4')
    try:
        df=pd.DataFrame(item)
        df['cancelamento_pelo_restaurante'] = df['cancelamento_pelo_restaurante'].replace(np.nan,0)
        df['cancelamento_pelo_cliente'] = df['cancelamento_pelo_cliente'].replace(np.nan,0)
        print('5')
    except:
        item = nc_financeiro.objects.values().filter(cliente = request.user, mes = month_current)
        print('6')


    df = pd.DataFrame(item)

    item2 = avaliacao.objects.values().filter(cliente = request.user)
    df2 = pd.DataFrame(item2)
    df3 = pd.DataFrame(item2)

    df3.rename(columns={'loja':'restaurante'}, inplace=True)
    df3 = df3[['cliente','restaurante','data', 'avaliação']] 
    
    df3 = pd.merge(df, df3, how = 'outer', on = ['restaurante','cliente','data'])
    df3 = df3[df3['id'].notna()]

    df2.rename(columns={'loja':'restaurante'}, inplace=True)
    df2 = df2[['cliente','restaurante','data', 'avaliação']] 
    
    df2_df = pd.merge(df, df2, how = 'outer', on = ['restaurante','cliente','data'])
    df2_df = df2_df[df2_df['faturamento_bruto'].notna()]

    #df2_df = df2_df.drop_duplicates()

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
        lista4 = lista.objects.filter(cliente = request.user, data = today0)
    elif name_loja != "":
        lista4 = lista.objects.filter(loja = name_loja, cliente = request.user, data = today0)
    else:
        lista4 = lista.objects.filter(cliente = request.user, data = today0)

    ##tabela disponibilidade

    if name_loja == None:
        lista0 = disponibilidade.objects.filter(cliente= request.user, data = today0)
    elif name_loja != "":
        lista0 = disponibilidade.objects.filter(loja = name_loja, cliente= request.user, data = today0)
    else:
        lista0 = disponibilidade.objects.filter(cliente= request.user, data = today0)

    ####card_fat_danterior###

    df['data'] = pd.to_datetime(df['data'])
    card_fat_danterior = df[df['data'] == last_1days]
    card_fat_danterior = df['faturamento_bruto'].sum()

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
    incentivo_geral = round(incentivo_loja + incentivo_ifood,2)

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

    incentivo_geral = '{0:,}'.format(incentivo_geral)
    incentivo_geral = incentivo_geral.replace(',','.')

    fim = incentivo_geral[-3:].replace('.',',')
    inicio = incentivo_geral[:len(incentivo_geral)-3]
    
    incentivo_geral = inicio + fim

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
    cancelamento_total = round(canc_cliente + canc_restaurante, 2)

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

    cancelamento_total = '{0:,}'.format(cancelamento_total)
    cancelamento_total = cancelamento_total.replace(',','.')

    fim = cancelamento_total[-3:].replace('.',',')
    inicio = cancelamento_total[:len(cancelamento_total)-3]
    
    cancelamento_total = inicio + fim
    
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

    ###taxa_efetiva_card###

    if name_loja == None:
        tx_efetiva_card = df['taxa_efetiva'].mean()

    elif name_loja != "":
        tx_efetiva_card = df[df['restaurante'] == name_loja]
        tx_efetiva_card = tx_efetiva_card['taxa_efetiva'].mean()

    else:
        tx_efetiva_card = df['taxa_efetiva'].mean()
    
    tx_efetiva_card = round(tx_efetiva_card,2)

    tx_efetiva_card = '{:.2%}'.format(tx_efetiva_card)

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
    fatxtaxa['taxa_efetiva'] = fatxtaxa['taxa_efetiva'].round(decimals = 2)

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

    ###NPS_DIA_GRÁFICO###

    df2 = df2_df.groupby(by=['data'], dropna=False).mean()
    df2 = df2[['avaliação']]
    df2.reset_index(inplace=True)

    df2['data'] = pd.to_datetime(df2['data'])
    df2['mes'] = df2['data'].dt.month
    #df2 = df2[df2['mes'] == month_current]
    df2['data'] = df2['data'].dt.strftime('%Y-%m-%d')
    df2 = df2.replace(np.nan,'')

    nps_dia = df2['avaliação'].tolist()
    labels_nps = df2['data'].tolist()

    ###NPS_CARD###
    
    df2_df['avaliação'] = df2_df['avaliação'].replace(np.nan,0)
    df2_df['data'] = pd.to_datetime(df2_df['data'])
    df2_df['mes'] = df2_df['data'].dt.month
    #df2_df = df2_df[df2_df['mes'] == month_current]

    if name_loja == None:
        nps_card = df2_df[df2_df['avaliação'] != 0].mean()
        
    elif name_loja != "":
        nps_card = df2_df[df2_df['restaurante'] == name_loja]
        nps_card = nps_card[nps_card['avaliação'] != 0].mean()

    else:
        nps_card = df2_df[df2_df['avaliação'] != 0].mean()

    nps_card = nps_card.avaliação

    if math.isnan(float(nps_card)):
        nps_card = 0
        
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

    item_lista  = lojas.objects.values().filter(cliente = request.user)

                        ### METAS ###

    ######dataframe tabela financeiro########

    df_item5 = pd.DataFrame(item)

    df_item5['data'] = pd.to_datetime(df_item5['data'], format='%Y-%m-%d')
    df_item5['dayofweek'] = df_item5['data'].dt.strftime('%A')
    df_item5['month'] = df_item5['data'].dt.strftime('%m')
    df_financeiro = df_item5[['cliente', 'restaurante', 'data', 'faturamento_bruto', 'month', 'dayofweek']]
    df_financeiro['dayofweek'] = df_financeiro['dayofweek'].str.lower()

    ##########dataframe metas######
    
    item3  = metas.objects.values().filter(cliente = request.user)
    df_metas = pd.DataFrame(item3)
    df_metas['data'] = pd.to_datetime(df_metas['data'], format='%Y-%m-%d')
    df_metas['month'] = df_metas['data'].dt.strftime('%m')
    df_metas['dayofweek'] = df_metas['data'].dt.strftime('%A')
    df_metas['dayofweek'] = df_metas['dayofweek'].str.lower()


    df_concat = pd.merge(df_financeiro,
                    df_metas[['cliente','restaurante', 'month', 'meta']],
                    how = 'outer',
                    on = ['month','cliente','restaurante']
                    )
    
    for i in range(len(df_concat)):
        if df_concat['month'][i][:1] == '0':
            df_concat['month'][i] = df_concat['month'][i][1:]

    #############dataframe metas por dia############

    item4 = metas_dia.objects.values().filter(cliente = request.user)
    df_perc_meta = pd.DataFrame(item4)
    df_perc_meta = pd.melt(df_perc_meta,
                        id_vars=['restaurante', 'cliente'],
                        value_vars=['monday','tuesday','wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        )

    df_perc_meta.rename(columns={'value':'percent', 'variable':'dayofweek'}, inplace=True)

    ############dataframe final############

    df_merge = pd.merge(df_concat,
                 df_perc_meta[['cliente','restaurante','dayofweek', 'percent']],
                 how = 'outer',
                 on = ['dayofweek', 'cliente','restaurante']
                )
    df_merge['meta_real'] = df_merge['percent'] * df_merge['meta']
    df_merge['month'] = df_merge['month'].astype(str)
    for i in range(len(df_merge)):
        if df_merge['month'][i][:1] == '0':
            df_merge['month'][i] = df_merge['month'][i][1:]
    
    df_merge['dayofweek'] = df_merge['dayofweek'].str.lower()

    df_date = pd.date_range("2022-01-01", periods=365, freq="d")
    df_date = pd.DataFrame(columns = ['data'], data = df_date)
    df_date['dayofweek'] = df_date['data'].dt.strftime('%A')
    df_date['month'] = df_date['data'].dt.strftime('%m')
    df_date['dayofweek'] = df_date['dayofweek'].str.lower()

    for i in range(len(df_date)):
        if df_date['month'][i][:1] == '0':
            df_date['month'][i] = df_date['month'][i][1:]
        
    df_date = df_date.groupby(['month','dayofweek']).count()
    df_date.reset_index(inplace=True)
    df_date.rename(columns={'data':'count_dayofweek'}, inplace=True)

    df_final = pd.merge(df_merge,
                    df_date[['dayofweek','month', 'count_dayofweek']],
                    how = 'inner',
                    on = ['month','dayofweek']
                    )


    df_final['meta_dia'] = df_final['meta_real'] / df_final['count_dayofweek']

    ###meta_taxa_efetiva###

    card_meta_tx = round(df_metas['meta_tx'].mean(),2)
    
    card_meta_tx = '{:.2%}'.format(card_meta_tx)

    ###gap_meta_tx###


    if card_meta_tx=="0,0":
        gap_card_meta_tx = '0'
    else:
        gap_card_meta_tx = round(float(tx_efetiva_card.replace('.','').replace(',','.').replace('%','.'))/float(card_meta_tx.replace('%','.').replace('.','').replace(',','.')) -1, 4)
        gap_card_meta_tx = '{:.2%}'.format(gap_card_meta_tx)
    
    primeiro_digito_gap2 = gap_card_meta_tx[:1]


    ### CARD_META_DO_DIA_ANTERIOR ###

    card_meta_danterior = df_final[df_final['data'] == last_1days]

    if name_loja == None:
        card_meta_danterior = card_meta_danterior['meta_dia'].sum()

    elif name_loja != "":
        card_meta_danterior = card_meta_danterior[card_meta_danterior['restaurante'] == name_loja]
        card_meta_danterior = card_meta_danterior['meta_dia'].sum()

    else:
        card_meta_danterior = card_meta_danterior['meta_dia'].sum()
    
    card_meta_danterior = round(card_meta_danterior,2)

    card_meta_danterior = '{0:,}'.format(card_meta_danterior)
    card_meta_danterior = card_meta_danterior.replace(',','.')

    fim = card_meta_danterior[-3:].replace('.',',')
    inicio = card_meta_danterior[:len(card_meta_danterior)-3]

    card_meta_danterior = inicio + fim

    ### CARD_META_DO_DIA_ATUAL ###

    card_meta_datual = df_final[df_final['data'] == current_day]

    if name_loja == None:
        card_meta_datual = card_meta_datual['meta_dia'].sum()

    elif name_loja != "":
        card_meta_datual = card_meta_datual[card_meta_datual['restaurante'] == name_loja]
        card_meta_datual = card_meta_datual['meta_dia'].sum()

    else:
        card_meta_datual = card_meta_datual['meta_dia'].sum()
    
    card_meta_datual = round(card_meta_datual,2)

    card_meta_datual = '{0:,}'.format(card_meta_datual)
    card_meta_datual = card_meta_datual.replace(',','.')

    fim = card_meta_datual[-3:].replace('.',',')
    inicio = card_meta_datual[:len(card_meta_datual)-3]

    card_meta_datual = inicio + fim

    ### CARD_FATURAMENTO_DIA_ANTERIOR ###

    card_fat_danterior = df_final[df_final['data'] == last_1days]
    card_fat_danterior = card_fat_danterior.drop_duplicates(subset="data")

    if name_loja == None:
        card_fat_danterior = card_fat_danterior['faturamento_bruto'].sum()

    elif name_loja != "":
        card_fat_danterior = card_fat_danterior[card_fat_danterior['restaurante'] == name_loja]
        card_fat_danterior = card_fat_danterior['faturamento_bruto'].sum()

    else:
        card_fat_danterior = card_fat_danterior['faturamento_bruto'].sum()
    
    card_fat_danterior = round(card_fat_danterior,2)

    card_fat_danterior = '{0:,}'.format(card_fat_danterior)
    card_fat_danterior = card_fat_danterior.replace(',','.')

    fim = card_fat_danterior[-3:].replace('.',',')
    inicio = card_fat_danterior[:len(card_fat_danterior)-3]

    card_fat_danterior = inicio + fim



    ###gap_meta_fat_dia###

    if card_fat_danterior=="0,0":
        gap_meta_fat_dia_anterior = '0'
    else:
        gap_meta_fat_dia_anterior = round(float(card_fat_danterior.replace('.','').replace(',','.'))/float(card_meta_danterior.replace('.','').replace(',','.')) -1, 4)
        gap_meta_fat_dia_anterior = '{:.2%}'.format(gap_meta_fat_dia_anterior)
    
    ###primeiro_digito###

    primeiro_digito_gap = gap_meta_fat_dia_anterior[:1]
    digito = '-'

    ###meta faturamento bruto mensal###

    meta_fat_bruto = df_final['meta_dia'].sum()
    meta_fat_bruto = round(meta_fat_bruto,2)

    meta_fat_bruto = '{0:,}'.format(meta_fat_bruto)
    meta_fat_bruto = meta_fat_bruto.replace(',','.')

    fim = meta_fat_bruto[-3:].replace('.',',')
    inicio = meta_fat_bruto[:len(meta_fat_bruto)-3]

    meta_fat_bruto = inicio + fim

    ###gap_meta_fat_mes###

    if faturamento_card=="0,0":
        gap_meta_fat_mes = '0'
    else:
        try:
            gap_meta_fat_mes = round(float(faturamento_card.replace('.','').replace(',','.'))/float(meta_fat_bruto.replace('.','').replace(',','.')) -1, 4)
            gap_meta_fat_mes = '{:.2%}'.format(gap_meta_fat_mes)
        except:
            gap_meta_fat_mes = str(0)
    
    ###primeiro_digito###

    primeiro_digito_gap1 = gap_meta_fat_mes[:1]

    ## DICIONÁRIO COM VALORES ##

    if name_loja == None:
        name_loja = "Todas as lojas"

    try:
        if start_date == '':
            start_date = "Todas as data"
    except:
        start_date = ""
        end_date = ""


    context={

        ##card_meta_tx##

        'card_meta_tx':card_meta_tx,

        ##gap_card_meta_tx##

        'gap_card_meta_tx':gap_card_meta_tx,

        ##primeiro_digito2##

        'primeiro_digito_gap2':primeiro_digito_gap2,

        ###tx_efetiva_card###

        'tx_efetiva_card':tx_efetiva_card,
        
        ###meta_fat_bruto##

        'gap_meta_fat_mes': gap_meta_fat_mes,
        'meta_fat_bruto':meta_fat_bruto,

        ##primeiro_digito##

        'primeiro_digito_gap1':primeiro_digito_gap1,

        ##primeiro_digito##

        'primeiro_digito_gap':primeiro_digito_gap,
        'digito':digito,

        ##card_gap_meta_fat_dia##

        'gap_meta_fat_dia_anterior':gap_meta_fat_dia_anterior,

        ###CARD_FAT_DIA_ANTERIOR###

        'card_fat_danterior':card_fat_danterior,

        ###CARD_META_DIA_ANTERIOR###

        'card_meta_danterior':card_meta_danterior,

        ###CARD_META_DIA_ATUAL###

        'card_meta_datual':card_meta_datual,

        ##LOJA E DATAS ATUAL##
        
        'data_inicial':start_date,
        'data_final':end_date,
        'restaurante_atual':name_loja,

        ###INCENTIVOS_CARD###

        'incentivo_loja':incentivo_loja,
        'incentivo_ifood':incentivo_ifood,
        'incentivo_geral':incentivo_geral,

        ###CANCELAMENTOS_CARD###

        'canc_restaurante':canc_restaurante,
        'canc_cliente':canc_cliente,
        'cancelamento_total': cancelamento_total,

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

def logout_user(request):
    logout(request)
    return redirect('/login')