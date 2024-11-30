# Customer Support Application

## Overview
This is a **Django-based web application** designed to provide customer services for gas utilities. It allows customers to create and track service requests while enabling support staff to view, filter, and update the status of these requests.

---

## Features

### Customer Functionality
- **Login/Register:** Secure authentication for customers.
- **Create Service Requests:** Submit requests with optional file attachments.
- **Track Requests:** View details and status updates for submitted requests.

### Support Staff Functionality
- **Login/Register:** Role-based access for support staff.
- **Dashboard:** View and filter service requests by status.
- **Request Management:** Update the status of service requests.

### Admin Functionality
- Manage users, including assigning roles (`is_support_staff`).
- View and edit service request details via Django admin.

---

## Installation and Setup

### Prerequisites
- Python 3.10+
- Django 4.2+
- SQLite (or any preferred database)

### Steps
1. **Clone the Repository**
   ```bash
   git clone <repo_url>
   cd customer_support_app
