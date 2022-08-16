/*
$(document).ready( function() {   // Esta parte del código se ejecutará automáticamente cuando la página esté lista.
    $("#botonenviar").click( function() { 
   // function getData() {
    if(validaForm()){   
        $.post( "/postmethod", 
        $("#form_login").serialize(), 
        function(err, req, res){
            if(res == 1){
                window.location.href = "/administracion/"+res["responseJSON"]["id_usuario"]; //Cambiamos a una ruta de respuesta con el nombre del archivo
                console.log(res);    // Si hemos tenido éxito, hacemos aparecer el div "exito" con un efecto fadeIn lento tras un delay de 0,5 segundos.
            } else {
                window.location.href = "/";   // Si no, lo mismo, pero haremos aparecer el div "fracaso"
            }
        
        });
    }
  //  }
    //validar formulario
    function validaForm(){
        // Campos de texto
        if($("#user").val() == ""){
            alert("El campo usuario no puede estar vacío.");
            $("#user").focus();       // Esta función coloca el foco de escritura del usuario en el campo Nombre directamente.
            return false;
        }
        if($("#passwd").val() == ""){
            alert("El campo contraseña no puede estar vacío.");
            $("#passwd").focus();
            return false;
        }
        return true; // Si todo está correcto
    }

/*
    //Asignacion de funciones para validar
    $( "#botonenviar" ).click(function(){
    getData();
    });
  });
});
*/