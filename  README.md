# Bank Management System

A menu-driven Bank Management System built with Python to practise Object-Oriented Programming (OOP) concepts.

## Features

- Create Savings and Current accounts
- Deposit money into an account
- Withdraw money from an account
- View account details and balances
- Calculate interest for savings accounts
- View transaction history
- Compare accounts using `__eq__()`
- Add account balances using `__add__()`
- Display account details using `__str__()`
- Handle errors using exceptions
- Interactive menu that runs until the user exits

## OOP Concepts Used

- **Classes and Objects:** Represent bank accounts and transactions.
- **Encapsulation:** Protect account balance using a private attribute (`__balance`).
- **Inheritance:** `SavingsAccount` and `CurrentAccount` inherit from `Bank`.
- **Abstraction:** Use `ABC` and `@abstractmethod` to define the account interface.
- **Polymorphism:** Different account types implement `calculate_interest()`.
- **Composition:** A bank account stores its transaction history using `Transaction` objects.
- **Special Methods:** Implement `__init__()`, `__str__()`, `__eq__()`, and `__add__()`.
- **Exception Handling:** Handle invalid transactions and insufficient funds.

## Technologies Used

- Python 3
- Python Standard Library

## Project Structure

```text
Bank-Management-System/
│
├── main.py
└── README.md
```

`main.py` contains the classes and the menu-driven program.

## Requirements

- Python 3 installed on your computer
- A code editor such as VS Code or PyCharm

No external libraries are required.

## How to Run

1. Clone or download this repository.
2. Open the project folder in your terminal or code editor.
3. Run the program:

   ```bash
   python main.py
   ```

   If your file has a different name, replace `main.py` with that filename.

4. Select an option from the menu and follow the instructions.

## Default Accounts

The program starts with three accounts:

| Account Number | Account Holder | Account Type | Initial Balance |
|---|---|---|---:|
| 101 | Bob | Savings | 1,000 |
| 102 | Alice | Savings | 2,000 |
| 103 | John | Current | 3,000 |

The savings accounts have different interest rates configured in the program.

## Menu Options

1. Create Account
2. Deposit Money
3. Withdraw Money
4. Show All Balances
5. Calculate Interest
6. View Transaction History
7. Exit

## Learning Objectives

This project helps practise Python OOP concepts by applying them to a practical banking scenario. It also provides experience with lists, loops, conditional statements, user input, and exception handling.

## Future Improvements

- Store accounts and transactions in a database
- Add account deletion and account updates
- Add unit tests
- Implement authentication and user roles
- Build a graphical interface or web application using Django

## Disclaimer

This project is intended for educational purposes. It is not designed for real banking transactions or production use.
