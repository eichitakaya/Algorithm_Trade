from BacktestBase import *

class BacktestLongOnly(BacktestBase):
    
    def run_sma_strategy(self, SMA1, SMA2):
        """ Backtesting an SMA-based strategy.
        
        Parameters
        ==========
        SMA1, SMA2: int
            shorter and longer term simple moving average (in days)
        """
        msg = f'\n\nRunning SMA strategy | SMA1={SMA1} & SMA2={SMA2}'
        msg += f'\nfixed costs {self.ftc} |'
        msg += f'proportional costs {self.ptc}'
        print(msg)
        print('-' * 55)
        self.position = 0 # initial neutral position
        self.trades = 0 # no trades yet
        self.amount = self.initial_amount # reset initial capital
        self.data["SMA1"] = self.data["price"].rolling(SMA1).mean()
        self.data["SMA2"] = self.data["price"].rolling(SMA2).mean()
        
        for bar in range(SMA2, len(self.data)):
            if self.position == 0:
                if self.data["SMA1"].iloc[bar] > self.data["SMA2"].iloc[bar]:
                    self.place_buy_order(bar, amount=self.amount)
                    self.position = 1 # long position
            elif self.position == 1:
                if self.data["SMA1"].iloc[bar] < self.data["SMA2"].iloc[bar]:
                    self.place_sell_order(bar, units=self.units)
                    self.position = 0 # market neutral
        self.close_out(bar)
        
    def run_momentum_strategy(self, momentum):
        """ Backtesting a momentum-based strategy
        
        Parameters
        ==========
        momentum: int
            number of days for mean return calculation
        """
        msg = f'\n\nRunning momentum strategy | {momentum} days'
        msg += f'\nfixed costs {self.ftc} |'
        msg += f'proportional costs {self.ptc}'
        print('=' * 55)
        self.position = 0 # initial neutral position
        self.trades = 0 # no trades yet
        self.amount = self.initial_amount # reset initial capital
        