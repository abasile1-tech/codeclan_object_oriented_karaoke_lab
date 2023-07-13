class Guest:
	def __init__(self, name, wallet, favourite_song):
		self.name = name
		self.wallet = wallet
		self.favourite_song = favourite_song

	def check_playlist(self, room):
		if self.favourite_song in room.playlist:
			return "WooHoo!"
		else:
			return "Boo!"

	def pay_entry_fee(self, room):
		if len(room.guests) < room.guest_capacity and self.wallet >= room.entry_fee:
			self.wallet -= room.entry_fee
			room.guests.append(self)
			room.till += room.entry_fee