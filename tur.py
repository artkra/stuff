import turtle

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(15)
        tree(branchLen-10,t)
        t.left(30)
        tree(branchLen-10,t)
        t.right(15)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(150)
    t.down()
    t.color('black')
    tree(100,t)
    myWin.exitonclick()

main()