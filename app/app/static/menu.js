$(document).ready(function(){
    $("[href]").each(function() {
        if (this.href == window.location.href) {
            $(this).parent().addClass("active");
        }
    })
});
