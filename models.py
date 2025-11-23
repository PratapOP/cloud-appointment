from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """
    Users hold login credentials and role.
    role: 'patient' | 'doctor' | 'admin'
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default="patient", nullable=False)

class Doctor(db.Model):
    """
    Doctor profile linked to User account.
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)      # <--- FIX ADDED
    name = db.Column(db.String(100), nullable=False)
    speciality = db.Column(db.String(100))
    experience = db.Column(db.String(100))

class Appointment(db.Model):
    """
    Appointment record.
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    doctor_id = db.Column(db.Integer, nullable=False)
    doctor_name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    time = db.Column(db.String(50), nullable=False)
    issue = db.Column(db.String(300))
    symptoms = db.Column(db.String(500))
    status = db.Column(db.String(20), default="Pending")
