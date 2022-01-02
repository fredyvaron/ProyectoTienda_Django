$(document).ready(function() {
    // Upvote
    $(".upvote-click").on("click", function() {
        var commentario = $(this).data("comentario");
        console.log(commentario)
            // Ajax
        $.ajax({
            url: '/save-upvotes',
            type: "POST",
            data: {
                comentarioid: commentario,
                'csrfmiddlewaretoken': '{{csrf_token}}',
            },
            dataType: "json",
            success: function(res) {
                var _prevupvote = $(".upvote-count-" + commentarioid).text();
                if (res.bool == true) {
                    $(".upvote-count-" + commentarioid).text(parseInt(_prevupvote) + 1);
                }
            },
        });
    });

    // Downvote
    $(".downvote-click").on("click", function() {

        var commentarioid = $(this).data("comentario");
        console.log(commentarioid)
            // Ajax
        $.ajax({
            url: "/save-downvote",
            type: "POST",
            headers: { 'X-CSRFToken': csrftoken },
            data: {
                commentarioid: commentarioid,
                'csrfmiddlewaretoken': '{{ csrf_token }}',
            },
            dataType: "json",
            success: function(res) {
                var _prevupvote = $(".downvote-count-" + commentarioid).text();
                if (res.bool == true) {
                    $(".downvote-count-" + commentarioid).text(parseInt(_prevupvote) + 1);
                }
            },
        });
    });
});