from functools import wraps
from datetime import datetime

def log_operacao(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print(
            f"[{datetime.now()}] "
            f"{func.__name__}"
        )

        return func(*args, **kwargs)

    return wrapper