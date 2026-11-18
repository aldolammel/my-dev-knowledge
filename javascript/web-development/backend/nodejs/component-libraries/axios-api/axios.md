#### JavaScript > Node > API
# Axios

---

Axios is a popular HTTP client library for Node.js (and browsers) that simplifies making HTTP requests. So Axios provides a promise-based interface for making HTTP requests, offering a cleaner and more feature-rich alternative to Node.js's built-in http module or the browser's `fetch()` API.

About: https://axios-http.com/

**Its strengths include:**
- Automatic JSON transformation
- Request/response interceptors
- Better error handling than Fetch
- Browser and Node.js support
- Request cancellation
- Built-in CSRF protection

---
## Key features examples:
Request Methods: Supports all standard HTTP methods (GET, POST, PUT, DELETE, PATCH, etc.) with simple method calls:
```js
// GET request
const response = await axios.get('https://api.example.com/users');

// POST request with data
const response = await axios.post('https://api.example.com/users', {
	name: 'John Doe',
	email: 'john@example.com'
});

```

Request/Response Interceptors: Allows you to transform requests or responses before they're handled:
```js
// Add auth token to all requests
axios.interceptors.request.use(config => {
	config.headers.Authorization = `Bearer ${token}`;
	return config;
});
```

---
## Installing Axios:

Before:
- Assuming you're in the `/frontend/` folder.

On project front-end folder:
```bash
npm install axios
```

If vulnerability:
```bash
npm audit fix
# or using this flag:
npm audit fix --force
```

---
## Integrations:
For Vue.js: [javascript/web-development/frontend/vue/3-component-libraries/axios-for-vue/axios-integration-with-vue](javascript/web-development/frontend/vue/3-component-libraries/axios-for-vue/axios-integration-with-vue.md)

---
## For simplest solution in JS:
[/javascript/js-knowledge/api](/javascript/js-knowledge/api.md)



