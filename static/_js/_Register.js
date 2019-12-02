function validar(){
	
	var usuario = document.getElementById('username').value;
	var idade = document.getElementById('age').value;
	var genero = document.getElementById('genre').value;
	var email = document.getElementById('email').value;
	var senha = document.getElementById('password').value;
	var conf = document.getElementById('confirm_password').value;
	
	if (usuario == "") {
		alert("!Por favor, Preenchar o campo usuário!");
		document.form.usename.focus();
		return false;
	}

	if (idade != "Maior de 18" && idade != "Maior de 18" ) {
		alert("!Por favor insira o campo idade com 'Maior de 18' ou 'Menor de 18'!");
		document.form.age.focus();
		return false;
		}
	
	if (genero == "") {
		alert("!Por favor informe um gênero!");
		document.form.genre.focus();
		return false;
	}

	if (email == "" || document.form.email.value.indexOf('@') == -1 || document.form.email.value.indexOf('.') == -1) {
		alert(" !Preenchar o campo E-mail com um e-mail válido, ele deve conter um '@' e um '.'! ");
		document.form.email.focus();
		return false;
	}

	if (senha == "") {
		alert("!Por favor insira uma senha!");
		document.form.password.focus();
		return false;
	}

	if (conf != senha) {
		alert("!Por favor verifique as senhas, elas devem ser condizentes!");
		document.form.confirm_password.focus();
		return false;
	}
}