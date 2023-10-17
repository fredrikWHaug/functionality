
#class declaration for point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# function declaration for matching point with case
def where_is(point):
    match point:
        case Point(x=0, y=0):
            print(f'Origin')
        case Point(x=x, y=0):
            print(f'x={x} y=0')
        case Point(x=0, y=y):
            print(f'x=0 y={y}')
        case Point(x=x, y=y):
            print(f'x={x} y={y}')
        case Point():
            print('Not a point')
        case _:
            print('Not a point')

# main exection
if __name__ == '__main__':
    p1 = Point(1, 9)
    p2 = Point(69, 420)
    where_is(p1)
    where_is(p2)