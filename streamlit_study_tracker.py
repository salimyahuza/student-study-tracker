import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Embedded dataset
data = {
    "study_hours": [1, 2, 3, 4, 5, 2.5, 3.5, 4.5, 1.5, 3],
    "mood": [3, 4, 5, 4, 5, 3, 4, 5, 2, 3],
    "sleep_hours": [6, 7, 8, 6.5, 7.5, 6, 7, 8, 5.5, 7],
    "score": [50, 60, 80, 70, 90, 65, 75, 85, 45, 68]
}
df = pd.DataFrame(data)

st.title("📊 Student Study Progress Tracker (AI-powered)")

st.subheader("Raw Data")
st.dataframe(df)

# Correlation heatmap
st.subheader("📈 Correlation Analysis")
fig, ax = plt.subplots()
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Mood vs Score scatterplot
st.subheader("🎯 Mood vs. Score")
fig2, ax2 = plt.subplots()
sns.scatterplot(data=df, x="mood", y="score", hue="study_hours", palette="viridis", ax=ax2)
ax2.set_title("How Mood and Study Hours Affect Score")
st.pyplot(fig2)

# Score prediction tip based on average study and mood
st.subheader("🧠 AI Insight (Basic)")
avg_study = df['study_hours'].mean()
avg_mood = df['mood'].mean()
expected_score = round(df['score'].mean() + (avg_study - 3) * 5 + (avg_mood - 3) * 3)
st.success(f"Based on average study time and mood, an estimated performance score could be: {expected_score}")
