


class BankAccount:
    def __init__(self,
                 id,
                 account_number,
                 account_owner,
                 currency,
                 opening_amount,
                 transactions
                 ) -> None:
        self.id = id
        self.account_number = account_number
        self.account_owner = account_owner
        self.currency = currency
        self.opening_amount = opening_amount
        self.transactions = transactions

