function validateDate() {
    const appointmentDate = document.getElementById('appointment_date').value;
    const today = new Date().toISOString().split('T')[0]; 
    
    if (appointmentDate < today) {
        alert("Choose proper appointment date!!!");
        return false; 
    }
    return true;
}
// Toggle dropdown visibility
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
document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("cancel").addEventListener("click", function () {
    window.location.href = '/booking';
  });
});
// Retrieve doctor details from sessionStorage
document.getElementById('doctor_name').value = sessionStorage.getItem('doctor_name');
document.getElementById('doctor_id').value = sessionStorage.getItem('doctor_id');
document.getElementById('specialization').value = sessionStorage.getItem('specialization')
  
