# ATM Service Point

## Overview

This project is an Interactive ATM Web Application developed using Flask, a lightweight Python web framework. The application allows users to perform basic ATM functions such as checking balance, depositing money, withdrawing money, and viewing transaction history. The user interface is crafted with HTML and CSS for a professional and user-friendly experience. The backend logic, written in Python, manages the transactions and ensures data integrity.

## Features

- **Check Balance**: View the current balance of your account.
- **Deposit Money**: Add money to your account.
- **Withdraw Money**: Withdraw money from your account.
- **Transaction History**: View a history of all transactions performed.

## Project Structure
```
.
├── app.py
├── templates
│   ├── index.html
│   ├── balance.html
│   ├── deposit.html
│   ├── withdraw.html
│   ├── transactions.html
│   └── result.html
├── static
│   ├── styles.css
│   ├── bg.jpg
│   ├── atm.png
│   └── icon.png
└── README.md

```

## Files Description

- **app.py**: The main Flask application file that contains all routes and the ATM logic.
- **templates/**: Contains HTML files for different pages of the application.
    - `index.html`: The homepage of the application.
    - `balance.html`: Displays the current balance.
    - `deposit.html`: Allows users to deposit money.
    - `withdraw.html`: Allows users to withdraw money.
    - `transactions.html`: Shows the transaction history.
    - `result.html`: Displays the result of deposit or withdrawal operations.
- **static/**: Contains static files like CSS and images.
    - `styles.css`: The stylesheet for the application.
    - `bg.jpg`: Background image used in the application.
    - `atm.png`: Image displayed on the homepage.
    - `icon.png`: Favicon for the application.

## Live Project Link
   https://atm-service-point.onrender.com/
