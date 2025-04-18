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



function valida2()
{
	
	dt1=document.getElementById("dtenvio").value;
	dt2=document.getElementById("dtsaida").value;


	if (dt1 > dt2)
	{
		alert("A data de saída não pode ser menor que a data de envio.");
	    document.getElementById("dtsaida").value = "";
	    document.getElementById("dtenvio").focus();
	}

}	


function noback()
{
	javascript:window.history.forward(1);	
}					


function doDecimal(pStr, campo) {
    
  console.log("função");

    let valorAutor = 0;
    let valorUniao = 0;
    let situacao = "";      
     
    valorUniao = parseFloat(document.getElementById("campo8").value.replace(/[^\d,]/g, '').replace(",", "."));
    valorAutor = parseFloat(document.getElementById("campo9").value.replace(/[^\d,]/g, '').replace(",", "."));
    situacao = document.getElementById("situacao").value;

    if (campo === "valoruniao" && !isNaN(valorUniao) && !isNaN(valorAutor)) {
                        
            if ((valorUniao > valorAutor) && (situacao === "Ré")) {
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
 
    // Remover todos os caracteres que não são dígitos ou vírgula
    let value = input.value.replace(/[^\d,]/g, '');
               
    // Formatar o número com separadores de milhar
    //let valorFormatado = 'R$ ' + value.replace(/\B(?=(\d{3})+(?!\d))/g, '.');
    let valorFormatado = value.replace(/\B(?=(\d{3})+(?!\d))/g, '.');
    
    if ((valorFormatado === 0) || (valorFormatado ==="")) {
      valorFormatado = 0;
    }

    // Definir o valor formatado no campo de input
    input.value = valorFormatado;
    
    
}

// funçao utilizada para evitar duplo clique no botao de gravar dados
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

