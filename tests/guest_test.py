import unittest

from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):
	def setUp(self):
		self.eye_of_the_tiger = Song("Eye of the Tiger")
		self.thriller = Song("Thriller")
		self.somewhere_over_the_rainbow = Song("Somewhere Over the Rainbow")
		self.jerry = Guest("Jerry", 100, self.eye_of_the_tiger)
		self.rob = Guest("Rob", 50, self.thriller)
		self.steve = Guest("Steve", 2000, self.somewhere_over_the_rainbow)
		self.thunder_room = Room("Thunder Room", 500, [self.eye_of_the_tiger, self.thriller], [self.jerry], 2, 10)
	
	def test_check_playlist(self):
		self.assertEqual("WooHoo!", self.jerry.check_playlist(self.thunder_room))
		self.assertEqual("Boo!", self.steve.check_playlist(self.thunder_room))

	def test_pay_entry_fee(self):
		self.assertEqual(True, self.rob.pay_entry_fee(self.thunder_room))
		self.assertEqual(40, self.rob.wallet)
		self.assertEqual([self.jerry, self.rob], self.thunder_room.guests)
		self.assertEqual(510, self.thunder_room.till)
		self.assertEqual(False, self.steve.pay_entry_fee(self.thunder_room))

	def test_bribe_the_room(self):
		self.rob.pay_entry_fee(self.thunder_room)
		self.assertEqual([self.jerry, self.rob], self.thunder_room.guests)
		self.assertEqual(False, self.steve.pay_entry_fee(self.thunder_room))
		self.steve.bribe_the_room(self.thunder_room)
		self.assertEqual([self.steve],self.thunder_room.guests)
		self.assertEqual(55, self.rob.wallet)
		self.assertEqual(1000,self.steve.wallet)
		self.assertEqual(115, self.jerry.wallet)
		self.assertEqual(1480, self.thunder_room.till)