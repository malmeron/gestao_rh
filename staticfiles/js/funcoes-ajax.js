function teste() {
    alert('Funcionou!');
}

function utilizouHoraExtra(id) {
    console.log(id);

    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    valor = document.getElementById('campoX').value;
    $.ajax({
        type: 'POST',
        url: '/horas-extras/utilizou-hora-extra/'+ id + '/',
        data: {
            csrfmiddlewaretoken: token,
            outro_parametro: valor
        },
        success: function(result){
            console.log(result);
            $("#mensagem").text(result.mensagem);
            $("#horas_atualizadas").text(result.horas);
            $("#passando_texto").text(result.valor);
        }
    });
}