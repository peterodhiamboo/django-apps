var modalDiv = $("#modal-div");

$(".js-update-post").on("click", function () {
    $.ajax({
        url: $(this).attr("data-url"),

        beforeSend: function () {
            $("#myEdit").modal("show");
        },
        success: function (data) {
            $("#myEdit .modal-content").html(data);
        }
    });
});