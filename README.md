# AI Resume Screening System

## Project Overview

The AI Resume Screening System is a cloud-based web application developed to simplify and automate the resume screening process for recruiters and hiring teams. The application allows users to upload candidate resumes in PDF format, automatically extracts resume content, analyzes candidate skills, calculates candidate scores based on required skills, and provides recruiter-friendly insights.

The project was developed using Python and Streamlit for the frontend interface and application logic. AWS cloud services such as AWS S3 and AWS EC2 were integrated to provide cloud storage and cloud deployment functionality. SQLite database was used to store candidate information and maintain recruiter analytics.

The system helps recruiters reduce manual effort in resume shortlisting by automatically identifying matched skills, missing skills, and generating AI-style recommendations and interview questions for candidates.

---

## Features

- Resume Upload System
- PDF Resume Parsing
- Resume Text Extraction
- Skill Matching and Filtering
- Candidate Score Calculation
- Missing Skills Identification
- AI-style Resume Analysis
- Suggested Interview Questions
- Candidate Recommendation System
- AWS S3 Cloud Resume Storage
- SQLite Candidate Database
- Dashboard Analytics
- Data Visualization and Charts
- Cloud Deployment using AWS EC2
- Publicly Accessible Web Application

---

## Technologies Used

### Programming Language
- Python

### Frontend & Application
- Streamlit

### Cloud Services
- AWS EC2
- AWS S3

### Database
- SQLite

### Libraries Used
- pdfplumber
- pandas
- matplotlib
- boto3
- sqlite3

---

## System Workflow

1. User uploads a resume in PDF format.
2. Resume file gets uploaded to AWS S3 cloud storage.
3. PDF content is extracted using pdfplumber.
4. Resume skills are compared with required skills.
5. Candidate score is calculated automatically.
6. Missing skills and matched skills are identified.
7. AI-style analysis and interview questions are generated.
8. Candidate details are stored in SQLite database.
9. Dashboard displays candidate analytics and visual charts.
10. Application is deployed and hosted using AWS EC2.

---

## Project Objectives

- Automate the manual resume screening process
- Improve recruiter efficiency
- Reduce hiring time
- Provide cloud-based resume management
- Demonstrate cloud computing and Python development skills
- Implement real-world deployment using AWS services

---

## AWS Services Used

### AWS EC2
Used for deploying and hosting the Streamlit web application publicly.

### AWS S3
Used for storing uploaded resume files securely in cloud storage.

---

## Screenshots

### Main Application

![Application Screenshot 1](screenshots/app1.png)

![Application Screenshot 2](screenshots/app2.png)



---

### Dashboard and Analytics

![Dashboard Screenshot 1](screenshots/dashboard1.png)

![Dashboard Screenshot 2](screenshots/dashboard2.png)

![Dashboard Screenshot 2](screenshots/dashboard3.png)

![Dashboard Screenshot 2](screenshots/dashboard4.png)

---

### AWS Deployment

![AWS EC2](screenshots/aws1.png)

![AWS S3](screenshots/aws2.png)

![AWS S3](screenshots/aws3.png)

---

## Future Improvements

- Real AI integration using Gemini or OpenAI APIs
- Recruiter Login Authentication
- Email Notifications to Candidates
- Resume Ranking System
- Docker Container Deployment
- CI/CD Pipeline Integration
- AWS RDS Database Integration
- Multi-user Recruiter Dashboard

---

## Conclusion

The AI Resume Screening System successfully demonstrates the integration of Python development, cloud computing, database management, and deployment technologies into a real-world project. The project highlights practical implementation of AWS cloud services along with automation features useful for recruitment and hiring workflows.

---

## Author

Swathi