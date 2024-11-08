document.addEventListener("DOMContentLoaded", function () {
    //index .html click buttons
    document.getElementById("patient").addEventListener("click", function () {
        window.location.href = '/plogin';
    });
    document.getElementById("doctor").addEventListener("click", function () {
        window.location.href = '/dlogin';
    });
    // Set the minimum date for the appointment date to tomorrow's date
    var today = new Date();
    var tomorrow = new Date(today);
    tomorrow.setDate(today.getDate() + 1);
    
    var day = tomorrow.getDate();
    var month = tomorrow.getMonth() + 1; // Months are zero-based
    var year = tomorrow.getFullYear();
    
    // Format the date as YYYY-MM-DD
    if (month < 10) month = '0' + month;
    if (day < 10) day = '0' + day;

    var minDate = year + '-' + month + '-' + day;
    document.getElementById('appointment_date').setAttribute('min', minDate);
});
