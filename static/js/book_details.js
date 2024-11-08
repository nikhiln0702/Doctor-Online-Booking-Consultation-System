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
  
