# TenderLens Product Requirement Document (PRD)

**Version:** 1.0
**Status:** Draft
**Author:** Celestine Wangechi
**Last Updated:** 17 July 2026

## 1. Product review

### Product Name
**TenderLens**

### Product Description
*TenderLens* is an AI-Powered tender document analysis platform that transformas Request for Tender(RFT) documents and Request For Proposal(RFP) documents into structured, categorised compliance checklists. The generated checklist can be reviewed online and exported as  PDF or Excel, helping organizations analyse tender requrements faster, reduce manual effort and  improve compliance.
---

## 2. Problem Statement
Tender documents are often lenthy and complex, with legal, financial, technical and administartive requirements spread across multiple sections. Manual review is often time consuming, prone to human error and increases the risk of missed requirements, poor bid/no bid decisions and unsuccessful submissions.
---

## 3. Target Users
| User | Primary Goal |
|------|--------------|
| Tender consultants | Reduce document review time and improve accuracy |
| Bid Managers | Make faster bid/no-bid decisions |
| Procurement Consultants | Prepare compliant tender submissions |
| Government Contractors | Organize tender requirements efficiently |
| NGOs | Simplify grants and procurement applications |
| Construction and Engineering firms | Reduce compliance risks |
| SMEs | Copmplete effectivrly with out dedicated bid teams|

---

## 4. Product Goal
The MVP should:
- Process tender documents within seconds.
- Extract key requirements accurately.
- Categorize requirements into logical sections.
- Genarate a structred checklist.
- Allow users to export the check list as PDF or Excel.
- Provide tracability by linking each requirement to its source page or clause.

---

## 5. MVP Features

### Document processing

- Upload PDF tender documents.
- Extract document text.
- Identify document sections

### Requirement Extraction

- Extract legal requirements.
- Extract administrative requirements.
- Extract technical requirements.
- Extract finacial requirements.
- Idedntify mandatory and optional requirements.

### Checklist Genaration

- Generate a structured compliance checklist.
- Include page and clause references for every extracted item.
- Display results within the application.
- Export checklist as PDF.
- Export checklist as Excel.

---

## 6. Outof scope(Future Releases)

The following features are intentionaly excluded from the MVP:

- AI chats with Tender documents.
- Automated bid/no bid recommendations.
- Risk detection and contract clause analysis.
- Company profile compliance checking.
- Expiary validation of company documents.
- OCR support for scanned documents.
- Team collaboration.
- Multi language support.
- User roles and permissions

---

## 7. User journey

1. User signs in.
2. User uploads  a tender documant(PDF).
3. The system validates the uploaded file.
4. The system extracts the document text.
5. The AI anayses and categorises the document.
6. The system generates a srtuctured checklist.
7. The user reviews the extracted requrements.
8. The user exports the checklist as PDF or Excel.

---

## 8. Success Criteria

The MVP should be considered successful if it can:

- Analyze a typical tender documant in under 60 seconds.
- Extract tender requirements with high accuracy.
- Generate a structured checklist with out omitting key requirements.
- Minimize AI hallucinations through structured extraction.
- Link ever requirement to its page and clause.
- Significantly reduce manual tender review.

---

## 9. Assumptions

- User Upload text-based  PDF tender documents.
- Documents are primarily written in English.
- Users verify AI-generated outputs before submissions.
- Internet connectivity is available for AI processing.

---

## 10. Constraints

- Scanned PDFs are not supported by the MVP.
- Processing speeds depend on the selected AI provider.
- Large documents may require higher processing times.
- TenderLens assists with document analysis but does not replace professional judgment.

---

## 11. Non-Functional Requirements.

### Perfomance
 
- Process a standard tender document in under 60 seconds.

### Reliabilty

- Handle processong failures gracefully and provide clear error messages.

### Security

- Uploaded documents are available only to the authenticated user.

### Userbility

- Users  should be able to upload  a document and export resultswith minimal steps.

### Maintainability

- Code base should follow a modular architecture with docimentation and tests where appropriate.

---

## 12. Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| FastAPI | Backend API development |
| React | Frontend user interface |
| PostgreSQL | Store users, tender metadata, extracted requirements, and application data |
| SQLAlchemy | Database ORM |
| Pydantic | Data validation and API schemas |
| OpenAI API (or another LLM provider) | AI-powered requirement extraction |
| JSON | Structured communication between the AI model, backend, and frontend |
| Docker *(Future)* | Containerized deployment |
| Git & GitHub | Version control and collaboration |

---

## 13. User Stories

- **As a tender consultant**, I want to upload a tender document so that I can generate a structured compliance checklist in minutes instead of manually reviewing hundreds of pages.

- **As a bid manager**, I want every extracted requirement to reference its original page or clause so that I can verify the AI's output.

- **As a procurement officer**, I want to export the checklist to Excel or PDF so that I can share it with my team.

- **As an SME owner**, I want tender requirements organized into categories so that I can quickly understand what documents and information are needed before deciding whether to bid.

---

## 14. Future Vision

TenderLens will evolve into an AI-powered procurement assistant capable of:

- Conversational chat with tender documents.
- Automated bid/no-bid recommendations.
- Risk and contract clause analysis.
- Company document compliance checking.
- Tender comparison across multiple documents.
- Intelligent procurement insights and reporting.