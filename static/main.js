$(document).on("click", ".browse", function () {
  var file = $(this).parents().find(".thumbnail");
  file.trigger("click");
});
$('input[type="file"]').change(function (e) {
  var fileName = e.target.files[0].name;
  $("#thumbnail").val(fileName);

  var reader = new FileReader();
  reader.onload = function (e) {
    document.getElementById("preview").src = e.target.result;
  };
  reader.readAsDataURL(this.files[0]);
});