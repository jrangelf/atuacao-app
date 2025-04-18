function upperCase() {
  const x = document.getElementById("nomexeq");
  x.value = x.value.toUpperCase();
}


function inabValorAutor(situacao)
{	//alert("Situação da União " + situacao);

	if(situacao == "Autora")// valor do campo situação da união
        {
          //campos a serem habilitados
          document.getElementById("campo9").value = "";
          document.getElementById("campo9").readOnly=true;
        } else {
          document.getElementById("campo9").readOnly=false;	
        }
}


function inabcampo1()
{
  	//alert("selecionou campo2!");
  	document.getElementById("campo1").value = "";
}


function inabcampo2()
{
	//alert("selecionou campo1!");
	//alert(document.getElementById("campo2").value)		
	document.getElementById("campo2").value = "";
}


function valida1()
{
  const dataAtual = new Date();
  dt1=document.getElementById("dtenvio").value;	  
  const data1 = new Date(dt1);
	if (data1 > dataAtual) 
  {
    alert("A data de envio não pode ser maior que a data de hoje.");
    document.getElementById("dtenvio").value = "";
    document.getElementById("dtsaida").focus();

  }  
}


function valida2()
{		
  dt1=document.getElementById("dtenvio").value;
	dt2=document.getElementById("dtsaida").value;
  const dataAtual = new Date();
	if (dt1 > dt2)
	{
		alert("A data de saída não pode ser menor que a data de envio.");
	    document.getElementById("dtsaida").value = "";
	    document.getElementById("dtenvio").focus();
	}  
  const data2 = new Date(dt2);
  if (data2 > dataAtual) 
  {
    alert("A data de saída não pode ser maior que a data de hoje.");
    document.getElementById("dtsaida").value = "";
    document.getElementById("dtenvio").focus();
  }
}	 

function validaDatas() 
{
  
  const dataAtual = new Date();

  const dtenvio = document.getElementById("dtenvio").value;
  const dtsaida = document.getElementById("dtsaida").value;

  if (dtenvio > dataAtual) {
    alert("A data de saída não pode ser maior que a data de hoje.");
    document.getElementById("dtsaida").value = "";
    document.getElementById("dtenvio").focus();

  } else if (dtenvio > dtsaida) {
    alert("A data de saída não pode ser menor que a data de envio.");
    document.getElementById("dtsaida").value = "";
    document.getElementById("dtenvio").focus();

  } else if (dtsaida > dataAtual) {
    alert("A data de envio não pode ser maior que a data de hoje.");
    document.getElementById("dtenvio").value = "";
    document.getElementById("dtsaida").focus();
  }
}


function noback()
{
	javascript:window.history.forward(1);	
}					




function doDecimal(pStr, campo) {
    
    let valorAutor = 0;
    let valorUniao = 0;      
     
    valorUniao = parseFloat(document.getElementById("campo8").value.replace(/[^\d,]/g, '').replace(",", "."));
    valorAutor = parseFloat(document.getElementById("campo9").value.replace(/[^\d,]/g, '').replace(",", "."));
    
    var situacaoElement = document.getElementById("situacao");
    var situacao = situacaoElement ? situacaoElement.textContent : undefined;    
    
    var selecao1Element = document.getElementById("selecao1");
    var selecao = selecao1Element ? selecao1Element.value : undefined;

    if (situacao === undefined && selecao !== undefined) {
      situacao = selecao; 
    }
    
    if (campo === "valoruniao" && !isNaN(valorUniao) && !isNaN(valorAutor)) {
                        
            if ((valorUniao > valorAutor) && (situacao ==="Ré")) {
                alert("O valor da União não pode ser superior ao valor do Autor");
                //document.getElementById("campo8").value = document.getElementById("campo9").value;
                document.getElementById("campo8").value = ""; 
            } 
    }    
    
    if (campo === "valorautor" && !isNaN(valorUniao) && !isNaN(valorAutor) && valorAutor !== "") {
                        
            if (valorUniao > valorAutor) {
                alert("O valor da União não pode ser superior ao valor do Autor");
                //document.getElementById("campo8").value = document.getElementById("campo9").value;
                document.getElementById("campo9").value = "";
            } 
    }   
}
    


function validaQtdExeq(str_valor){
	let valor = parseInt(str_valor);					
	//alert ("quantidade de exequentes: "); // + numero);
	if (valor == 0) {
		alert("O número de exequentes não pode ser zero!");
		document.getElementById("cmp1").value = "";	
	}
	if (valor < 0) {
		alert("O número de exequentes deve ser um valor positivo");
		document.getElementById("cmp1").value = "";	
	}								    
}


function formatarNumero(input) {
 
    //console.log("formatarNumero");

    // Remover todos os caracteres que não são dígitos ou vírgula
    let value = input.value.replace(/[^\d,]/g, '');
               
    // Formatar o número com separadores de milhar
    //let valorFormatado = 'R$ ' + value.replace(/\B(?=(\d{3})+(?!\d))/g, '.');
    let valorFormatado = value.replace(/\B(?=(\d{3})+(?!\d))/g, '.');
    
    // Definir o valor formatado no campo de input
    //if (valorFormatado === "") {
    //  valorFormatado = 0;
    //}
     
    input.value = valorFormatado;
    
    
}


function substituirConteudo(tdId) {
  //console.log("substituirConteudo");
  // Obtém uma referência ao elemento <td> com base no ID passado como parâmetro
  var tdElement = document.getElementById(tdId);
  var tdElementButton = document.getElementById(tdId + "_bt");

  // Obtém o conteúdo atual do <td>
  var nome = tdElement.textContent || tdElement.innerText;

  // Cria um novo elemento input
  var inputElement = document.createElement("input");

  // Define o tipo do input como "text"
  inputElement.type = "text";

  // Define o valor padrão como o conteúdo atual do <td>
  inputElement.value = nome;

  // Remove o conteúdo atual do <td>
  tdElement.innerHTML = "";

  // Adiciona o input criado ao <td>
  tdElement.appendChild(inputElement);

  // Oculta o botão
  //tdElementButton.style.display = "none";
  
  // Remove o botão
  tdElementButton.parentNode.removeChild(tdElementButton);
        
}


function habilitarCampo(tdId) {
  var inputElement = document.getElementById(tdId);           
  inputElement.removeAttribute("readonly");
 
}

function formatarNumeroProcesso(input) {
  var valorOriginal = input.value;
  var valorNumerico = valorOriginal.replace(/\D/g, ''); // Remove todos os caracteres não numéricos

  // Limita a 20 dígitos
  if (valorNumerico.length > 20) {
    valorNumerico = valorNumerico.substring(0, 20);
  }

  input.value = valorNumerico;
}

function confirmarExclusao() {
  console.log("confirmarExclusao");
  var confirmacao = confirm("Confirma que quer apagar o registro?");
  if (confirmacao) {
      var cabecalho = document.getElementById("cabecalho");
      var botao = document.getElementById("botao");
      
      cabecalho.innerHTML = "REGISTRO APAGADO";
      botao.innerHTML = "";
  } else {
      //alert("A ação foi cancelada.");
      return false; // Isso impede que o formulário seja enviado
  }
}


function desabilitaGravar(event) {
  event.preventDefault(); // Impede o envio padrão do formulário
  console.log("funcao desabilita com validação");

  const form = document.forms[0];

  // Valida o formulário antes de enviar
  if (form.checkValidity()) {
    document.getElementById("gravar").disabled = true;
    form.submit(); // Envia o formulário somente se válido
  } else {
    form.reportValidity(); // Exibe mensagens de erro para os campos inválidos
  }
}




