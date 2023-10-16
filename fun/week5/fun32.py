
# class definition
class Point:
    def __init__(self,x, y):
        self.x = x
        self.y = y

# function decleration to locate a point
def where_is(point):
    match Point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"x={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
    
# main execution
if __name__ == '__main__':
    p1 = Point(3,5)
    where_is(p1)