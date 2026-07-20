# ADR-001: Technology Stack Selection

**Status:** Accepted

**Date:** 2026-07-20

## Context

TenderLens is an AI-powered web application that analyzes tender documents and generates structured compliance checklists.

The application requires:

- A modern backend API.
- A responsive web interface.
- Integration with Large Language Models (LLMs).
- Structured data validation.
- A relational database.
- Future scalability for additional AI features.

The technology stack should be easy to develop, maintain, and scale while also helping the developer gain industry-relevant AI engineering skills.

---

## Decision

TenderLens will use the following technology stack:

| Component | Technology |
|-----------|------------|
| Backend | FastAPI |
| Frontend | React |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Data Validation | Pydantic |
| AI Integration | OpenAI API (provider may change) |
| Version Control | Git & GitHub |
| Containerization | Docker (Future) |

---

## Rationale

### FastAPI

Chosen because it:

- Provides excellent performance.
- Automatically generates API documentation.
- Integrates well with Python AI libraries.
- Uses type hints for better code quality.
- Is widely adopted for modern AI applications.

---

### React

Chosen because it:

- Creates reusable UI components.
- Supports interactive user interfaces.
- Separates frontend and backend responsibilities.
- Is widely used in modern web development.

---

### PostgreSQL

Chosen because it:

- Is reliable and production-ready.
- Supports structured relational data.
- Handles JSON data effectively.
- Is commonly used in AI and enterprise applications.

---

### SQLAlchemy

Chosen because it:

- Simplifies database interactions.
- Reduces raw SQL.
- Works well with PostgreSQL.
- Integrates naturally with FastAPI.

---

### Pydantic

Chosen because it:

- Validates API requests and responses.
- Reduces data validation errors.
- Integrates directly with FastAPI.

---

### OpenAI API

Chosen because it:

- Provides high-quality language models.
- Supports structured JSON outputs.
- Enables document analysis without training custom models.

The AI provider may change in future versions if another provider better meets project requirements.

---

## Consequences

### Positive

- Modern, scalable architecture.
- Strong alignment with AI engineering practices.
- Clear separation between frontend and backend.
- Easy integration with additional AI services.
- Technology stack commonly used in production environments.

### Negative

- React introduces additional frontend complexity.
- FastAPI requires learning asynchronous programming concepts.
- AI APIs introduce usage costs.
- Docker adds deployment complexity when introduced.

---

## Alternatives Considered

### Flask

Pros

- Simpler for beginners.
- Large ecosystem.

Cons

- Requires additional libraries for features that FastAPI provides out of the box.
- Less optimized for API-first development.

---

### Django

Pros

- Batteries included.
- Excellent admin interface.

Cons

- More features than required for the MVP.
- Steeper learning curve for this project.

---

### WordPress

Pros

- Rapid website development.

Cons

- Better suited for content management than AI-powered web applications.
- Limited flexibility for custom AI workflows.
- Does not align as closely with the goal of becoming an AI Engineer.

---

## Review

This decision will be revisited if project requirements change significantly.