FIRST_WON = 'FIRST_WON'
SECOND_WON = "SECOND_WON"
DRAW = 'DRAW'
UNFINISHED = 'UNFINISHED'


class AddThreeGame:
    def __init__(self):
        self.p1_hand = []
        self.p2_hand = []
        self.played = []
        self.p1_3sum = 0
        self.p2_3sum = 0
        self.stats = UNFINISHED

    def get_current_state(self):

        return self.stats

    def make_move(self, player, number):
        if number in self.played:
            print('The number has been chosen before, re-pick one.')
            return False
        if number < 1 or number > 9:
            print('Out of range, re-pick the number')
            return False

        if player == 'first':
            self.played.append(number)
            self.p1_hand.append(number)

            for i in range(0, len(self.p1_hand) - 2):
                for j in range(i + 1, len(self.p1_hand) - 1):
                    for k in range(j + 1, len(self.p1_hand)):
                        self.p1_3sum = self.p1_hand[i] + self.p1_hand[j] + self.p1_hand[k]
                        if self.p1_3sum == 15 and self.p2_3sum < 15:
                            self.stats = FIRST_WON
                            print('Player 1 has won')
                            return True

        elif player == 'second':
            self.played.append(number)
            self.p2_hand.append(number)

            for i in range(0, len(self.p2_hand) - 2):
                for j in range(i + 1, len(self.p2_hand) - 1):
                    for k in range(j + 1, len(self.p2_hand)):
                        self.p2_3sum = self.p2_hand[i] + self.p2_hand[j] + self.p2_hand[k]
                        if self.p2_3sum == 15 and self.p1_3sum < 15:
                            self.stats = SECOND_WON
                            print('Player 2 has won')
                            return True

        if self.p1_3sum == self.p2_3sum == 15:
            self.stats = DRAW

        if len(self.played) == 9 and self.p1_3sum != 15 and self.p2_3sum != 15:
            self.stats = DRAW


game = AddThreeGame()
game.make_move("second", 2)
game.make_move("first", 8)
game.make_move("second", 9)
game.make_move("first", 6)
game.make_move("second", 4)
game.make_move("first", 1)
