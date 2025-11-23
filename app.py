from flask import Flask, render_template, request, redirect, session, flash
from flask_session import Session
from models import db, User, Doctor, Appointment
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET", "supersecretkey")

# DB CONFIG
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Abhiuday17%40@localhost/cloud_appointments"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["SESSION_TYPE"] = "filesystem"
Session(app)
db.init_app(app)

# Symptom List
SYMPTOMS_POOL = [
    "Fever","Cold","Headache","Nausea","Fatigue","Stomach Pain",
    "Cough","Dizziness","Chest Pain","Breathing Issues",
    "High BP","Low BP","Muscle Pain","Joint Pain",
    "Skin Rash","Anxiety","Depression","Vomiting",
    "Diarrhea","Eye Pain","Ear Pain","Back Pain"
]

def current_user():
    uid = session.get("user_id")
    return User.query.get(uid) if uid else None


@app.route("/")
def home():
    return render_template("index.html")


# ---------------- REGISTER ----------------
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()
        role = request.form.get("role", "patient")

        if not username or not password:
            flash("Username and password required.", "error")
            return redirect("/register")

        if User.query.filter_by(username=username).first():
            flash("Username already exists.", "error")
            return redirect("/register")

        # Create user
        new_user = User(username=username, password=password, role=role)
        db.session.add(new_user)
        db.session.commit()

        # If doctor registers → create doctor profile
        if role == "doctor":
            doc = Doctor(
                name=username,
                speciality="",
                experience="",
                user_id=new_user.id
            )
            db.session.add(doc)
            db.session.commit()

        flash("Registration successful. Please login.", "success")
        return redirect("/login")

    return render_template("register.html")


# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()

        user = User.query.filter_by(username=username, password=password).first()
        if not user:
            flash("Invalid credentials.", "error")
            return redirect("/login")

        session["user_id"] = user.id
        session["role"] = user.role
        return redirect("/dashboard")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/login")

    if session["role"] == "admin":
        return redirect("/admin")
    if session["role"] == "doctor":
        return redirect("/doctor")

    appointments = Appointment.query.filter_by(user_id=session["user_id"]).all()
    return render_template("dashboard.html", appointments=appointments)


# ---------------- BOOK APPOINTMENT ----------------
@app.route("/book", methods=["GET","POST"])
def book():
    if "user_id" not in session:
        return redirect("/login")

    doctors = Doctor.query.all()

    if request.method == "POST":
        doctor_id = request.form["doctor_id"]
        date = request.form["date"]
        time_ = request.form["time"]
        issue = request.form.get("issue", "")
        symptoms = ",".join(request.form.getlist("symptoms"))

        doc = Doctor.query.get(doctor_id)

        appt = Appointment(
            user_id=session["user_id"],
            doctor_id=doc.id,
            doctor_name=doc.name,
            date=date,
            time=time_,
            issue=issue,
            symptoms=symptoms,
            status="Pending"
        )
        db.session.add(appt)
        db.session.commit()

        flash("Appointment booked!", "success")
        return redirect("/dashboard")

    return render_template("book.html", doctors=doctors, symptoms=SYMPTOMS_POOL)


# ---------------- ADMIN PANEL ----------------
@app.route("/admin")
def admin_home():
    if session.get("role") != "admin":
        return "Access Denied"

    appointments = Appointment.query.all()
    return render_template("admin.html", appointments=appointments)


# ---------------- DOCTOR DASHBOARD ----------------
@app.route("/doctor")
def doctor_dashboard():
    if session.get("role") != "doctor":
        return "Access Denied"

    user = current_user()
    doc = Doctor.query.filter_by(user_id=user.id).first()

    if not doc:
        return render_template("doctor.html", appointments=[])

    appointments = Appointment.query.filter_by(doctor_id=doc.id).all()
    return render_template("doctor.html", appointments=appointments)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
