# Mortoti Pay

Mortoti Pay is a Python-based simulation of a secure mobile payment system that supports account management, transactions, and airtime purchases within a closed user network.

# FEATURES


## Mortoti Number Registration:
- Users must register with a valid Mortoti number starting with 090 or 095.
- All transactions can only be made to other users registered in the Mortoti Pay system.

## Core Functionalities:
- Secure account creation with PIN protection
- Deposit and withdrawal functionality
- Transfer between Mortoti Pay accounts
- Airtime purchase (for self or others)
- Balance checking
- Change PIN
- Delete account
- Transaction fee system


## SECURITY FEATURES


- 3-attempt PIN validation limit
- PIN hashing using SHA-256
- Secure PIN entry using getpass
- Input validation for all operations
- Error handling for transactions


## REQUIREMENTS


- Python 3.x
- Uses built-in modules:
  - json
  - getpass
  - hashlib


## INSTALLATION


1. Clone the repository:
   git clone https://github.com/Mortoti/mortoti-pay.git

2. Navigate into the folder and run:
   cd mortoti-pay
   python main.py


## USAGE


1. Create Account:
   - Enter a phone number starting with 090 or 095
   - Set a 4-digit PIN

2. Login:
   - Enter registered Mortoti number and PIN

3. Main Menu:
   - Deposit money
   - Transfer funds
   - Withdraw cash
   - Purchase airtime
   - Check balance
   - Change PIN
   - Delete account
   - Logout


## TRANSACTION FEES


- Below GHS 100: Flat fee of GHS 0.50
- GHS 100 and above: 1% of the transaction amount


## DATA STORAGE


- User info stored in users.json
- PINs hashed before saving
- Each account maintains balance 


## CONTRIBUTING


1. Fork the repo
2. Create a feature branch
3. Commit changes
4. Open a pull request


## LICENSE — MIT


MIT License

Copyright (c) 2025 Mortoti

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in  
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN  
THE SOFTWARE.


## AUTHOR


Mortoti-Agogyi Jephthah Lorlornyo  
Backend Developer in training  
Focus: FinTech, payments, and real-world logic systems  
Email: mortoti.dev@gmail.com


## FUTURE GOALS


- Move data from JSON to SQLite/PostgreSQL
- Add unit tests
- Build Django-based web version
- Add session/auth systems
- Refactor into a REST API
