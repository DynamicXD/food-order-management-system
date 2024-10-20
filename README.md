# Food Order Management System

## Overview

The **Food Order Management System** is a Python-based application designed to streamline the process of taking and managing food orders. The system provides a simple command-line interface (CLI) for customers to place orders and for restaurant staff to track, prepare, and deliver these orders efficiently. No database is required, and food items are managed in a separate `foods.py` file.

## Features

- **Customer Order Placement**: The system allows customers to place orders by providing their details, selecting food items from the menu, and specifying quantities.
- **Order Queue**: Orders are stored in the order they are received to ensure they are prepared in the correct sequence.
- **Order Status Update**: After preparing an order, the system can update its status to indicate that it is ready for delivery.
- **Order Tracking**: Each order is assigned a unique order ID, which allows staff to track and manage orders efficiently.
- **Order Completion**: Once an order has been prepared and delivered, staff can mark the order as completed, finishing the process.

## Technology Stack

- **Programming Language**: Python 3.x
- **Data Storage**: In-memory storage (lists)
- **UI**: Command-line interface (CLI)

## Prerequisites

To run this project locally, you need:

- Python 3.x installed

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/food-order-management-system.git
   cd food-order-management-system
   ```
2. Run the application:
   ```bash
   python main.py
   ```
## Contribution
Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.
