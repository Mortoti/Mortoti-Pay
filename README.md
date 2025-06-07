# Mortoti Pay
Mortoti Pay is a Python-Based simulation of a secure mobile payment system with account management, transaction capabilities, and airtime purchase features.

## Features
- Secure account creation with PIN protection
- Deposit and withdrawal functionality
- Money transfer between accounts
- Airtime purchase capabilities
- Balance checking
- PIN management
- Account deletion
- Transaction fee system

## Security Features
- PIN validation with 3 attempts limit
- PIN hashing using SHA-256
- Input validation for all operations
- Secure PIN entry using getpass
- Transaction validation and error handling

## Requirements
- Python 3.x
- `json` (built-in)
- `getpass` (built-in)
- `hashlib` (built-in)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/Mortoti/mortoti-pay.git
```
2. Run the main file:
```bash
python main.py
```

## Usage
The system provides a simple menu-driven interface:
1. Create Account:
   - Enter a valid phone number (090 or 095 prefix)
   - Set a 4-digit PIN
2. Login:
   - Enter your phone number
   - Validate with PIN
3. Available Operations:
   - Deposit money
   - Transfer to other accounts
   - Withdraw cash
   - Purchase airtime
   - Check balance
   - Change PIN
   - Delete account
   - Logout

## Transaction Fees
- Amounts under GHS 100: Fixed fee of 0.5 GHS
- Amounts GHS 100 and above: 1% of transaction amount

## Data Storage
- User data is stored securely in `users.json`
- PINs are hashed before storage
- Balance and transaction history maintained per account

## Contributing
Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License
MIT License

## Author
- Mortoti-Agogyi Jephthah Lorlornyo
- Backend Developer in training
- Focused on FinTech, payments, and real world logic systems
- [Email](mortoti.dev@gmail.com)

## Future Goals
- Move Data from JSON to SQLite or PostgreSQL
- Add unit tests
- Build a Django-based web version
- Add session/auth systems
- Refractor into a proper API