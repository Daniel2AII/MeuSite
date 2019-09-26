function validar(){
	
	var usuariop = document.getElementById('usuario').value;
	var nomep = document.getElementById('nome').value;
	var idadep = document.getElementById('age').value;
	var sexop = document.getElementById('sex').value;
	var emailp = document.getElementById('mail').value;
	var senhap = document.getElementById('pass1').value;
	var confp = document.getElementById('pass2').value;
	
	if (usuariop == "") {
		alert("!Por favor, Preenchar o campo usuário!");
		document.form.usuario.focus();
		return false;
	}

	if (nomep == "") {
		nomep = "Anônimo"
		document.form.nome.focus();
	}

	if (idadep == "") {
		alert("!Por favor informe sua idade!");
		document.form.age.focus();
		return false;
		}
	
	if (sexop == "") {
		alert("!Por favor informe seu sexo!");
		document.form.sex.focus();
		return false;
	}

	if (emailp == "" || document.form.mail.value.indexOf('@') == -1 || document.form.mail.value.indexOf('.') == -1) {
		alert(" !Preenchar o campo E-mail com um e-mail válido, ele deve conter um '@' e um '.'! ");
		document.form.mail.focus();
		return false;
	}

	if (senhap == "") {
		alert("!Por favor insira uma senha!");
		document.form.pass1.focus();
		return false;
	}

	if (confp != senhap) {
		alert("!Por favor verifique as senhas, elas devem ser condizentes!");
		document.form.pass2.focus();
		return false;
	}


	alert(usuariop+" "+nomep+" "+idadep+" "+sexop+" "+emailp);
 	
}