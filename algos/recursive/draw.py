import turtle

# 递归画螺旋正方形
def draw_spiral(tur, line_len):
    if line_len > 0:
        tur.forward(line_len)
        tur.right(90)
        draw_spiral(tur, line_len - 5)


# 递归绘制分形树
def _draw_tree(tur, branch_len):
    if branch_len > 5:
        tur.forward(branch_len)
        tur.right(20)
        _draw_tree(tur, branch_len - 15)
        tur.left(40)
        _draw_tree(tur, branch_len - 15)
        tur.right(20)
        tur.backward(branch_len)


def draw_tree(t, branch_len):
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    _draw_tree(t, branch_len)


my_turtle = turtle.Turtle()
my_win = turtle.Screen()
# draw_spiral(my_turtle, 85)
draw_tree(my_turtle, 85)
my_win.exitonclick()
