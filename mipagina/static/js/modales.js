$("table tr td a").on("click",function(e){
		e.preventDefault()
		var urla=$(this).attr("href");  
		if (urla == '/ok/'){
			var r=$(this).attr("id");
			//alert(r);
			//window.load('/kardex/'+r);
			$.ajax({
				type:'GET',
				url:'/kardex/'+r,
				beforeSend:Espera,
				success:function(res){
					$('#categorias').html(res);
				}
			});
			function Espera(){
        		$("#categorias").html('<img src="{{STATIC_URL}}img/loader.gif"></img>');
     		}
		}
		else{
			cargarFormularios(urla)
				$("#ventanas").dialog({
					modal:true,
					show:"blind",
					width: 600,
					hide:"explode",
					title:"Detalles.",
					position: "center"
				});	
		}
		
	});
cargarFormularios=function(url){
				$.ajax({
						url: url,
						type: 'GET',
						data: {}
					})
					.done(function(response) {
						$("#ventanas").html(response);
					})
					.fail(function() {
						console.log("error");
					})
					.always(function() {
						console.log("complete");
					});
			}