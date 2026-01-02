class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        span = 1
        while self.prices and self.prices[-1][0] <= price:
            prev_price, prev_span = self.prices.pop()
            span += prev_span
        self.prices.append((price, span))
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)