document.addEventListener("DOMContentLoaded", function () {
    //index .html click buttons
    document.getElementById("patient").addEventListener("click", function () {
        window.location.href = '/plogin';
    });
    document.getElementById("doctor").addEventListener("click", function () {
        window.location.href = '/dlogin';
    });
    document.getElementById("admin").addEventListener("click", function () {
            window.location.href = '/alogin';
    });
});