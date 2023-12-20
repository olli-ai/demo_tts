class Shape:
    def accept(self, visitor):
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor):
        print("OK1")
        visitor.visit_circle(self)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def accept(self, visitor):
        print("OK1")
        visitor.visit_rectangle(self)


class ShapeVisitor:
    def visit_circle(self, circle):
        raise NotImplementedError

    def visit_rectangle(self, rectangle):
        raise NotImplementedError


class AreaCalculator(ShapeVisitor):
    def visit_circle(self, circle):
        return 3.14 * circle.radius**2

    def visit_rectangle(self, rectangle):
        return rectangle.width * rectangle.height


class Drawer(ShapeVisitor):
    def __init__(self, canvas):
        self.canvas = canvas

    def visit_circle(self, circle):
        # Draw a circle on the canvas
        pass

    def visit_rectangle(self, rectangle):
        # Draw a rectangle on the canvas
        pass


# Main function
def main():
    circle = Circle(5)
    rectangle = Rectangle(3, 4)

    area_calculator = AreaCalculator()

    print(f"Circle area: {area_calculator.visit_circle(circle)}")
    print(f"Rectangle area: {area_calculator.visit_rectangle(rectangle)}")

    drawer = Drawer("canvas")

    drawer.visit_circle(circle)
    drawer.visit_rectangle(rectangle)


if __name__ == "__main__":
    main()
