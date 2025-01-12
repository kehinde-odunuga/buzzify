# Buzzify API

This project is a backend implementation of  **Buzzify API** built using Django and Django REST Framework (DRF). It provides functionalities for user authentication, profile management, posting content, interacting with posts (likes, reposts, comments), and managing notifications. This API is modular, scalable, and designed with security and performance in mind.

---

## **Features**

### **User Management**
- User registration, login, and authentication (JWT-based).
- Profile management with fields like bio, profile picture, cover photo, website, and location.
- Follow/unfollow functionality.
- Retrieve followers and following lists.

### **Post Management**
- Create, view, and delete posts.
- Support for media uploads.
- Engage with posts through likes, comments, and reposts.
- Hashtag tagging and mention support.
- Trending posts based on engagement.

### **Comments**
- Add, view, and interact with comments on posts.

### **Notifications**
- Real-time notifications for activities like follows, likes, comments, mentions, and reposts.
- Mark notifications as read.

### **Feed**
- Personalized feed with posts from followed users.
- Trending posts from the last 24 hours based on engagement.

---

## **Tech Stack**

- **Backend Framework:** Django, Django REST Framework
- **Database:** SQLite (can be configured to use PostgreSQL/MySQL)
- **Authentication:** JWT (via `rest_framework_simplejwt`)
- **Media Storage:** Configured for local file storage
- **Dependencies:**
  - `djangorestframework`
  - `djangorestframework-simplejwt`
  - `django-filter`
  - `Pillow`

---

## **Setup and Installation**

### **Prerequisites**
- Python 3.8+
- pip (Python package manager)
- Virtual environment tool (e.g., `venv` or `virtualenv`)

### **Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/social-media-api.git
   cd social-media-api
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the API at `http://127.0.0.1:8000/api/`.

---

## **API Walkthrough**

### **Authentication**
#### Register
- **Endpoint:** `POST /api/auth/register/`
- **Request:**
  ```json
  {
    "username": "exampleuser",
    "email": "user@example.com",
    "password": "securepassword"
  }
  ```
- **Response:**
  ```json
  {
    "token": "JWT_TOKEN",
    "refresh": "REFRESH_TOKEN",
    "user": { ... }
  }
  ```

#### Login
- **Endpoint:** `POST /api/auth/login/`
- **Request:**
  ```json
  {
    "username": "exampleuser",
    "password": "securepassword"
  }
  ```
- **Response:** Similar to registration.

### **User Profile**
- **Get All Users:** `GET /api/users/`
- **Get Specific User:** `GET /api/users/{id}/`
- **Follow User:** `POST /api/users/{id}/follow/`
- **Unfollow User:** `POST /api/users/{id}/unfollow/`

### **Posts**
- **Create Post:** `POST /api/posts/`
  ```json
  {
    "content": "Hello, world!",
    "media": "image.jpg"
  }
  ```
- **Like Post:** `POST /api/posts/{id}/like/`
- **Trending Posts:** `GET /api/trending/`

### **Comments**
- **Add Comment to Post:** `POST /api/posts/{id}/comments/`
- **View Comments:** `GET /api/posts/{id}/comments/`

### **Notifications**
- **View Notifications:** `GET /api/notifications/`
- **Mark All Read:** `POST /api/notifications/mark-all-read/`

### **Feed**
- **User Feed:** `GET /api/feed/`

---

## **Folder Structure**

```
.
├── users/             # User-related models, views, serializers, and URLs
├── posts/             # Post-related models, views, serializers, and URLs
├── core/              # Project-level settings and configurations
├── media/             # Uploaded media files
├── requirements.txt   # Project dependencies
└── README.md          # Project documentation
```

---

## **Future Enhancements**

1. **Real-time Updates:** Integrate WebSockets for live notifications and updates.
2. **Analytics Dashboard:** Provide insights on user engagement and activity trends.
3. **Advanced Search:** Implement fuzzy matching for post and user searches.
4. **Cloud Integration:** Move media storage to cloud-based solutions like AWS S3.

---

## **Contributing**

Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, please open an issue first to discuss your ideas.

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Contact**

- **Author:** Kehinde Odunuga
- **Email:** omobolaji92@gmail.com
- **LinkedIn:** [kehinde-odunuga](https://www.linkedin.com/in/kehinde-odunuga/)
- **GitHub:** [kehinde-odunuga](https://github.com/kehinde-odunuga)
