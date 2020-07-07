#Water Jug Problem for Jugs having capacity 4 & 3 which reaches any of the Goal States (x=2,y=0), (x=2,y=1),(x=2,y=2),(x=2,y=3)
CapacityA=4
CapacityB=3
print("[Intially Both Jugs are empty...]")
print("[Capacity of Jug A is 4 and capacity of Jug B is 3]")
print("[Your Goal is to reach any of the Goal States (x=2,y=0), (x=2,y=1),(x=2,y=2),(x=2,y=3)]")
goal_x = 2
goal_y = (0,1,2,3)
x = 0
y = 0
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
        
    if(x!=goal_x or (y not in goal_y)):
        process()
    else:
        print("\nGoal Achieved...")

        
def fillA():
    global x,y, goal_x, goal_y, CapacityA, CapacityB
    if(x<CapacityA):
        print("A Filled Successfully...")
        x=4
        print("(",x,",",y,")")
    else:
        print("A is already Filed...")
        print("(",x,",",y,")")
        
def fillB():
    global x,y, goal_x, goal_y, CapacityA, CapacityB
    if(y<CapacityB):
        print("B Filled Successfully...")
        y=3
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
    if(x+y<=3):
        y=x+y
        x=0
        
    else:
        x=x-(3-y)
        y=3
    print("(",x,",",y,")")

def transfer_BtoA():
    global x,y, goal_x, goal_y, CapacityA, CapacityB
    if(x+y<=4):
        x=x+y
        y=0
    else:
        y=y-(4-x)
        x=4
        
    print("(",x,",",y,")")
    
process()    

