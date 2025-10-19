from turtle import Turtle

STARTING_POSITINS = [(0, 0), (-20, 0), (-40, 0)]



class Snake:
    def __init__(self):
      self.all_segments = []
      self.create_snake()
      self.head = self.all_segments[0]  # The first segment is the head of the snake

    def create_snake(self): # Create the initial snake by adding segments at the starting positions
        for position in STARTING_POSITINS:
            self.add_segment(position)

    def add_segment(self, position):    # Add a new segment to the snake at the given position
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.all_segments.append(new_segment) 

    def move(self): # Move the snake forward by updating the position of each segment
        for seg_num in range(len(self.all_segments) - 1, 0, -1):
            new_x = self.all_segments[seg_num - 1].xcor()
            new_y = self.all_segments[seg_num - 1].ycor()
            self.all_segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)
