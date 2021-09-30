from config import value

class APIException(Exception):
    pass

class MoneyPrice():
    @staticmethod
    def get_price(base: str, quote: str, amount: str):


        try:
            base_t = value[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту: {base}')

        try:
            quote_t = value[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту: {quote}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать колличество: {amount}')
        total = value[quote] / value[base] * amount
        return total

