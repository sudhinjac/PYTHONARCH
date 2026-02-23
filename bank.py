import logging

logger = logging.getLogger(__name__)


class InsufficientFunds(Exception):
    pass


class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")

        self.balance += amount
        logger.info(f"{self.owner} deposited {amount}")
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")

        if amount > self.balance:
            logger.error("Insufficient funds")
            raise InsufficientFunds("Not enough balance")

        self.balance -= amount
        logger.info(f"{self.owner} withdrew {amount}")
        return self.balance