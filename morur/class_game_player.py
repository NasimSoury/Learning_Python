class game_player():
    def __init__(self, name_input, score_input):
        self.name=name_input
        self.score=score_input
    def show_info(self):
        print(f"{self.name} has {self.score} points!")

    def add_score(self, amount):
        self.score=self.score+ amount

my_player=game_player("ali" , 50)
my_player.show_info()

my_player.add_score(20)
my_player.show_info()
class uhfkeuh