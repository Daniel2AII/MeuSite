function validar(){
	
	var usuarioD = document.getElementById('usuario').value;
	var nomeD = document.getElementById('nome').value;
	var idadeD = document.getElementById('age').value;
	var sexoD = document.getElementById('sex').value;
	var emailD = document.getElementById('mail').value;
	var senhaD = document.getElementById('pass1').value;
	var confD = document.getElementById('pass2').value;
	var identD = document.getElementById("ident").value;
	
	if (usuarioD == "") {
		alert("!Por favor, Preenchar o campo usuário!");
		document.form.sex.focus();
		return false;
		
	}

	if (nomeD == "") {
		alert("!Por favor Preenchar o campo nome!");
		document.form.usuario.focus();
		return false;
		
	}

	if (idadeD == "") {
		alert("!Por favor informe sua idade!");
		document.form.age.focus();
		return false;
		}
	
	if (sexoD == "") {
		alert("!Por favor informe seu sexo!");
		document.form.sex.focus();
		return false;
	}

	if (emailD == "" || document.form.mail.value.indexOf('@') == -1 || document.form.mail.value.indexOf('.') == -1) {
		alert(" !Preenchar o campo E-mail com um e-mail válido, ele deve conter um '@' e um '.'! ");
		document.form.mail.focus();
		return false;
	}

	if (senhaD == "") {
		alert("!Por favor insira uma senha!");
		document.form.pass1.focus();
		return false;
	}

	if (confD != senhaD) {
		alert("!Por favor verifique as senhas, elas devem ser condizentes!");
		document.form.pass2.focus();
		return false;
	}

	if (identD == "") {
		alert("!Por favor, Preenchar o campo de ID/Matricula, é de extrema importância!");
		document.form.ident.focus();
		return false;
	}



	alert(usuarioD+" "+nomeD+" "+idadeD+" "+sexoD+" "+emailD+" "+identD);
 	
}