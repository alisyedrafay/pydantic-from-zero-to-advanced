# Learn Pydantic

A hands-on project to understand and practice **Pydantic** for data validation, parsing, and type-safe modeling in Python.

---

## 📌 What is Pydantic?

Pydantic is a Python library that uses **type hints** to validate, parse, and manage data. It is widely used in **FastAPI**, backend services, and AI/ML pipelines for ensuring clean and reliable data.

---

## 🎯 Project Goals

* Understand Pydantic models and type annotations
* Perform data validation and parsing
* Use field constraints and default values
* Work with nested models
* Handle custom validators
* Learn real-world use cases

---

## 🧱 Topics Covered

* BaseModel
* Field validation
* Data type enforcement
* Optional & required fields
* Nested models
* Custom validators
* Error handling
* Pydantic v1 vs v2 basics

---

## 📂 Suggested Folder Structure

```
learn-pydantic/
│── basics/
│   ├── simple_model.py
│   ├── type_validation.py
│
│── advanced/
│   ├── nested_models.py
│   ├── custom_validators.py
│
│── examples/
│   ├── user_schema.py
│   ├── api_payload.py
│
│── requirements.txt
│── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Install Pydantic

```bash
pip install pydantic
```

For Pydantic v2:

```bash
pip install pydantic>=2.0
```

---

### 2️⃣ Simple Example

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

user = User(id=1, name="Ali", email="ali@example.com")
print(user)
```

---

## ✅ Why Use Pydantic?

* Automatic data validation
* Clean and readable schemas
* Strong typing
* Seamless FastAPI integration
* Better error handling

---

## 🛠 Use Cases

* FastAPI request/response models
* Data validation in ML pipelines
* Configuration management
* API payload validation
* JSON parsing

---

## 📖 Who Is This For?

* Python beginners
* Backend developers
* AI/ML engineers
* Students learning data validation

---

## 🤝 Contributions

Contributions, improvements, and suggestions are welcome.
Feel free to fork and experiment.

---

## ⭐ Support

If you find this helpful, consider giving it a ⭐ on GitHub.

---

Happy Learning 🚀
