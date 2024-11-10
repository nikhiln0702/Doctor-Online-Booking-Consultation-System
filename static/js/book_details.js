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

  function capitalizeWords(str) {
    return str.replace(/\b\w/g, char => char.toUpperCase());
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


function bookdetails(patient_name, patient_age, appointment_date,appointment_time,mode,payment_option) {
  // Store details in sessionStorage
  // Capitalize data before storing
  const formattedPatientName = capitalizeWords(patient_name);
  const formattedMode = capitalizeWords(mode);
  const formattedPaymentOption = capitalizeWords(payment_option);
  sessionStorage.setItem('patient_name', formattedPatientName);
    sessionStorage.setItem('patient_age', patient_age);
    sessionStorage.setItem('appointment_date', appointment_date);
    sessionStorage.setItem('appointment_time', appointment_time);
    sessionStorage.setItem('mode', formattedMode);
    sessionStorage.setItem('payment_option', formattedPaymentOption);
}
function handleFormSubmit(event) {
  // Prevent the form from submitting immediately
  event.preventDefault();
  validateDate();

  // Get form values
  const patient_name = document.getElementById('patient_name').value;
  const patient_age = document.getElementById('patient_age').value;
  const appointment_date = document.getElementById('appointment_date').value;
  const appointment_time = document.getElementById('appointment_time').value;
  const mode = document.getElementById('mode').value;
  const payment_option = document.getElementById('payment_option').value;

  // Call the bookdetails function with the form values
  bookdetails(patient_name, patient_age, appointment_date, appointment_time, mode, payment_option);


  // Submit the form
  event.target.submit();
}