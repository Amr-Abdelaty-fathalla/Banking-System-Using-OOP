# Bank Account Management System 🏦
A Python-based banking system designed to manage accounts with custom exception handling, ensuring a realistic and engaging user experience.

## 💡 Overview
This dynamic, object-oriented project provides a comprehensive solution for banking operations. It includes a robust system for managing various account types, each tailored to meet different financial needs:

- **Standard BankAccount**: Enables users to perform essential banking operations such as deposits, withdrawals, and transfers, forming the backbone of personal finance management.
- **InterestRewardsAccount**: This account not only supports standard transactions but also offers a 5% interest on deposits, encouraging users to save more.
- **SavingsAccount**: Designed for those focused on long-term savings, this account applies a small withdrawal fee to promote thoughtful spending, reflecting real-world banking practices.

## 🌟 Key Features
- **Custom Exception Handling**: The `BalanceException` class gracefully manages insufficient funds, providing users with clear, informative feedback during transactions.
- **User-Friendly Functions**: Methods like `withdraw()`, `deposit()`, `transfer()`, and `getBalance()` are designed for simplicity, making it easy for users to navigate their finances without hassle.
- **Extensible Account Management**: The architecture allows for easy addition of new account types or functionalities, ensuring the system can grow with user needs.

## 💻 Code Walkthrough
This code is structured for clarity and extensibility:

- **BankAccount Class**: Serves as the foundation, implementing essential methods for handling transactions and maintaining balance integrity.
- **InterestRewardsAccount**:  Inherits from BankAccount, adding a 5% reward to deposits.
- **SavingsAccount**: Builds upon InterestRewardsAccount by applying a withdrawal fee for every transaction, reinforcing the discipline of saving.

## 🧑‍💻 Getting Started
1. Clone the repo and run the script in your Python environment.
2. Set up initial account balances and names to simulate real user scenarios.
3. Engage with the system by testing various transactions and experience the power of custom exception handling firsthand!

## 🔄 Future Improvements
- **Expanded Account Types**: Explore the addition of checking accounts, business accounts, or investment accounts to cater to a broader audience.
- **Graphical Interface**: Developing a user-friendly GUI to enhance interaction and make banking intuitive for all users.

Feel free to explore, test, and enhance this foundational code! Happy coding! 🚀
