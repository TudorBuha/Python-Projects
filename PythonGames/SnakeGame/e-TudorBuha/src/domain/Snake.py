class Snake:
    def __init__(self, initial_position, initial_length=3, initial_direction='RIGHT'):
        self.direction = initial_direction
        self.segments = [Segment(initial_position[0], initial_position[1] - i) for i in range(initial_length)]

    def move(self):
        new_head = self.create_new_head()
        self.segments.insert(0, new_head)
        self.segments.pop()

    def grow(self):
        tail = self.segments[-1]
        new_segment = Segment(tail.x, tail.y)
        self.segments.append(new_segment)

    def create_new_head(self):
        head = self.segments[0]
        if self.direction == 'UP':
            return Segment(head.x, head.y - 1)
        elif self.direction == 'DOWN':
            return Segment(head.x, head.y + 1)
        elif self.direction == 'LEFT':
            return Segment(head.x - 1, head.y)
        elif self.direction == 'RIGHT':
            return Segment(head.x + 1, head.y)

    def change_direction(self, new_direction):
        opposite_directions = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
        if new_direction != opposite_directions[self.direction]:
            #print("The snake cant turn 180 degrees!")
            self.direction = new_direction


class Segment:
    def __init__(self, x, y):
        self.x = x
        self.y = y
