# System Architecture Diagram
## Secure Cloud-Based Healthcare Management System

---

## ASCII Art Diagram (Simple Version)

```
┌─────────────────────────────────────────────────────────────────┐
│                        CLIENT LAYER                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │   Patient    │  │    Doctor    │  │   Admin      │         │
│  │   Browser    │  │   Browser    │  │   Browser    │         │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘         │
│         │                  │                  │                 │
└─────────┼──────────────────┼──────────────────┼─────────────────┘
          │                  │                  │
          └──────────────────┴──────────────────┘
                             │
                             │ HTTPS/SSL
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                      WEB SERVER LAYER                           │
│                    ┌─────────────────┐                          │
│                    │  Nginx (Proxy)   │                          │
│                    │  - SSL/TLS      │                          │
│                    │  - Static Files │                          │
│                    │  - Load Balance │                          │
│                    └────────┬────────┘                          │
└─────────────────────────────┼───────────────────────────────────┘
                              │
                              │ HTTP
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                  APPLICATION SERVER LAYER                       │
│                    ┌─────────────────┐                          │
│                    │   Gunicorn      │                          │
│                    │  (WSGI Server)  │                          │
│                    └────────┬────────┘                          │
└─────────────────────────────┼───────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    DJANGO APPLICATION                           │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                    URL Routing                             │  │
│  └──────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              Views & Business Logic                      │  │
│  │  • Authentication (Login, Registration)                 │  │
│  │  • Appointment Management                               │  │
│  │  • User Profile Management                              │  │
│  │  • Search & Filtering                                    │  │
│  └──────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              Security Layer                               │  │
│  │  • PBKDF2-SHA256 (Password Hashing)                     │  │
│  │  • Role-Based Access Control (RBAC)                      │  │
│  │  • CSRF Protection                                       │  │
│  │  • Session Management                                    │  │
│  └──────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                    Models (ORM)                           │  │
│  │  • User Model                                             │  │
│  │  • Profile Model                                          │  │
│  │  • Appointment Model                                      │  │
│  │  • Speciality Model                                       │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      DATA LAYER                                  │
│  ┌──────────────────┐         ┌──────────────────┐             │
│  │   PostgreSQL     │         │   Media Storage   │             │
│  │   (Production)   │         │   (Images, Files)│             │
│  │                  │         │                  │             │
│  │  • Users         │         │  • Doctor Photos │             │
│  │  • Profiles      │         │  • Documents     │             │
│  │  • Appointments  │         │  • Specialities  │             │
│  │  • Specialities  │         │                  │             │
│  └──────────────────┘         └──────────────────┘             │
└─────────────────────────────────────────────────────────────────┘
```

---

## Detailed Component Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                         USER INTERFACE LAYER                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐         │
│  │   PATIENT     │    │    DOCTOR     │    │   ADMIN      │         │
│  │  INTERFACE   │    │  INTERFACE   │    │  INTERFACE   │         │
│  ├──────────────┤    ├──────────────┤    ├──────────────┤         │
│  │ • Search      │    │ • Dashboard   │    │ • Admin Panel │         │
│  │ • Book        │    │ • Appointments│   │ • User Mgmt   │         │
│  │ • Profile     │    │ • Profile     │   │ • System Ctrl │         │
│  │ • History     │    │ • Patients    │   │ • Reports     │         │
│  └──────┬───────┘    └──────┬───────┘    └──────┬───────┘         │
│         │                   │                   │                  │
└─────────┼───────────────────┼───────────────────┼──────────────────┘
          │                   │                   │
          └───────────────────┴───────────────────┘
                              │
                              │ HTTPS (SSL/TLS)
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         PRESENTATION LAYER                          │
├─────────────────────────────────────────────────────────────────────┤
│  • HTML5 Templates                                                   │
│  • CSS3 (Bootstrap 4)                                                │
│  • JavaScript (jQuery)                                               │
│  • Responsive Design                                                 │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         WEB SERVER (NGINX)                          │
├─────────────────────────────────────────────────────────────────────┤
│  • Reverse Proxy                                                     │
│  • SSL/TLS Termination                                               │
│  • Static File Serving                                               │
│  • Load Balancing                                                    │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    APPLICATION SERVER (GUNICORN)                    │
├─────────────────────────────────────────────────────────────────────┤
│  • WSGI Server                                                       │
│  • Process Management                                                │
│  • Request Handling                                                  │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      DJANGO FRAMEWORK                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │                    URL ROUTING                                │  │
│  │  /patients/  /doctors/  /bookings/  /admin/                 │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                              │                                      │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │                    VIEWS (Business Logic)                     │  │
│  │  • Authentication Views                                       │  │
│  │  • Appointment Views                                          │  │
│  │  • Profile Views                                              │  │
│  │  • Search Views                                                │  │
│  │  • Admin Views                                                 │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                              │                                      │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │              SECURITY MIDDLEWARE                               │  │
│  │  • CSRF Protection                                            │  │
│  │  • Authentication Middleware                                  │  │
│  │  • Role-Based Access Control (Custom Mixins)                  │  │
│  │  • Session Management                                         │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                              │                                      │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │                    MODELS (ORM)                               │  │
│  │  • User (with role: patient/doctor/admin)                   │  │
│  │  • Profile (avatar, phone, address, specialization)          │  │
│  │  • Appointment (patient, doctor, date, time, status)         │  │
│  │  • Speciality (name, description, icon)                      │  │
│  │  • Review (patient, doctor, rating, comment)                 │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                              │                                      │
└──────────────────────────────┼──────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         DATA LAYER                                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────────────────┐    ┌──────────────────────────┐      │
│  │    DATABASE              │    │    FILE STORAGE          │      │
│  │  (PostgreSQL/SQLite)     │    │    (Media Files)         │      │
│  ├──────────────────────────┤    ├──────────────────────────┤      │
│  │ • Users Table            │    │ • Doctor Images          │      │
│  │ • Profiles Table         │    │ • Speciality Icons       │      │
│  │ • Appointments Table     │    │ • Documents               │      │
│  │ • Specialities Table     │    │ • Uploads                 │      │
│  │ • Reviews Table          │    │                          │      │
│  └──────────────────────────┘    └──────────────────────────┘      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## User Role Flow Diagram

```
                    ┌─────────────────┐
                    │   USER LOGIN    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  AUTHENTICATION │
                    │  (PBKDF2-SHA256)│
                    └────────┬────────┘
                             │
                ┌────────────┼────────────┐
                │            │            │
                ▼            ▼            ▼
        ┌───────────┐  ┌───────────┐  ┌───────────┐
        │  PATIENT  │  │  DOCTOR   │  │   ADMIN   │
        └─────┬─────┘  └─────┬─────┘  └─────┬─────┘
              │              │              │
              ▼              ▼              ▼
    ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
    │   Patient   │  │   Doctor    │  │   Admin     │
    │  Dashboard  │  │  Dashboard  │  │   Panel     │
    │             │  │             │  │             │
    │ • Search    │  │ • Appts     │  │ • Users     │
    │ • Book      │  │ • Patients  │  │ • System    │
    │ • Profile   │  │ • Profile   │  │ • Reports   │
    └─────────────┘  └─────────────┘  └─────────────┘
```

---

## Security Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    SECURITY LAYERS                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  LAYER 1: TRANSPORT SECURITY                               │ │
│  │  • HTTPS/SSL (TLS 1.2+)                                    │ │
│  │  • Secure Cookie Transmission                              │ │
│  │  • HSTS (HTTP Strict Transport Security)                   │ │
│  └──────────────────────────────────────────────────────────┘ │
│                              │                                  │
│                              ▼                                  │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  LAYER 2: AUTHENTICATION SECURITY                          │ │
│  │  • PBKDF2-SHA256 Password Hashing                          │ │
│  │  • Salted Passwords (Unique per user)                      │ │
│  │  • Session Management                                      │ │
│  │  • CSRF Token Protection                                   │ │
│  └──────────────────────────────────────────────────────────┘ │
│                              │                                  │
│                              ▼                                  │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  LAYER 3: AUTHORIZATION SECURITY                           │ │
│  │  • Role-Based Access Control (RBAC)                       │ │
│  │  • Custom Mixins (PatientRequiredMixin, etc.)             │ │
│  │  • Permission Checks                                       │ │
│  │  • URL Access Restrictions                                 │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Deployment Architecture (Cloud)

```
                    ┌─────────────────┐
                    │   INTERNET      │
                    └────────┬────────┘
                             │
                             │ HTTPS (Port 443)
                             ▼
                    ┌─────────────────┐
                    │  DNS / CDN      │
                    │  (Cloudflare)   │
                    └────────┬────────┘
                             │
                             ▼
        ┌───────────────────────────────────────┐
        │         NGINX (Web Server)             │
        │  • SSL/TLS Termination                 │
        │  • Static File Serving                 │
        │  • Reverse Proxy                       │
        └───────────────┬───────────────────────┘
                        │
                        │ HTTP (Port 8000)
                        ▼
        ┌───────────────────────────────────────┐
        │      GUNICORN (App Server)            │
        │  • WSGI Server                        │
        │  • Multiple Workers                   │
        │  • Process Management                 │
        └───────────────┬───────────────────────┘
                        │
                        ▼
        ┌───────────────────────────────────────┐
        │      DJANGO APPLICATION               │
        │  • Views & Business Logic             │
        │  • Models & ORM                       │
        │  • Security Middleware                 │
        └───────────────┬───────────────────────┘
                        │
        ┌───────────────┴───────────────┐
        │                               │
        ▼                               ▼
┌───────────────┐            ┌──────────────────┐
│  PostgreSQL   │            │  Media Storage    │
│  Database     │            │  (S3/Cloud)      │
│               │            │                   │
│ • Users       │            │ • Images          │
│ • Appointments│            │ • Documents       │
│ • Profiles    │            │ • Static Files    │
└───────────────┘            └──────────────────┘
```

---

## How to Create Visual Diagrams

### Option 1: PowerPoint/Google Slides
1. Use the ASCII diagrams above as a guide
2. Create shapes and arrows in PowerPoint
3. Use consistent colors and styling
4. Export as high-resolution images

### Option 2: Online Tools
- **Draw.io (diagrams.net)** - Free, web-based
- **Lucidchart** - Professional diagrams
- **Creately** - Collaborative diagramming
- **Miro** - Whiteboard-style diagrams

### Option 3: Code-Based Tools
- **Mermaid** - Markdown-based diagrams
- **PlantUML** - Text-based UML diagrams
- **Graphviz** - Graph visualization

---

## Recommended Visual Style

**Colors:**
- **Client Layer:** Light Blue (#E3F2FD)
- **Web Server:** Green (#C8E6C9)
- **Application:** Orange (#FFE0B2)
- **Database:** Purple (#E1BEE7)
- **Security:** Red (#FFCDD2) with lock icons

**Shapes:**
- **Rectangles:** Components/Services
- **Cylinders:** Databases
- **Clouds:** External services
- **Arrows:** Data flow (label with protocol)

**Text:**
- **Bold:** Component names
- **Italic:** Protocols/Technologies
- **Small:** Details/descriptions

---

## Key Points to Highlight in Diagram

1. **Three-Tier Architecture** - Clear separation of layers
2. **Security at Every Layer** - HTTPS, encryption, RBAC
3. **Scalability** - Load balancing, multiple workers
4. **Cloud-Ready** - Shows deployment architecture
5. **User Roles** - Clear distinction between patient/doctor/admin

---

## Presentation Tips for Architecture Diagram

1. **Start Simple:** Show high-level overview first
2. **Drill Down:** Then show detailed components
3. **Highlight Security:** Use different colors for security layers
4. **Show Data Flow:** Use arrows to show request/response flow
5. **Explain Each Layer:** Don't just show, explain what each does

