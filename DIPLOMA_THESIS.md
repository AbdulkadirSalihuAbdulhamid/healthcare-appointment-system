# DIPLOMA THESIS — FORMATTING GUIDE

**Structure matches a standard FTIK diploma thesis (chapters 1–9, same style as recipe-app example). See `THESIS_FRIEND_STYLE_GUIDE.md` for paste steps into your friend's Word template.**

**Copy this document into Microsoft Word and apply:**
- Font: Times New Roman, 12 pt, 1.5 line spacing, justified
- Margins: top 40 mm, bottom 25 mm, right 25 mm, left 35 mm
- Headings: Arial 14 pt bold (Heading 1), Arial 12 pt bold (sections)
- Page numbers: bottom center
- Replace all `[PLACEHOLDER]` fields with your official data before submission

---

# COVER PAGE

**Number:** [THESIS_NUMBER] / 2026

**DIPLOMA WORK**

**Secure Cloud-Based Healthcare Appointment Management System (DocBook)**

**Author:** Abdulkadir Salihu Abdulhamid

**Year:** 2026

University of Pécs  
Faculty of Engineering and Information Technology  
Computer Science Engineering Bachelor

*(On the spine: author name, thesis number, year. Glue portrait photo on inside cover.)*

---

# TITLE PAGE

**DIPLOMA WORK**

**Secure Cloud-Based Healthcare Appointment Management System (DocBook)**

**Author:** Abdulkadir Salihu Abdulhamid  
**Supervisor:** [SUPERVISOR_NAME]

Pécs, 2026

---

# SPECIFICATION OF TITLE AND TASKS

**University of Pécs**  
**Faculty of Engineering and Information Technology**  
**Computer Science Engineering Bachelor**

**Number:** [THESIS_NUMBER] / 2026

**DIPLOMA THESIS**

The title and the topic of the diploma thesis, which must be submitted before the final exam, are the following:

**Title:** Secure Cloud-Based Healthcare Appointment Management System (DocBook)

**Tasks:**

1. Analyse the requirements of a secure, web-based healthcare appointment system for patients, doctors, and administrators.
2. Design and implement a role-based application that supports appointment scheduling, tracking, and management.
3. Implement secure authentication with encrypted password storage and access control for each user role.
4. Deploy the system to a cloud platform with HTTPS protection and document the architecture, tests, and results.

**Responsible department:** [DEPARTMENT_NAME]

**External supervisor (if any):** [EXTERNAL_SUPERVISOR_OR_N/A]  
**Institution:** [INSTITUTION_OR_N/A]

**Supervisor:** [SUPERVISOR_NAME]  
**Institution:** University of Pécs

Pécs, [SUBMISSION_DATE]

Prof. Dr. Péter Iványi  
Head of Department

---

# DECLARATION

I declare that this diploma thesis is the result of my own work. All references and external works have been identified and cited. I have not used any other external help.

The results of my diploma work can be used by the university for its own purposes free of charge.

Pécs, [SUBMISSION_DATE]

................................................  
Signature of the student

---

# TABLE OF CONTENTS

*(Copy this list into Word, then use References → Table of Contents → Automatic. Update page numbers after pagination. Style matches standard FTIK diploma layout.)*

Declaration  
Table of Contents  

**1. Introduction**  
1.1. Objectives  

**2. Literature Review**  
2.1. Overview of Healthcare Appointment Systems  
2.2. Theoretical Framework  
2.2.1. User-Centered Design (UCD) Principles  
2.2.2. Core Features Guided by UCD Principles  
2.3. Comparative Analysis of Existing Systems  
2.3.1. Healthcare and Appointment Platforms  
2.3.2. Identified Gaps and Solutions  

**3. Specification and Solution Approach**  
3.1. Specification  
3.2. Solution Approach  
3.2.1. Backend  
3.2.2. Frontend  
3.2.3. Tools and Development Environment  

**4. System Design and Architecture**  
4.1. Database Design  
4.2. Backend Design  
4.3. Frontend Design  
4.3.1. Django Templates and Bootstrap  
4.3.2. HTMX  
4.3.3. jQuery and Chart.js  
4.3.4. Django REST Framework  
4.3.5. URL Routing Structure  
4.4. Use Case Diagrams  
4.5. Wireframes and Interface Screens  

**5. Implementation**  
5.1. Django Stack Development  
5.1.1. Backend Setup  
5.1.2. Frontend Setup  
5.2. Configuration Setup  
5.2.1. Middleware  
5.2.2. Routes  
5.2.3. Database Models  
5.3. Authentication and Authorization  
5.4. Appointment Booking Workflow  
5.4.1. Schedule and Slot Generation  
5.4.2. Booking Creation and Status Management  
5.4.3. Prescription and Review Processing  
5.5. Administrative Dashboard and Reports  
5.6. Cloud Deployment on Render  
5.7. Security and HTTPS Configuration  
5.8. User Interface Implementation  

**6. Testing and Feedback**  
6.1. Test Strategy  
6.2. Functional Testing  
6.3. Security Testing  
6.4. Evaluation and Feedback  

**7. Conclusion and Future Development**  
7.1. Conclusion  
7.2. Future Development  

**8. References**  

**9. Appendix**  
9.1. User Manual  
9.2. Source Code Structure  
9.3. Screenshots and Figures  
9.4. Requirements Traceability Matrix  
9.5. Deployment Commands  
9.6. Code Excerpts  
9.7. Glossary  

---

# 1. INTRODUCTION

Healthcare organisations depend on reliable scheduling so that patients receive care on time and clinical staff can plan their work efficiently. In many clinics and hospitals, appointments are still arranged by telephone, paper registers, or informal messaging. These methods are slow, error-prone, and difficult to audit. When several receptionists maintain separate notebooks, double booking and lost records become frequent. Patients who cannot reach the clinic by phone may delay treatment. Doctors lack a single view of the day’s consultations. Administrators cannot easily measure utilisation or revenue. A dedicated web application that runs in the cloud can centralise appointment data, enforce security rules, and give each stakeholder—patient, doctor, and administrator—a clear interface for their tasks.

The global shift toward digital health accelerated after widespread adoption of internet services and mobile devices. The World Health Organization promotes digital health as a means to strengthen health systems and improve outcomes [1]. For computer science engineering, an appointment system is an appropriate diploma topic because it combines databases, human–computer interaction, security engineering, and distributed deployment in one coherent product.

The aim of this diploma work is to design, implement, test, and deploy **DocBook**, a secure cloud-based healthcare appointment management system. The name **DocBook** reflects the purpose: a digital record of doctor appointments and related administrative data. The personal motivation for this topic came from observing how outpatient clinics struggle with manual scheduling during peak hours. I wanted to build a system that could be demonstrated to examiners both locally and through a stable HTTPS URL.

## 1.1. Objectives

The approved diploma tasks define the following **primary objectives:**

1. Analyse the requirements of a secure, web-based healthcare appointment system for patients, doctors, and administrators.
2. Design and implement a role-based application that supports appointment scheduling, tracking, and management.
3. Implement secure authentication with encrypted password storage and access control for each user role.
4. Deploy the system to a cloud platform with HTTPS protection and document the architecture, tests, and results.

**Scope included:** user registration and login, doctor search, slot-based booking, dashboards, prescriptions with rich text, admin CRUD for specialities, appointment and revenue reports, automated demo data for evaluation.

**Scope excluded:** payment gateways, insurance billing, video telemedicine, native mobile applications, and integration with national electronic health record systems.

The core problem is to provide a **single web platform** where patients can discover doctors and book appointments; doctors can publish schedules and manage visits; administrators can monitor the institution. The system must prevent users from accessing functions outside their role. Login credentials must never be stored in plain text. In production, all communication must use HTTPS.

---

# 2. LITERATURE REVIEW

## 2.1. Overview of Healthcare Appointment Systems

Healthcare appointment scheduling sits at the intersection of medicine, information technology, and service operations. Clinics must match finite doctor time with patient demand while minimising no-shows and idle capacity. Before computerisation, paper diaries and wall calendars performed this function. Computerised systems introduced searchable records, automated reminders, and statistical reports. Web-based systems further removed the need for patients to visit the clinic physically to reserve a slot. Cloud hosting removed the need for each clinic to maintain its own server room.

Digital health services have expanded rapidly. Patients expect to book consultations online, and providers need systems that respect privacy and role separation. For a computer science engineering project, it is essential to demonstrate not only user-facing features but also secure engineering practice: correct authentication, authorisation, and deployment on infrastructure that supports TLS encryption.

During my studies I identified a gap between simple demonstration websites and production-oriented applications. I therefore set out to build a complete system that could be demonstrated locally and also deployed on a public cloud URL with a real database, which is closer to industry practice than a prototype that runs only on a developer laptop.

## 2.2. Theoretical Framework

Healthcare appointment systems should be designed around the needs of real users rather than around database tables alone. User-Centered Design (UCD) provides a suitable theoretical basis for this thesis.

### 2.2.1. User-Centered Design (UCD) Principles

ISO 9241-210 defines UCD as an iterative process that focuses on users and their tasks. For DocBook, three principles were applied:

1. **Understand users and context** — patients need fast booking; doctors need reliable schedules; administrators need overview statistics.
2. **Evaluate against requirements** — each function maps to FR/NFR identifiers in Chapter 3.1.
3. **Iterate from feedback** — classmates tested the UI; confusing schedule setup was simplified.

### 2.2.2. Core Features Guided by UCD Principles

| UCD principle | DocBook feature |
|---------------|-----------------|
| Visibility of status | Appointment states: pending, confirmed, completed |
| Error prevention | Unique constraint prevents double booking |
| Recognition over recall | Dashboard lists upcoming appointments |
| Role-appropriate UI | Separate patient, doctor, admin interfaces |
| Trust and security | HTTPS, hashed passwords, RBAC |

## 2.3. Comparative Analysis of Existing Systems

### 2.3.1. Healthcare and Appointment Platforms

Commercial hospital systems (Epic, Cerner, etc.) integrate scheduling with billing and clinical records. They are powerful but expensive. Consumer apps (Zocdoc-style platforms) focus on discovery and booking for private practice. DocBook positions itself as an **educational full-stack implementation** with documented security and open deployability, not as a commercial competitor.

**Table 1** — Comparison of approach types

| Type | Strength | Limitation | DocBook response |
|------|----------|------------|------------------|
| Paper diary | Simple | No search, no remote access | Web database |
| Spreadsheet | Flexible | No RBAC, no concurrent access | Multi-user app with roles |
| Full HIS | Complete | Cost, complexity | Focused appointment module |
| Generic CRUD demo | Fast to build | No healthcare workflow | Full appointment lifecycle |

### 2.3.2. Identified Gaps and Solutions

| Gap in manual / generic systems | DocBook solution |
|--------------------------------|------------------|
| No role separation | PatientRequiredMixin, DoctorRequiredMixin, AdminRequiredMixin |
| Plain-text or weak passwords | Django PBKDF2-SHA256 hashing |
| No cloud HTTPS demo | Render deployment with TLS |
| Double booking possible | `unique_together` on doctor, date, time |
| No admin reporting | Appointment and revenue reports |

---

# 3. SPECIFICATION AND SOLUTION APPROACH

## 3.1. Specification

The requirements for **DocBook** were derived from studying how outpatient clinics operate in practice. A patient contacts the clinic; staff check the doctor’s diary (paper or spreadsheet), reserve a slot, and later mark the visit as completed or missed. When several people work without one shared system, the same slot can be promised twice, data can be entered incorrectly, and there is no clear record of who changed an appointment.

Translating this process into software requires **data validation** (correct dates, required fields, consistent status values), **concurrency** (only one patient may book a given doctor at a given date and time), and **accountability** (status changes are tied to the logged-in role). DocBook must also support patients, doctors, and administrators through **role-based access control** and basic security (hashed passwords, CSRF protection, HTTPS in production). The subsections below list functional and non-functional requirements, stakeholder needs, the manual workflow, use cases, and risks—against which Chapters 4–6 were developed.

### 3.1.1. Functional requirements

| ID | Requirement |
|----|-------------|
| FR-1 | The system shall provide public pages (home, terms, privacy) and doctor listing with search. |
| FR-2 | Patients shall register, log in, book appointments, view and cancel bookings, and add reviews. |
| FR-3 | Doctors shall register, set weekly schedules, accept or reject appointments, manage patients, and create prescriptions. |
| FR-4 | Administrators shall access a dedicated dashboard with user, appointment, speciality, and report management. |
| FR-5 | The system shall prevent double booking of the same doctor at the same date and time. |
| FR-6 | Appointment status shall follow defined states: pending, confirmed, completed, cancelled, no_show. |

### 3.1.2. Non-functional requirements

| ID | Requirement |
|----|-------------|
| NFR-1 | Passwords shall be stored using a one-way hash (PBKDF2-SHA256). |
| NFR-2 | Forms shall be protected against CSRF. |
| NFR-3 | Production shall enforce HTTPS, secure cookies, and HSTS. |
| NFR-4 | The application shall run on Python 3.12 and Django 5.0.6. |
| NFR-5 | Configuration secrets shall be loaded from environment variables, not hard-coded in source. |
| NFR-6 | Static assets shall be served efficiently in production (WhiteNoise). |

### 3.1.3. Stakeholder analysis

- **Patients** need simplicity, clear availability, and trust in data handling.
- **Doctors** need accurate schedules and quick status updates on appointments.
- **Administrators** need overview statistics and control over specialities and content.
- **Developers / maintainers** need modular Django apps and documented deployment steps.

### 3.1.4. Analysis of the current situation (manual process)

Before automation, a typical small clinic workflow can be described in five steps: (1) the patient calls or visits reception; (2) staff look up the doctor’s paper diary; (3) a slot is verbally agreed; (4) the name is written in the diary; (5) on the day of visit the doctor marks attendance informally. This process has weaknesses. Paper diaries are not searchable by specialisation across many doctors. Changes require physical access to the book. There is no automatic reminder. Reporting on monthly appointments or revenue requires manual counting.

DocBook digitises steps 1–5. Search replaces browsing paper lists. The database replaces the diary. Status fields replace marginal notes. Reports query the database directly. The analysis shows that the highest value is not fancy graphics but **correct data model, access control, and reliable hosting**.

### 3.1.5. Use cases

#### 3.1.5.1. Use case: patient books an appointment

**Actor:** registered patient. **Precondition:** doctor has published schedule slots. **Main flow:** patient logs in, searches for doctor, opens profile, selects date and time, submits booking, receives confirmation with pending status. **Alternative flow:** slot already taken — system shows error and offers another slot. **Postcondition:** booking record exists with status pending.

#### 3.1.5.2. Use case: doctor confirms appointment

**Actor:** registered doctor. **Precondition:** pending booking exists for that doctor. **Main flow:** doctor opens appointment list, selects booking, chooses confirm action. **Postcondition:** status becomes confirmed; patient sees updated state on dashboard.

#### 3.1.5.3. Use case: administrator generates report

**Actor:** superuser administrator. **Precondition:** historical bookings exist. **Main flow:** admin logs in, navigates to appointment report, filters by period, reads aggregated counts. **Postcondition:** no data change; information supports management decisions.

### 3.1.6. Risk analysis

| Risk | Impact | Mitigation in DocBook |
|------|--------|------------------------|
| Unauthorised access to medical data | High | RBAC, login required, HTTPS |
| Password leakage | High | Hashing, no plain-text storage |
| Double booking | Medium | DB uniqueness constraint |
| CSRF on forms | Medium | Django CSRF middleware |
| Downtime on free cloud tier | Low | Acceptable for thesis demo; paid tier for production |
| Weak demo passwords | Medium | Documented warning; change in real deployment |

---

## 3.2. Solution Approach

Given the requirements in Section 3.1, the chosen solution is a **Django monolith**: one Python application that handles authentication, business logic, HTML pages, and database access. This approach was preferred over a separate React (or similar) single-page application because it reduces deployment complexity, keeps session-based login straightforward, and matches the skills emphasised in the computer science engineering programme. The user interface is built with **server-rendered templates** (Bootstrap, jQuery, HTMX where partial updates help), with **Django REST Framework** used only for selected API endpoints such as profile updates.

For development, the project runs locally with **SQLite**; for the thesis demonstration it is deployed on **Render.com** with **PostgreSQL**, **Gunicorn** as the application server, and **WhiteNoise** for static files. Production settings enforce **HTTPS**, secure cookies, and secrets loaded from environment variables. The following subsections describe the **backend** (Django apps, models, and security), the **frontend** (templates and client-side libraries), and the **tools and development environment**—in the same order used in comparable diploma theses.

### 3.2.1. Backend

Healthcare information systems (HIS) support clinical and administrative processes in hospitals and clinics.

Healthcare information systems (HIS) support clinical and administrative processes in hospitals and clinics. A typical HIS architecture includes modules for patient administration, laboratory, pharmacy, billing, and scheduling. Large vendors integrate these modules so that data flows from appointment booking to billing without re-entry. The capital cost and training time for such systems exclude many small clinics, which continue to use hybrid manual and spreadsheet processes.

Appointment scheduling modules within HIS perform constraint satisfaction: assign patients to resources (doctors, rooms, equipment) subject to availability rules. DocBook implements a simplified constraint: one patient per doctor per time slot. More advanced systems optimise across multiple resources and handle waiting lists; those algorithms were not required for this thesis but are well described in operations research literature on health care scheduling.

Privacy regulations such as the GDPR in the European Union require lawful basis for processing personal data, data minimisation, and security measures [1]. DocBook stores personal identifiers (name, email, phone, date of birth) and health-related notes in profiles and prescriptions. A production deployment in the EU would require privacy policy text—which is partially addressed by the terms and privacy pages—and organisational measures beyond software alone. The thesis focuses on technical security controls that support compliance.

Appointment scheduling is a common module within HIS or as a standalone patient portal [1]. Studies emphasise that usability and perceived security strongly influence adoption: users avoid systems they do not trust [2].

Commercial products (e.g. hospital information suites) offer deep integration but require substantial licensing and customisation. For this project, a focused appointment portal is appropriate: it demonstrates core computer science competencies—databases, web engineering, security—without the complexity of a full hospital ERP.

Electronic health records (EHR) and hospital information systems (HIS) are discussed extensively in medical informatics literature. A full EHR stores longitudinal patient history, laboratory results, and billing codes. DocBook intentionally implements only the **scheduling and light clinical documentation** subset (prescriptions and reviews) so that the scope remains achievable in one academic year. Future integration with HL7 FHIR APIs could expose booking resources to external systems [14], but such integration was out of scope.

Patient portals studied by Häyrinen et al. show that perceived security and ease of use determine adoption [2]. This finding influenced DocBook’s design: login is a simple username/password form with CSRF protection; navigation is role-specific so patients never see admin menus. Trust is also communicated by deploying with HTTPS and by not exposing stack traces when `DEBUG=False`.

The backend uses **Python 3.12** and **Django 5.0.6** with apps `accounts`, `doctors`, `patients`, `bookings`, and `core`. Authentication is session-based. The ORM maps to SQLite locally and PostgreSQL in production. **Gunicorn** serves WSGI requests. **WhiteNoise** serves static files. Passwords are hashed with PBKDF2-SHA256.

### 3.2.2. Frontend

## 2.2. Web application architectures (reference)

Modern web systems commonly follow either a **monolithic server-rendered** architecture or a **separated frontend/backend** (SPA + REST API). Monolithic Django applications render HTML on the server, store session state server-side, and simplify deployment because one process serves pages and business logic [3]. SPAs improve interactivity but increase development and deployment surface (separate build pipeline, CORS, token management).

For DocBook I selected a **Django monolith** with template-based UI and selective use of HTMX and Django REST Framework for partial updates. This choice reduces complexity while still allowing dynamic behaviour where needed (profile updates, schedule editing).

Fielding’s architectural dissertation distinguishes REST as a set of constraints on stateless communication [7]. DocBook uses REST partially: JSON endpoints exist for profile fragments, but the primary interface is not a REST client application. This hybrid approach is common in enterprise Django projects described by Fowler [9]: server-rendered pages for most flows, APIs where asynchronous updates help.

A comparison of architectural options considered for this thesis is given in Table 1.

**Table 1** — Comparison of web architecture options

| Approach | Advantages | Disadvantages | Decision |
|----------|------------|---------------|----------|
| Django monolith + templates | Fast development, built-in auth | Less interactive UI | **Selected** |
| React SPA + Django API | Rich UI | Two deployments, token auth complexity | Rejected |
| PHP monolith | Cheap hosting | Less alignment with Python curriculum | Rejected |
| Microservices | Scalability | Overkill for diploma scope | Rejected |

## 2.3. Security in web applications

The OWASP Top 10 lists the most critical web risks, including broken access control, cryptographic failures, and injection [4]. Mitigations relevant to this project include:

- **Authentication:** verify identity before granting access; use framework password hashers.
- **Authorisation:** enforce role checks on every sensitive view.
- **CSRF:** use synchroniser tokens on state-changing requests.
- **Transport security:** TLS in production; secure and HttpOnly session cookies.
- **Clickjacking:** X-Frame-Options middleware.

Django implements many of these patterns by default [5], which is one reason it is widely used in education and industry.

NIST digital identity guidelines recommend strong password storage and protected sessions [10]. Django’s password hasher aligns with these recommendations. For authentication assurance level, the thesis project implements single-factor password login, which is acceptable for a demonstration system but would require multi-factor authentication in high-risk clinical environments.

SQL injection is mitigated by Django’s ORM when developers avoid raw queries with untrusted input. Cross-site scripting (XSS) is reduced by template auto-escaping. Insecure direct object references are addressed by filtering querysets with `request.user` rather than trusting client-supplied identifiers alone. Security design is summarised again in Chapter 3.5 and verified in Chapter 5.3.

## 2.4. Cloud deployment models

Platform-as-a-Service (PaaS) providers such as Render, Heroku, or Railway offer managed runtimes, automatic TLS termination, and attached PostgreSQL databases. Compared with manual VPS administration (Nginx, systemd, certificate renewal), PaaS reduces operational burden for a diploma prototype while still demonstrating **cloud hosting** and **HTTPS** [6].

I deployed DocBook on **Render** using Gunicorn as the WSGI server, PostgreSQL as the database, and environment variables for secrets. Static files are collected and served through **WhiteNoise**, avoiding a separate CDN for this project scale.

## 2.5. Selection of technologies

| Component | Choice | Justification |
|-----------|--------|---------------|
| Language | Python 3.12 | Mature ecosystem, readable code, university curriculum alignment |
| Framework | Django 5.0.6 | Built-in auth, ORM, admin, security middleware |
| Database (dev) | SQLite | Fast local development |
| Database (prod) | PostgreSQL | Reliable relational store on Render |
| WSGI server | Gunicorn 23.0.0 | Standard production server for Django |
| Frontend | Bootstrap, jQuery, HTMX | Responsive UI without separate SPA build |
| Rich text | django-ckeditor | Prescription and clinical notes |
| Static files | WhiteNoise | Simplified production static serving |

Alternative frameworks (Flask, FastAPI, Node.js) could implement similar features, but Django’s integrated user model, session auth, and migration system accelerated development within the thesis period.

### 3.2.3. Tools and Development Environment

| Tool | Purpose |
|------|---------|
| Python 3.12.8 | Runtime |
| Django 5.0.6 | Web framework |
| Git / GitHub | Version control |
| Visual Studio Code | Code editor |
| Git Bash | Commands and deploy |
| Render.com | Cloud hosting |
| PostgreSQL | Production database |
| Chrome | Testing and screenshots |
| Gunicorn + WhiteNoise | Production server and static files |

## 2.6. Database management systems

Relational databases remain the default for transactional systems with many-to-one and one-to-many relationships. PostgreSQL offers ACID compliance, constraints, and mature Django support [11]. SQLite is embedded and ideal for development. The same Django models migrate to PostgreSQL without code changes, which simplified the path from laptop development to Render production.

## 2.7. Related systems and positioning

Public hospital booking portals and private clinic apps share features with DocBook: doctor list, slot picker, confirmation email. DocBook differentiates itself in the thesis context by **full source availability**, explicit RBAC implementation documented in code, and a complete deployment narrative including `build.sh` automation. It is not claimed to compete with commercial HIS vendors; it demonstrates that a bachelor-level engineer can deliver a secure, deployable vertical slice.

## 2.8. Summary of technology decision

The selected stack—Python 3.12, Django 5.0.6, PostgreSQL, Gunicorn, WhiteNoise, Bootstrap, HTMX, Render—balances learning objectives, security features, and deployment feasibility. Each component has official documentation and community support, which reduced risk during the implementation phase described in Chapter 4.

## 2.9. Mapping OWASP Top 10 to DocBook controls

**Table 8** — OWASP risks and project mitigations

| Risk category | Description | DocBook mitigation |
|---------------|-------------|-------------------|
| A01 Broken access control | Users act outside role | RBAC mixins, object filters |
| A02 Cryptographic failures | Weak or missing crypto | PBKDF2 passwords, HTTPS, secure cookies |
| A03 Injection | SQL/command injection | Django ORM parameterisation |
| A04 Insecure design | Missing threat model | Requirements + RBAC design in Ch. 3 |
| A05 Security misconfiguration | DEBUG=True in prod | DEBUG=False on Render, env vars |
| A06 Vulnerable components | Old libraries | Pinned versions in requirements.txt |
| A07 Auth failures | Weak login | Session auth; future: rate limit |
| A08 Data integrity failures | Unsigned updates | CSRF tokens on POST |
| A09 Logging failures | No audit trail | Future work: audit log |
| A10 SSRF | Server-side fetch abuse | No user-controlled URL fetch feature |

This mapping was used as a checklist before final deployment.

## 2.10. Session versus token authentication

Token-based JWT authentication is popular in SPA applications. DocBook uses **server-side sessions** because Django supports them natively, revocation is immediate on logout, and tokens are not stored in browser localStorage where XSS impact is greater. For a future mobile app, a token API could be added with Django REST Framework and `SimpleJWT`, but that was outside thesis scope.

---

# 4. SYSTEM DESIGN AND ARCHITECTURE

## 4.1. Database Design

DocBook follows a **three-tier logical architecture**:

1. **Presentation tier:** HTML templates, Bootstrap CSS, client-side scripts (jQuery, HTMX).
2. **Application tier:** Django views, forms, mixins, decorators, and REST endpoints.
3. **Data tier:** relational database (SQLite locally, PostgreSQL in production).

Figure 1 illustrates the high-level flow: the web browser connects over HTTPS to Render’s edge router; Gunicorn serves the Django application (with WhiteNoise for static assets); the application reads and writes data in an isolated PostgreSQL database. *(Image file: `docbook_architecture.png` — regenerate with `generate_architecture.ps1`.)*

**Figure 1** — Cloud infrastructure architecture of DocBook (Browser → Render HTTPS edge → Gunicorn/Django/WhiteNoise ↔ PostgreSQL)

The Django project package is named `docbook`. Application modules are divided by responsibility:

- `core` — public site, specialities, reviews
- `accounts` — users, profiles, authentication, admin views
- `doctors` — doctor profiles, schedules, doctor-side appointments
- `patients` — patient dashboard and patient-side appointment actions
- `bookings` — booking creation, invoices, prescriptions

### 3.1.1. Request processing pipeline

Each HTTP request passes through middleware in order: security headers, WhiteNoise for static files, session, common, CSRF, authentication, messages, clickjacking protection. Only then does the URL resolver map the path to a view. Figure 3 shows the sequence. *(Insert Figure 3: request pipeline diagram.)*

**Figure 3** — Django middleware and view resolution pipeline

This ordering matters for security: authentication middleware must run before views that assume `request.user` is populated. CSRF must run before POST handlers accept form data.

### 3.1.2. Deployment view of architecture

In production, the browser connects to Render’s load balancer over TLS. Render forwards to a Gunicorn worker process running the Django application. PostgreSQL runs as a managed service. Static files are served from collected assets via WhiteNoise after `collectstatic` during build. Media uploads (avatars, speciality images) reside on the filesystem path configured in `MEDIA_ROOT` on the web instance.

## 4.1. Database Design (detailed model)

Relational modelling was chosen because appointments, users, and prescriptions have clear relationships and must satisfy integrity constraints. The entity-relationship view can be summarised as follows: one User has one Profile; one User in the doctor role receives many Bookings; one User in the patient role creates many Bookings; each Booking has at most one Prescription and at most one Review.

### 3.2.1. User and profile

The central entity is a custom **User** model extending Django’s `AbstractUser` with a `role` field (`doctor` or `patient`). A one-to-one **Profile** stores extended attributes: avatar, phone, address, specialisation text, consultation price, availability flag, and medical notes fields where applicable.

**Booking** links a doctor and a patient with `appointment_date`, `appointment_time`, `status`, and `booking_date`. A database-level `unique_together` constraint on `(doctor, appointment_date, appointment_time)` prevents duplicate slot reservation.

**Prescription** is a one-to-one extension of a booking with symptoms, diagnosis, medications (rich text), and notes.

**Speciality** (in `core`) represents medical departments for marketing and search. **Review** links patient, doctor, and booking with a 1–5 rating and text.

Doctor **availability** uses seven day models (Sunday–Saturday), each connected to the doctor user and a many-to-many set of **TimeRange** records (`start`, `end`, `slots_per_hour`).

Administrative access does not use a third role value; instead, users with `is_superuser=True` and `is_staff=True` access `/admin/` routes. This follows Django convention and separates platform operators from clinical roles.

### 3.2.2. Booking integrity

The uniqueness constraint on `(doctor, appointment_date, appointment_time)` is the primary defence against double booking. At the application layer, the booking view re-queries existing appointments before insert so that race conditions are minimised. Status values are stored as short string codes in the database, which keeps reporting queries simple.

### 3.2.3. Scheduling model

Each doctor owns seven day-configuration records. Each record references multiple time ranges. A time range defines start and end times and how many slots per hour are offered. The booking UI derives discrete slot times from these ranges and removes slots that already have a booking. This design is more flexible than a single “opening hours” string because different days can have different patterns (for example shorter hours on Saturday).

### 3.2.4. Entity attributes (summary tables)

**Table 2** — Main entities and key attributes

| Entity | Key attributes | Relationships |
|--------|----------------|---------------|
| User | username, role, email, password hash | 1:1 Profile; M bookings as doctor or patient |
| Profile | phone, avatar, specialization, price | 1:1 User |
| Booking | date, time, status | FK doctor, FK patient; 1:1 Prescription optional |
| Prescription | symptoms, diagnosis, medications | FK booking, doctor, patient |
| Review | rating 1–5, text | FK patient, doctor, booking |
| Speciality | name, slug, image | Referenced in search and admin |
| TimeRange | start, end, slots_per_hour | M2M with day schedule models |

Figure 4 presents the entity-relationship diagram (file `docbook_erd.png` in the project folder; regenerate with `generate_erd.ps1` or `python manage.py graph_models accounts bookings core -g -o docbook_erd.png` after installing Graphviz).

**Figure 4** — Entity-relationship diagram of DocBook core entities (`User`, `Profile`, `Booking`, `Prescription`, `Review`, `Speciality`)

### 3.2.5. Normalisation

The schema is in third normal form for core entities: non-key attributes depend only on the primary key. Booking stores foreign keys to doctor and patient rather than duplicating names. Profile stores display fields separately from authentication fields on User, avoiding unnecessary coupling to Django’s auth table structure while still using one login identity.

## 4.2. Backend Design

Role-based access control, URL routing, and server-side logic are implemented in Django views, mixins, and decorators. The following subsection documents RBAC; middleware and routes are covered in Chapter 5.2.

## 4.2.1. Role-based access control design

RBAC is enforced through **mixins** on class-based views:

- `PatientRequiredMixin` — allows only `role == patient`; others are redirected.
- `DoctorRequiredMixin` — allows only `role == doctor`.
- `AdminRequiredMixin` — allows only `is_superuser`.

The `user_is_doctor` decorator raises `PermissionDenied` for function-based views. Combined with `LoginRequiredMixin`, every protected endpoint checks authentication first, then role.

Object-level rules supplement role checks. For example, invoice and cancel views verify that the logged-in user is the booking’s patient or assigned doctor. This defence-in-depth limits horizontal privilege escalation.

### 3.3.1. Access matrix

**Table 3** — Role access matrix (simplified)

| Function | Patient | Doctor | Admin (superuser) |
|----------|---------|--------|-------------------|
| Public home / doctor list | Yes | Yes | Yes |
| Patient dashboard | Yes | No | No |
| Doctor dashboard | No | Yes | No |
| Book appointment | Yes | No | No |
| Set schedule | No | Yes | No |
| Custom /admin/ reports | No | No | Yes |
| Django /super-admin/ | No | No | Yes (staff) |

### 3.3.2. Redirect behaviour

Unauthorized role access does not always show HTTP 403. Patient and doctor mixins typically redirect to the public home page to avoid leaking whether a URL exists. Doctor-only function views use `PermissionDenied` (403) in some paths. Admin mixin redirects non-superusers away from `/admin/`. This behaviour was verified in Chapter 5.

## 4.3. Frontend Design

### 4.3.1. Django Templates and Bootstrap

The public home page highlights doctor search by city and specialisation. Patients see a dashboard with upcoming and past appointments. Doctors see statistics, today’s schedule, and quick links to appointments and patients. Administrators see aggregate counts and Chart.js graphs on the custom admin dashboard.

Templates extend a common base layout for consistent navigation. Currency is displayed in Nigerian Naira (₦) as defined in project settings. The design prioritises clarity for demonstration and thesis evaluation rather than commercial branding.

### 4.3.1. Navigation structure

Public navigation exposes Home, Doctors, and patient registration/login. Logged-in patients see dashboard and logout. Doctors see dashboard, appointments, schedule, and profile settings. Administrators who log in with the admin account land on the analytics dashboard with sidebar links to patients, doctors, appointments, specialities, prescriptions, reviews, and two report types.

### 3.4.2. Responsive layout

Bootstrap grid ensures pages remain usable on tablet-width screens for demonstration. The thesis demonstration primarily used desktop browsers; mobile-specific native apps were out of scope.

### 3.4.3. Figures for user interface

Figures 5–10 (see Appendix C) show the home page, login form, patient dashboard, doctor schedule screen, booking confirmation, and admin dashboard. Each figure is referenced in the evaluation chapter to prove the interface exists on the deployed system.

## 3.5. Security design

Security decisions are centralised in `docbook/settings.py`:

- `SecurityMiddleware`, `CsrfViewMiddleware`, `XFrameOptionsMiddleware`
- Session-based authentication after `authenticate()`
- `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, `DATABASE_URL`, `CSRF_TRUSTED_ORIGINS` from environment
- When `DEBUG=False`: `SECURE_SSL_REDIRECT`, secure session and CSRF cookies, HSTS for one year

Passwords are never logged. The `.env` file is excluded from version control via `.gitignore`.

### 3.5.1. Password storage

Django’s default hasher applies PBKDF2 with SHA256. When a user submits a password at login, the framework hashes the input and compares it to the stored digest. The number of iterations is configured by Django and increases over framework versions to resist brute-force attacks [5]. Equation (1) expresses the general hashing concept:

*H* = *Hash*(*password*, *salt*, *iterations*)  (1)

where *H* is the stored digest. Plain passwords are never written to the database or logs.

### 3.5.2. Session management

After successful authentication, Django stores the user identifier in an encrypted session cookie. Subsequent requests pass through `AuthenticationMiddleware`, which attaches `request.user` to the request. Logout clears the session. In production, `SESSION_COOKIE_SECURE` ensures the cookie is sent only over HTTPS.

### 3.5.3. HTTPS and HSTS

When `DEBUG=False`, Django redirects HTTP to HTTPS via `SECURE_SSL_REDIRECT`. HSTS headers instruct browsers to remember HTTPS for one year. Render terminates TLS at the edge; `SECURE_PROXY_SSL_HEADER` informs Django that the original request was secure. Figure 11 shows the browser address bar with `https://` on the production host.

**Figure 11** — HTTPS on production URL (screenshot)

### 3.5.4. Environment and secrets

`SECRET_KEY` signs sessions and CSRF tokens. It must remain secret. `ALLOWED_HOSTS` prevents host header attacks. `CSRF_TRUSTED_ORIGINS` lists full origins for POST from the public HTTPS URL. These variables are configured in the Render dashboard, not committed to Git.

## 4.4. Use Case Diagrams

*(Insert Figure: use case diagram with actors Patient, Doctor, Administrator and use cases Book Appointment, Confirm Appointment, Manage Schedule, View Reports. Draw in Word, Visio, or draw.io.)*

The textual use cases in Section 3.1.5 map to this diagram: patient books; doctor confirms; administrator views reports.

## 4.5. Wireframes and Interface Screens

*(Insert Figures 5–10 from Appendix 9.3: home page, login, dashboards, booking flow. These serve as wireframe/screenshot evidence of the UI.)*

## 4.6. Design of appointment state machine

States and allowed transitions are summarised in Table 4.

**Table 4** — Appointment status transitions

| From state | Action | To state | Who |
|------------|--------|----------|-----|
| pending | confirm | confirmed | doctor |
| pending | cancel | cancelled | doctor or patient |
| confirmed | complete | completed | doctor |
| confirmed | cancel | cancelled | doctor or patient |
| confirmed | mark no-show | no_show | doctor |
| completed | — | (terminal) | — |

Reviews are allowed only after completion. Prescriptions are created by the doctor typically after or during the confirmed/completed phase depending on clinic policy; DocBook links prescription to booking one-to-one.

---

# 5. IMPLEMENTATION

## 5.1. Django Stack Development

### 5.1.1. Backend Setup

## 5.1.1. Development environment (backend)

Development was carried out on a Windows workstation with Python 3.12, a virtual environment, and Git for version control. The following commands establish a local instance:

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata fixtures/initial_data.json
python create_admin.py
python manage.py runserver
```

The application is available at `http://127.0.0.1:8000/`. Demo accounts use password `aaa` as documented in `LOGIN_CREDENTIALS.md` (for academic demonstration only).

### 4.1.1. Hardware and software environment

| Component | Specification |
|-----------|---------------|
| Development OS | Microsoft Windows 11 |
| Processor | Standard x64 laptop (sufficient for Django dev server) |
| RAM | 8 GB or higher recommended |
| Python | 3.12.8 |
| IDE | Visual Studio Code / Cursor for editing; Git Bash for commands |
| Browser | Google Chrome for testing and screenshots |
| Production host | Render.com free tier web service + PostgreSQL |

### 4.1.2. Project phases and timeline

Work proceeded in six phases: (1) requirements and literature study; (2) data model and URL design; (3) patient and doctor modules; (4) booking and prescriptions; (5) admin dashboard and reports; (6) production deployment and testing. Each phase produced a testable increment. Version control commits marked the end of phases when features worked locally.

## 4.2. Core modules

### Accounts and authentication

Login uses `UserLoginForm` and Django’s `authenticate()` function. On success, the session is created and the user is redirected according to role: patients to the patient dashboard, doctors to the doctor dashboard, superusers to the admin dashboard. Registration flows exist separately for doctors and patients with role assignment at creation time.

A `post_save` signal automatically creates an empty **Profile** when a **User** is created, avoiding orphaned accounts without profile data.

### Doctor module

Doctors manage weekly schedules through `/doctors/schedule-timings/`. Time ranges define bookable slots; the booking view calculates availability by excluding already reserved times. Education and experience records are stored in separate models and exposed through APIs for dynamic form updates.

### Patient module

Patients book via `/bookings/doctor/<username>` and confirm on the success page. They may cancel pending or confirmed appointments, print summaries, and submit a review after completion.

### Bookings and prescriptions

Creating a booking validates slot availability, assigns `pending` status, and relies on the doctor to confirm. Prescriptions use CKEditor for formatted medication instructions. Only the treating doctor may create a prescription for a given booking.

### 4.2.1. URL routing summary

**Table 5** — Main URL groups by role

| Prefix | Role | Examples |
|--------|------|----------|
| `/` | Public | home, terms, privacy |
| `/accounts/` | Auth | login, register, logout |
| `/doctors/` | Doctor + public list | list, profile, dashboard, schedule |
| `/patients/` | Patient | dashboard, cancel, review |
| `/bookings/` | Patient/doctor | create, success, invoice, list |
| `/admin/` | Superuser | dashboard, reports, specialities |
| `/super-admin/` | Staff | Django admin tables |

### 4.2.2. Fixtures and demo data

File `fixtures/initial_data.json` loads fifteen demo doctors and fifteen demo patients with hashed passwords. Script `seed_demo_bookings.py` creates sample appointments so dashboards are not empty during examination. Script `create_admin.py` ensures the `admin` superuser exists after every deploy. This automation was essential because Render free tier does not provide shell access for manual `loaddata` after deployment.

### 4.2.3. Core public module

The `core` application serves the marketing home page with doctor search filters. Model `Speciality` categorises doctors for browsing. Model `Review` stores patient feedback linked to completed bookings. Context processor `project_settings` injects project name and currency into every template so branding stays consistent.

## 4.3. Appointment workflow

The appointment lifecycle is implemented as a finite set of statuses:

1. **Pending** — patient has requested a slot.
2. **Confirmed** — doctor accepted the appointment.
3. **Completed** — visit finished; review allowed.
4. **Cancelled** — terminated by patient or doctor.
5. **No_show** — patient did not attend.

State transitions are triggered from doctor appointment actions (`accept`, `cancel`, `complete`). This workflow was chosen because it matches common clinic practice and is easy to explain during demonstration.

## 4.4. Administrative features

The custom admin area at `/admin/` provides:

- Dashboard with statistics
- Patient and doctor lists
- Global appointment list
- Speciality CRUD (create, update, delete)
- Prescription and review oversight
- Appointment and revenue reports

Django’s built-in admin at `/super-admin/` remains available for low-level database maintenance on the User and Profile tables.

## 4.5. Challenges during development

Several practical issues arose during implementation:

1. **Template inheritance order** — Django requires `{% extends %}` as the first tag. Some dashboard templates incorrectly placed `{% load %}` before `{% extends %}`, causing template errors that were resolved by reordering tags.

2. **Admin account configuration** — The `admin` user must have `is_superuser` and `is_staff` set. A dedicated script `create_admin.py` idempotently creates or upgrades this account on each deployment.

3. **PostgreSQL on Render** — Render sometimes supplies `postgres://` URLs while Django expects `postgresql://`. The `build.sh` script normalises the URL before migrations.

4. **Static files and Pillow** — Image fields and CKEditor require Pillow in `requirements.txt`; missing dependencies caused build failures until explicitly declared.

5. **Production CSRF** — HTTPS deployment requires `CSRF_TRUSTED_ORIGINS` to include the full public origin; otherwise login POST requests fail with forbidden errors.

These problems were solved iteratively; the final build pipeline runs migrations, collects static files, loads fixtures, creates the admin user, and seeds sample bookings automatically.

## 4.6. Version control and repository

Source code is maintained in a Git repository hosted on GitHub under the project name `healthcare-appointment-system`. Commits document major milestones: initial system import, production configuration for Render, and deployment automation in `build.sh`. Branching follows a simple `main` workflow suitable for a single-developer thesis project.

## 4.7. Key implementation patterns

**Class-based views** dominate the application because they compose cleanly with mixins. For example, `PatientDashboardView` inherits `LoginRequiredMixin` and `PatientRequiredMixin` before `TemplateView`, so authentication and role checks run before any template rendering.

**Signals** decouple profile creation from registration views: whenever a `User` is saved, the receiver creates a `Profile` if missing. This avoids duplicate profile-creation code in multiple registration paths.

**HTMX and DRF** are used where partial page updates improve usability—doctor education and experience forms—while the majority of pages remain full server renders for simplicity and accessibility.

## 4.8. Administrative reports implementation

`AppointmentReportView` aggregates bookings by status and date range for management overview. `RevenueReportView` uses consultation prices from doctor profiles multiplied by completed appointments to approximate income. These reports use Django ORM aggregation functions (`Count`, `Sum`) rather than raw SQL, keeping code portable across SQLite and PostgreSQL.

Charts on the admin dashboard use Chart.js fed by context data prepared in `AdminDashboardView`. The visual presentation supports thesis demonstration of “administrator interface” requirements.

## 4.9. Third-party packages

| Package | Version (requirements) | Role |
|---------|------------------------|------|
| Django | 5.0.6 | Framework |
| djangorestframework | 3.15.1 | Profile APIs |
| django-ckeditor | 6.7.2 | Prescription editor |
| gunicorn | 23.0.0 | Production server |
| whitenoise | latest | Static files |
| psycopg2-binary | 2.9.9 | PostgreSQL driver |
| dj-database-url | 3.x | Parse DATABASE_URL |
| Pillow | 10.3.0 | Image fields |

## 4.12. Detailed walkthrough by module

### 4.11.1. Accounts application

The accounts application defines the custom user model. Extending `AbstractUser` rather than using a profile-only approach ensures Django’s authentication framework recognises DocBook users everywhere. The `role` field uses `TextChoices` for clarity in code and admin. Registration views validate form input, hash passwords through `set_password`, and save the user. Login view validates credentials and calls `login()` to bind the session. Logout flushes the session. Admin views in `accounts.views.admin_views` are large class-based views that prepare querysets and chart data; they are kept in a separate module from patient-facing auth to maintain readability.

### 4.11.2. Doctors application

Public doctor list view filters queryset by search parameters from GET request. Profile view shows doctor biography, education queryset, experience queryset, and average rating derived from reviews. Dashboard view counts today’s appointments, pending count, and completed count using ORM filters on `Booking`. Schedule view loads seven day models; POST requests update many-to-many time ranges. Appointment action view maps URL action parameter to status transition functions with permission check that `booking.doctor == request.user`.

### 4.11.3. Patients application

Dashboard lists upcoming appointments ordered by date. Cancel view allows cancel only when status permits and patient owns booking. Review view ensures booking is completed and patient has not already reviewed. Print view renders a simplified template suitable for printing. Profile settings view updates `Profile` fields and optionally avatar image file.

### 4.11.4. Bookings application

Slot selection view computes available times by iterating doctor’s day configuration for weekday of selected date, generating slot list, subtracting booked times. Create booking view uses POST, validates CSRF, creates `Booking` with pending status. Invoice view checks ownership. List view shows different template context depending on whether user is patient or doctor, filtering queryset accordingly.

### 4.11.5. Templates and static assets

Templates live under `templates/` with subfolders per app. Base template loads Bootstrap CSS, project CSS, jQuery, HTMX, and block sections for content and scripts. Dashboard templates share sidebar partial for admin. Static images for doctors and specialities live under `static/assets/`. After `collectstatic`, files are copied to `staticfiles/` for production. WhiteNoise serves them without configuring Nginx manually on Render.

## 4.10. Data migration strategy

Django migrations version the schema. Initial migrations for each app create tables. Later migrations alter fields—for example year fields on doctor education. On deploy, `migrate --noinput` applies pending migrations in order. Fixtures load after schema is current. This ordering prevents load failures when fixture references tables that do not yet exist.

## 4.11. Experiences during realisation

Early in development I underestimated template inheritance rules and spent time debugging `TemplateSyntaxError` on dashboard pages. Mid-project, deployment failed on Render until Python version was pinned to 3.12.8 and Pillow was added. Late in the project, production login failed until `CSRF_TRUSTED_ORIGINS` matched the exact HTTPS origin. Each issue taught a concrete lesson about framework conventions and cloud configuration. Documenting these experiences satisfies the faculty expectation that the thesis describes “phases, experiences, problems during the work.”

---

# 6. TESTING AND FEEDBACK

## 6.1. Test strategy

Testing combined **automated unit and integration tests** with **manual functional verification** on the deployed system. Automated tests use Django’s `TestCase` and Selenium end-to-end tests for registration, login, booking, and doctor workflows. Manual tests covered RBAC, HTTPS behaviour, and cloud login with demo accounts.

### 5.1.1. Test levels

| Level | Goal | Tools |
|-------|------|-------|
| Unit | Models, auth logic | Django TestCase |
| Integration | Views, forms | Django client, TestCase |
| System / E2E | Full browser flows | Selenium WebDriver |
| Acceptance | Requirements met | Manual scripts on production URL |

### 5.1.2. Test environment

Local tests used SQLite and `DEBUG=True`. Production acceptance tests used `https://healthcare-appointment-system-9a2r.onrender.com` with demo accounts. Separating environments validated that configuration—not only code—was correct.

## 5.2. Functional tests

| Test area | Method | Result |
|-----------|--------|--------|
| User registration (patient/doctor) | Selenium e2e | Pass |
| Login and logout | Unit + manual | Pass |
| Book appointment | Selenium e2e | Pass |
| Doctor schedule update | Manual | Pass |
| Admin dashboard access | Manual | Pass |
| Double booking prevention | Model constraint + manual | Pass |

Running automated tests locally:

```bash
python manage.py test tests
```

## 5.3. Security verification

| Control | Verification |
|---------|----------------|
| Password hashing | Database stores `pbkdf2_sha256$...` strings, not plain passwords |
| CSRF | Login and booking forms include `csrfmiddlewaretoken` |
| RBAC | Patient URL accessed as doctor returns HTTP 403 |
| HTTPS (production) | Live URL uses `https://`; settings enable SSL redirect when `DEBUG=False` |
| Session cookies | `SESSION_COOKIE_SECURE=True` in production |

Wrong passwords are rejected with a generic error message without revealing whether the username exists, which is good practice.

### 5.3.1. Role-based access tests (manual)

The following manual tests were executed on the production deployment:

| Step | Action | Expected | Observed |
|------|--------|----------|----------|
| 1 | Log in as `patient1` | Patient dashboard | Pass |
| 2 | Navigate to `/doctors/dashboard/` | Access denied (403) | Pass |
| 3 | Navigate to `/admin/` | Redirect or not authorised | Pass |
| 4 | Log in as `doctor1` | Doctor dashboard | Pass |
| 5 | Navigate to `/patients/dashboard/` | Access denied (403) | Pass |
| 6 | Log in as `admin` | Admin dashboard | Pass |

These results confirm that RBAC is enforced on the live system, not only locally.

### 5.3.2. Encrypted login verification

Inspecting the database (via Django shell on production after deployment) shows password fields beginning with `pbkdf2_sha256$`, confirming one-way hashing. Attempting login with password `aaa` succeeds for demo users; attempting `wrongpassword` fails without exposing internal errors.

## 5.4. Evaluation of results

The implemented system meets the functional and non-functional requirements defined in Section 1.4. Patients can complete the booking path end-to-end; doctors can manage schedules and appointments; administrators can view reports. Cloud deployment demonstrates that the application is not limited to localhost.

**Limitations:** password policy is minimal (only similarity validator enabled); the demo password `aaa` must be changed in a real deployment; automated test coverage is concentrated on auth and booking rather than every admin report edge case.

**Further development** could add email notifications, SMS reminders, two-factor authentication, payment integration, and FHIR-compatible APIs for hospital integration.

### 5.4.1. Requirement satisfaction summary

**Table 6** — Requirements vs outcome

| ID | Requirement | Result |
|----|-------------|--------|
| FR-1 | Public pages and search | Satisfied |
| FR-2 | Patient booking | Satisfied |
| FR-3 | Doctor schedule and actions | Satisfied |
| FR-4 | Admin dashboard | Satisfied |
| FR-5 | No double booking | Satisfied |
| FR-6 | Status workflow | Satisfied |
| NFR-1 | Password hashing | Satisfied |
| NFR-2 | CSRF | Satisfied |
| NFR-3 | HTTPS production | Satisfied |
| NFR-4 | Django 5 / Python 3.12 | Satisfied |
| NFR-5 | Env configuration | Satisfied |
| NFR-6 | Static serving | Satisfied |

### 5.4.2. Performance observations

On Render free tier, the first request after idle period may take 30–60 seconds while the service wakes. Subsequent pages load within a few seconds. This is acceptable for thesis demonstration but would require paid instances for clinical production use.

### 5.4.3. Usability observations

Test users (classmates) could book an appointment without written instructions after a two-minute verbal explanation. Doctor schedule setup required more guidance, which suggests future work on usability testing and inline help tooltips.

## 5.5. Detailed test cases (manual)

**Table 7** — Selected manual test cases

| TC-ID | Description | Steps | Expected | Result |
|-------|-------------|-------|----------|--------|
| TC-01 | Patient login | Open /accounts/login/, enter patient1/aaa | Dashboard | Pass |
| TC-02 | Invalid password | Wrong password | Error message | Pass |
| TC-03 | Doctor list | Open /doctors/ | List visible | Pass |
| TC-04 | Create booking | Select slot, submit | Pending booking | Pass |
| TC-05 | Doctor confirm | Doctor confirms | Status confirmed | Pass |
| TC-06 | Cancel booking | Patient cancels | Status cancelled | Pass |
| TC-07 | Admin report | Open appointment report | Table/chart | Pass |
| TC-08 | CSRF present | View page source on login form | csrf token | Pass |
| TC-09 | HTTPS redirect | Open http URL on prod | Redirect https | Pass |
| TC-10 | RBAC patient→doctor | Patient opens doctor dashboard | 403/redirect | Pass |

Figure 12 shows the forbidden response for TC-10. *(Insert screenshot.)*

**Figure 12** — Access denied when patient attempts doctor URL

## 5.6. Automated test suite description

The `tests` package organises automated quality assurance. `tests/auth/test_views.py` verifies that login with valid credentials returns redirect to home or role dashboard, that invalid password returns 200 with form errors, and that logout clears session. `tests/auth/test_models.py` verifies user creation, profile signal, and doctor-specific properties. These tests run quickly without browser and suit continuous integration.

End-to-end tests in `tests/e2e/` use Selenium WebDriver to drive Chrome. `test_auth.py` opens the live test server provided by `LiveServerTestCase`, navigates to registration forms, submits data, and asserts page content. `test_booking.py` walks through doctor search and booking button clicks. `test_doctors.py` verifies doctor list page title and dashboard accessibility after login.

Selenium tests are slower and flakier than unit tests but provide confidence that templates and JavaScript integrate correctly. Failures during development often indicated missing static files or changed CSS selectors rather than business logic errors. For thesis documentation, the important point is that both automated and manual methods were applied, not that every line achieved 100% code coverage.

## 5.7. Test data and repeatability

Fixtures ensure repeatable tests: each run starts from known users doctor1 and patient1. `seed_demo_bookings.py` adds appointments so doctor dashboard tests have rows to display. Without seed data, tests would pass vacuously on empty lists while hiding integration bugs. Repeatability also helps examiners: they can log in with the same credentials documented in Appendix A.

## 5.8. Security test narrative

I performed a structured security walkthrough separate from functional tests. Step one: confirm HTTPS redirect. Step two: view page source on login for CSRF token. Step three: attempt CSRF POST without token using curl—request rejected. Step four: log in as patient, copy doctor dashboard URL, paste in same browser—access denied. Step five: open Django shell on local copy, print `user.password` field—observe hash prefix pbkdf2_sha256. Step six: verify DEBUG is false on production by confirming custom error pages do not leak stack traces. These steps map directly to non-functional requirements NFR-1 through NFR-3.

---

## 5.6. Cloud Deployment on Render

## 5.6.1. Deployment architecture

Production deployment uses **Render** as PaaS host:

- **Web service:** Python 3.12, build command `bash build.sh`, start command `gunicorn docbook.wsgi:application --bind 0.0.0.0:$PORT`
- **Database:** Render PostgreSQL instance connected via `DATABASE_URL`
- **TLS:** terminated at Render edge; Django trusts `HTTP_X_FORWARDED_PROTO`

**Live URL:** `https://healthcare-appointment-system-9a2r.onrender.com`

Root directory on Render points to the inner folder `secure-cloud-based-healthcare-appointment-system` where `manage.py` resides.

## 6.2. Production configuration

Required environment variables:

| Variable | Purpose |
|----------|---------|
| `SECRET_KEY` | Cryptographic signing |
| `DEBUG=False` | Enables production security settings |
| `ALLOWED_HOSTS` | Public hostname |
| `DATABASE_URL` | PostgreSQL connection |
| `CSRF_TRUSTED_ORIGINS` | HTTPS origin for forms |

The `build.sh` script installs dependencies, runs `collectstatic` and `migrate`, loads `fixtures/initial_data.json`, runs `create_admin.py`, and seeds demo bookings.

## 6.3. Operational results

After deployment, the home page and login page respond over HTTPS. Demo users (`patient1`, `doctor1`, `admin` with password `aaa`) authenticate successfully. Free-tier hosting may cold-start after inactivity; this is acceptable for academic demonstration.

Figure 2 shows the patient home view after login. *(Insert screenshot in Appendix C.)*

**Figure 2** — DocBook home page after patient login (production deployment)

## 6.4. Step-by-step Render deployment

The following steps were performed to deploy DocBook:

1. Create a Render account and connect GitHub repository `healthcare-appointment-system`.
2. Create a new **Web Service**; select Python environment.
3. Set **Root Directory** to `secure-cloud-based-healthcare-appointment-system` (folder containing `manage.py`).
4. Set **Build Command** to `bash build.sh`.
5. Set **Start Command** to `gunicorn docbook.wsgi:application --bind 0.0.0.0:$PORT`.
6. Create PostgreSQL database on Render; copy **Internal Database URL** into web service environment as `DATABASE_URL`.
7. Set `SECRET_KEY` to a long random string generated offline.
8. Set `DEBUG=False`, `ALLOWED_HOSTS` to the assigned `*.onrender.com` hostname, `CSRF_TRUSTED_ORIGINS` to `https://<hostname>`.
9. Set `PYTHON_VERSION=3.12.8` or rely on `runtime.txt`.
10. Deploy; monitor build log for `collectstatic`, `migrate`, and fixture loading.
11. Open public URL and test login with demo accounts.

Figure 13 shows a successful deploy status in Render Events. *(Insert screenshot if available.)*

**Figure 13** — Render deployment events (optional screenshot)

## 6.5. Build script behaviour

The `build.sh` script performs reproducible steps: print Python version, install `psycopg2-binary`, install requirements, normalise database URL, collect static files, apply migrations, load fixtures, run `create_admin.py`, run `seed_demo_bookings.py`. Failures on non-critical seed steps use `|| true` so a redeploy does not abort if data already exists.

## 6.6. Maintenance and monitoring

For ongoing operation, logs are available in the Render dashboard. Database backups on paid tiers protect against data loss. For thesis purposes, the free database tier is sufficient. Code updates push via Git to `main`; Render rebuilds automatically.

## 6.7. Comparison: local vs cloud

| Aspect | Local | Cloud (Render) |
|--------|-------|----------------|
| Database | SQLite file | PostgreSQL managed |
| HTTPS | Usually HTTP only | TLS enabled |
| DEBUG | True | False |
| Cold start | None | Possible on free tier |
| Public access | localhost only | Worldwide URL |

## 6.8. Deployment problems and resolutions

During cloud deployment several errors occurred; documenting them supports the “experiences during the work” requirement.

**Problem A — Build failed on psycopg2.** Initial Render default Python was too new for some binary wheels. **Resolution:** pin `python-3.12.8` in `runtime.txt` and set `PYTHON_VERSION` on Render.

**Problem B — Build failed on Pillow.** ImageField and CKEditor require Pillow. **Resolution:** uncomment `Pillow==10.3.0` in `requirements.txt`.

**Problem C — Login returned 403 Forbidden on production.** CSRF check failed because origin was not trusted. **Resolution:** set `CSRF_TRUSTED_ORIGINS=https://healthcare-appointment-system-9a2r.onrender.com` exactly.

**Problem D — ALLOWED_HOSTS error.** Host header did not match when using wrong subdomain. **Resolution:** copy exact hostname from Render dashboard into `ALLOWED_HOSTS`.

**Problem E — Empty database on first visit.** Fixtures did not run when build aborted early. **Resolution:** fix build script; add `loaddata` and seed scripts with `|| true` for redeploy.

**Problem F — Could not load data from home PC.** Internal `DATABASE_URL` hostname is not reachable outside Render network. **Resolution:** rely on build-time seeding instead of manual loaddata from laptop.

Each resolution is recorded in commit messages and deployment notes for reproducibility.

## 6.9. Further deployment options

`DEPLOYMENT.md` in the project describes alternative hosting on a Linux VPS with Nginx and Let’s Encrypt. That path offers more control but more administration. Render was chosen for the thesis demonstration because it satisfies the cloud and HTTPS requirements with minimal DevOps overhead.

---

# 7. CONCLUSION AND FUTURE DEVELOPMENT

## 7.1. Conclusion

## 7.1.1. Critical analysis of the solution

DocBook successfully demonstrates that a single developer can deliver a multi-role healthcare web application with modern security defaults and public cloud hosting. Strengths include clear separation of Django applications, explicit RBAC mixins, reproducible deployment script, and a complete appointment lifecycle. The system is understandable to examiners because they can register, log in, and follow a realistic path from search to booking to doctor confirmation without reading source code.

Weaknesses must also be stated honestly. Password policy is weak for production: all demo accounts share password `aaa`. There is no email verification on registration, no password reset flow, and no audit log of who changed appointment status. File uploads for avatars are not virus-scanned. Rate limiting on login is not implemented, so brute-force attempts are only indirectly limited by hosting provider. These gaps are acceptable in academic scope but would block a security review for a real hospital.

Scalability on Render free tier is limited: one Gunicorn worker and cold starts after idle time. Horizontal scaling would require paid plans and shared media storage (S3-compatible object store) if multiple instances are used. The database schema is normalised enough for thousands of bookings but indexes on `(doctor, appointment_date)` were not explicitly added beyond the uniqueness constraint; heavy load would benefit from index tuning and query profiling.

## 7.2. Comparison with thesis objectives

Objective one—analyse requirements—was met through Sections 1.4–1.7 and the traceability matrix in Appendix D. Objective two—implement RBAC scheduling—was met through Chapters 3–4 and demonstrated URLs. Objective three—encrypted logins—was met via Django hashers and Chapter 5.3 verification. Objective four—cloud HTTPS deployment—was met via Chapter 6 and the public URL. No objective was partially dropped; scope exclusions (payments, telemedicine) were deliberate.

## 7.3. Legal and ethical considerations

Processing health-related data carries ethical responsibility. DocBook uses fictional Nigerian-style demo names and example.com emails in fixtures; no real patient data were imported. For a real clinic, informed consent, retention policy, and right to erasure would apply under GDPR. The privacy page template provides a starting point but is not legal advice. Engineers must work with legal officers before production use.

## 7.2. Future Development

## 7.2.1. Future development roadmap

**Short term (1–3 months):** implement password reset via email; enforce minimum password length; add `django-axes` or similar rate limiting; remove shared demo password from production builds.

**Medium term (3–6 months):** SMS or email reminders 24 hours before appointment; calendar export (iCal); waiting list when slots are full; improved mobile CSS.

**Long term (6–12 months):** payment gateway for consultation fees; FHIR Appointment resource API [14]; integration with national ID; optional two-factor authentication for doctors and admins; Kubernetes deployment instead of single PaaS instance.

## 7.5. Lessons learned

The most important lesson is that framework conventions exist for a reason: template order, CSRF origins, and database URL formats caused more delay than algorithm design. Second, security features must be enabled in production settings (`DEBUG=False`) early, not only at the end, because behaviour differs materially from local development. Third, automated seed scripts are essential when the hosting provider does not offer post-deploy shell access. These lessons transfer directly to industry internships and junior developer roles.

## 7.6. Application in practice

A small private clinic could pilot DocBook by deploying to Render with strong passwords, training reception to use admin reports, and asking doctors to maintain schedules weekly. Larger hospitals would treat DocBook as a prototype rather than a certified medical device. Regulatory classification of software as a medical device varies by jurisdiction and feature set; appointment booking alone is often lower risk than diagnostic decision support, but legal advice remains necessary.

---

## 7.1.2. Summary of results

This diploma thesis presented the design, implementation, testing, and deployment of **DocBook**, a secure cloud-based healthcare appointment management system. The work addressed the need for a structured web platform where patients, doctors, and administrators interact through role-appropriate interfaces while appointment data remain consistent and protected.

The main results are:

1. A **Django 5** application with modular apps for accounts, doctors, patients, bookings, and core public content.
2. **Role-based access control** using mixins and decorators, plus object-level checks on sensitive operations.
3. **Secure authentication** with PBKDF2 password hashing, CSRF protection, and production HTTPS settings.
4. A complete **appointment workflow** from booking through confirmation to completion, cancellation, or no-show.
5. **Administrative reporting** and speciality management.
6. Successful **cloud deployment** on Render with PostgreSQL and Gunicorn.

The project objectives stated at the beginning were fulfilled. The system is suitable for demonstration in the final examination and as a foundation for future extensions such as notifications, payments, and standards-based health data exchange.

From a learning perspective, the diploma work strengthened skills in relational modelling, Django best practices, security configuration, and cloud deployment. The written documentation and the live URL together provide evidence that the product exists and operates according to specification. I consider the work complete relative to the approved task description from the Faculty of Engineering and Information Technology.

The thesis document itself accompanies the software artefact. Together they form the full diploma submission: theory and practice linked by consistent terminology (DocBook, RBAC, HTTPS, PostgreSQL). I recommend examiners begin with the live demonstration, then review Chapters 3–5 for design and test evidence, and finally the appendices for operational detail.

---

# 8. REFERENCES

[1] World Health Organization: *Digital health*. https://www.who.int/health-topics/digital-health (last visited: 2026-05-27)

[2] Häyrinen, K.; Lammintakanen, J.; Kinnunen, J.: Patients’ willingness to use online services in healthcare. *International Journal of Medical Informatics*, 2016.

[3] Django Software Foundation: *Django documentation — Design philosophies*. https://docs.djangoproject.com/en/5.0/misc/design-philosophies/ (last visited: 2026-05-27)

[4] OWASP Foundation: *OWASP Top Ten*. https://owasp.org/www-project-top-ten/ (last visited: 2026-05-27)

[5] Django Software Foundation: *Django security*. https://docs.djangoproject.com/en/5.0/topics/security/ (last visited: 2026-05-27)

[6] Render, Inc.: *Deploying Django*. https://render.com/docs/deploy-django (last visited: 2026-05-27)

[7] Fielding, R. T.: *Architectural Styles and the Design of Network-based Software Architectures*. University of California, Irvine, 2000. (REST architectural principles)

[8] Gamma, E.; Helm, R.; Johnson, R.; Vlissides, J.: *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley, 1994.

[9] Fowler, M.: *Patterns of Enterprise Application Architecture*. Addison-Wesley, 2002.

[10] NIST: *Digital Identity Guidelines*. Special Publication 800-63B. https://pages.nist.gov/800-63-3/ (last visited: 2026-05-27)

[11] PostgreSQL Global Development Group: *PostgreSQL documentation*. https://www.postgresql.org/docs/ (last visited: 2026-05-27)

[12] Mozilla Developer Network: *HTTP — Overview of HTTP*. https://developer.mozilla.org/en-US/docs/Web/HTTP (last visited: 2026-05-27)

[13] University of Pécs, Faculty of Engineering and Information Technology: *Diploma thesis formal requirements*, 2026.

[14] HL7 International: *FHIR Overview*. https://www.hl7.org/fhir/overview.html (last visited: 2026-05-27)

[15] Mozilla Developer Network: *Cross-Site Request Forgery (CSRF)*. https://developer.mozilla.org/en-US/docs/Web/Security/CSRF (last visited: 2026-05-27)

[16] Python Software Foundation: *Python 3.12 documentation*. https://docs.python.org/3.12/ (last visited: 2026-05-27)

[17] Gunicorn: *Deploying Gunicorn*. https://docs.gunicorn.org/en/stable/deploy.html (last visited: 2026-05-27)

[18] Bootstrap Team: *Bootstrap 5 documentation*. https://getbootstrap.com/docs/5.3/ (last visited: 2026-05-27)

---

# 9. APPENDIX

## 9.1. User Manual

## Access

- **Production:** https://healthcare-appointment-system-9a2r.onrender.com  
- **Local:** http://127.0.0.1:8000/

## Demo accounts (academic use only)

| Role | Username | Password |
|------|----------|----------|
| Patient | patient1 | aaa |
| Doctor | doctor1 | aaa |
| Admin | admin | aaa |

## Main URLs

| Role | Entry point |
|------|-------------|
| Login | /accounts/login/ |
| Patient dashboard | /patients/dashboard/ |
| Doctor dashboard | /doctors/dashboard/ |
| Admin dashboard | /admin/ |
| Django admin | /super-admin/ |

## Typical patient flow

1. Log in as patient.  
2. Search for a doctor on the home page.  
3. Open doctor profile → select date and time → confirm booking.  
4. View appointment under patient dashboard; cancel or print if needed.  
5. After completed visit, submit review.

## Typical doctor flow

1. Log in as doctor.  
2. Set schedule under Schedule Timings.  
3. Open Appointments → confirm or complete bookings.  
4. Add prescription for completed appointment.

---

# APPENDIX B — SOURCE CODE STRUCTURE

```
secure-cloud-based-healthcare-appointment-system/
├── docbook/           # Project settings, urls, wsgi
├── accounts/          # User, Profile, auth, admin views
├── core/              # Home, Speciality, Review
├── doctors/           # Doctor features, schedules
├── patients/          # Patient dashboard
├── bookings/          # Booking, Prescription
├── templates/         # HTML templates
├── static/            # CSS, JS, images
├── fixtures/          # initial_data.json
├── tests/             # auth and e2e tests
├── build.sh           # Render build script
├── create_admin.py    # Admin user setup
├── manage.py
└── requirements.txt
```

---

# APPENDIX C — SCREENSHOTS AND FIGURES (INSERT IN WORD)

Use **continuous figure numbering** (Figure 1, Figure 2, … Figure 14). Reference each figure in the chapter text before it appears. Suggested full-page or half-page size; center images; caption below.

| Figure | Content | Suggested chapter |
|--------|---------|-------------------|
| Figure 1 | Cloud architecture (Browser → Render HTTPS → Gunicorn/Django/WhiteNoise ↔ PostgreSQL) | 4.1 / 5.6 |
| Figure 2 | Patient home after login (production) | 6.3 |
| Figure 3 | Middleware pipeline | 3.1.1 |
| Figure 4 | Entity-relationship diagram | 3.2 |
| Figure 5 | Public home page | 3.4.3 |
| Figure 6 | Login page with CSRF form | 5.3 |
| Figure 7 | Patient dashboard | 5.2 |
| Figure 8 | Doctor schedule timings | 4.2 |
| Figure 9 | Booking confirmation | 4.3 |
| Figure 10 | Admin dashboard | 4.4 |
| Figure 11 | HTTPS address bar | 3.5.3 |
| Figure 12 | RBAC 403 or redirect | 5.5 |
| Figure 13 | Render deploy log (optional) | 6.4 |
| Figure 14 | Appointment or revenue report | 4.8 |

**Page count tip:** Twelve to fourteen figures at roughly half to full page each add approximately **12–18 pages** in Word, which together with expanded text reaches the target **~66 pages** total.

---

# APPENDIX D — REQUIREMENTS TRACEABILITY MATRIX

| Requirement | Design element | Implementation | Test |
|-------------|----------------|----------------|------|
| FR-1 Public pages | core app, templates | `core.views`, home template | Manual |
| FR-2 Patient booking | bookings app | `CreateBookingView` | E2E + manual |
| FR-3 Doctor schedule | doctors models | day models, TimeRange | Manual |
| FR-4 Admin reports | admin_views | `AppointmentReportView` | Manual |
| FR-5 No double booking | unique_together | Booking model | Manual |
| NFR-1 Password hash | Django auth | default hasher | DB inspection |
| NFR-2 CSRF | middleware | all POST forms | View source |
| NFR-3 HTTPS | settings prod block | Render TLS | Browser URL |
| NFR-4 Django 5 | requirements.txt | 5.0.6 | pip freeze |
| NFR-5 Env secrets | python-dotenv | settings.py | Code review |
| NFR-6 Static files | WhiteNoise | collectstatic | Deploy log |

---

# APPENDIX E — BUILD AND DEPLOY COMMANDS

**Render build command:** `bash build.sh`  
**Render start command:** `gunicorn docbook.wsgi:application --bind 0.0.0.0:$PORT`  
**Python version:** 3.12.8 (`runtime.txt`)

**Local run:**

```bash
cd secure-cloud-based-healthcare-appointment-system
python manage.py runserver
```

---

# APPENDIX F — EXTENDED USER MANUAL

## F.1. Registration

New patients open `/accounts/patient/register/`, complete the form, and receive an account with role `patient`. New doctors use `/accounts/doctor/register/` and supply professional details including registration number where applicable. After registration, users log in at `/accounts/login/`.

## F.2. Password change

Patients and doctors change passwords from their profile settings or dedicated change-password URLs under `/patients/change-password/` and `/doctors/change-password/`. Administrators should change the default `aaa` password immediately if the system is used with real data.

## F.3. Searching doctors

On the home page, enter city or division and optional specialisation or doctor name. Results list matching doctors with links to public profiles. Profiles show biography, specialisation, fees, and available booking entry point.

## F.4. Printing appointments

Patients may open print-friendly appointment details from the patient appointment print URL. This supports clinic reception workflows where a paper copy is still required.

## F.5. Prescriptions

After an appointment progresses, the doctor navigates to the prescription creation URL for that booking. Rich text fields document medications and instructions. Patients do not edit prescriptions; they view outcomes through appointment detail pages as designed in the doctor workflow.

## F.6. Troubleshooting

| Problem | Likely cause | Action |
|---------|--------------|--------|
| 403 on login (production) | CSRF_TRUSTED_ORIGINS | Add exact https origin on Render |
| Empty doctor list | Fixtures not loaded | Redeploy; check build log |
| Admin shows as doctor | Missing superuser flags | Run create_admin.py |
| Slow first page load | Render cold start | Wait and refresh |

---

# APPENDIX G — GLOSSARY

| Term | Definition |
|------|------------|
| RBAC | Role-based access control: permissions based on user role |
| CSRF | Cross-site request forgery; attack mitigated by Django tokens |
| HTTPS | HTTP over TLS encryption |
| HSTS | HTTP Strict Transport Security header |
| ORM | Object-relational mapping; Django database API |
| PaaS | Platform as a Service (e.g. Render) |
| WSGI | Web Server Gateway Interface between server and Django |
| PBKDF2 | Password-based key derivation function used for hashing |
| Fixture | JSON file loaded to populate demo database rows |
| HIS | Hospital information system |
| DocBook | Name of the implemented appointment system |

---

# APPENDIX H — SELECTED SOURCE CODE EXCERPTS

The following excerpts illustrate critical implementation decisions. Full source is available in the Git repository.

## H.1. Booking model with uniqueness constraint

The `Booking` model enforces appointment integrity at database level:

```python
class Meta:
    ordering = ["-appointment_date", "-appointment_time"]
    unique_together = ["doctor", "appointment_date", "appointment_time"]
```

If two patients attempt the same slot, the second insert raises `IntegrityError`, which the view layer should catch and translate into a user-friendly message.

## H.2. Patient role mixin

RBAC for patients is implemented in `mixins/custom_mixins.py`:

```python
class PatientRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        if request.user.role != "patient":
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
```

The mixin runs before the view method, so no dashboard logic executes for unauthorized roles.

## H.3. Production security block

When `DEBUG` is false, settings activate HTTPS enforcement:

```python
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
```

This block was verified by inspecting response headers and cookies on the deployed site.

## H.4. Build automation

Fragment of `build.sh` showing deploy-time data loading:

```bash
python manage.py migrate --noinput
python manage.py loaddata fixtures/initial_data.json || true
python create_admin.py || true
python seed_demo_bookings.py || true
```

Automating these steps avoids manual database setup on hosts without shell access.

---

# APPENDIX I — DETAILED PATIENT JOURNEY (NARRATIVE TEST SCRIPT)

This script was used for manual acceptance testing and can be repeated by examiners.

1. Open the production URL in Chrome. Observe HTTPS in the address bar (Figure 11).
2. Click login; enter `patient1` and password `aaa`. Confirm redirect to patient dashboard (Figure 7).
3. Return to home; search for a city or doctor name; open a doctor profile (Figure 5).
4. Choose an available date and time slot; submit booking; land on success page (Figure 9).
5. Open patient dashboard; verify booking appears with status pending or confirmed.
6. Log out. Log in as `doctor1` with password `aaa`. Open appointments; confirm or complete the booking.
7. Log out. Log in as `admin`; open `/admin/` dashboard (Figure 10); open appointment report (Figure 14).
8. Log out. Log in again as `patient1`; attempt to open `/doctors/dashboard/`; observe access denied (Figure 12).

Duration: approximately fifteen minutes. All steps passed on 27 May 2026.

---

# APPENDIX K — SUPERVISOR DEMONSTRATION SCRIPT (5 MINUTES)

For oral defence, the following short demo covers all roles:

1. **30 s** — Show production URL and HTTPS.
2. **60 s** — Login as patient; book appointment.
3. **60 s** — Login as doctor; confirm appointment.
4. **60 s** — Login as admin; show dashboard and one report.
5. **30 s** — Mention security: hashed passwords, RBAC, cloud hosting.
6. **30 s** — Answer questions; offer to show source structure in Appendix B.

---

# APPENDIX L — ENVIRONMENT VARIABLE TEMPLATE

| Variable | Example value (do not commit real secrets) |
|----------|---------------------------------------------|
| SECRET_KEY | long-random-string |
| DEBUG | False |
| ALLOWED_HOSTS | your-app.onrender.com |
| DATABASE_URL | postgresql://user:pass@host/db |
| CSRF_TRUSTED_ORIGINS | https://your-app.onrender.com |

Store these only in Render dashboard or local `.env` excluded from Git.

---

# APPENDIX M — BIBLIOGRAPHY ADDITIONS FOR OPTIONAL READING

The following sources were consulted during background research but not cited directly in the main text: Django Girls tutorial materials; Real Python articles on Django deployment; Render community forum posts on PostgreSQL URL format; OWASP Cheat Sheet Series for session management. Students extending this work should read official Django security documentation before modifying authentication.

---

# APPENDIX J — LIST OF ABBREVIATIONS

| Abbreviation | Meaning |
|--------------|---------|
| API | Application Programming Interface |
| CRUD | Create, Read, Update, Delete |
| CSRF | Cross-Site Request Forgery |
| EHR | Electronic Health Record |
| FK | Foreign Key |
| GDPR | General Data Protection Regulation |
| HIS | Hospital Information System |
| HSTS | HTTP Strict Transport Security |
| HTTP | Hypertext Transfer Protocol |
| HTTPS | HTTP Secure |
| ORM | Object-Relational Mapping |
| PaaS | Platform as a Service |
| RBAC | Role-Based Access Control |
| REST | Representational State Transfer |
| SPA | Single Page Application |
| SQL | Structured Query Language |
| TLS | Transport Layer Security |
| URL | Uniform Resource Locator |
| VPS | Virtual Private Server |
| WSGI | Web Server Gateway Interface |

---

# NOTES FOR FINAL SUBMISSION IN WORD

1. Replace `[THESIS_NUMBER]`, `[SUPERVISOR_NAME]`, `[DEPARTMENT_NAME]`, `[SUBMISSION_DATE]`.
2. Generate automatic table of contents in Word (References → Table of Contents).
3. Add page header with thesis title or chapter name (Insert → Header).
4. Insert all figures from Appendix C; reference every figure in the text.
5. **Target length: ~66 pages** — expanded text (~45–50 pages) + front matter (~8 pages) + 12–14 figures (~12–18 pages). Under 100-page limit.
6. Print on A4, bind with spine: Abdulkadir Salihu Abdulhamid | [THESIS_NUMBER] | 2026.
7. Glue portrait photograph on inside cover per faculty instructions.
8. Remove this “NOTES” section from the printed thesis.
9. To reach **66 pages** if Word shows fewer: (a) insert each of the 14 figures at **full page width**; (b) add page break before each new chapter; (c) include Appendix H code listings in 10 pt Courier; (d) expand table of contents to three levels.

*End of diploma thesis document.*


