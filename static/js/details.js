function validateDateofBirth() {
    // Get the value of Date of Birth input
    const DoB = document.getElementById('dob').value;
    
    // Convert the date string (YYYY-MM-DD) into a Date object
    const today = new Date();
    const birthDate = new Date(DoB); // Date object of input value

    // Compare the two dates
    if (birthDate > today) {
        alert("Date of Birth cannot be in the future.");
        return false; // Prevent form submission
    }

    return true; // Allow form submission
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
  
