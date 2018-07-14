class Direction:
   """
   Uses the state pattern to assign which direction to next add integers

   next_space_to_fill and next_direction are left as empty to imply that they're
   defined by the subclasses below
   """

   def next_space_to_fill(self, x, y):
      """
      Returns where in the matrix to next place values
      """
      raise NotImplementedError()

   def next_direction(self):
      """
      Returns the next state
      """
      raise NotImplementedError()

   def has_obstruction(self, matrix, x, y):
      """
      There's an obstruction if the next area to place numbers
      is over the matrix bounds,
      or if there has already been a value assigned to that cell

      A value is defined to be a non-0 value
      """

      x, y = self.next_space_to_fill(x, y)
      x_len = len(matrix[0])
      y_len = len(matrix)

      # Next index exceeds matrix index
      if x>=x_len or y>=y_len:
         print("Reached length")
         return True

      # Has a value
      if matrix[y][x]!=0:
         print("Has value")
         return True
      return False

class Up(Direction):
   def next_space_to_fill(self, x, y):
      return(x, y-1)

   def next_direction(self):
      return Right()

class Right(Direction):
   def next_space_to_fill(self, x, y):
      return(x+1, y)

   def next_direction(self):
      return Down()

class Down(Direction):
   def next_space_to_fill(self, x, y):
      return(x, y+1)

   def next_direction(self):
      return Left()

class Left(Direction):
   def next_space_to_fill(self, x, y):
      return(x-1, y)

   def next_direction(self):
      return Up()

class Context:
   def __init__(self, matrix, direction=Right()):
      self.matrix = matrix
      self.direction = direction
      self.x = -1 #We start at a negative index so that the next cell to place values is (0,0)
      self.y = 0

   def fill_matrix(self):
      print("direction: {}".format(self.direction))
      x_len = len(self.matrix[0])
      y_len = len(self.matrix)
      limit = x_len*y_len+1

      # We start at 1 since 0 is our place holder for an empty value
      for i in range(1, limit):
         has_obstruction = self.direction.has_obstruction(self.matrix, self.x, self.y)

         if has_obstruction:
            self.direction = self.direction.next_direction()

         self.x, self.y = self.direction.next_space_to_fill(self.x, self.y)
         self.matrix[self.y][self.x] = i

         self._print_status(i)

   def _print_status(self, i):
      """
      Prints information about the matrix such as:
      the current value of i,
      and how the matrix currently looks like
      """

      # Print a nice border to separate the different print statement groups
      print("="*25)

      print("i is: {}".format(i))
      for row in self.matrix:
         print(row)

      print()
      print("next space to fill: ({},{})".format(self.x,self.y))
      print()