# RiskLens

RiskLens is a lightweight cybersecurity asset exposure assessment platform designed to help organizations identify exposed network services, assess potential security risks, and maintain a history of security scans. It provides an intuitive way to scan network assets, detect open ports, classify risks, and generate actionable security recommendations.

---

## Features

* Asset management
* TCP port scanning
* Open service detection
* Risk severity classification
* Security recommendations for detected services
* Scan history management
* RESTful API built with Flask

---

## Tech Stack

### Backend

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Migrate
* SQLite

### Frontend (still In Progress)

* HTML5
* Tailwind CSS
* JavaScript

---

## Project Structure

```text
risklens/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── utils/
│   └── __init__.py
│
├── migrations/
├── scripts/
├── run.py
├── config.py
├── requirements.txt
└── README.md
```

---


### Clone the repository

```bash
git clone https://github.com/halcyon4975-ux/risklens.git
cd risklens
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```



### Install dependencies

```bash
pip install -r requirements.txt
```

### Apply database migrations

```bash
flask db upgrade
```

### Run the application

```bash
python run.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

---

## API Endpoints

### Assets

| Method | Endpoint       | Description               |
| ------ | -------------- | ------------------------- |
| POST   | `/assets`      | Create a new asset        |
| GET    | `/assets`      | Retrieve all assets       |
| GET    | `/assets/<id>` | Retrieve a specific asset |

### Scans

| Method | Endpoint                   | Description           |
| ------ | -------------------------- | --------------------- |
| POST   | `/assets/<asset_id>/scan`  | Start a scan          |
| GET    | `/scans/<scan_id>`         | Retrieve scan results |
| GET    | `/assets/<asset_id>/scans` | Retrieve scan history |

---

## Current Workflow

```text
Create Asset
      │
      ▼
Start Scan
      │
      ▼
Port Discovery
      │
      ▼
Service Identification
      │
      ▼
Risk Classification
      │
      ▼
Store Scan Results
      │
      ▼
Retrieve Historical Results
```

---

## Current Project Status

Backend MVP 70% completed.

Implemented:

* Asset management
* Port scanning engine
* Scan result storage
* Risk severity classification
* Historical scan retrieval
* REST API

Frontend dashboard and user interface are currently under development.

---

## Future Improvements


* Dashboard analytics
* Authentication and authorization
* Scheduled scans
* Export scan reports
* CVE integration
* Scan profile customization
* Asset search and filtering

---

## License

This project is developed for educational purposes and cybersecurity research.

## Authur
Derick