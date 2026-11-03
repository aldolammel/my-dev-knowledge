#### API
# What is it

---

An API (Application Programming Interface) is a set of rules, protocols, and tools that allows different software applications to communicate with each other. It defines how requests and responses should be structured, enabling seamless interaction between systems, services, or components.
### Key Concepts
- **Standardized Communication:**  APIs define a structured way for software to exchange data (e.g., using HTTP requests, gRPC, or WebSockets).
- **Abstraction:** APIs hide complex internal logic, exposing only the necessary endpoints (e.g., a weather API provides temperature data without revealing its back-end algorithms).
- **Statelessness (Common in Web APIs):**  Each request contains all the information needed to process it (e.g., REST APIs).

**Web API core layers:**
- **Endpoint** is the URL route and the HTTP method (e.g., `POST /api/v1/users/`) that receives the request and sends back the response. It is the *doorway*.
- **Serializer** is the mechanism (commonly found in frameworks like Django REST Framework) that converts complex data types like model instances into native Python datatypes that can easily be rendered into JSON, and vice versa. It is the **translator and gatekeeper** that handles validation and formatting.
- **Views / Controllers:** The business logic that takes the request from the endpoint, processes it (often using the serializer), and decides what response to return.
- **Models / ORM (Database):** The structure and connection to where your data is actually stored and retrieved.
- **Authentication & Permissions:** The security layer that verifies _who_ the user is and _what_ actions they are allowed to perform.
- **Routers / URL Configs:** The mapping system that directs an incoming URL to the correct view or handler.
- **Middleware:** Functions that sit in the request/response lifecycle to handle cross-cutting concerns like logging, security headers, or rate limiting.

---
## How it works:

**Client Sends a Request**
E.g: A mobile app requests weather data via GET https://api.weatherexample.com/v1.1/forecast?city=PortoAlegre

**Server Processes the Request:**
E.g. The API validates the request, fetches data (e.g., from a database), and formats it (usually as JSON/XML).

**Server Sends a Response:**
Json e.g.:
```json
{
	"temperature": 22,
	"conditions": "sunny"
}
```

**Client Uses the Data:**
E.g. The app displays the weather to the user. "Porto Alegre, now is sunny, 22ºC"

---
## Types of APIs:

| Type          | Description                       | Use case                         |
| ------------- | --------------------------------- | -------------------------------- |
| Web APIs      | HTTP-based, used for web services | Fetching Twitter data via REST.  |
| Library APIs  | Exposed by software libraries     | Using requests in Python.        |
| OS APIs       | Allow apps to interact with an OS | Windows API for file operations. |
| Hardware APIs | Control hardware devices          | Raspberry Pi sensor APIs.        |

---
## Data manipulation methods:

Sometimes you'll need to use these methods to manipulate the data from an API
- GET
- POST
- PUT
- DELETE

---
## How to plan your API:
[/api/\_how-to-plan-an-api](/api/_how-to-plan-an-api.md)

---
## How to convert objects to a JSON, for example:
Read more about Serializers: [/api/serializers](/api/serializers.md)

