"""
Chef is playing badminton today. The service rules of this singles game of badminton are as follows:

The player who starts the game serves from the right side of their court.
Whenever a player wins a point, they serve next.
If the server has won an even number of points during a game, then they will serve from the right side of the service court for the subsequent point.
Chef will be the player who begins the game.

Given the number of points P obtained by Chef at the end of the game, please determine how many times Chef served from the right side of the court.

Please see the sample cases below for explained examples.
"""
n = int(input())

for i in range(n):
    x=int(input())
    y=(x-int(x/2))
    if (x%2==0):
        print(y+1)
    else:
        print(y)
    
