# Vendor-Management-Project
Vendor Management Project 


# Authentication
For authentication purpose you can use the token below as a **Bearer token** 
inorder to access the routes of Vendor Management System


TOKEN = **"e{yJ0[eXAiOiJKV1#QiL!CJhbGc$=i><]OiJ@IUz}I1NiJ9"** 



# Postman Workspace
Postman workspace ID **d0a828c2-4c8a-4183-b64b-7dce61dfe29d**


# ALL API Routes


## 1- Vendor Profile Management Routes
- **GET** http://127.0.0.1:8000/api/vendors/    (List all vendors.)
- **POST** http://127.0.0.1:8000/api/vendors/   (Create a new vendor)
- **GET** http://127.0.0.1:8000/api/vendors/<vendor_id>/    (Retrieve a specific vendor's details)
- **PUT** http://127.0.0.1:8000/api/vendors/<vendor_id>/    (Update a vendor's details.)
- **DELETE** http://127.0.0.1:8000/api/vendors/<vendor_id>/ (Delete a vendor)


## 2- Purchase Order Tracking
- **GET** http://127.0.0.1:8000/api/purchase_orders/
- **POST** http://127.0.0.1:8000/api/purchase_orders/
- **GET** http://127.0.0.1:8000/api/purchase_orders/<purchase_orders_id>/
- **PUT** http://127.0.0.1:8000/api/purchase_orders/<purchase_orders_id>/
- **DELETE** http://127.0.0.1:8000/api/purchase_orders/<purchase_orders_id>/


## 3- Vendor Performance Evaluation
- **GET** http://127.0.0.1:8000/api/vendors/<vendor_id>/performance/
- **POST** http://127.0.0.1:8000/api/purchase_orders/<purchase_orders_id>/acknowledge/
