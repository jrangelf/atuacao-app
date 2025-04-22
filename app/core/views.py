from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from src.dbld_constantes import INSTANCIAS_UTILIZADAS
from src.dbld_sql_server import *

def home(request):
        return render(request,'home.html',{})

def entradadados(request):
        
        contexto = {}
        instancia={}
        origemprocesso={}
        tipocalculo={}
        objetoacao={}
        unidade={}

        sql_data = SQLData()        

        # seleciona o código e a descrição das tabelas do SQLServer
        instancia = sql_data.selecionaColunas('03',0,1)
        instancia = {chave: valor for chave, valor in instancia.items() if valor in INSTANCIAS_UTILIZADAS}
        
        origemprocesso = sql_data.selecionaColunas('04',0,4)        
        tipocalculo = sql_data.selecionaColunas('02',0,1)
        objetoacao = sql_data.selecionaColunas('07',0,1)
        unidade = sql_data.selecionaColunas('09',0,1)
        responsavel = sql_data.selecionaColunas('14',0,1)
        
        del objetoacao[83]

        if request.method == "POST":              

                lista_registros = []
                valores = dict(request.POST.items())
                
                for valor in valores.values():
                        lista_registros.append(valor)

                lista_regs_formatada = sql_data.formatarListaRegistros(
                                                                lista_registros,
                                                                instancia,
                                                                origemprocesso,
                                                                tipocalculo,
                                                                objetoacao,
                                                                unidade,
                                                                valores)

                
                sql_id, duplicado = sql_data.gravarRegistro(lista_regs_formatada)
                registro = sql_data.selecionaRegistro(sql_id, "id")
                
                if registro:
                        _situacaouniao = "Ré" if int(registro[7]) == 1 else "Autora"
                        _instancia = instancia[Decimal(registro[4])]
                        #_origemprocesso = origemprocesso[Decimal(registro[6])]
                        _origemprocesso = ''
                        _tipocalculo = tipocalculo[Decimal(registro[8])]
                        _objetoacao = objetoacao[Decimal(registro[9])]
                        _unidade = unidade[Decimal(registro[23])]

                        vr_uniao = "{:,.2f}".format(float(registro[13])).replace(",", "X").replace(".", ",").replace("X", ".")
                        vr_autor = "{:,.2f}".format(float(registro[12])).replace(",", "X").replace(".", ",").replace("X", ".")
                        
                        botao_voltar = False
                        if duplicado == False:
                                msg = 'Registro inserido com sucesso!'
                                messages.success (request, (msg))
                        else:
                                msg = 'REGISTRO DUPLICADO! Foi identificado que o registro possui o mesmo número de processo, bem como os mesmos valores do Autor e da União.'
                                messages.warning (request, (msg))
                                botao_voltar = True
                        
                        

                        return render(request,'entradadados.html',{'inseridos':'inseridos',
                                                            'registro':registro,
                                                            'instancia':_instancia,
                                                            'origem':_origemprocesso,
                                                            'situacaouniao':_situacaouniao,
                                                            'tipocalculo':_tipocalculo,
                                                            'objetoacao':_objetoacao,
                                                            'necap':_unidade,
                                                            'vr_autor':vr_autor,
                                                            'vr_uniao':vr_uniao,
                                                            'botao': botao_voltar
                                                            })
                else:
                        msg = 'Não foi possível gravar o registro no banco Atuação!'
                        messages.warning (request, (msg))
                        
                                                                                                     
        else:
                contexto['instancia']=instancia
                contexto['origemprocesso'] = '' 
                contexto['tipocalculo']=tipocalculo
                contexto['objetoacao']=objetoacao
                contexto['unidade']=unidade
                contexto['responsavel']=responsavel
                
                return render(request, 'entradadados.html', context=contexto)


def consulta(request):        

        if request.method == "POST":

                sql_data = SQLData()

                itens = request.POST.items()
                dict_itens = {}
                for key, value in itens:
                        dict_itens[key]=value               
                
                try:
                        if len(dict_itens['exequente']) > 0:
                                idproc = dict_itens['idproc'].strip()
                                update = sql_data.updateRegistro(dict_itens)                                
                                registros = sql_data.selecionaRegistro(idproc, "id")
                
                                if registros is not None and len(registros) != 0:                        
                                        reg_ajustados = ajusta_registro(registros)
                                        lista_de_registros = reg_ajustados['registros']
                                        msg = "Registro alterado com sucesso"
                                        messages.success (request, (msg)) 
                                        return render(request,'consulta.html',{'lista':lista_de_registros})
                                
                except:                                       
                        numproc = request.POST.get('numproc').strip()
                        idproc = request.POST.get('idproc').strip()

                        if not (numproc or idproc):
                                return render(request, 'consulta.html',{})               
                
                        if numproc:
                                tipo = "numproc"
                                valor = numproc
                        else:
                                tipo = "id"
                                valor = idproc

                        registros = sql_data.selecionaRegistro(valor, tipo)
                
                        if registros is not None and len(registros) != 0:                        
                                reg_ajustados = ajusta_registro(registros)
                                lista_de_registros = reg_ajustados['registros']
                                return render(request,'consulta.html',{'lista':lista_de_registros})
                        else:                        
                                msg = "Registro não encontrado"
                                messages.success (request, (msg))
                                return render(request, 'consulta.html',{})               
                                                

        else:
                return render(request,'consulta.html',{})
                
                
                
def altera(request):

        if request.method == "POST":
                sql_data = SQLData()
                idproc = request.POST.get('idproc').strip()
                if not (idproc):                        
                        return render(request, 'altera.html',{})               
                else:
                        valor=idproc

                registros = sql_data.selecionaRegistro(valor, "id")
                
                if registros is not None and len(registros) != 0:                        
                        reg_ajustados = ajusta_registro(registros)
                        lista_de_registros = reg_ajustados['registros']
                        numero_processo = lista_de_registros[0][1]
                        desformatado = numero_processo.replace("-", "").replace(".", "")
                        lista_de_registros[0][1] = desformatado
                        if lista_de_registros[0][18] == None:
                                lista_de_registros[0][18]=''
                        return render(request,'altera.html',{'lista':lista_de_registros})
                else:                        
                        msg = "Registro não encontrado"
                        messages.success (request, (msg))
                        return render(request, 'altera.html',{})
        
        else:
                return render(request,'altera.html',{})
        


def exclusao(request):    

        if request.method == "POST":

                sql_data = SQLData()
                itens = request.POST.items()
                dict_itens = {}
                for key, value in itens:
                        dict_itens[key]=value
               
                try:
                        if len(dict_itens['num-processo']) > 0 and len(dict_itens['id-processo'])>0:

                                idproc = dict_itens['id-processo'].strip()
                                sql_data.deletaRegistro(idproc)
                                msg = f"Registro {idproc} excluído"
                                messages.success (request, (msg))

                                return render(request,'exclusao.html',{})
                                
                except: 
                        idproc = dict_itens['idproc'].strip()
                        if not (idproc):                        
                                return render(request, 'exclusao.html',{})               
                        else:
                                valor=idproc

                        registros = sql_data.selecionaRegistro(valor, "id")
                
                        if registros is not None and len(registros) != 0:                        
                                reg_ajustados = ajusta_registro(registros)
                                lista_de_registros = reg_ajustados['registros']
                                if lista_de_registros[0][18] == None:
                                        lista_de_registros[0][18]=''                        
                                return render(request,'exclusao.html',{'lista':lista_de_registros})
                        else:                        
                                msg = "Registro não encontrado"
                                messages.success (request, (msg))
                                return render(request, 'exclusao.html',{})      
        else:
                return render(request,'exclusao.html',{})
        
                
