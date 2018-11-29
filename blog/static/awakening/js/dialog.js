$(function () {
    $(".js-create-post").click(function () {
        $.ajax({
            url: $(this).attr("data"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-post").modal("show");
            },
            success: function (data) {
                $("#modal-post .modal-content").html(data.html_form);
            }
        });
    });

});



$("#modal-post").on("submit", ".js-post-create-post", function () {
    var form = $(this);
    $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',

        success: function (data) {
            if (data.form_is_valid) {
                alert("New Post created!");  // <-- This is just a placeholder for now for testing
                $("#modal-post").modal("hide");  // <-- Close the modal
                return true;
            }
            else {
                $("#modal-post .modal-content").html(data.html_form);
            }
        }
    });
    return false;
});