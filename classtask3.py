class card():
	suit_names= ['clubs','diamonds','hearts','spades']
	rank_names=[none ,'ace','2','3','4','5','6','7','8','9','jack','queen','king']


	def __init__(self, suit=0 , rank=1):
		self.suit=suit
		slef.rank=rank

	def__str__(self):
		return f"the rank in {card.rank_names[self.rank]} and the suit is {card.suit_names[self.suit]}"

ace_of_spades = card(3,1)

print (ace_of_spades)
