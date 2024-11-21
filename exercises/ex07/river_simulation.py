__author__: str = "730715418"

from river import River

# Create a River with 10 Fish and 2 Bears
my_river = River(num_fish=10, num_bears=2)

# Call the view_river method to view the river's status
my_river.view_river()

# Simulate one week in the river
my_river.one_river_week()
