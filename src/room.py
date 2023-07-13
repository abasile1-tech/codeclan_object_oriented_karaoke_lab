class Room:
	def __init__(self, name, till, playlist, guests, guest_capacity, entry_fee):
		self.name = name
		self.till = till
		self.playlist = playlist
		self.guests = guests
		self.guest_capacity = guest_capacity
		self.entry_fee = entry_fee