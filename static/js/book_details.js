function validateDate() {
    console.log("validateDate function called");  // Debug line
    const appointmentDate = document.getElementById('appointment_date').value;
    const today = new Date().toISOString().split('T')[0]; 
    
    if (appointmentDate < today) {
        alert("Choose proper appointment date!!!");
        return false; 
    }
    return true;
}
