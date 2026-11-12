#### JavaScript > API
# FechtAPI (JS native solution)

---

```js
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
```

---
## For Node.js, you got Axios API:
[/javascript/nodejs/component-libraries/axios-api/axios](/javascript/nodejs/component-libraries/axios-api/axios.md)
## For Vue, API with composition:
[/javascript/web-development/frontend/z-examples/fetch-api-on-vuejs/App_approach_compositionApi](/javascript/web-development/frontend/z-examples/fetch-api-on-vuejs/App_approach_compositionApi.md)
## For Vue, API with options:
[/javascript/web-development/frontend/z-examples/fetch-api-on-vuejs/App_approach_optionsApi](/javascript/web-development/frontend/z-examples/fetch-api-on-vuejs/App_approach_optionsApi.md)
## For Vue, API with Vuex:
[/javascript/web-development/frontend/z-examples/fetch-api-on-vuejs/vuex_action_using_fetchApi](/javascript/web-development/frontend/z-examples/fetch-api-on-vuejs/vuex_action_using_fetchApi.md)



