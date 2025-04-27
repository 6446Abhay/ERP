// scripts.js

// Simulate a simple login flow for demonstration purposes
document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // Check credentials for different users
    if (password === '1234') {
        // Redirect based on role
        switch (username.toLowerCase()) {
            case 'teacher':
                window.location.href = 'teacher_dashboard.html';
                break;
            case 'student':
                window.location.href = 'student_dashboard.html';
                break;
            case 'admin':
                window.location.href = 'admin_dashboard.html';
                break;
            case 'parent':
                window.location.href = 'parent_dashboard.html';
                break;
            default:
                alert('Invalid username');
                break;
        }
    } else {
        alert('Invalid password, please try again.');
    }
});
