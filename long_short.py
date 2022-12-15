from BacktestBase import *

class BacktestLongShort(BacktestBase):
    
    def go_long(self, bar, units=None, amount=None):
        if self.position == -1:
            self.place_buy_order(bar, units=-self.units)
        if units:
            self.place_buy_order(bar, units=units)
        elif amount:
            if amount == "all":
                amount = self.amount
            self.place_buy_order(bar, amount=amount)
    
    def go_short(self, bar, units=None, amount=None):
        if self.position == 1:
            self.place_sell_order(bar, units=self.units)
        if units:
            self.place_sell_order(bar, units=units)
        elif amount:
            if amount == "all":
                amount = self.amount
            self.place_sell_order(bar, amount=amount)
    
    def run_sma_strategy(self, SMA1, SMA2):
        msg = f''
        