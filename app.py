from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path
from datetime import datetime
import os

BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "change-this-in-production")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", f"sqlite:///{BASE_DIR / 'portfolio.db'}"
).replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(160), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

with app.app_context():
    db.create_all()

PROFILE = {
    "name": "Korapati Sreedhar",
    "role": "Software Engineer | Python & Flask Developer",
    "tagline": "Building production-style backend systems and full-stack web applications.",
    "email": "korapatisreedhar9999@gmail.com",
    "phone": "+91 9346668551",
    "github": "https://github.com/korapatisreedhar",
    "linkedin": "https://www.linkedin.com/in/sreedhar-korapati-77a0b024a",
    "summary": (
        "Software Engineer with a B.Tech in Artificial Intelligence & Data Science, "
        "AWS Academy training in Cloud Foundations and Generative AI Foundations, and a "
        "6-month Python with AI & ML internship. Built and deployed two full-stack web "
        "applications using Python, Java, Flask and SQL, with hands-on experience in "
        "REST APIs, relational database design, authentication, authorization and debugging."
    )
}

SKILLS = [
    ("Python", "Programming"),
    ("Flask", "Backend"),
    ("REST APIs", "Backend"),
    ("SQL", "Database"),
    ("Java", "Programming"),
    ("JavaScript", "Frontend"),
    ("HTML5 / CSS3", "Frontend"),
    ("Bootstrap", "Frontend"),
    ("MySQL / SQLite", "Database"),
    ("Git", "Tools"),
    ("AWS Fundamentals", "Cloud"),
    ("Machine Learning", "AI / ML"),
]

PROJECTS = [
    {
        "title": "AI-Based Coding Platform",
        "type": "Team Project · Flask Backend Developer",
        "stack": ["Python", "Flask", "SQLite", "HTML", "CSS"],
        "icon": "bi-code-slash",
        "description": "A platform designed to replace slow manual code review with real-time automated code evaluation.",
        "highlights": [
            "Implemented secure authentication and role-based access control for admin and user roles.",
            "Built problem management with custom test-case validation.",
            "Implemented a multi-language code execution engine with automated result verification.",
            "Automated the evaluation workflow to provide instant feedback."
        ]
    },
    {
        "title": "Smart Service Booking & Management System",
        "type": "Flask Backend Developer",
        "stack": ["Python", "Flask", "SQLite", "HTML", "CSS", "Bootstrap"],
        "icon": "bi-calendar-check",
        "description": "A secure real-time system that digitizes offline service booking and management workflows.",
        "highlights": [
            "Designed RESTful APIs for authentication, service management and bookings.",
            "Supported admin, service provider and customer roles.",
            "Implemented password encryption and Flask-Mail notifications.",
            "Built a modular backend with optimized database queries."
        ]
    }
]

EDUCATION = [
    ("B.Tech", "Artificial Intelligence & Data Science", "Muthayammal Engineering College (Autonomous), Rasipuram — Anna University", "2022 – 2026", "CGPA: 7.64 / 10"),
    ("Intermediate", "MPC", "Narayana Junior College, Gudur — BIEAP State Board", "2020 – 2022", "75.4%"),
    ("High School", "SSC", "Narayana E-Techno School, Gudur — BSEAP State Board", "2020", "96%"),
]

CERTIFICATIONS = [
    ("AWS Academy Graduate — Cloud Foundations", "20 course hours · Issued 09/03/2024", "https://credly.com/go/Mh8CQO0n"),
    ("AWS Academy Graduate — Generative AI Foundations", "12 course hours · Issued 09/22/2025", "https://credly.com/badges/006347e3-b0c2-4b7e-8e74-ee17e98fd7c4"),
    ("Foundations of Cloud IoT Edge ML — NPTEL", "NPTEL Certification", None),
    ("Distributed Systems — NPTEL", "NPTEL Certification", None),
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        profile=PROFILE,
        skills=SKILLS,
        projects=PROJECTS,
        education=EDUCATION,
        certifications=CERTIFICATIONS,
    )

@app.get("/resume")
def view_resume():
    return send_from_directory(BASE_DIR, "resume.pdf", mimetype="application/pdf")

@app.get("/download-cv")
def download_cv():
    return send_from_directory(
        BASE_DIR,
        "resume.pdf",
        mimetype="application/pdf",
        as_attachment=True,
        download_name="Korapati-Sreedhar-CV.pdf",
    )

@app.post("/contact")
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        flash("Please fill in all contact fields.", "danger")
        return redirect(url_for("home") + "#contact")

    if "@" not in email or len(email) > 160:
        flash("Please enter a valid email address.", "danger")
        return redirect(url_for("home") + "#contact")

    db.session.add(ContactMessage(name=name, email=email, message=message))
    db.session.commit()
    flash("Thanks! Your message has been received.", "success")
    return redirect(url_for("home") + "#contact")

@app.get("/api/profile")
def api_profile():
    return jsonify(PROFILE)

@app.get("/health")
def health():
    return {"status": "ok", "service": "sreedhar-portfolio"}

if __name__ == "__main__":
    app.run(debug=True)
