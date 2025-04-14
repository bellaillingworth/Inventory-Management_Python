# Grocery Store Inventory Manager 

An interactive Python terminal app for managing a grocery store's inventory using CSV-based storage. Built for BAIS3020, it allows users to add, remove, update, and search for products, with validation and summary features.

## Files

- `Assignment2.py`: Main application script with a text-based menu system
- `utilities.py`: Includes `safe_input()` for safe numeric input handling
- `inventory.csv`: Stores inventory data (auto-loaded and saved)

## Features

- Add new products with auto-incrementing IDs
- Remove, update, and search products (supports partial, case-insensitive search)
- Display product lists and summaries in formatted tables
- Calculate total inventory value per category
- Input validation for price, quantity, and IDs
- CSV persistence (loads on start, saves on exit)

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/bellaillingworth/Inventory-Management_Python.git
   cd Inventory-Management_Python
