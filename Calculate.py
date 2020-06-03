import pygame


class Calculate():

    def __init__(self, dealerhand, playerhand):
        self.dealerhand = dealerhand
        self.playerhand = playerhand

    def handcheck(self):
        hand = []
        for i in range(len(self.dealerhand)):
            hand.append(self.dealerval(i))
        if sum(hand) >= 17:
            return True
        else:
            return False

    def handcal(self):
        dealerhand = []
        playerhand = []

        if len(self.dealerhand) > 2:
            for i in range(len(self.dealerhand)):
                dealerhand.append(self.dealerval(i))
        else:
            for i in range(len(self.dealerhand)):
                dealerhand.append(self.dealerval(i))
        if len(self.playerhand) > 2:
            for i in range(len(self.playerhand)):
                playerhand.append(self.playerval(i))
        else:
            for i in range(len(self.playerhand)):
                playerhand.append(self.playerval(i))
        dealer_score = sum(dealerhand)
        player_score = sum(playerhand)

        print(player_score)
        print(dealer_score)
        if player_score > 21:
            return 'You lose'
        elif dealer_score > 21:
            return 'You Win'
        else:
            if (21 - player_score) > (21 - dealer_score):
                return 'You lose'
            elif (21 - player_score) == (21 - dealer_score):
                return 'Draw'
            else:
                return 'You win'

    def dealerval(self, index):
        if 'C' in self.dealerhand[index]:
            c1 = self.dealerhand[index].split('C')
            c1val = 0
            if ('K' in c1[0]) or ('Q' in c1[0]) or ('J' in c1[0]):
                c1val += 10
            elif 'A' in c1[0]:
                if c1val <= 10:
                    c1val += 11
                else:
                    c1val += 1
            else:
                c1val += int(str(c1[0]))
            return c1val
        if 'D' in self.dealerhand[index]:
            d1 = self.dealerhand[index].split('D')
            d1val = 0
            if ('K' in d1[0]) or ('Q' in d1[0]) or ('J' in d1[0]):
                d1val += 10
            elif 'A' in d1[0]:
                if d1val <= 10:
                    d1val += 11
                else:
                    d1val += 1
            else:
                d1val += int(str(d1[0]))
            return d1val
        if 'H' in self.dealerhand[index]:
            h1 = self.dealerhand[index].split('H')
            h1val = 0
            if ('K' in h1[0]) or ('Q' in h1[0]) or ('J' in h1[0]):
                h1val += 10
            elif 'A' in h1[0]:
                if h1val <= 0:
                    h1val += 11
                else:
                    h1val += 1
            else:
                h1val += int(str(h1[0]))
            return h1val
        if 'S' in self.dealerhand[index]:
            s1 = self.dealerhand[index].split('S')
            s1val = 0
            if ('K' in s1[0]) or ('Q' in s1[0]) or ('J' in s1[0]):
                s1val = 10

            elif 'A' in s1[0]:
                if s1val <= 0:
                    s1val += 11
                else:
                    s1val += 1
            else:
                s1val += int(str(s1[0]))
            return s1val

    def playerval(self, index):
        if 'C' in self.playerhand[index]:
            c1 = self.playerhand[index].split('C')
            if ('K' in c1[0]) or ('Q' in c1[0]) or ('J' in c1[0]):
                c1val = 10
            elif 'A' in c1[0]:
                c1val = 1
            else:
                c1val = int(str(c1[0]))
            return c1val
        if 'D' in self.playerhand[index]:
            d1 = self.playerhand[index].split('D')
            if ('K' in d1[0]) or ('Q' in d1[0]) or ('J' in d1[0]):
                d1val = 10

            elif 'A' in d1[0]:
                d1val = 1

            else:
                d1val = int(str(d1[0]))
            return d1val
        if 'H' in self.playerhand[index]:
            h1 = self.playerhand[index].split('H')
            if ('K' in h1[0]) or ('Q' in h1[0]) or ('J' in h1[0]):
                h1val = 10

            elif 'A' in h1[0]:
                h1val = 1

            else:
                h1val = int(str(h1[0]))
            return h1val
        if 'S' in self.playerhand[index]:
            s1 = self.playerhand[index].split('S')
            if ('K' in s1[0]) or ('Q' in s1[0]) or ('J' in s1[0]):
                s1val = 10

            elif 'A' in s1[0]:
                s1val = 1
            else:
                s1val = int(str(s1[0]))
            return s1val
