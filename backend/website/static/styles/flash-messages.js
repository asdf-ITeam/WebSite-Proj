// flash-messages.js

document.addEventListener("DOMContentLoaded", function () {
    var flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(function (message) {
        setTimeout(function () {
            message.style.opacity = '0';
            setTimeout(function () {
                message.style.display = 'none';
            }, 1000); 
        }, 4000); 
    });
});
