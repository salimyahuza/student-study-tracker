# Student Study Tracker 🧠📊

![Logo](https://raw.githubusercontent.com/salimyahuza/StudySprint-Tracker/main/Logo.jpg)

## About the Project

Student Study Tracker is a lightweight, Python-based progress tracker designed for learners at various stages — from secondary school to advanced learners. It helps track learning goals, study hours, task completion, and offers **daily motivational quotes** to keep you energized!

This app is designed and built by **Salim Yahuza Gwarjo**, an M.Sc. Data Science student (M.A.H.E. India), ICT teacher, and education reform advocate. Salim has worked with over 3,000 students and redesigned ICT curricula for schools in Katsina State, Nigeria.

## Motivation

Many students struggle to stay on track due to lack of personalized guidance and motivational support. This tool solves that by combining **goal tracking** and **inspiration** in one place — especially tailored for learners with limited access to advanced tech tools.

## Features

- 🌟 Tracks daily/weekly study goals
- 📊 Visualizes progress with charts
- 💬 Daily motivational quote system
- 🖼️ Lightweight — runs on Google Colab
- 🔗 No login, no install — easy access
- ✅ Daily Study Logging: Input study subject, duration, and comments.
- ✅ Search & Filter: View study sessions by subject or date range.
- ✅ Calendar Heatmap: Visualize consistency with a daily calendar heatmap.
- ✅ Study Summary: See total study time and logs per subject.
- ✅ Download Logs: Export your full log as a CSV file.
- ✅ Email Reminders (Optional): Send yourself reminder emails using SMTP.
- ✅ Google Calendar Integration (Optional & Disabled by Default): Add sessions directly to your Google Calendar (requires setup).

## 🚀 Quick Start

1. Open the Colab notebook.
2. Log your study sessions by subject and time.
3. Track your daily tasks with helpful summaries.
4. Get inspired by your daily quote.
5. Watch your progress with visualizations and heatmap!
6. Optionally, set reminders via email or Google Calendar.


## Built With
- Python
- Pandas
- Matplotlib
- Google Colab
- GitHub

## 🔔 Optional Reminder Features


📨 Email Reminder via SMTP

You can enable email reminders by setting up your email credentials.
For Gmail users:
Enable 2-Step Verification and create an App Password.

Python code:

send_email_reminder("salimyahuza@gmail.com", "Deep Learning with PyTorch", "2025-07-25", "10:00")

## 📅 Google Calendar Integration (Disabled by Default)

If you want to sync reminders to Google Calendar:
1. Create a project in Google Cloud Console.
2. Enable the Google Calendar API.
3. Download credentials.json and place it in your notebook directory.
4. Uncomment the line in the code cell:
python
add_study_reminder("Python Programming", "2025-07-23", "20:00", duration_minutes=90)

## 📦 Requirements

Install these once:

python

!pip install calmap

!pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

## 📁 Files

study_log.csv: Stores the saved study logs.

token.pickle: (If Google Calendar is used) Stores OAuth tokens.

credentials.json: (User-supplied) Google credentials file.


## License

MIT License

## 🙋‍♂️ Author
**Name**: Salim Yahuza Gwarjo

**3MTT Fellowship ID**: FE/23/61894589

**Track**: Data Science

**Cohort**: 3


### Contact:

**GitHub**:  https://github.com/salimyahuza

**LinkedIn**: https://www.linkedin.com/in/salim-yahuza-gwarjo-15b45313b

**Email**:  salimyahuza@gmail.com





## 🙏 Acknowledgements
I want to thank our tutors for their mentorship, hardwork and patience. Their guidance enabled me to develop this app as part of the 3MTT Knowledge Showcase – July Edition. Thank you 3MTT, thank you Darey, thank you panel of Judges (competiton team) and thank you fellow leaners!
