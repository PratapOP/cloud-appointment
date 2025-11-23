# 🏥 Cloud Appointment Booking System  
A cloud-ready **Doctor Appointment Booking System** built using **Flask, MySQL, HTML, CSS, JS**.

This project allows:
- Patients to book appointments  
- Doctors to view appointments  
- Admins to manage doctors & patients  
- Secure login system  
- Professional UI  
- Cloud deployment support (Render)

---

## 🚀 Features

### 👤 **Patient Features**
- Register/Login  
- Book appointment  
- Select doctor from dropdown  
- Select symptoms from 20+ checklist  
- View booked appointments  
- Cancel appointment (optional feature)

### 🧑‍⚕️ **Doctor Features**
- Doctor login  
- See only their assigned appointments  
- View patient details, timing & symptoms  
- Update appointment status  
 
### 🛠️ **Admin Features**
- Admin login  
- Add / Edit / Delete doctors  
- Add / Edit / Delete patients  
- View all appointments  
- Manage system data

---

## 🧰 Tech Stack

### **Frontend**
- HTML5  
- CSS3  
- JavaScript  

### **Backend**
- Python Flask  
- Flask-Session  
- Flask-SQLAlchemy  

### **Database**
- MySQL (Local)  
- PostgreSQL (Cloud – Render)

### **Cloud Platform**
- Render (FREE Hosting)

---

## 📁 Project Structure

cloud-appointment/
│── app.py
│── models.py
│── requirements.txt
│── render.yaml
│── README.md
│
├── templates/
│ ├── login.html
│ ├── register.html
│ ├── dashboard.html
│ ├── doctor.html
│ ├── book.html
│ ├── admin.html
│ ├── admin_doctors.html
│ ├── admin_patients.html
│ └── admin_edit_doctor.html
│
└── static/
├── style.css
└── script.js

yaml
Copy code

---

## 🗄️ Database ER Diagram (Simple)

+-----------+ +-------------+ +----------------+
| User | | Doctor | | Appointment |
+-----------+ +-------------+ +----------------+
| id | 1 ─| id |─ M | id |
| username | | name | | user_id |
| password | | speciality | | doctor_id |
| role | | experience | | date |
+-----------+ +-------------+ | time |
| symptoms |
| status |
+----------------+

yaml
Copy code

---

## ⚙️ How to Run Locally

### 1️⃣ Install dependencies
pip install -r requirements.txt

graphql
Copy code

### 2️⃣ Update your MySQL credentials inside `app.py`
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:YOUR_PASSWORD@localhost/cloud_appointments"

shell
Copy code

### 3️⃣ Create database in MySQL
CREATE DATABASE cloud_appointments;

shell
Copy code

### 4️⃣ Run the app
python app.py

yaml
Copy code

App will run on:

👉 **http://127.0.0.1:5000/**

---

## ☁️ Cloud Deployment (FREE on Render)

### 1️⃣ Push project to GitHub  
(Already done!)

### 2️⃣ Create **render.yaml**  
(Already added)

### 3️⃣ Go to Render → Create New → Web Service  
- Select your GitHub repo  
- Choose **Free Plan**  
- Render automatically detects `render.yaml`  
- Deploy

### 4️⃣ Create FREE Database on Render  
- PostgreSQL Free Tier  
- Replace SQLAlchemy URI with Render database URI  

✨ Done! Your project is now cloud-hosted.

---

## 📸 Screenshots (Add These)

### 🔹 Login Page  
(Add screenshot)

### 🔹 Book Appointment Page  
(Add screenshot)

### 🔹 Admin Panel  
(Add screenshot)

### 🔹 Doctor Dashboard  
(Add screenshot)

---

## 📘 Submission Notes (Cloud Computing Practical)

This project covers:
- SaaS-style web application  
- Cloud deployment using PaaS  
- Database management on cloud  
- Authentication & authorization  
- Full-stack implementation  
- Git-based version control  

Perfect for academic submission ✔

---

## 👨‍💻 Developed By
**Abhiuday Pratap Singh**  
CSE Undergraduate | Python & Web Developer  

---

# 🎉 You're Ready for Submission!
Your GitHub is now perfect for your Cloud Practical.

If you want:

✅ Help writing **Practical File PDF**  
✅ Deployment to Render  
✅ Database migration steps  
✅ More screenshots  
➡️ Just tell me!
