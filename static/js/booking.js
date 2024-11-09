function toggleDropdown(event) {
    event.preventDefault();
    document.querySelector(".dropdown-menu").classList.toggle("show");
  }
  
  // Close dropdown when clicking outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.user_profile')) {
      var dropdowns = document.getElementsByClassName("dropdown-menu");
      for (var i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }
  function bookAppointment(doctorName, specialization, doctorId) {
    // Store details in sessionStorage
    sessionStorage.setItem('doctor_name', doctorName);
    sessionStorage.setItem('specialization', specialization);
    sessionStorage.setItem('doctor_id', doctorId);
    // Redirect to the booking details page
    window.location.href = "book_details";
}