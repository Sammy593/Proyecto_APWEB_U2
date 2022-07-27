var boton = document.getElementById("btn_Go");
var boton_txt = document.getElementById("text_btn_go");


function boton_aparecer(){
    boton.style.width = '600px';
    boton.style.height = '200px';
    boton.style.fontSize = '12px';
    boton.style.transition = 'all 2s';


    boton_txt.style.fontSize = '100px';
    boton_txt.style.transition = 'all 2s';
 
    setTimeout(function(){
    boton.style.animation = 'a_boton 2s linear infinite';
    boton_txt.style.animation = 'a_Tgo 2s linear infinite';
    } , 2500);
};

boton.addEventListener('click', function(){

    setTimeout(
        function(){
            window.location.href = "/game";
        }, 1000);
});