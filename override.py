
def PrintMsg(x):
    print(x)

def PrintMsg(x):
    print("-->",x)

PrintMsg(11)

class parent:
    
    def show(self):
        print("inside parent")

class child(parent):
    
    def show(self):
        # EXPLICIT CALL TO PARENT CLASS
        super().show()
        print("inside child")

s = child()
s.show()
