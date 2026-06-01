# How to Use Your Friend's Word Template with Your DocBook Thesis

Your friend's thesis uses **chapters 1–9**. Your content is in `DIPLOMA_THESIS.md`, now aligned to the **same structure**. Follow this guide when pasting into your friend's `.docx` file.

---

## Step 1 — Prepare your friend's Word file

1. Open your friend's thesis `.docx`.
2. **Save As** → `Abdulkadir_DocBook_Thesis_2026.docx`
3. Delete **all body text** from Introduction through Appendix.
4. **Keep:** margins, fonts (Times 12, Arial headings), header, footer, page number style, cover layout.

---

## Step 2 — Paste in this order (use **Keep Text Only**)

| Order | Friend's heading | Copy from `DIPLOMA_THESIS.md` section |
|-------|------------------|--------------------------------------|
| 1 | Cover / Title / Tasks / Declaration | Top of file (before TOC) |
| 2 | **1. Introduction** | `# 1. INTRODUCTION` |
| 3 | **1.1. Objectives** | `## 1.1. Objectives` |
| 4 | **2. Literature Review** | `# 2. LITERATURE REVIEW` through end of `2.3.2` |
| 5 | **3. Specification and Solution Approach** | `# 3. SPECIFICATION...` through `3.2.3` / technology stack |
| 6 | **4. System Design and Architecture** | Old `# 3. SYSTEM DESIGN` or `# 4. SYSTEM DESIGN` section |
| 7 | **4.4. Use Case Diagrams** | Section `3.1.5. Use cases` — draw diagram in Word |
| 8 | **4.5. Wireframes** | Appendix C screenshots / your UI images |
| 9 | **5. Implementation** | Implementation + Cloud deployment chapters |
| 10 | **6. Testing and Feedback** | Testing chapter |
| 11 | **7. Conclusion and Future Development** | Summary + Chapter 7 |
| 12 | **8. References** | `# REFERENCES` |
| 13 | **9. Appendix** | All APPENDIX sections |

---

## Step 3 — Apply Word styles (same as friend)

| Your heading in markdown | Word style |
|--------------------------|------------|
| `# 1. INTRODUCTION` | **Heading 1** (Arial 14 bold) |
| `## 1.1. Objectives` | **Heading 2** (Arial 12 bold) |
| `### 3.2.1. Backend` | **Heading 3** (Arial 12 bold) |

---

## Step 4 — Table of Contents

1. Place cursor after Declaration.
2. **References → Table of Contents → Automatic Table 1**
3. Should look like your friend's:

```
1. Introduction
1.1. Objectives
2. Literature Review
2.1. Overview of Healthcare Appointment Systems
...
7. Conclusion and Future Development
8. References
9. Appendix
```

---

## Your TOC (copy into Word if auto-TOC fails)

```
1. Introduction
1.1. Objectives
2. Literature Review
2.1. Overview of Healthcare Appointment Systems
2.2. Theoretical Framework
2.2.1. User-Centered Design (UCD) Principles
2.2.2. Core Features Guided by UCD Principles
2.3. Comparative Analysis of Existing Systems
2.3.1. Healthcare and Appointment Platforms
2.3.2. Identified Gaps and Solutions
3. Specification and Solution Approach
3.1. Specification
3.2. Solution Approach
3.2.1. Backend
3.2.2. Frontend
3.2.3. Tools and Development Environment
4. System Design and Architecture
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
5. Implementation
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
6. Testing and Feedback
6.1. Test Strategy
6.2. Functional Testing
6.3. Security Testing
6.4. Evaluation and Feedback
7. Conclusion and Future Development
7.1. Conclusion
7.2. Future Development
8. References
9. Appendix
```

---

## Mapping: Friend's recipe thesis → Your healthcare thesis

| Friend (recipe app) | You (DocBook) |
|---------------------|---------------|
| Personalized Recipe Applications | Healthcare Appointment Systems |
| MERN Stack | Django + PostgreSQL + Render |
| Recipe Suggestion Algorithm | Appointment Booking Workflow |
| Social Recipe Feed | Admin Dashboard and Reports |
| Capacitor (mobile) | Cloud Deployment on Render |
| Firebase Notifications | Security and HTTPS |
| Material UI / Tailwind | Bootstrap / HTMX / Templates |

---

## Figures (like your friend)

Insert **14 figures** with captions under chapters 4 and 5. Reference each in text: "as shown in Figure 5". Full list in `DIPLOMA_THESIS.md` Appendix 9.3 / C.

---

## Page target (~66 pages)

- Text from `DIPLOMA_THESIS.md` (~50+ pages formatted)
- 12–14 full-page screenshots
- Same as friend's length (their sample was ~56 pages TOC ending at 56)

---

## Do NOT copy from friend

- Any sentences about recipes, ingredients, MERN, Firebase, Capacitor
- Their name, thesis number, or screenshots

Only copy **formatting and chapter structure**.
