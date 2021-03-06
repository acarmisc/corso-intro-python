from random import randint


class Blackjack:

	def __init__(self, mode="40"):
		suits = ['clubs', 'diamonds', 'hearts', 'spades']
		values = range(2, 12)

		cards = list()

		if mode == "40":
			for s in suits:
				for v in values:
					cards.append((s, v))
		else:
			raise NotImplementedError

		self.cards = cards

	def pop_card(self):
		card = self.cards.pop(randint(0, len(self.cards)-1))
		return card

	def sum_cards(self, clist):
		sum = 0
		for c in clist:
			sum += c[1]

		return sum

	def delta_cards(self, clist):
		sum = self.sum_cards(clist)
		return 21 - sum

    def delta_win(self, total):
        return 21 - total

    def get_winner(self, player1, player2):
        if self.delta_win(player1) > self.delta_win(player2):
            return 2

        return 1

	def ask_next(self, clist, courage=1):
		# courage: 1,2,3 increasing
		delta = self.delta_cards(clist)
		print delta		

		if courage == 1 and delta < 6:
			return False
		if courage == 2 and delta < 4:
			return False		
		if courage == 3 and delta < 2:
			return False

		return True

if __name__ == '__main__':
	b = Blackjack()
	print "Disponibili %s carte" % len(b.cards)

	again, again_ccounter = True, True
	user_cards = []
	while again:
		c = b.pop_card()
		user_cards.append(c)
		print "Hai tirato su %s" % str(c)
		resp = raw_input("Vuoi continuare? [s/n]")
		if resp == "n" or b.sum_cards(user_cards) >= 21:
			again = False

	user_sum = b.sum_cards(user_cards)
	print "Hai ottenuto %s" % user_sum
	ccounter_cards = []
	while again_ccounter:
		c = b.pop_card()
		print "Il banco ha tirato su %s" % str(c)
		ccounter_cards.append(c)	
		if not b.ask_next(ccounter_cards, courage=randint(1,4)) or b.sum_cards(ccounter_cards) >= 21: 
			again_ccounter = False

    ccounter_sum = b.sum_cards(ccounter_cards) 
	print "Il banco ha ottenuto %s" % ccounter_sum

    if user_sum <= 21:
        winner = b.get_winner(user_sum, ccounter_sum)
        print "Vince %s (1: giocatore, 2: banco)" % winner 
    else:
        print "Avrebbe comunque vinto il banco!"

