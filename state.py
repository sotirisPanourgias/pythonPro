class State:
    def __init__(self, missionaries_left, cannibals_left, boat_position, total_time=0):
        self.missionaries_left = missionaries_left
        self.cannibals_left = cannibals_left
        self.boat_position = boat_position
        self._f = 0
        self._g = total_time
        self._h = 0
        self._father = None
        self._total_time = total_time


    @property
    def f(self):
        return self._f

    @property
    def g(self):
        return self._g

    @property
    def h(self):
        return self._h

    @property
    def father(self):
        return self._father

    @property
    def total_time(self):
        return self._total_time

    @f.setter
    def f(self, f):
        self._f = f

    @g.setter
    def g(self, g):
        self._g = g

    @h.setter
    def h(self, h):
        self._h = h

    @father.setter
    def father(self, f):
        self._father = f

    @total_time.setter
    def total_time(self, time):
        self._total_time = time

    def evaluate(self, N, M):
        self._h = (self.missionaries_left + self.cannibals_left - self.boat_position) / M
        self._f = self._g + self._h


    def get_children(self,N):
        children = []
        move_directions = [(-1, -1), (-1, 0), (0, -1), (-2, 0), (0, -2)]

        for d_m, d_c in move_directions:
            new_missionaries_left = self.missionaries_left + d_m * (-1 if self.boat_position == 0 else 1)
            new_cannibals_left = self.cannibals_left + d_c * (-1 if self.boat_position == 0 else 1)
            new_boat_position = 1 - self.boat_position

            new_state = State(new_missionaries_left, new_cannibals_left, new_boat_position, self._total_time + 1)
            if new_state.is_valid(N):
                new_state.father = self
                children.append(new_state)

        return children
    def is_valid(self,N):
        if self.missionaries_left < 0 or self.cannibals_left < 0:
            return False
        if self.missionaries_left > 0 and self.missionaries_left < self.cannibals_left:
            return False
            # Απέναντι όχθη
        missionaries_right = N - self.missionaries_left
        cannibals_right = N - self.cannibals_left
        if missionaries_right > 0 and missionaries_right < cannibals_right:
            return False
        return True

    def is_final(self):
        return self.missionaries_left == 0 and self.cannibals_left == 0

    def __eq__(self, obj):
        return (self.missionaries_left == obj.missionaries_left and
                self.cannibals_left == obj.cannibals_left and
                self.boat_position == obj.boat_position)

    def __hash__(self):
        return hash((self.missionaries_left, self.cannibals_left, self.boat_position))

    def __lt__(self, s):
        return self.f < s.f