# 🐶 Pet Training Tips Search Microservice

This microservice provides categorized pet training tips and lets users view their saved favorite tips. It communicates over a RESTful API using HTTP and JSON.

## Communication Contract
* Protocol: HTTP/ 1.1
* Communication Format: JSON
* Request Method: GET
* Endpoints:
  * ```/tips?category={category}```
  * ```/favorites?username={username}```
* Response Status Codes:
  * ```200 OK``` - valid response with data or message
  * ```400 Bad Request``` - missing required query parameter
  * ```404 Not Found``` - username not found

### How to **Request** Data
#### 1. Retrieve Training Tips by Category
Endpoint:
```
GET /tips?category={category}
```

Example Required Paramter:
* ```category``` - string (e.g., ```"puppy"```, ```"crate training"```)

Example Call:
```python
import requests

response = request.get("http://localhost:5000/tips", params={"category": "puppy"})
```

#### 2. View Favorite Tips by Username
Endpoint:
```
GET /favorites?username={username}
```

Required Paramter:
* ```username``` - string (e.g., ```"alex"```)

Example Call:
```python
import requests

response = request.get("http://localhost:5000/tips", params={"username": "alex"})
```
---

### How to **Receive** Data
The microservice responds to client with a JSON object. 
 
Example Call:
```python
import requests

response.json()
```

Example Responses:
* Response Tips by Category
  ```
  {
    "category": "puppy",
    "tips": [
        "The earlier you start training the better; take advantage of their prime learning time.",
        "Keep training sessions short and frequent to maximize learning potential and to not overwhelm your puppy.",
        "Heap on rewards like treats and praise when your puppy does desired behaviors."
    ]
  }
  ```
* Response Favorite Tips by Username
  ```
  {
    "username": "alex",
    "favorites": [
        "The earlier you start training the better; take advantage of their prime learning time.",
        "Remove attractive items that you can to keep temptation at bay.",
        "Start with very short periods of time in the crate and gradually increase the amount of time as your dog becomes more comfortable."
    ]
  }
  ```
* Username Not Found
  ```
  {
    "error": "Username 'N/A' not found.
  }
  ```

> [!TIP]
> To handle cases as below gracefully, **response status codes** can be utilized.
> * Invalid parameter
> * Valid parameter but no values (empty)

> ```
> response.status_code
> ```

## UML Sequence Diagram