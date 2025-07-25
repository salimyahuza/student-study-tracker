import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
from datetime import datetime
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to send email reminder
def send_email_reminder(receiver_email, subject, date, time):
    sender_email = st.secrets["EMAIL_USER"]
    sender_password = st.secrets["EMAIL_PASSWORD"]

    message = MIMEMultipart("alternative")
    message["Subject"] = "\U0001F4DA Study Reminder"
    message["From"] = sender_email
    message["To"] = receiver_email

    html = f"""
    <html>
      <body>
        <p>Hi there!<br><br>
           This is a reminder to study <b>{subject}</b> on <b>{date}</b> at <b>{time}</b>.<br>
           Stay consistent! 💪
        </p>
      </body>
    </html>
    """

    part = MIMEText(html, "html")
    message.attach(part)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        return True
    except Exception as e:
        st.error(f"Failed to send email: {e}")
        return False

# Load or initialize data
log_file = "study_log.csv"
if os.path.exists(log_file):
    df = pd.read_csv(log_file)
else:
    df = pd.DataFrame(columns=['Date', 'Subject', 'Hours Studied', 'What You Learned', 'Challenges Faced'])

# App Layout
st.set_page_config(page_title="\U0001F4DA Student Study Tracker", layout="centered", page_icon="https://raw.githubusercontent.com/salimyahuza/StudySprint-Tracker/main/Logo.jpg")
st.image("https://raw.githubusercontent.com/salimyahuza/StudySprint-Tracker/main/Logo.jpg", width=100)
st.title("\U0001F4DA Student Study Tracker")

# -- Load motivational quotes --
quotes = [
    "Success doesn’t come from what you do occasionally, it comes from what you do consistently.",
    "Don’t watch the clock; do what it does. Keep going.",
    "Small progress is still progress.",
    "Push yourself, because no one else is going to do it for you.",
    "It’s not about having time, it’s about making time.",
    "The only way to do great work is to love what you do.",
    "Your present circumstances don't determine where you can go; they merely determine where you start.",
    "Fall seven times, stand up eight.",
    "An investment in knowledge pays the best interest.",
    "The expert in anything was once a beginner."
]

st.subheader("✨ Quote of the Day")
st.info(random.choice(quotes))

# -- Input form --
st.subheader("\U0001F4DD Log Today's Study Session")
with st.form("log_form"):
    subject = st.text_input("Subject/Topic")
    hours = st.number_input("Hours Studied", min_value=0.0, step=0.5)
    what_learned = st.text_area("What did you learn today?")
    challenges = st.text_area("Any challenges?")
    email = st.text_input("Optional: Enter your email to receive a study reminder")
    reminder_time = st.time_input("Set Reminder Time (Optional)")
    submitted = st.form_submit_button("Save Entry")

if submitted:
    new_entry = {
        'Date': datetime.now().strftime("%Y-%m-%d"),
        'Subject': subject,
        'Hours Studied': hours,
        'What You Learned': what_learned,
        'Challenges Faced': challenges
    }
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(log_file, index=False)
    st.success("✅ Entry saved successfully!")

    if email:
        sent = send_email_reminder(email, subject, new_entry['Date'], reminder_time.strftime("%H:%M"))
        if sent:
            st.success("\U0001F4E7 Email reminder sent!")

# -- Filter logs --
st.subheader("🔍 Search Study Logs")
search_term = st.text_input("Enter subject or date (YYYY-MM-DD)")

if search_term:
    try:
        filtered = df[df['Date'] == pd.to_datetime(search_term).strftime('%Y-%m-%d')]
    except:
        filtered = df[df['Subject'].str.contains(search_term, case=False, na=False)]

    if not filtered.empty:
        st.write(filtered)
    else:
        st.warning("No matching study sessions found.")

# -- Visualizations --
st.subheader("📊 Visualize Study Progress")
if not df.empty:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    tab1, tab2 = st.tabs(["📈 Hours Over Time", "📚 Subjects Frequency"])

    with tab1:
        fig, ax = plt.subplots(figsize=(10, 4))
        sns.lineplot(data=df, x="Date", y="Hours Studied", marker="o", ax=ax)
        ax.set_title("Daily Hours Studied")
        ax.grid(True)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    with tab2:
        fig, ax = plt.subplots(figsize=(10, 4))
        sns.countplot(data=df, x="Subject", order=df['Subject'].value_counts().index, ax=ax)
        plt.xticks(rotation=45)
        ax.set_title("Study Frequency by Subject")
        st.pyplot(fig)

# -- Export --
st.subheader("📄 Export Logs")
st.download_button("Download CSV", data=df.to_csv(index=False), file_name="study_log.csv", mime="text/csv")

# -- AI-powered Insight --
st.subheader("🧠 AI Insights: See Your Learning Patterns")
if not df.empty:
    if 'Hours Studied' in df.columns:
        avg_hours = df['Hours Studied'].mean()
        st.metric(label="📊 Average Study Hours per Day", value=round(avg_hours, 2))

        last_7_days = df[df['Date'] >= (datetime.now() - pd.Timedelta(days=7))]
        recent_avg = last_7_days['Hours Studied'].mean()
        if recent_avg < avg_hours:
            st.warning(f"⚠️ Your recent average study time ({round(recent_avg, 2)} hrs) is below your overall average.")
            st.info("Try setting a more consistent routine or adjusting your goals!")
        else:
            st.success("✅ You're on track! Keep up the momentum!")

        subject_avg = df.groupby("Subject")["Hours Studied"].mean()
        lowest = subject_avg.idxmin()
        highest = subject_avg.idxmax()
        st.markdown(f"📌 You've spent the least time on **{lowest}**. Consider allocating more focus there.")
        st.markdown(f"✅ You're doing great in **{highest}** — keep it up!")

    try:
        st.write("### 🔍 Correlation Heatmap Explanation")
        st.markdown("This heatmap shows the relationship between numerical variables in your study log. A strong positive correlation (closer to +1) means they rise together, while negative (closer to -1) means as one increases, the other decreases. It's a quick way to uncover patterns in your habits.")
        numeric_df = df.select_dtypes(include=['float64', 'int64'])
        fig, ax = plt.subplots()
        sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
    except:
        st.warning("Correlation heatmap not available for current data.")

# -- Footer --
st.markdown("---")
st.caption("Developed by Salim Yahuza Gwarjo, a Data Science fellow of 3MTT Cohort 3. Fellowship ID: FE/23/61894589. For inquiries, please contact salimyahuza@gmail.com")
