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

### Frontend 

* React
* Vite
* TypeScript

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



## API Endpoints

### 1. Create Asset

**POST** `/assets`

Creates a new asset using either an IP address or a domain name as the target.

**Request Body**

```json
{
    "name": "OWASP Juice Shop",
    "target": "owasp-juice.shop",
    "description": "Deliberately vulnerable web application"
}
```

**Response (201 Created)**

```json
{
    "message": "Asset created successfully",
    "asset": {
        "id": 1,
        "name": "OWASP Juice Shop",
        "target": "owasp-juice.shop",
        "ip_address": "81.169.145.156"
    }
}
```

---

### 2. Get All Assets

**GET** `/assets`

Returns all registered assets.

---

### 3. Start Scan

**POST** `/assets/{asset_id}/scan`

Starts a port scan for the specified asset.

**Example**

```
POST /assets/1/scan
```

**Response**

```json
{
    "message": "Scan created",
    "scan_id": 8,
    "status": "COMPLETED"
}
```

---

### 4. Get Scan Result

**GET** `/scans/{scan_id}`

Returns the detailed results of a completed scan.

**Example**

```
GET /scans/8
```

---

### 5. Get Scan History (Optional)

**GET** `/assets/{asset_id}/scans`

Returns all scans performed on a specific asset.

**Example**

```
GET /assets/1/scans
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

## Author
Derick