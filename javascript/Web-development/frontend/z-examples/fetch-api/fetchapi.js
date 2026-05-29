// Make a GET request to JSONPlaceholder API
fetch('https://jsonplaceholder.typicode.com/posts/1')
  .then(response => {
    // Check if the request was successful
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    // Parse the JSON response
    return response.json();
  })
  .then(data => {
    // Work with the JSON data
    console.log(data);
  })
  .catch(error => {
    // Handle any errors
    console.error('There was a problem with the fetch operation:', error);
  });