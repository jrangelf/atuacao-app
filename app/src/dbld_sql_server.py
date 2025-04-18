from decimal import Decimal
from datetime import datetime, date
from src.dbld_sql_queries import * 
from src.dbld_constantes import *  
from src.dbld_conexao import *  


class SQLData():

    num_instancias = 0

    def __init__(self):
        SQLData.num_instancias += 1
	
    def get_num_instancias(cls):
        return cls.num_instancias
    
    def formatar_valor(valor):
        valor_formatado = ''.join(caractere for caractere in valor if caractere.isdigit() or caractere == ',')
        valor_formatado = valor_formatado.replace(',', '.')
        return valor_formatado

    def conexao():	    
        conn = conecta_db_sqlserver(SQL_SERVER,SQL_DB,SQL_USER,SQL_PASSWORD) 
        return conn    
    
    def selecionaTabela(self, sufixo: str):
        self.sufixo = sufixo
        str_query = 'query_select_t' + self.sufixo
        con = SQLData.conexao()
        cursor = con.cursor()
        cursor.execute(eval(str_query))
        rows = cursor.fetchall()
        con.close()
        return rows
    
        
    def selecionaColunas(self, tabela: str, colunai: int, colunad: int):
        
        """ Este método busca os valores das colunas que contêm os códigos (colunai) 
        e as descrições (colunad) de cada tabela do banco SQLServer Atuação para serem 
        utilizados como opções nos campos de seleção. Recebe como parametro de entrada
        o número referente a tabela do SQL que se quer obter os valores, bem como as 
        colunas do código e da descricao, retona um dicionário: {'índice': 'descrição}"""
    
        self.tabela = tabela
        self.colunai = colunai
        self.colunad = colunad
        
        _indice = 0
        _valores={}

        rows = self.selecionaTabela(self.tabela)
    
        """ a tabela dos responsáveis possui dois campos como chave primária, por isso
        o índice do dicionário foi alterado por um contador, além disso, somente o
        código (100) deve ser selcionado para não alterar a tabela do SQL Server, 
        foi necessário retirar TJ e JT"""
    
        for row in rows:
            if self.tabela=="14":
                if row[0]==100:
                    _indice += 1
                    _valores[_indice]=row[self.colunad]            
            elif self.tabela=="03":
                if row[1]!="TJ" and row[1]!="JT":
                    _valores[row[self.colunai]]=row[self.colunad]            
            else:    		
                _valores[row[self.colunai]]=row[self.colunad]    
        return _valores
        
    
    def selecionaRegistro(self, valor,tipo):
        """ ID(0)
            NUM_PROCESSO(1)            
            NOME EXEQUENTE(2
            QUANTIDADE EXEQUENTES(3)
            COD INSTANCIA(4)
            COD ORGAO REPRESENTADO(5)
            COD UNIDADE(6)
            COD SITUACAO UNIAO(7)
            COD TIPO CALCULO(8)
            COD OBJETO ACAO(9)
            COD TIPO PARECER(10)
            NUM PARECER(11)
            VR AUTOR(12)
            VR UNIAO(13)
            DT ENVIO NECAP(14)
            DT PRAZO ADVOGADO(15)
            DT RECEBIMENTO TECNICO(16)
            DT SAIDA NECAP(17)
            OBSERVACAO(18)
            NOME RESPONSAVEL(19)
            SN PERICIA(20)
            DT DIGITACAO(21)
            NUM ACAO ORIGINARIA(22)
            COD DESC NECAP(23)"""
                
        self.valor = str(valor)
        self.tipo = tipo
        query = eval('query_select_registro_sql_' + self.tipo)
        str_query = query.replace('@', self.valor)
                
        con = SQLData.conexao()
        cursor = con.cursor()
        cursor.execute(str_query)        
        rows = cursor.fetchall()        
        con.close()

        if len(rows) ==1:
            return rows[0] 
        else:
            return rows
             
    
    def updateRegistro(self, dicionario):
        
        id_processo = dicionario['idproc']
        num_processo = dicionario['numprocesso']
        exequente = dicionario['exequente']
        qtde_exec = dicionario['qtexeq']
        valoruniao = dicionario['valoruniao']
        valorautor = dicionario['valorautor']
        observacao = dicionario['observacao']
        vlr_autor = SQLData.formatar_valor(valorautor)
        vlr_uniao = SQLData.formatar_valor(valoruniao)

        str_query = query_update_t01
        str_query = query_update_t01.replace('$1', id_processo)
        str_query = str_query.replace('$2', num_processo)
        str_query = str_query.replace('$3', exequente)
        str_query = str_query.replace('$4', qtde_exec)
        str_query = str_query.replace('$6', vlr_uniao)
        str_query = str_query.replace('$5', vlr_autor)
        str_query = str_query.replace('$7', observacao)

        con = SQLData.conexao()
        cursor = con.cursor()
        cursor.execute(str_query)        
        con.commit()
        con.close()

        return 0
    
    def deletaRegistro(self, idRegistro):        
        str_query = query_delete_t01.replace('$1', idRegistro)        
        con = SQLData.conexao()
        cursor = con.cursor()
        cursor.execute(str_query)        
        con.commit()
        con.close()
        return 0
    
    
    
    def gravarRegistro(self, record_to_insert: list):
        """ Recebe a lista com os campos formatados e grava o registro no banco 
            SQLServer retornando o id do registro gravado.
            Obs: caso o registro possua o mesmo número do processo, valor do autor e
            valor da união de um registro já gravado no banco, esse registro não
            será gravado no banco """       
        
        
        self.record = record_to_insert
                
        def converter_valor(valor_str):
            try:
                # Remove R$, pontos e substitui vírgula por ponto
                valor_limpo = valor_str.replace('R$', '').replace('.', '').replace(',', '.').strip()
                return valor_limpo                
            except:
                return '0.0' # Valor padrão em caso de erro
        
        str_valor_autor = self.record[13]
        str_valor_uniao = self.record[14]
        self.record[13] = converter_valor(str_valor_autor)
        self.record[14] = converter_valor(str_valor_uniao)
        
        _records = tuple(self.record)

        con = SQLData.conexao()
        cursor = con.cursor()
        
        # verificar se já existe registro com mesmo num_processo, valor_autor, valor_uniao
        cursor.execute(query_verificacao, (self.record[2], self.record[14], self.record[13]))
        count = cursor.fetchone()[0]
        
        if count > 0:
            cursor.execute(query_segunda_verificacao, (self.record[2], self.record[14], self.record[13]))
            id_processo = cursor.fetchall()[0][0]
            registro_duplicado = True            
            con.close()
        else:
            registro_duplicado=False
            cursor.execute(query_insert_registro_sqlserver, _records)
            con.commit()
            str_query = query_registro_inserido_sql_id.replace('$1',str(self.record[2]))
            str_query = str_query.replace('$2',str(self.record[3]))
            str_query = str_query.replace('$3',str(self.record[18]))
            str_query = str_query.replace('$4',str(self.record[20]))        
            cursor.execute(str_query)	
            row_sqlid = cursor.fetchone()
            id_processo = row_sqlid[0]
            con.close()

        return id_processo, registro_duplicado

    
    def formatarListaRegistros(self, registros: list,
                               instancia: dict,
                               origemprocesso: dict,
                               tipocalculo: dict,
                               objetoacao: dict,
                               unidade: dict,
                               valores: dict):
        
        """ este método formata os campos para persistir na tabela principal
            do banco atuação no SQLServerver. A lista registros possui 17 
            campos do POST, mas a tabela T01_PROCESSO possui 21 parâmetros.
            Retorna uma lista com os valores formatados para serem gravados
            na tabela T01_PROCESSO. 
            
            registros = [
                        'csrfmiddlewaretoken', 
                        'Situação da União', 
                        'N. do processo', 
                        'Nome do autor', 
                        'Instância', 
                        'Origem do processo', 
                        'Quant. exequentes', 
                        'Tipo de cálculo', 
                        'Objeto da ação', 
                        'Unidade', 
                        'N. do parecer', 
                        'Valor da União', 
                        'Valor do Autor', 
                        'Data de envio para unidade', 
                        'Data de saída', 
                        'Nome responsavel', 
                        'Observação']            
            """
        
        self.regs = registros
        self.instancia = instancia
        self.origemprocesso = origemprocesso
        self.tipocalculo = tipocalculo
        self.objetoacao = objetoacao
        self.unidade = unidade
        self.valores = valores

        # retirar o 'token'
        self.regs.remove(self.regs[0])		
        self.regs[0]= '2' if self.regs[0] == 'Autora' else '1'		
		
		# fixar em N - Cálculo
        self.regs.insert(1,'N')
        
        qtde_exequentes = self.regs[4]

        cod_instancia = getKeyByValue(self.instancia, self.valores['instancia'])        
        self.regs[4]=int(cod_instancia)		
        
        cod_origem_processo = getKeyByValue(self.origemprocesso, self.valores['origemprocesso'])        
        self.regs[5]=int(cod_origem_processo)
        
        self.regs[6]=qtde_exequentes
        
        cod_tipo_calculo = getKeyByValue(self.tipocalculo, self.valores['tipocalculo'])
        self.regs[7]=int(cod_tipo_calculo)		
        
        cod_objeto_acao = getKeyByValue(self.objetoacao, self.valores['objeto'])
        self.regs[8]=int(cod_objeto_acao)		
		
		# fixar em 1 - Advocacia-Geral da União
        self.regs.insert(9,1)		
		
        cod_unidade = getKeyByValue(self.unidade, self.valores['unidade'])
        self.regs[10] = int(cod_unidade)
		
		# com a desterritorialização somente há um tipo de parecer (conclusivo)
        self.regs.insert(11,1)

        # inserir número parecer fixo '100'
        self.regs.insert(12,'100')

		# inserir nulo para o prazo do advogado
        self.regs.insert(16,None)

        data_atual = datetime.now()
        data_formatada =  data_atual.strftime("%Y-%m-%d %H:%M:%S")
        self.regs.append(data_formatada)
        
        return self.regs
 

def getKeyByValue(dicionario: dict, valor: str):
    """passa o valor de um item de um dicionário e se existir sua chave é retornada"""
    _lista = [k for k,v in dicionario.items() if v == valor]
    return str(_lista[0])


def buscar_dados_entrada():
    """seleciona o código e a descrição das tabelas do SQLServer"""
    instancia={}
    origemprocesso={}
    tipocalculo={}
    objetoacao={}
    unidade={}

    sql_data = SQLData()
    
    instancia = sql_data.selecionaColunas('03',0,1)
    origemprocesso = sql_data.selecionaColunas('04',0,4)        
    tipocalculo = sql_data.selecionaColunas('02',0,1)
    objetoacao = sql_data.selecionaColunas('07',0,1)
    unidade = sql_data.selecionaColunas('09',0,1)
    responsavel = sql_data.selecionaColunas('14',0,1)
       
    del objetoacao[83]

    return {'instancia':instancia,
            'origemprocesso':origemprocesso,
            'tipocalculo':tipocalculo,
            'objetoacao':objetoacao,
            'unidade':unidade,
            'responsavel':responsavel}



def ajusta_registro(registros):   
    
    def substituir(lista, registro):
        lista[0] = registro[0]
        try:
            numero = registro[1]
            numero_formatado = f"{numero[:7]}-{numero[7:9]}.{numero[9:13]}.{numero[13:14]}.{numero[14:16]}.{numero[16:]}"
            lista[1] = numero_formatado
        except:
            lista[1] = registro[1]

        #lista[1] = registro[1]
        lista[2] = registro[2]
        lista[3] = registro[3]
        lista[14] = registro[14]
        lista[17]= registro[17]
        lista[18] = registro[18]
        lista[19] = registro[19]
        lista[21] = registro[21]
        lista[7] = "Ré" if int(registro[7]) == 1 else "Autora" # situação da união
        try:
            lista[4] = dados['instancia'][Decimal(registro[4])]   # instancia    
        except KeyError:
            lista[4] = "Não informada"
        try:
            lista[8] = dados['tipocalculo'][Decimal(registro[8])] # tipo de cálculo
        except KeyError:
            lista[8] = "Não informado"        
        try:
            lista[9] = dados['objetoacao'][Decimal(registro[9])] # objeto da ação        
        except KeyError:
            lista[9] = "Não informado"

        if registro[23] is not None:
            try:
                lista[23] = dados['unidade'][Decimal(registro[23])] # unidade
            except KeyError:
                lista[23] = 'Não informada'
        else:
            lista[23] = "Não informada"

        try:
            vr_uniao = "{:,.2f}".format(float(registro[13])).replace(",", "X").replace(".", ",").replace("X", ".")
            lista[13] = vr_uniao
        except Exception as e:
            lista[13] = 0
        try:
            vr_autor = "{:,.2f}".format(float(registro[12])).replace(",", "X").replace(".", ",").replace("X", ".")
            lista[12] = vr_autor
        except Exception as e:
            lista[12] = 0

        return lista
    
    dados = buscar_dados_entrada()    
    lista_regs = []

    if isinstance(registros,tuple):
        tp_registro =[0] * 24
        tp_lista = substituir(tp_registro,registros)
        lista_regs.append(tp_lista)
    else:        
        for registro in registros:
            lista_reg = [0] * 24
            lista = substituir(lista_reg, registro)
            lista_regs.append(lista)
    
    return {'registros': lista_regs}
    