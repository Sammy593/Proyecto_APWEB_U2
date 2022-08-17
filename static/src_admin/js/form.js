$(document).ready(function() {
     $("#form").validate({
         rules: {
             //Aqui aplicamos cada regla segun la etiqueta creada en el el form HTML
             user: {
                 required: true
             },
             passwd: {
                 required: true
             }
         },
         messages: {
             //Personalizamos nuestro mensajes de error para las etiquetas y campos de validacion que especifiquemos
             user: {
                 required: "Campo requerido",
             },
             passwd :{
                 required: "Campo requerido"
             }
         }
     });
   });
 
 