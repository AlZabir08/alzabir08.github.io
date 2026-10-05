import re

with open('certificates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    "Hepatitis C Detection Using Ensemble Boosting": "Hepatitis C Detection Using Ensemble Boosting",
    "Prediction Of Nightmares In Children": "Prediction Of Nightmares In Children",
    "Stress Detection Using Ppg Signals": "Stress Detection Using PPG Signals",
    "Predicting Fear-related Nightmares In Children": "Predicting Fear-Related Nightmares In Children",
    "Basic Robotic Behaviors And Odometry": "Basic Robotic Behaviors And Odometry",
    "Machine Learning Specialization": "Machine Learning Specialization",
    "Programming Foundations With Javascript, Html And Css": "Programming Foundations With JavaScript, HTML And CSS",
    "Sql (basic)": "SQL (Basic)",
    "Python": "Python",
    "Unconscious Bias In Medicine": "Unconscious Bias In Medicine",
    "Introduction To Artificial Intelligence (ai)": "Introduction To Artificial Intelligence (AI)"
}

for k, v in replacements.items():
    content = content.replace(f"<h2>{k}</h2>", f"<h2>{v}</h2>")

with open('certificates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
