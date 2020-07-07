#Water Jug Problem 
CapacityA=int(input("Enter Capacity of Jug A:"))
CapacityB=int(input("Enter Capacity of Jug B:"))
goal_x = int(input("Enter Goal State of Jug A:"))
goal_y = int(input("Enter Goal State of Jug B:"))
x = 0
y = 0
print("\n[Intially Both Jugs are empty...]")
print("[Capacity of Jug A is", CapacityA," and capacity of Jug B is ",CapacityB,"]")
print("[Your Goal is to reach Goal State (",goal_x,",",goal_y,")]")

def process():
    global x,y, goal_x, goal_y, CapacityA, CapacityB
    print("\nEnter 1 to Fill A, Enter 2 to Fill B, Enter 3 to Empty A, Enter 4 to Empty B, Enter 5 to Transfer A to B, Enter 6 to Transfer B to A ")
    key=int(input("Enter Your choice:"))
    if(key==1):
        fillA()
    if(key==2):
        fillB()
    if(key==3):
        emptyA()
    if(key==4):
        emptyB()
    if(key==5):
        transfer_AtoB()
    if(key==6):
        transfer_BtoA()
        
    if(x!=goal_x or y!=goal_y):
        process()
    else:
        print("\nGoal Achieved...")

        
def fillA():
    global x,y, goal_x, goal_y, CapacityA, CapacityB
    if(x<CapacityA):
        print("A Filled Successfully...")
        x=CapacityA
        print("(",x,",",y,")")
    else:
        print("A is already Filed...")
        print("(",x,",",y,")")
        
def fillB():
    global x,y, goal_x, goal_y, CapacityA, CapacityB
    if(y<CapacityB):
        print("B Filled Successfully...")
        y=CapacityB
        print("(",x,",",y,")")
    else:
        print("B is already Filled...")
        print("(",x,",",y,")")

       
def emptyA():
    global x,y, goal_x, goal_y, CapacityA, CapacityB
    if(x>0):
        print("A Emptied Successfully...")
        x=0
        print("(",x,",",y,")")
    else:
        print("A is already Empty...")
        print("(",x,",",y,")")
    
def emptyB():
    global x,y, goal_x, goal_y, CapacityA, CapacityB
    if(y>0):
        print("B Emptied Successfully...")
        y=0
        print("(",x,",",y,")")
    else:
        print("B is already Empty...")
        print("(",x,",",y,")")
    
def transfer_AtoB():
    global x,y, goal_x, goal_y, CapacityA, CapacityB
    if(x+y<=CapacityB):
        y=x+y
        x=0
        
    else:
        x=x-(CapacityB-y)
        y=CapacityB
    print("(",x,",",y,")")

def transfer_BtoA():
    global x,y, goal_x, goal_y, CapacityA, CapacityB
    if(x+y<=CapacityA):
        x=x+y
        y=0
    else:
        y=y-(CapacityA-x)
        x=CapacityA
        
    print("(",x,",",y,")")
    
process()    

