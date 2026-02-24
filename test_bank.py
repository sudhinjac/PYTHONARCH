import pytest
from bank import BankAccount, InsufficientFunds


# =========================
# FIXTURES
# =========================

@pytest.fixture
def account():
    return BankAccount("Sudhin", 100)


# =========================
# DEPOSIT TESTS
# =========================

@pytest.mark.parametrize("amount, expected_balance", [
    (50, 150),
    (25, 125),
    (1, 101),
])
def test_deposit(account, amount, expected_balance):
    balance = account.deposit(amount)
    assert balance == expected_balance
    assert account.balance == expected_balance


def test_deposit_zero(account):
    with pytest.raises(ValueError):
        account.deposit(0)


def test_deposit_negative(account):
    with pytest.raises(ValueError):
        account.deposit(-10)


# =========================
# WITHDRAW TESTS
# =========================

@pytest.mark.parametrize("amount, expected_balance", [
    (50, 50),
    (25, 75),
])
def test_withdraw(account, amount, expected_balance):
    balance = account.withdraw(amount)
    assert balance == expected_balance
    assert account.balance == expected_balance


def test_withdraw_exact_balance(account):
    account.withdraw(100)
    assert account.balance == 0


def test_withdraw_negative(account):
    with pytest.raises(ValueError):
        account.withdraw(-5)


def test_overdraft(account):
    with pytest.raises(InsufficientFunds):
        account.withdraw(200)


# =========================
# LOGGING TESTS
# =========================

def test_deposit_logs(account, caplog):
    with caplog.at_level("INFO"):
        account.deposit(10)

    assert "deposited 10" in caplog.text


def test_withdraw_logs(account, caplog):
    with caplog.at_level("INFO"):
        account.withdraw(10)

    assert "withdrew 10" in caplog.text


def test_overdraft_logs(account, caplog):
    with caplog.at_level("ERROR"):
        with pytest.raises(InsufficientFunds):
            account.withdraw(200)

    assert "Insufficient funds" in caplog.text


# =========================
# INVARIANT TEST
# =========================

def test_balance_never_negative(account):
    with pytest.raises(InsufficientFunds):
        account.withdraw(200)

    assert account.balance >= 0