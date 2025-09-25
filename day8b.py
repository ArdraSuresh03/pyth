class Account:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def __add__(self, other):
        return self._balance + other._balance

    def show_details(self):
        return f"Account Holder: {self._name}\nBalance: {self._balance}"


class SavingsAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.05


class CurrentAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.02


if __name__ == "__main__":
    ravi_account = SavingsAccount("Ravi", 10000)
    anjali_account = CurrentAccount("Anjali", 15000)

    print("---- Savings Account ----")
    print(ravi_account.show_details())
    print(f"Interest: {ravi_account.calculate_interest()}\n")

    print("---- Current Account ----")
    print(anjali_account.show_details())
    print(f"Interest: {anjali_account.calculate_interest()}\n")

    total_balance = ravi_account + anjali_account
    print("---- Total Balance ----")
    print(total_account.show_details())
