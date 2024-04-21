stack=[]
top=-1
n=5
def push(val):
    global top
    if top>=n-1:
        print("stack overflow")
    else:
        top+=1
        stack.append(val)
def pop():
    global top
    if top<=-1:
        print("stack underflow")
    else:
        print(f"the poped element is {stack[top]}")
        stack.pop()
        top-=1
def isfull():
    global top
    if top>=n-1:
        print("stack overflow")
    else:
        print("No,stack is not full")
def isempty():
    global top
    if top<=-1:
        print("stack underflow")
    else:
        print("NO,stack is not empty")
def display():
    global top
    if top>=0:
        print("the stack elements are :",end=" ")
        for i in range(top,-1,-1):
            print(stack[i], end=" ")
        print()
    else:
        print("stack is empty")
if __name__=="__main__":
    while True:
        print("1)Push to Stack")
        print("2)Pop from Stack")
        print("3)Is stack full?")
        print("4)Is stack empty?")
        print("5)Display Stack")
        print("6)Exit")
        ch=int(input("Enter choice : "))
        if ch==1:
            val=int(input("enter the value for push : "))
            push(val)
        elif ch==2:
            pop()
        elif ch==3:
            isfull()
        elif ch==4:
            isempty()
        elif ch==5:
            display()
        elif ch==6:
            print("exit")
            break
        else:
            print("invalid choice")
