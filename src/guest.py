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
			return True
		else:
			return False

	def bribe_the_room(self, room):
		if self.wallet > 1000:
			for guest in room.guests:
				guest.wallet += room.entry_fee
				guest.wallet += 5
				room.till -= room.entry_fee
				room.till -= 5
			room.guests.clear()
			room.guests.append(self)
			self.wallet -= 1000
			room.till += 1000
			return True
		return False

