import turtle


class Brush(turtle.Turtle):

    def __init__(self):
        super().__init__()
        
    def draw(self, func):
        self.pendown()
        self.lt(90)
        self.fd(100)
        func()
        self.penup()
        self.home()

    def one(self):
        self.rt(90)
        self.fd(45)

    def two(self):
        self.penup()
        self.bk(33)
        self.pendown()
        self.rt(90)
        self.fd(45)

    def three(self):
        self.rt(125)
        self.fd(50)

    def four(self):
        self.penup()
        self.bk(33)
        self.pendown()
        self.rt(55)
        self.fd(55)

    def five(self):
        self.rt(90)
        self.fd(45)
        self.rt(135)
        self.fd(65)

    def six(self):
        self.penup()
        self.rt(90)
        self.fd(45)
        self.rt(90)
        self.pendown()
        self.fd(33)

    def seven(self):
        self.rt(90)
        self.fd(45)
        self.rt(90)
        self.fd(33)

    def eight(self):
        self.penup()
        self.bk(33)
        self.pendown()
        self.rt(90)
        self.fd(45)
        self.lt(90)
        self.fd(32)

    def nine(self):
        self.penup()
        self.bk(33)
        self.pendown()
        self.rt(90)
        self.fd(45)
        self.lt(90)
        self.fd(32)
        self.lt(90)
        self.fd(46)

    def ten(self):
        self.lt(90)
        self.fd(45)

    def twenty(self):
        self.bk(33)
        self.pendown()
        self.lt(90)
        self.fd(45)

    def thirty(self):
        self.lt(125)
        self.fd(50)
