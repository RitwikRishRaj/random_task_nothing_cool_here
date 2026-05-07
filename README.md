# Random Task (Nothing Cool Here™)

🚚 **Delivery Time Prediction API** — Because waiting for packages is painful, and knowing how long *exactly* you'll suffer makes it slightly better. And it was random task assigned

## 🌐 Live Demo

https://random-task-nothing-cool-here.onrender.com

## 📌 How to Use

Send a **POST** request to `/predict` with distance and weight, get back your estimated delivery time. Physics does the rest.

### Request example

```bash
curl -X POST https://random-task-nothing-cool-here.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{"distance": 50, "weight": 5}'
```

Or if you're fancy:

```python
import requests

response = requests.post(
    "https://random-task-nothing-cool-here.onrender.com/predict",
    json={"distance": 50, "weight": 5}
)
print(response.json())
```

### Response

```json
{
  "est_delivery_time_hrs": 12.5
}
```

**Parameters:**
- `distance` (number): Distance in km
- `weight` (number): Weight in kg

**Returns:**
- `est_delivery_time_hrs` (number): Estimated delivery time in hours

---

*Made with minimal effort, maximum vibes. No warranty on accuracy.* 📦
