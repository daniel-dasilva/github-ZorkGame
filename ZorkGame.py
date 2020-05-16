import sys 

class tupledict(dict):
    def __contains__(self, key):
        if super(tupledict, self).__contains__(key):
            return True
        return any(key in k for k in self)

class Game:
	""" Represent the Game platform"""
	_gameOver = False
	_roomObjects= [ 'key', 'box', 'map', 'gps', 'atlas', 'book', 'page-number', 'section-number']
	_roomMap = {0: [2,1,3,None], 1:[None,None,5,0], 2:[None,None,0,None], 3:[0,5,None,4], 4:[None,3,None,None], 5:[1,6,7,3], 6:[None, None, None, 5], 7:[5,None,None, None]}
	_directions = {"east":0, "north":1, "west":2, "south":3}
	_inventory = []
	_playerName = ""
	_currentRoomNumber = 1
	_gameDict = tupledict({('key','box'): 'compass',  ('map','compass'): 'coordinates', ('gps','coordinates'): 'country name', ('atlas', 'country name'): 'cypher',
						 ('book', 'page-number'): 'text', ('section-number', 'text'): 'decoding function', ('decoding function', 'cypher'):'THE MESSAGE'})
	
	def __init__(self, name):
		""""Return to library id, title, location and states of item """
		self._playerName = name

	def call_func(self, func):
		_dispatcher = { 'room0' : self.room0, 'room1' : self.room1, 'room2' : self.room2, 'room3' : self.room3, 'room4' : self.room4, 'room5' : self.room5, 'room6' : self.room6 , 'room7' : self.room7}
		try:
			return _dispatcher[func]()
		except:
			return "Invalid function"

	def gotoroom(self,n):
		function_name="room"+str(n)
		self._currentRoomNumber = n
		self.call_func(function_name)
		return None	

	def testgo(self,n):
		rooms=self._roomMap[self._currentRoomNumber]
		if rooms[n] == None:
			return None
		else:
			return rooms[n]
		
	def check(self, **kwargs):
		
		if kwargs['command'] == "look":
			if (kwargs['thing'] in self._inventory) or (kwargs['thing'] not in self._roomObjects): 
				print("{} has already been found".format(kwargs['thing']))
				
			else:
				self._inventory.append(kwargs['thing'])
				self._roomObjects.remove(kwargs['thing'])
				print("{} has been added to your inventory".format(kwargs['thing']))
				
		if kwargs['command'] == "inventory":
			print( *self._inventory)

		if kwargs['command'] == "go":
			try:
				n =self.testgo(self._directions.get(kwargs['predicate']))
				if n != None:
					self. gotoroom(n)
				else:
					print('Nothing there')
			except:
				print("Add a valid direction")
		
		if kwargs['command'] == "use":
			try:
				if kwargs['predicate'] in self._inventory:
					if kwargs['predicate'] in self._gameDict:
						keys = [k for k in self._gameDict if k[0]==kwargs['predicate'] or k[1]==kwargs['predicate']]
						if keys[0][0] in self._inventory and keys[0][1] in self._inventory:
							print("You used the {} and the {}. You have now a {} in the inventory".format(keys[0][0], keys[0][1], self._gameDict.get((keys[0][0],keys[0][1]))))
							self._inventory.remove(keys[0][0])
							self._inventory.remove(keys[0][1])
							self._inventory.append(self._gameDict.get((keys[0][0],keys[0][1])))
							if self._inventory == ['THE MESSAGE']:
								print('*'*20)
								print("You found the secret message and escape the room!")
								print('*'*20)
								self._gameOver=True
															
						else:
							print("You are missing something")
					else:
						print("I forgot to add that to the game")
				else:
					print("You do not have this object!")
			except:
				print("Error")
		if kwargs['command'] == "help":
			print('''Following commands can be used:
look:  		to look for an item in the room
go (direction):	to move to next room where direction can be east, west, north or south
use (object):	to use an object from the inventory
inventory:	to print the inventory			
			
			''')


	def get_input(self, room_object):
		while not self._gameOver:
			order=input (">>>")
			orders = order.split(" ")
			if len(orders)==1:
				self.check(command=orders[0], thing=room_object)

			if len(orders)==2:
				self.check(command=orders[0], predicate=orders[1], thing=room_object)
		return

	def room1(self ):
		room_object="key"
		print("############### ROOM Oniris #################")
		self.get_input(room_object)
			
	def room2(self):
		room_object="box"
		print("############### ROOM Twindle #################")
		self.get_input(room_object)	

	def room3(self):
		room_object="map"
		print("############### ROOM Throbing #################")
		self.get_input(room_object)	

	def room4(self):
		room_object="gps"
		print("############### ROOM Forbiden #################")
		self.get_input(room_object)	

	def room5(self):
		room_object="atlas"
		print("############### ROOM Fiveresk #################")
		self.get_input(room_object)	

	def room6(self):
		room_object="book"
		print("############### ROOM Sectarian #################")
		self.get_input(room_object)	

	def room7(self):
		room_object="page-number"
		print("############### ROOM Sevenesk #################")
		self.get_input(room_object)	
	
	def room0(self):
		room_object="section-number"
		print("############### ROOM Zebra #################")
		self.get_input(room_object)	

newgame =Game("Player1")
newgame.room1()


	


