$(document).ready(function() {
    const sign_container = $('#sign-container');
    const form_container = $('#form-container');
    const paisaje_container = $('.paisaje-container');
    const comentarios = $('.comentario');
    const ruta = window.location.pathname

    form_container.hide();
    sign_container.hide();
    paisaje_container.hide();
    comentarios.hide();

    switch (true){
        case (ruta === '/signin/' || ruta === '/signup/'):
            sign_container.fadeIn(2500);
            form_container.slideDown(700);
            form_container.animate({width: '800px'}, 400);
            form_container.animate({width: '600px'}, 1000);
            break
        case (
            ruta === '/paisajes/paisaje1/' ||
            ruta === '/paisajes/paisaje2/'||
            ruta === '/paisajes/paisaje3/'
        ):
            paisaje_container.fadeIn(2500);
            break
        case (ruta === '/comentarios/'):
            comentarios.fadeIn(2500);
            break
    }
})