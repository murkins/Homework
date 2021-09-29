'''Task6_7. Implement a class Money to represent value and currency.
You need to implement methods to use all basic arithmetics expressions (comparison, division, multiplication, addition and subtraction).
Tip: use class attribute exchange rate which is dictionary and stores information about exchange rates to your default currency:
```python
exchange_rate = {
    "EUR": 0.93,
    "BYN": 2.1} '''

class Money:
    exchange_rate = {
        "EUR": 0.86,
        "BYN": 2.49,
        "JPY": 111.52,
        "USD": 1.0
    }

    def __init__(self,value, currency = "USD"):
        self.value = value
        self.currency = currency


    def __float__(self):
        return self.value / Money.exchange_rate[self.currency]

    def __add__(self, other):
        left_usd = float(self)
        right_usd = float(other)

        return Money((left_usd + right_usd) * Money.exchange_rate[self.currency],
                     self.currency)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        left_usd = float(self)
        right_usd = float(other)
        return Money((left_usd - right_usd) * Money.exchange_rate[self.currency],
                     self.currency)

    def __mul__(self, other):
        left_usd = float(self)
        right_usd = float(other)
        return Money(left_usd * right_usd * Money.exchange_rate[self.currency],
                     self.currency)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        left_usd = float(self)
        right_usd = float(other)
        return Money(left_usd / right_usd * Money.exchange_rate[self.currency],
                     self.currency)

    def __cmp__(self, other):
        left_usd = float(self)
        right_usd = float(other)

        res = None
        if left_usd > right_usd:
            res = 1
        elif left_usd < right_usd:
            res = -1
        else:
            res = 0
        return res

    def __repr__(self):
        return f"{self.value} {self.currency}"

x = Money(10, "BYN")
y = Money(11)
z = Money(12.34, "EUR")
print(z + 3.11 * x + y * 0.8)

lst = [Money(10,"BYN"), Money(11), Money(12.01, "JPY")]
s = sum(lst)
print(s)

