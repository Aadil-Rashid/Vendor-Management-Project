# Vendor Management Project

## Authentication
To authenticate, you can use the token below as a **Bearer token** to access the routes of Vendor Management System.

TOKEN = **"e{yJ0[eXAiOiJKV1#QiL!CJhbGc$=i><]OiJ@IUz}I1NiJ9"**

## Postman Workspace
Postman workspace ID: **d0a828c2-4c8a-4183-b64b-7dce61dfe29d**
Postman_workspace_link : [Debug Url](https://www.postman.com/lively-meadow-351188/workspace/d0a828c2-4c8a-4183-b64b-7dce61dfe29d/collection/17525478-b38d2f2e-56d7-4413-a338-2eb01e65ac40?action=share&creator=17525478)

## All API Routes
**base_url** = http://127.0.0.1:8000

### 1- Vendor Profile Management Routes

>> Postman_doc_link : [Debug Url](https://documenter.getpostman.com/view/17525478/2sA3JGeiPT)

- **GET**: List all vendors
    - **base_url**/api/vendors/

- **POST**: Create a new vendor
    - **base_url**/api/vendors/

- **GET**: Retrieve a specific vendor's details
    - **base_url**/api/vendors/**<vendor_id>**/

- **PUT**: Update a vendor's details
    - **base_url**/api/vendors/**<vendor_id>**/

- **DELETE**: Delete a vendor
    - **base_url**/api/vendors/**<vendor_id>**/


### 2- Purchase Order Tracking
>> Postman_doc_link : [Debug Url](https://documenter.getpostman.com/view/17525478/2sA3JGeiPW)

- **GET**: List all purchase orders
    - **base_url**/api/purchase_orders/

- **POST**: Create a new purchase order
    - **base_url**/api/purchase_orders/

- **GET**: Retrieve a specific purchase order's details
    - **base_url**/api/purchase_orders/**<purchase_orders_id>**/

- **PUT**: Update a purchase order's details
    - **base_url**/api/purchase_orders/**<purchase_orders_id>**/

- **DELETE**: Delete a purchase order
    - **base_url**/api/purchase_orders/**<purchase_orders_id>**/


### 3- Vendor Performance Evaluation
>> Postman_doc_link : [Debug Url](https://documenter.getpostman.com/view/17525478/2sA3JGeiPX)

- **GET**: View performance evaluation for a specific vendor
    - **base_url**/api/vendors/**<vendor_id>**/performance/

- **POST**: Update Acknowledgment Endpoint
    - **base_url**/api/purchase_orders/**<purchase_orders_id>**/acknowledge/
