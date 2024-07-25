from player import Player
from stock_market import StockMarket
from user_input import choice_input

TURN_ACTIONS = [
    "Buy Stock",
    "Sell Stock",
    "Get Stock Info",
    "Check Portfolio",
    "Allocate to Buyout Fund",
    "Check Balance"
    "End Turn"
]


class Game:
    def __init__(self, num_players):
        self.num_players = num_players
        self.players = []
        self.stock_market = StockMarket()

    def initialize_game(self):
        self.stock_market.initialize_stocks()
        self.stock_market.print_market_status(True)
        self.players = [
            Player("Player 1", 1000.0, 33.33),
            Player("Player 2", 1000.0, 33.33),
            Player("Player 3", 1000.0, 33.33),
        ]

    def play_build_phase(self):
        print("Build Phase Begins:\n")
        for turn in range(3):
            print(f"Turn {turn + 1}:\n")
            self.stock_market.fluctuate_market()
            self.stock_market.print_market_status(False)
            for player in self.players:
                self.player_turn(player)

    def player_turn(self, player):
        print(f"-------------{player.name}'s TURN-------------")
        while(True):
            action: str = choice_input(
                TURN_ACTIONS, "Choose an action: ", "Actions")[1]
            if action == "Buy Stock":
                self.buy_stock_action(player)
            elif action == "Sell Stock":
                self.sell_stock_action(player)
            elif action == "Check Portfolio":
                player.check_portfolio()
            elif action == "Check Balance":
                player.check_balance()
            elif action == "Allocate to Buyout Fund":
                inp = input("Enter amount to allocate to Buyout Fund: ")
                if inp.isdigit():
                    amount = int(inp)
                    player.allocate_to_buyout_fund(amount)
                else:
                    print("Error: Invalid amount.")
            elif action == "End Turn":
                print(f"{player.name} completed their turn.")
                break
            elif action == "Get Stock Info":
                stockname = input("Enter stock ticker:")
                if(stockname in self.stock_market.stockandtickers):
                    stock = self.stock_market.get_stock(stockname)
                    stock.printinfo()
                else:
                    print(f"Error: Stock ticker {stockname} not found")
        print()

    def buy_stock_action(self, player):
        self.stock_market.print_market_status(False)
        ticker = input("Enter the ticker of the stock you want to buy: ")
        inp = input("Enter the quantity you want to buy: ")
        if ticker in self.stock_market.stockandtickers and inp.isdigit():
            quantity = int(inp)
            curstock = self.stock_market.get_stock(ticker)
            player.buy_stock(curstock, quantity)
        else:
            print("Error: Invalid input.")

    def sell_stock_action(self, player):
        player.check_portfolio()
        stock_ticker = input("Enter the ticker of the stock you want to sell: ")
        inp = input("Enter the quantity you want to sell: ")
        if stock_ticker in self.stock_market.stockandtickers and inp.isdigit():
            quantity = int(inp)
            curstock = self.stock_market.get_stock(stock_ticker)
            player.sell_stock(curstock, quantity)
        else:
            print("Error: Invalid input.")
            

    def play_golden_opportunity_phase(self):
        print("Golden Opportunity Phase Begins:")
        # Logic for Golden Opportunity Phase

    def end_game(self):
        print("Game Over. Final Portfolios:")
        for player in self.players:
            player.check_portfolio()
        print("Thank you for playing!")

    def run(self):
        self.initialize_game()
        self.play_build_phase()
        self.play_golden_opportunity_phase()
        self.end_game()


if __name__ == "__main__":
    game = Game(num_players=3)
    game.run()
