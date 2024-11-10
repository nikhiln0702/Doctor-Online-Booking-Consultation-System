// Function to display appointment details from session storage
function displayAppointmentDetails() {
  document.getElementById("patient-name").textContent = sessionStorage.getItem('patient_name');
  document.getElementById("patient-age").textContent = sessionStorage.getItem('patient_age');
  document.getElementById("doctor-name").textContent = sessionStorage.getItem('doctor_name');
  document.getElementById("doctor_name").textContent = sessionStorage.getItem('doctor_name');
  document.getElementById("appointment-date").textContent = sessionStorage.getItem('appointment_date');
  document.getElementById("appointment-time").textContent = sessionStorage.getItem('appointment_time');
  document.getElementById("appointment-mode").textContent = sessionStorage.getItem('mode');
  document.getElementById("payment-option").textContent = sessionStorage.getItem('payment_option');
}

// Call this function when the page loads
window.onload = function() {
  displayAppointmentDetails();
};



// Function to download as PDF
function downloadPDF() {
    const element = document.getElementById("acknowledgment-content");
    const options = {
        margin:       0.5,
        filename:     'Appointment_Confirmation.pdf',
        image:        { type: 'jpeg', quality: 0.98 },
        html2canvas:  { scale: 2 },
        jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' }
    };
    
    html2pdf().set(options).from(element).save();
}

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