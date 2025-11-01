# LTM Backend API Documentation

## Base URL
```
http://localhost:5000/api
```

## Authentication
Currently no authentication required. Future versions will implement JWT-based auth.

## Endpoints

### Health Check

**GET** `/health`

Returns the health status of the API.

**Response:**
```json
{
  "status": "healthy",
  "service": "LTM Backend API",
  "version": "0.1.0"
}
```

---

### Get Questions

**GET** `/questions`

Retrieve all questions filtered by type.

**Query Parameters:**
- `type` (optional): Question type - `couple` or `parent`. Default: `couple`

**Example Request:**
```bash
curl "http://localhost:5000/api/questions?type=couple"
```

**Response:**
```json
{
  "success": true,
  "count": 45,
  "questions": [
    {
      "id": 1,
      "text": "Why should we marry?",
      "category": "Understanding Self and Marriage",
      "question_type": "couple",
      "options": null
    },
    ...
  ]
}
```

---

### Get Single Question

**GET** `/questions/<id>`

Retrieve a specific question by ID.

**URL Parameters:**
- `id`: Question ID (integer)

**Example Request:**
```bash
curl "http://localhost:5000/api/questions/1"
```

**Response:**
```json
{
  "success": true,
  "question": {
    "id": 1,
    "text": "Why should we marry?",
    "category": "Understanding Self and Marriage",
    "question_type": "couple",
    "options": null
  }
}
```

**Error Response (404):**
```json
{
  "success": false,
  "error": "Question not found"
}
```

---

### Submit Couple Responses

**POST** `/responses/couple`

Submit questionnaire responses for a couple.

**Request Body:**
```json
{
  "responses": [
    {
      "question_id": 1,
      "response": "We want to start a family and build a life together."
    },
    {
      "question_id": 2,
      "response": "I love their kindness and values."
    }
  ]
}
```

**Example Request:**
```bash
curl -X POST "http://localhost:5000/api/responses/couple" \
  -H "Content-Type: application/json" \
  -d '{
    "responses": [
      {
        "question_id": 1,
        "response": "My answer here"
      }
    ]
  }'
```

**Response:**
```json
{
  "success": true,
  "message": "Responses received successfully",
  "count": 2
}
```

**Error Response (400):**
```json
{
  "success": false,
  "error": "Invalid request data"
}
```

---

### Submit Parent Responses

**POST** `/responses/parent`

Submit questionnaire responses from a parent.

**Request Body:**
```json
{
  "responses": [
    {
      "question_id": 283,
      "response": "We are ready to welcome them into our family."
    }
  ]
}
```

**Example Request:**
```bash
curl -X POST "http://localhost:5000/api/responses/parent" \
  -H "Content-Type: application/json" \
  -d '{
    "responses": [
      {
        "question_id": 283,
        "response": "My answer"
      }
    ]
  }'
```

**Response:**
```json
{
  "success": true,
  "message": "Responses received successfully",
  "count": 1
}
```

---

## Error Responses

All error responses follow this format:

```json
{
  "success": false,
  "error": "Error message describing what went wrong"
}
```

**HTTP Status Codes:**
- `200 OK` - Success
- `400 Bad Request` - Invalid request data
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server error

## CORS

The API is configured to accept requests from:
- `http://localhost:5173` (Vite dev server)
- `http://localhost:3000` (React dev server)

For production, update CORS origins in `src/backend/app.py`.

## Rate Limiting

Currently no rate limiting. Consider adding rate limiting for production.

## Future Endpoints (Planned)

- `POST /api/users` - Create user account
- `POST /api/auth/login` - User authentication
- `GET /api/responses/couple/:couple_id` - Get couple responses
- `GET /api/responses/parent/:parent_id` - Get parent responses
- `PUT /api/questions/:id` - Update question (admin)
- `DELETE /api/questions/:id` - Delete question (admin)

