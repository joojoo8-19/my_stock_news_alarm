class TickerModel:
    def __init__(self, symbol: str, growth_rate: float, latest_data: dict, previous_data: dict):
        self.symbol = symbol
        self.growth_rate = growth_rate
        self.latest_data = latest_data
        self.previous_data = previous_data

    def to_dict(self):
        return {
            "symbol": self.symbol,
            "growth_rate": self.growth_rate,
            "latest_data": self.latest_data,
            "previous_data": self.previous_data
        }
