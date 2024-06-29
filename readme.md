# Dat Straight E-commerce Platform

Dat Straight is a versatile E-commerce platform built with Django and React, supporting categories like fashion, groceries, and more. It features JWT authentication, custom user models, and seamless multi-vendor capabilities. The front end uses Vite for performance, with Stripe and PayPal integrations for secure payments.

## Features

- Versatile Categories: Supports various categories like fashion, groceries, and more, allowing for a wide range of products.
- JWT Authentication: Implements secure JWT authentication with custom user models for enhanced security and flexibility.
- Multi-vendor Support: Provides seamless multi-vendor capabilities, enabling multiple sellers to manage their products and sales.
- Front-end Performance: Utilizes React with Vite for superior performance, ensuring fast load times and a smooth user experience.
- Secure Payments: Integrated with Stripe and PayPal, offering secure and reliable payment options for users.

## Backend Technologies

- Django: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- Django REST Framework: A powerful and flexible toolkit for building Web APIs.
- JWT Authentication: JSON Web Token authentication for secure and stateless user authentication.
- Django CORS Headers: Handles Cross-Origin Resource Sharing (CORS) for secure interaction between the backend and frontend.

## Frontend Technologies

- React: A JavaScript library for building user interfaces, providing a component-based architecture.
- Vite: A build tool that significantly improves the performance of development and production builds.
- Axios: A promise-based HTTP client for making requests to the backend API.
- React Router: A collection of navigational components that compose declaratively with your application.

## Payment Integration

- Stripe: An online payment processing platform for internet businesses, integrated for secure payments.
- PayPal: A widely used payment gateway that enables users to make payments using various methods.

## User and Vendor Management

- Custom User Models: Tailored user models to accommodate specific requirements for both customers and vendors.
- Multi-vendor System: Allows multiple vendors to manage their own stores, products, and orders independently.

## Additional Features

- Product Management: Comprehensive product management system including listing, detail view, and categorization.
- Cart and Checkout System: Efficient cart and checkout system to streamline the purchasing process.
- Order Management: Robust order management for tracking, updating, and processing orders.
- Review and Rating System: Allows customers to leave reviews and ratings for products, enhancing user engagement.
- Notification System: Informs users and vendors about important updates and activities within the platform.

For more detailed information and step-by-step setup instructions, please feel free to reach out to me.

# Frontend Technologies

- React: A JavaScript library for building user interfaces, providing a component-based architecture.
- Vite: A build tool that significantly improves the performance of development and production builds.
- Axios: A promise-based HTTP client for making requests to the backend API.
- React Router: A collection of navigational components that compose declaratively with your application.

## Project Structure

The frontend project structure is as follows:

`DjangoReactEcommerce/
├── frontend/
│ ├── public/
│ │ ├── index.html
│ ├── src/
│ │ ├── components/
│ │ ├── pages/
│ │ ├── App.jsx
│ │ ├── index.js
│ │ ├── ...
│ ├── package.json
│ ├── vite.config.js`

## Integration with Backend

The frontend communicates with the backend via REST APIs. Axios is used for making HTTP requests to the backend. The main interactions include:

- Authentication: Handling user login, registration, and token management.
- Product Management: Fetching product lists, product details, and managing cart functionalities.
- Order Management: Handling the checkout process and order tracking.
- Payment Processing: Integrating with Stripe and PayPal for secure transactions.

## Key Components

- Product Listing: Displays a list of products fetched from the backend.
- Product Detail: Shows detailed information about a specific product.
- Cart: Manages the items added to the user's cart.
- Checkout: Facilitates the checkout process, including payment integration.
- User Authentication: Handles user login, registration, and profile management.

## Additional Features

- Responsive Design: Ensures the application is usable on various devices and screen sizes.
- State Management: Uses Zustand for efficient and simplified state management.
- Notification System: Provides real-time notifications to users about their activities and updates.

# Backend Technologies

- Django: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- Django REST Framework: A powerful and flexible toolkit for building Web APIs.
- JWT Authentication: JSON Web Token authentication for secure and stateless user authentication.
- Django CORS Headers: Handles Cross-Origin Resource Sharing (CORS) for secure interaction between the backend and frontend.

## Project Structure

The backend project structure is as follows:

`DjangoReactEcommerce/
├── backend/
│   ├── manage.py
│   ├── backend/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   ├── asgi.py
│   ├── userauths/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   ├── store/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   ├── vendor/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   ├── customer/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   ├── requirements.txt
│   ├── .gitignore `

## Authentication

### JWT Authentication

The backend uses JWT (JSON Web Tokens) for authentication. This ensures secure and stateless user sessions.

- djangorestframework-simplejwt: This package is used to implement JWT in Django.

### Custom User Models

Custom user models are implemented to extend the default Django user model, providing more flexibility in handling user data.

## API Endpoints

The API is built using Django REST Framework, providing a robust and flexible toolkit for building Web APIs.

### User Authentication Endpoints

- Registration: Allows users to register with the platform.
- Login: Allows users to log in and obtain JWT tokens.
- Token Refresh: Refreshes JWT tokens to maintain user sessions.

### Product Management Endpoints

- Product Listing: Lists all available products.
- Product Detail: Provides detailed information about a specific product.
- Add to Cart: Allows users to add products to their cart.
- Checkout: Manages the checkout process, including payment integration.

### Order Management Endpoints

- Order Creation: Creates a new order based on the user's cart.
- Order Tracking: Allows users to track their order status.

### Vendor Management Endpoints

- Vendor Dashboard: Provides vendors with statistics and order information.
- Product Management: Allows vendors to manage their products.

## Payment Integration

### Stripe Integration

Stripe is integrated to handle secure payments within the platform. The backend interacts with the Stripe API to process transactions and handle webhooks.

### PayPal Integration

PayPal is also integrated to provide users with an alternative payment method. Similar to Stripe, the backend handles PayPal transactions and webhooks.

## Additional Features

### Notification System

A notification system is in place to inform users and vendors about important updates and activities within the platform.

### Review and Rating System

Customers can leave reviews and ratings for products, enhancing user engagement and providing valuable feedback to vendors.

## Environment Setup

1. Install Python 3.11.5 or the latest version
2. Create a virtual environment and activate it
3. Install the required packages from requirements.txt

### License

This project is licensed under the MIT License - see the LICENSE file for details.
