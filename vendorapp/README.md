# Vendor Management System API Documentation

## Introduction
Welcome to the Vendor Management System API documentation. This API allows you to manage vendors, track purchase orders, and calculate vendor performance metrics. The API is built using Django and Django REST Framework.

## Authentication
All endpoints require token-based authentication. You need to obtain a JWT token by authenticating with your credentials using the `/token/` endpoint. This token should be included in the `Authorization` header of your requests.

### Endpoints:
- `/token/`: Obtain JWT token (POST)
- `/token/refresh/`: Refresh JWT token (POST)

## Vendor Management
This section includes endpoints for managing vendors.

### Vendor Profile Management:
- `POST /api/vendors/`: Create a new vendor.
- `GET /api/vendors/`: List all vendors.
- `GET /api/vendors/{vendor_id}/`: Retrieve details of a specific vendor.
- `PUT /api/vendors/{vendor_id}/`: Update a vendor's details.
- `DELETE /api/vendors/{vendor_id}/`: Delete a vendor.

## Purchase Order Tracking
This section includes endpoints for tracking purchase orders.

### Purchase Order Management:
- `POST /api/purchase_orders/`: Create a new purchase order.
- `GET /api/purchase_orders/`: List all purchase orders with an option to filter by vendor.
- `GET /api/purchase_orders/{po_id}/`: Retrieve details of a specific purchase order.
- `PUT /api/purchase_orders/{po_id}/`: Update a purchase order.
- `DELETE /api/purchase_orders/{po_id}/`: Delete a purchase order.

## Vendor Performance Evaluation
This section includes endpoints for evaluating vendor performance metrics.

### Performance Metrics:
- `GET /api/vendors/{vendor_id}/performance/`: Retrieve performance metrics for a specific vendor.

## Additional Information
- **Authentication**: Token-based authentication is required for all endpoints.
- **Error Handling**: Proper error responses are provided for invalid requests.
- **Data Validation**: Input data is validated according to defined model constraints.
- **PEP 8 Compliance**: Python code follows PEP 8 style guidelines for readability.
- **Swagger UI**: Swagger UI is integrated for easy API exploration and testing.

For detailed information on each endpoint, refer to the API documentation or Swagger UI.

---

## Running the Project

Follow these steps to run the project:

1. Clone the repository:
   ```bash
   git clone [Vendor Management Repository](https://github.com/Alfastrek/Vendor-Management.git)

2. Navigate to the project directory:
   ```bash
   cd vendorapp

3. Install required dependecies:
   ```bash
   pip install -r requirements.txt

4. Apply database migrations:
   ```bash
   python manage.py migrate

5. Run the development server:
   ```bash
   python manage.py runserver

6. Access the API documentation at:
   ```bash
   http://localhost:8000/
