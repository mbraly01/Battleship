class Tile:
    def __init__(self, is_ship = False, is_hit = False):
        self.is_ship = is_ship
        self.is_hit = is_hit
    
    def ship_in(self):
        self.is_ship = True
        return
    
    def hit_on(self):
        self.is_hit = True

    def __str__(self):
        return str(self.is_ship)

class Ship:
    def __init__(self, length):
        self.length = length

class Board:

    def __init__(self, size, ship_space_count):
        self.ship_space_count = ship_space_count
        self.board_tiles = []
        self.size = size
        self.guess_calc = 0
        for i in range(0,self.size):
            self.board_tiles.append([])
            for j in range(0,self.size):
                self.board_tiles[i].append(Tile())
    
    def board_check(self, ship, x, y, d, b_size):
        if d == 'H':
            if ship.length + x > b_size:
                return False
            else:
                for i in range (0, ship.length):
                    if self.board_tiles[y][x + i].is_ship == True:
                        return False
                return True
        else:
            if ship.length + y > b_size:
                return False
            else:
                for i in range (0, ship.length):
                    if self.board_tiles[y + i][x].is_ship == True:
                        return False
                return True
    
    def ship_space_counter(self, ship_space_count):
        for i in range(0,self.size):
            for j in range(0,self.size):
                if self.board_tiles[i][j].is_ship:
                    if self.board_tiles[i][j].is_hit:
                        ship_space_count -= 1
        self.ship_space_count = ship_space_count

    def place_ship(self, ship, x, y, d):
        self.board_tiles[y][x].ship_in()
        for i in range(0, ship.length):
            if d == 'H':
                self.board_tiles[y][x + i].ship_in()
            else:
                self.board_tiles[y + i][x].ship_in()

    def __getitem__(self,index):
        return self.board_tiles[index]

    def __len__(self):
        return self.size

    def __str__(self):
        return str(self.board_tiles)
