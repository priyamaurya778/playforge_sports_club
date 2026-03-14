# 🏟️ PlayForge SportsClub – Django MVT Demo Project

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Django](https://img.shields.io/badge/Django-Framework-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📌 About the Project

**PlayForge SportsClub** is a beginner-friendly Django project created to demonstrate how the **MVT (Model–View–Template)** architecture works in Django.

This project includes **basic authentication features like login and logout** along with simple page rendering using Django templates.
It is intentionally kept **simple and easy to understand** so that new developers can explore how Django applications are structured.

This repository can also be used as a **starter template for learning or building small Django projects**.

---

## 🎯 Purpose

The main goal of this project is to help beginners:

* Understand the **Django project structure**
* Learn how **Models, Views, and Templates interact**
* See how **basic authentication works**
* Understand **URL routing in Django**
* Use the project as a **template for future projects**

---

## ⚙️ Features

* Simple Django project structure
* Demonstration of **MVT architecture**
* Basic **Login & Logout system**
* Django **template rendering**
* Beginner-friendly code
* Can be used as a **Django starter template**

---

## 📸 Project Demo

  ```
  ![Project Demo](static/club_app/images/demo.mp4)
  ```

## 📂 Project Structure

```
PlayForge Sportsclub/
│
├── manage.py
├── README.md
│
├── Sportsclub/        # Main Django project folder
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── app/               # Example Django app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── static/
│
└── .venv/             # Virtual environment
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```
git clone <https://github.com/priyamaurya778/sportsClub.git>
cd Sportsclub
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv .venv
```

---

### 3️⃣ Activate Virtual Environment

Windows:

```
.venv\Scripts\activate
```

Mac / Linux:

```
source .venv/bin/activate
```

---

### 4️⃣ Install Dependencies

```
pip install django
```

---

### 5️⃣ Apply Migrations

```
python manage.py migrate
```

---

### 6️⃣ Run the Development Server

```
python manage.py runserver
```

Open in your browser:

```
http://127.0.0.1:8000/
```

---

## 🧠 What You Can Learn From This Project

* Django **MVT architecture**
* URL routing
* Django templates
* Authentication basics
* Django project organization

---

## 🧩 Who Can Use This Project?

* Django beginners
* Students learning Django
* Developers exploring the **MVT pattern**
* Anyone who needs a **simple Django starter template**

---


## 👨‍💻 Author

Created as part of a **Django learning journey** to explore and understand the Django framework.
