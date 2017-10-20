import turtle

import math


class NodeDiagram:
    def __init__(self):
        self.my_nodes = []
        self.top = turtle.Turtle()
        self.top._screen.setup(700, 700)
        self.top.hideturtle()

    def addNode(self, node):
        self.my_nodes.append(node)

    def drawDiagram(self):
        self.top.penup()
        angle = 0
        rotate = 360 / len(self.my_nodes)

        for i in range(0, len(self.my_nodes)+1):
            x = 100 * math.sin(angle * 2 * math.pi / 360)
            y = 100 * math.cos(angle * 2 * math.pi / 360)
            self.top.seth(self.top.towards(x, y))
            if i > 0:
                self.top.pendown()
            self.top.color("blue")
            self.top.goto(x, y)
            self.top.dot(10, "red")
            self.top.color("black")
            if i < len(self.my_nodes):
                self.top.write(self.my_nodes[i][0])
                self.top.seth(self.top.heading() + 45)

                for j in range(0, len(self.my_nodes[i][1])):
                    self.top.seth(self.top.heading() - 15 * j)
                    oldx = self.top.xcor()
                    oldy = self.top.ycor()
                    self.top.pendown()
                    self.top.forward(130 + 30 * (j % 2))
                    self.top.write(self.my_nodes[i][1][j])
                    self.top.penup()
                    self.top.goto(oldx, oldy)
                    self.top.pendown()

            # self.top.seth(self.top.heading() + 45)

            angle += rotate

        self.top.penup()
        self.top.getscreen()._root.mainloop()


