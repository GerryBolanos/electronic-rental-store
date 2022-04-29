
# Electronic Rental Store

### Team Members
Gerardo Bolanos and July Pham

## Project Description
This project is a website that can be used to manage the inventory
for an electronics rental store. The items customers will be able to 
rent are laptops, tablets and mobile phones of various screen sizes,
operating systems and refresh rates. The main purpose of this website
will be to provide an inventory/catalog tool for a small rental store 
where customers can browse and rent any of the electronic devices available. 
Users of the application will also be able to view current stock of any item and will be able 
to issue rent relationships to the customers. The application will enable users to also 
manage the inventory - meaning they’ll be able to see what electronic 
device customers have rented and when they’re scheduled to return the item(s).

### Note
To make it easier to follow the necessary steps to get credit for this course, we're opting to use RAW queries
so that we can create parametrized queries that mimic PreparedStatements in Django, while also
having the option to call stored procedures and functions.

## Tech Stack
This project was created using Django which then connects to a MySQL database. The app itself is hosted on heroku while the database is hosted on an AWS RDS instance.

## Tables
This project consist of 5 main Tables.  
- CUSTOMER 
- ELECTRONICS
- PHONE
- RENTS
- LAPTOP (our materialized view for this project)

## Views
We have two views which represent 2/3 of our subclassese. (The 3rd subclass, Laptop, is represented by the materialized view specified in the tables section)
- MOBILEPHONE
- TABLET

## Function or Stored Procedures
We chose to use a function in this project that is used to retrieve the sum of the stock items for each of the subclass category. These numeric values can be seen on the main inventory page.

## Usability
There are 4 different pages within this web app.
- ```/inventory``` - serves as the main page with 4 separate tables. The first displays all the inventory (ELECTRONICS) table while the others show only the attributes that are specific to that subclass.
- ```/addItem``` - allows user to input a new item into the ELECTRONICS table. Depending on what the elctronic type is, the triggers will run to update the materialized view.
- ```/rentItem``` - allows users to rent a particular electronic item.
- ```/rented``` - displays the items that are currently loaned to specific customers.
