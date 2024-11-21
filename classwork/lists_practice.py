

my_numbers: list[float] = [] #literal
my_numbers: list[float] = list() #constructor

print(my_numbers)

my_numbers.append(1.5)
my_numbers.append(2.3)

print(my_numbers)

#Create an already populated list 
game_points: list[int] = [102, 86, 94]
print(game_points)

# Subscription Notation/Indexing
#print(game_points[2])
last_game: int = game_points[2]
#print(last_game)

# Modifying elements
game_points[1] = 72
print(game_points)


#Remove an element
game_points.pop(1)
print(game_points)

