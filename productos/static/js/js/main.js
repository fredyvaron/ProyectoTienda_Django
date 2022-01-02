$(document).ready(function() {

    /* 1. Visualizing things on Hover - See next part for action on click */
    $('#stars li').on('mouseover', function() {
        var onStar = parseInt($(this).data('value'), 10); // The star currently mouse on

        // Now highlight all the stars that's not after the current hovered star
        $(this).parent().children('li.star').each(function(e) {
            if (e < onStar) {
                $(this).addClass('hover');
            } else {
                $(this).removeClass('hover');
            }
        });

    }).on('mouseout', function() {
        $(this).parent().children('li.star').each(function(e) {
            $(this).removeClass('hover');
        });
    });


    /* 2. Action to perform on click */
    $('#stars li').on('click', function() {
        var onStar = parseInt($(this).data('value'), 10); // The star currently selected
        var stars = $(this).parent().children('li.star');
        console.log(onStar)
        for (i = 0; i < stars.length; i++) {
            $(stars[i]).removeClass('selected');
        }

        for (i = 0; i < onStar; i++) {
            $(stars[i]).addClass('selected');
        }

        // JUST RESPONSE (Not needed)
        var ratingValue = parseInt($('#stars li.selected').last().data('value'), 10);
        console.log(ratingValue)


        var msg = "";
        //if (ratingValue > 1) {
        //    msg = "Thanks! You rated this " + ratingValue + " stars.";
        //} else {
        //    msg = "We will improve ourselves. You rated this " + ratingValue + " stars.";
        //}
        //responseMessage(msg);


    });


});

$(document).on('submit', '#post-form', function(e) {
    const ratingval = parseInt($('#stars li.selected').last().data('value'), 10);
    console.log($('#contenido').val())


    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '',
        data: {
            contenido: $('#contenido').val(),
            ranking: ratingval,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        success: function(json) {
            document.getElementById("post-form").reset();
            $("#stars li").removeClass('selected');
            console.log("publicacion exitosa")


            Swal.fire({
                position: 'center',
                icon: 'success',
                title: 'Review Enviada',
                showConfirmButton: false,
                timer: 1500
            }).then(function() {
                window.location.reload();
            });




        },
        error: function(xhr, errmsg, err) {

            console.log(xhr.status + ": " + xhr.responseText); // proporcionar un poco más de información sobre el error a la consola
        }
    });
});

function refrescar() {
    //Actualiza la página
    location.reload();
}

function responseMessage(msg) {
    $('.success-box').fadeIn(200);
    $('.success-box div.text-message').html("<span>" + msg + "</span>");
}
window.setTimeout(function() {
    $(".alert").fadeTo(500, 0).slideUp(500, function() {
        $(this).remove();
    });
}, 2000);