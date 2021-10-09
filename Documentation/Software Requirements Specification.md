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
* Filtering by freshness of products.
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

Main scenario:
* User selects item “Products”;
* Application displays list of Products.

![](Products.PNG)
<br>Pic. 1.1 View the products list.

The list displays the following columns:
* ID – department number;
* Products - name of the products;
* Nubmer of products - number of products in stock;
* Price $ - average salary of all employees of the department
### 1.2 Add department

Main scenario:
* Administrator clicks the “Add” button in the 
department list view mode;
* Application displays form to enter department 
data(pic. 1.2);
* Administrator enters department data and presses 
“Save” button;
* If any data is entered incorrectly, incorrect 
data messages are displayed(pic. 1.3);
* If entered data is valid, then record is adding 
to database;
* If error occurs, then error message is
displaying(pic. 1.4);
* If new department record is successfully added,
then list of departments with added records is displaying.

Cancel operation scenario:
* Administrator clicks the “Add” button in the 
department list view mode;
* Application displays form to enter department data;
* Administrator enters department data and 
presses “Cancel” button;
* Data don’t save in data base, then list of 
departments records is displaying to administrator.
* If the administrator selects the menu item 
"Department", "Employee", "Positions" or 
"Specialization", the data will not be saved to the 
database and the corresponding form with updated data
will be opened.

![](add_departmentt.jpg)
<br>Pic. 2.2 Add department.

<b>When adding a department, the following details are entered:</b>
* Name department - name department
* Add employee - adding department employees(optional field)


<b>If the data is entered incorrectly, it will display the corresponding error.</b>
![](add_error_department.jpg)
<br>Pic. 2.3 Error when adding.

![](add_error_department1.jpg)
<br>Pic. 2.4 Error when adding.
