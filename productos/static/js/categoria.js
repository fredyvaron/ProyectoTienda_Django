$(document).on('submit', '#categoria-create-form', function(e) {
    console.log($('#nombre').val())
    console.log($('#image').val())


    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '',
        data: {
            nombre: $('#nombre').val(),
            image: $('#image').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        success: function(json) {
            console.log("Categoria Creada De Forma Exitosa")
            document.getElementById("categoria-create-form").reset();
            Swal.fire({
                position: 'center',
                icon: 'success',
                title: 'Review Enviada',
                showConfirmButton: false,
                timer: 1500
            })
            $("#categoriaModal").modal("toggle"); // Use toggle to close modal

        },
        error: function(xhr, errmsg, err) {

            console.log(xhr.status + ": " + xhr.responseText); // proporcionar un poco más de información sobre el error a la consola
        }
    });
});