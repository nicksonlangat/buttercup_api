# Buttercup_api

## APP SCREENS
Please follow [this link](https://github.com/nicksonlangat/buttercup.git) which has the app screens

## PROJECT BRIEF
Buttercup is an online e-commerce shop that stocks a wide variety of flowers. You are welcome to view flower catalog, individual flower detail, add flowers to your basket, place an order and schedule delivery and pick up. This repo houses all the server related code written in Python, Django and Django Rest Framework.

The frontend part of this project is found [in this repo](https://github.com/nicksonlangat/buttercup.git) and is written using JavaScript, Vue Js and Tailwind CSS.
The live demo of this project is accessible [via this link](http://localhost:8080/) so go ahead and try it out.

## FEATURES
- **Responsiveness**. This project can be viewed both on desktop browsers and mobile browsers and will adapt accordingly giving the user a smooth shopping experience.
- **List page**. This page displays all flowers in the database that potential buyers can browse through in search for what they need.
- **Detail page**. Each individual flower has a dedicated page with full information regarding it and call to action buttons.
- **Search input**. This functionality is handy when a potential buyer is looking for a specific flower and saves time used in browsing through the list page.
- **Shopping cart**. This is acts as a basket that the users add flowers that they would like to order.
- **Register & Login pages**. These pages allow users to create user accounts that they can use to place orders.

## CHANGELOG

### Version 1.0.1
#### New Features
- Added ability to add items to cart
- Added ability to remove items from cart
- Added ability clear the cart from current session
#### Bug fixes
- No bug fixes in this release

### Version 1.0.0
#### New Features
- Added category CRUD endpoints
- Added flowers CRUD endpoints
- Added cart service that uses sessions
- Added cart endpoints
#### Bug fixes
- No bug fixes in this release

## LOCAL DEV INSTALLATION
Follow the following commands in the directory you want to run the project in.

### Setting up and Activating a Virtual Environment
- Create a working space in your local machine
- Clone this [repository](https://github.com/nicksonlangat/buttercup_api.git) `git clone https://github.com/nicksonlangat/buttercup_api.git`
- Navigate to the project directory
- Create a virtual environment `python3 -m venv name_of_your_virtual_environment` and activate it `source name_of_your_virtual_environment/bin/activate`
- Create a .env file in root directory and put these key=values in it:
```
DEBUG=on
SECRET_KEY='your secret key'
DB_NAME='your_db_name'
DB_USER='your_db_user'
DB_PASSWORD='your_db_password'
DB_PORT='5432'
DB_HOST='localhost'

```
- Install dependencies to your virtual environment `pip install -r requirements.txt`
- Migrate changes to the newly created database `python manage.py migrate`

## Starting the server
- Ensure you are in the project directory on the same level with `manage.py` and the virtual environment is activated
- Run the server `python manage.py runserver`
- Find the API documentation via `localhost:8000/docs` for API request endpoints. You can get what each endpoint requires for a successful call.
- The project configs and settings is in the folder `mysite`
- Main app is `core`
  
