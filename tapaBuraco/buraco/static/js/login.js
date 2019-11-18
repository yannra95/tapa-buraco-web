$(function(){
	$('.btn').click(function(){
		var username = $("#inputEmail").val();
		var password = $("#inputPassword").val();
/*
		if (username==" " && password==" "){ 
			console.log("autenticado");
			window.location.href = "dashboard.html";
		}else{
			console.log("errado");
			$(".alert").show(800);
		}
*/

		//window.location.href = "dashboard.html";
		return false;
	});

});




/*
function Login(){
	var done=0;
	var username = document.getElementById('inputEmail');
	console.log(username);


	var password=document.login.password.value;
	
	username=username.toLowerCase();
	password=password.toLowerCase();
	
	

	if (done==0){ 
		alert("Senha ou Usuário inválido.");
	}

}
*/