from math import sqrt, sin, cos, hypot
import random, pygame


class Grid(object):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.points = set()

    def add_point(self, x, y):
        self.points.add((x, y))


class PoissonDisc(object):
    
    def __init__(self, radius, num_points_to_generate, grid_width, grid_height):
        self.radius = radius
        self.n = num_points_to_generate
        self.size = radius / sqrt(self.n)

        self.grid = Grid(grid_width, grid_height)

    def generate(self):
        x0, y0 = self._random_point()

        active = [(x0, y0)]
        self._add_point(x0, y0)

        while len(active) > 0:
            random_x, random_y = random.choice(active)
            
            point = self.find_next_point(random_x, random_y)
            if point is not None:
                active.append(point)
            else:
                active.remove((random_x, random_y))

        return self.grid.points

    def _random_point(self):
        return (random.random() * self.size, random.random() * self.size)

    def _add_point(self, x, y):
        self.grid.add_point(x, y)

    def find_next_point(self, x, y):
        for i in range(self.n):
            modifier = random.random() * self.radius
            distance = self.radius + random.random() * self.radius
            new_x = x + cos(modifier) * distance
            new_y = y + sin(modifier) * distance
            if not self.is_valid_point(new_x, new_y):
                continue
            else:
                self._add_point(new_x, new_y)
            return (new_x, new_y)
        return None

    def is_valid_point(self, x, y):
        if not self._is_in_grid(x, y):
            return False

        for point_x, point_y in self.grid.points:
            if hypot(x - point_x, y - point_y) < self.radius:
                return False

        return True

    def _is_in_grid(self, x, y):
        return x >= 0 and x < self.grid.width and y >= 0 and y < self.grid.height


def setup_screen(width):
    pygame.init()
    surface = pygame.display.set_mode((WIDTH,WIDTH), 0, 32)
    background = pygame.Surface(surface.get_size())
    background = background.convert()
    background.fill((250,250,250))
    surface.blit(background, (0,0))
    pygame.display.flip()

    return surface


def draw_points(points):
    for x, y in points:
        pygame.draw.circle(surface, (0,0,0), (int(x), int(y)), 1, 0)


if __name__ == '__main__':
    WIDTH = 200
    disc = PoissonDisc(8, 16, WIDTH, WIDTH) 
    surface = setup_screen(WIDTH)
    
    points = disc.generate()
    print(points)
    draw_points(points)
    
    while 1:
        pygame.display.flip()

