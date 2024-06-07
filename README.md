# Telecom Customer Management System

This project is a Django Rest API for managing telecom company customers. It handles the registration of new customers, plan selection, plan renewal, and plan upgrades/downgrades.

## Table of Contents

- Installation
- Testing
- API Endpoints
- Data Models

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/abhisheksahu92/telecom-customer-management.git
    ```
2. Change into the project directory:
    ```sh
    cd telecom-customer-management/telecom_system
    ```
3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Apply the migrations:
    ```sh
    python manage.py migrate
    ```
5. Start the development server:
    ```sh
    python manage.py runserver
    ```

### Testing
   ```sh
    python manage.py test customers
   ```

### API Endpoints
Please import Postman Json file to view all endpoints.

## Data Models

### Customer
- **Fields:**
  - `name`: CharField
  - `dob`: DateField
  - `email`: EmailField
  - `adhar_number`: CharField (12 Digits)
  - `registration_date`: DateField
  - `assigned_mobile_number`: CharField (10 Digits)

### Plan
- **Fields:**
  - `name`: CharField (Choices: Platinum365, Gold180, Silver90)
  - `cost`: IntegerField (Choices: 499, 299, 199)
  - `validity`: IntegerField (Choices: 365, 180, 90)
  - `status`: CharField (Choices: Active, Inactive)

### CustomerPlan
- **Fields:**
  - `customer`: ForeignKey (Customer)
  - `plan`: ForeignKey (Plan)
  - `renewal_date`: DateField
  - `existing_plan_name`: CharField
  - `new_plan_name`: CharField
  - `plan_status`: CharField (Choices: Active, Inactive)

