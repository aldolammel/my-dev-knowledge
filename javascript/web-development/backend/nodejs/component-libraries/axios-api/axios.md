#### JavaScript > Node > API
# Axios

---

Axios is a popular HTTP client library for [Node.js](/javascript/web-development/backend/nodejs/_about.md) (and browsers) that simplifies making HTTP requests. So Axios provides a promise-based interface for making HTTP requests, offering a cleaner and more feature-rich alternative to Node.js' built-in `http` module or the browser's `fetch()` API.

About: https://axios-http.com

**Its strengths include:**
- Automatic JSON transformation
- Request/response interceptors
- Better error handling than Fetch
- Browser and Node.js support
- Request cancellation
- Built-in [CSRF](/dev-concepts/csrf.md) protection

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
## 1) Installing Axios:

Before:
- Assuming you're in the `/frontend/` folder.

On project front-end folder:
```bash
npm install axios
```

If vulnerability:
```bash
npm audit fix
```

---
## 2) Define Axios versions range for future updates:
In `/frontend/package.json` define the limit version for Axios updates (it should be declared in the project's [TDD](/javascript/document-templates/techical-design-document-tdd.md)):
```json
{
	//...
	"dependencies": {
		//...
		"axios": ">=1.21.1 <2.0.0",
	}
}
```

---
## 3) Integrations:
- For Vue.js: [/javascript/web-development/frontend/vue/component-libraries/axios/integration-with-vue](/javascript/web-development/frontend/vue/component-libraries/axios/integration-with-vue.md)

---
## For simplest solution in JS:
[/javascript/js-knowledge/api](/javascript/js-knowledge/api.md)



