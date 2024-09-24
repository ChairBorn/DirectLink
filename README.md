# DirectLink 

## Open Source, Forever Free, User-Driven and Managed TikToc Alternative

The purpose of this project is to create space for Users to Interact with each other.

### The Technology Stack

#### Components
Mobile Clients:
iOS & Android Apps: Developed using a cross-platform framework.
API Gateway:
Handles authentication, rate limiting, and routing requests to appropriate backend services.
Web Application:
Frontend interface for users accessing DirectLink via browsers.
Backend API:
Business logic, data processing, and interaction with the database.
Database:
Stores user data, content, votes, and other essential information.
Additional Services:
Caching (Redis): For improving performance.
Content Delivery Network (CDN): For serving static assets quickly.
Logging & Monitoring: For maintaining application health and security.

#### Components Breakdown

- **Mobile Clients:**
    - **iOS & Android Apps:** Developed using a cross-platform framework.
    
- **API Gateway:**
    - Handles authentication, rate limiting, and routing requests to appropriate backend services.
    
- **Web Application:**
    - Frontend interface for users accessing DirectLink via browsers.
    
- **Backend API:**
    - Business logic, data processing, and interaction with the database.
    
- **Database:**
    - Stores user data, content, votes, and other essential information.
    
- **Additional Services:**
    - **Caching (Redis):** For improving performance.
    - **Content Delivery Network (CDN):** For serving static assets quickly.
    - **Logging & Monitoring:** For maintaining application health and security.

### Technology Stack

#### 1. Backend
- **Language:** Python
- **Framework:** FastAPI
    - **Reasons:** High performance, asynchronous support, easy to use, and modern features.
- **Authentication:** OAuth2 with JWT (JSON Web Tokens)
- **Database:** PostgreSQL
    - **Reasons:** Robust, open-source, and supports advanced features.
- **ORM:** SQLAlchemy or Tortoise ORM
- **Caching:** Redis
- **Web Server:** Uvicorn or Gunicorn with Uvicorn Workers
- **API Documentation:** Automatically generated with FastAPI (Swagger UI)

#### 2. Frontend (Web Application)
- **Framework:** React.js or Vue.js
    - **Reasons:** Highly popular, extensive ecosystem, and performance-oriented.

#### 3. Mobile Applications
- **Framework:** Flutter (Dart) or React Native (JavaScript/TypeScript)
    - **Recommendation:** Flutter for high performance and a rich set of widgets.

#### 4. Security Libraries
- **Authentication:** FastAPI Security
- **Input Validation:** Pydantic
- **Encryption:** PyJWT for JWT handling, bcrypt for password hashing
- **HTTPS:** Ensure all communications are over HTTPS using SSL/TLS

#### 5. DevOps & Deployment
- **Containerization:** Docker
- **Orchestration:** Kubernetes (if scaling is required)
- **CI/CD:** GitHub Actions, GitLab CI, or Jenkins
- **Hosting:** AWS, Google Cloud Platform (GCP), or Azure
- **Monitoring:** Prometheus & Grafana, Sentry for error tracking

### FrontEnd Structure and Deployment

To create your Project:
`npx create-react-app directlink-web [you can rename this]`  
`cd directlink-web`  
`npm install axios react-router-dom`  