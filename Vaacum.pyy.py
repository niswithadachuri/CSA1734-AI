import random

class VacuumCleaner:
    def _init_(self:  
        self.position = (0, 0)  
        self.environment = [
            ['Clean', 'Dirty'],
            ['Dirty', 'Clean']
        ]
    
    def is_dirty(self, row, col):
        return self.environment[row][col] == 'Dirty'
    
    def clean(self, row, col):
        print(fCleaning dirt at position ({row}, {col}))  
        self.environment[row][col] = 'Clean'
    
    def move(self):
        possible_moves = [
            (0, 1),   
            (0, -1),  
            (1, 0),   
            (-1, 0)   
        ]
        random_move = random.choice(possible_moves)
        new_position = (self.position[0] + random_move[0], self.position[1] + random_move[1])
        
       
        if 0 <= new_position[0] < 2 and 0 <= new_position[1] < 2:
            self.position = new_position
            print(f"Moving to position ({self.position[0]}, {self.position[1]})")
        else:
            print("Invalid move, staying in current position")
        
        
        if self.is_dirty(self.position[0], self.position[1]):
            self.clean(self.position[0], self.position[1])


cleaner = VacuumCleaner()


for _ in range(5):
    cleaner.move()
