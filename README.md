# Vendor-Management-Project
Vendor Management Project 


# Authentication
For authentication purpose you can use the token below as a **Bearer token** 
inorder to access the routes of Vendor Management System


TOKEN = **"e{yJ0[eXAiOiJKV1#QiL!CJhbGc$=i><]OiJ@IUz}I1NiJ9"** 



# Postman Workspace
Postman workspace ID **d0a828c2-4c8a-4183-b64b-7dce61dfe29d**


# ALL API Routes
**domain** = http://127.0.0.1:8000

### 1- Vendor Profile Management Routes
- **GET**: List all vendors

    -- **domain**/api/vendors/    

- **POST**: Create a new vendor

    -- **domain**/api/vendors/  

- **GET**: Retrieve a specific vendor's details
    
    -- **domain**/api/vendors/<vendor_id>/ 

- **PUT**: Update a vendor's details
    
    -- **domain**/api/vendors/<vendor_id>/ 

- **DELETE**: Delete a vendor
    
    -- **domain**/api/vendors/<vendor_id>/


### 2- Purchase Order Tracking
- **GET** http://127.0.0.1:8000/api/purchase_orders/
- **POST** http://127.0.0.1:8000/api/purchase_orders/
- **GET** http://127.0.0.1:8000/api/purchase_orders/<purchase_orders_id>/
- **PUT** http://127.0.0.1:8000/api/purchase_orders/<purchase_orders_id>/
- **DELETE** http://127.0.0.1:8000/api/purchase_orders/<purchase_orders_id>/


### 3- Vendor Performance Evaluation
- **GET** http://127.0.0.1:8000/api/vendors/<vendor_id>/performance/
- **POST** http://127.0.0.1:8000/api/purchase_orders/<purchase_orders_id>/acknowledge/





# Vendor Management Project

## Authentication
To authenticate, you can use the token below as a **Bearer token** to access the routes of Vendor Management System.

TOKEN = **"e{yJ0[eXAiOiJKV1#QiL!CJhbGc$=i><]OiJ@IUz}I1NiJ9"**

## Postman Workspace
Postman workspace ID: **d0a828c2-4c8a-4183-b64b-7dce61dfe29d**

## All API Routes
**domain** = http://127.0.0.1:8000

### 1- Vendor Profile Management Routes
- **GET**: List all vendors
    - **domain**/api/vendors/
- **POST**: Create a new vendor
    - **domain**/api/vendors/
- **GET**: Retrieve a specific vendor's details
    - **domain**/api/vendors/<vendor_id>/
- **PUT**: Update a vendor's details
    - **domain**/api/vendors/<vendor_id>/
- **DELETE**: Delete a vendor
    - **domain**/api/vendors/<vendor_id>/

### 2- Purchase Order Tracking
- **GET**: List all purchase orders
    - **domain**/api/purchase_orders/
- **POST**: Create a new purchase order
    - **domain**/api/purchase_orders/
- **GET**: Retrieve a specific purchase order's details
    - **domain**/api/purchase_orders/<purchase_orders_id>/
- **PUT**: Update a purchase order's details
    - **domain**/api/purchase_orders/<purchase_orders_id>/
- **DELETE**: Delete a purchase order
    - **domain**/api/purchase_orders/<purchase_orders_id>/

### 3- Vendor Performance Evaluation
- **GET**: View performance evaluation for a specific vendor
    - **domain**/api/vendors/<vendor_id>/performance/
- **POST**: Acknowledge a purchase order for performance evaluation
    - **domain**/api/purchase_orders/<purchase_orders_id>/acknowledge/
