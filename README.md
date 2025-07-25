# Student Study Tracker 

![Logo](https://raw.githubusercontent.com/salimyahuza/StudySprint-Tracker/main/Logo.jpg)

## About the Project

Student Study Tracker is a lightweight, Python-based progress tracker designed for learners at various stages — from secondary school to advanced learners. It helps track learning goals, study hours, task completion, and offers **daily motivational quotes** to keep you energized!

This app is designed and built by **Salim Yahuza Gwarjo**, an M.Sc. Data Science student (M.A.H.E. India), ICT teacher, and education reform advocate. Salim has worked with over 3,000 students and redesigned ICT curricula for schools in Katsina State, Nigeria.

## Motivation

Many students struggle to stay on track due to lack of personalized guidance and motivational support. This tool solves that by combining **goal tracking** and **inspiration** in one place — especially tailored for learners with limited access to advanced tech tools.

## Features

- Tracks daily/weekly study goals
- Visualizes progress with charts
- Daily motivational quote system
- Lightweight — runs on Google Colab
- No login, no install — easy access
- Daily Study Logging: Input study subject, duration, and comments.
- Search & Filter: View study sessions by subject or date range.
- Calendar Heatmap: Visualize consistency with a daily calendar heatmap.
- Study Summary: See total study time and logs per subject.
- Download Logs: Export your full log as a CSV file.
- Email Reminders (Optional): Send yourself reminder emails using SMTP.
- Google Calendar Integration (Optional & Disabled by Default): Add sessions directly to your Google Calendar (requires setup).

## AI-Powered Insight (v1.0)

- Calculates your **average study time**
- Detects recent dips or improvements in study patterns
- Flags **subjects needing attention**
- Suggests adjustments to help you stay on track

## What’s Coming Next?
This app is a minimum viable product, and several powerful features will be introduced in future versions:

AI Chatbot for interactive Q&A and study help

AI-assisted Reading Comprehension (auto-generating questions & summaries)

Calendar Integration for automated scheduling

Smarter insights from long-term learning trends

## Quick Start
On Streamlit Cloud
Just open the app online — no install needed.

## Local Setup
### Clone the repo:

git clone https://github.com/salimyahuza/student-study-tracker.git

cd student-study-tracker

### Install requirements:

pip install -r requirements.txt

### Run the app:

streamlit run streamlit_study_tracker.py


## Built With
Python

Streamlit

Pandas

Seaborn / Matplotlib

GitHub

SMTP (Email)

## Optional Reminder Features

### Files

**streamlit_study_tracker.py**: Main app script

**study_log.csv**: Stores your study history

**.streamlit/secrets.toml**: For secure credentials

**Logo.jpg**: App branding logo

### Email Reminder via SMTP

You can enable email reminders by setting up your email credentials.


### For Gmail users:

Enable 2-Step Verification and create an App Password.

Python code:

send_email_reminder("salimyahuza@gmail.com", "Deep Learning with PyTorch", "2025-07-25", "10:00")


## Google Calendar Integration (Disabled by Default)

If you want to sync reminders to Google Calendar:
1. Create a project in Google Cloud Console.
2. Enable the Google Calendar API.
3. Download credentials.json and place it in your notebook directory.
4. Uncomment the line in the code cell:
python
add_study_reminder("Python Programming", "2025-07-23", "20:00", duration_minutes=90)



## License

MIT License

## Author
**Name**: Salim Yahuza Gwarjo

**3MTT Fellowship ID**: FE/23/61894589

**Track**: Data Science

**Cohort**: 3



### Contact:

**GitHub**:  https://github.com/salimyahuza

**LinkedIn**: https://www.linkedin.com/in/salim-yahuza-gwarjo-15b45313b

**Email**:  salimyahuza@gmail.com





## Acknowledgements
I want to thank our tutors for their mentorship, hardwork and patience. Their guidance enabled me to develop this app as part of the 3MTT Knowledge Showcase – July Edition. Thank you 3MTT, thank you Darey, thank you panel of Judges (competiton team) and thank you fellow leaners!
