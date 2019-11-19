function validar(){
	
	var usuario = document.getElementById('usuario').value;
	var idade = document.getElementById('age').value;
	var sexo = document.getElementById('sex').value;
	var email = document.getElementById('mail').value;
	var senha = document.getElementById('pass1').value;
	var conf = document.getElementById('pass2').value;
	
	if (usuario == "") {
		alert("!Por favor, Preenchar o campo usuário!");
		document.form.usuario.focus();
		return false;
	}

	if (idade == "") {
		alert("!Por favor informe sua idade!");
		document.form.age.focus();
		return false;
		}
	
	if (sexo == "") {
		alert("!Por favor informe seu sexo!");
		document.form.sex.focus();
		return false;
	}

	if (email == "" || document.form.mail.value.indexOf('@') == -1 || document.form.mail.value.indexOf('.') == -1) {
		alert(" !Preenchar o campo E-mail com um e-mail válido, ele deve conter um '@' e um '.'! ");
		document.form.mail.focus();
		return false;
	}

	if (senha == "") {
		alert("!Por favor insira uma senha!");
		document.form.pass1.focus();
		return false;
	}

	if (conf != senha) {
		alert("!Por favor verifique as senhas, elas devem ser condizentes!");
		document.form.pass2.focus();
		return false;
	}


	alert(usuario+" "+nome+" "+sexo+" "+email);
 	
}