from datetime import datetime as dt



class Transaction:
    def __init__(self,
                 id: int,
                 created_at: dt,
                 transaction_type: str,
                 amount: float,
                 author: str) -> None:
        self.id: int = id
        self.created_at: dt = created_at
        self.transaction_type: str = transaction_type
        self.amount: float = amount
        self.author: str = author
        
    def __str__(self) -> str:
        return f'{self.created_at} {self.transaction_type} {self.amount}'