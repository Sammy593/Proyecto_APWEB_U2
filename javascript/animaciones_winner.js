var globos_d = document.getElementById("globos_der");
var globos_i = document.getElementById("globos_izq");

var globos_d_d = document.getElementById("globos_der_d");
var globos_i_d = document.getElementById("globos_izq_d");

var estrellas = document.getElementById("estrellas");
var estrellas_container = document.getElementById("tres_estrellas");
var seccion_g = document.getElementById("section1");
var seccion_g_d = document.getElementById("globos_down");

var confetti = document.getElementById("back_confetti");

var felicitaciones = document.getElementById("felicitaciones");

var confeti = document.getElementById("confeti");

function iniciar(){
    confetti.style.filter = "opacity(50%)"
    confetti.style.transition = 'all 3s';
    
    globos_d.style.paddingTop = '0px';
  //  globos_d.style.transform = 'rotate(0deg)';
    globos_d.style.transition = 'all 2s';

    globos_i.style.paddingTop = '0px';
   // globos_i.style.transform = 'rotate(0deg)';
    globos_i.style.transition = 'all 2s';

    globos_d_d.style.paddingTop = '0px';
    globos_d_d.style.transition = 'all 2s';

    globos_i_d.style.paddingTop = '0px';
    globos_i_d.style.transition = 'all 2s';

    seccion_g.style.marginLeft = '0%';
    seccion_g.style.marginRight = '0%';
    seccion_g.style.transition = 'all 2s';

    seccion_g_d.style.marginLeft = '0%';
    seccion_g_d.style.marginRight = '0%';
    seccion_g_d.style.transition = 'all 3s';

    estrellas.style.width = '600px';
    estrellas.style.height = '600px';
   
    estrellas.style.opacity = '100%';
    estrellas.style.transition = 'all 2s';

    estrellas_container.style.padding = '0';
    estrellas_container.style.transition = 'all 2s';
  //  estrellas_container.style.visibility = 'visible';

    felicitaciones.style.fontSize = "140px";
    felicitaciones.style.transition = 'all 1.5s';

    confeti.style.marginTop = "-275px";
    confeti.style.transition = 'all 4s';
    
};

/*
.globos_der:hover,
.globos_izq:hover{
    padding-top: 0px; 
    transition: all 2s;
}

.section1:hover{
    margin-left: 0%;
    margin-right: 0%;
    transition: all 2s;
}
*/