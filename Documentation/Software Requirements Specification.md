<h1 align="center">Web application for accounting of goods in the warehouse of the enterprise</h1>

## Vision

"Web application for accounting of goods in 
the warehouse of the enterprise"
is an application that allows you to record
information about goods that are stored 
in warehouses of enterprises.

Application should provide:

* Storing a list of products
in a database;
* Displaying a list of products ;
* Updating the list of products
(adding, editing, deleting);
* Display of the list of products sold ;
* Updating the list of products sold
(adding, editing, deleting);
* Filtering by date of sale;
* Display of the list of decommissioned goods ;
* Updating the list of decommissioned goods
(adding, editing, deleting);
* Filtering by the date of debiting;

## 1. Products
### 1.1 Display list of products
The mode is designed to view the list of products.

<b>Main scenario</b>:
* User selects item “Products”;
* Application displays list of Products.

![](Products.PNG)

Pic. 1.1 View the products list.

The list displays the following columns:
* ID – department number;
* Products - name of the products;
* Nubmer of products - number of products in stock;
* Unit of measurement - in what value is our product measured
* Unit price $ - price per product
* Product photo - photos of our product
### 1.2 Add product

<b>Main scenario</b>:
* Administrator clicks the “Add” button in the 
products list view mode;
* Application displays form to enter department 
data(pic. 1.2);
* Administrator enters products data and presses 
“Save” button;
* If any data is entered incorrectly, incorrect 
data messages are displayed(pic. 1.2.1);
* If entered data is valid, then record is adding 
to database;
* If new product record is successfully added,
then list of products with added records is displaying.

<b>Cancel operation scenario</b>:
* Administrator clicks the “Add” button in the 
products list view mode;
* Application displays form to enter product data;
* Administrator enters product data and 
presses “Cancel” button;
* Data don’t save in database, then list of 
products records is displaying to administrator.
* If the administrator selects the menu item 
"Products", "Sold" or "Decommissioned", the data will not be saved to the 
database and the corresponding form with updated data
will be opened.

![](Add_Product.PNG)

Pic. 1.2 Add product.

<b>When adding a product, the following 
details are entered:</b>
* Products name - name of the products;
* Nubmer of products - number of products in stock;
* Unit of measurement - in what value is our product measured;
* Unit price $ - price per product;
* Product photo - photos of our product;


<b>If the data is entered incorrectly, it will display the corresponding error.</b>

![](Errors_Add_Product.PNG)

Pic. 1.2.1 Error when adding.

### 1.3 Edit product

<b>Main scenario:</b>
* Administrator clicks the “Edit” button in 
the product list view mode;
* Application displays form to enter 
product data (pic. 1.3);
* Administrator edit product 
data and presses “Save” button;
* If any data is entered incorrectly, 
incorrect data messages are displayed (pic. 1.3.1);
* If entered data is valid, then edited data 
is added to database;
* If department record is successfully edited, then 
list of products with added records is displaying. 

<b>Cancel operation scenario:</b>
* Administrator clicks the “Edit” button in the 
product list view mode;
* Application displays form to enter product data;
* Administrator enters product data and presses 
“Cancel” button;
* Data don’t save in database, then list of 
product records is displaying to administrator.
* If the administrator selects the menu 
item "Products", "Sold" or "Decommissioned", the data 
will not be saved to the database and the corresponding 
form with updated data will be opened.

![](Edit_Product.PNG)

Pic. 1.3 Edit product.

<b>When editing a product, the following details 
are entered:</b>
* Products name - name of the products;
* Nubmer of products - number of products in stock;
* Unit of measurement - in what value is our product measured;
* Unit price $ - price per product;
* Product photo - photos of our product;

<b>If the data is entered incorrectly, it will 
display the corresponding error.</b>

![](Errors_Edit_Production.PNG)

Pic. 1.3.1 Error when editing.

### 1.4 Removing the product

<b>Main scenario:</b>
* Administrator, while in the list of products 
presses the "Delete" button in the selected product line;
* If the product can be removed, a confirmation 
dialog is displayed;
* In the selected dialog box, you must select
an operation: "Delete", "Put in 'Sold'", "Put in 
'Decommissioned'" (pic. 1.4);
* If the administrator selects the 'Delete' operation, the 
record is deleted from the database;
* If the administrator selects the 'Put in "Sold" operation',
the record is transferred to the database of the 'Sold' section;
* If the administrator selects the 'Put in "Decommissioned"'
operation, the record is transferred to the database of 
the 'Decommissioned' section;
* If a product record has been successfully deleted, a 
list of products without deleted records is displayed.
* If the product record has been successfully moved to the
"Decommissioned" or "Sold" section, a data field will 
be added to the desired column;

![](Delete_Product.PNG)

Pic. 1.4 Delete product dialog.

<b>Operation cancellation scenario:</b>
* The administrator is in the display mode of the list 
of products and presses the "Delete" button;
* The application displays a dialog box for selecting the 
action "What to do with this product?";
* The administrator presses the ”Cancel" button;
* The list of products without changes is displayed. 

