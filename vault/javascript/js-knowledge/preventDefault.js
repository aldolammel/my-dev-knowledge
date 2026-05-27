/*
  PREVENTDEFAULT()

  In JavaScript, "prevent" typically refers to preventDefault(), which is a method called on an
  event object to stop the default behavior that would normally occur when that event is triggered.
  For submit buttons in forms, here's what preventDefault() does:

*/

// Example of preventDefault() with a form submit
document.getElementById('myForm').addEventListener('submit', function(event) {
    // This prevents the form from submitting normally
    event.preventDefault();
    
    // Now you can handle the form submission with custom JavaScript
    console.log('Form submission prevented - handling with custom code');
    
    // Your custom form handling logic here
    validateForm();
    sendDataViaAjax();
});

/*

  >> What happens WITHOUT preventDefault():

    The form submits normally
    The page refreshes/redirects to the form's action URL
    Form data is sent using the traditional HTTP request
    Any JavaScript code after the submit is interrupted

  >> What happens WITH preventDefault():

    The normal form submission is blocked
    The page doesn't refresh or redirect
    You maintain full control over what happens next
    You can validate data, show loading indicators, send AJAX requests, etc.

*/