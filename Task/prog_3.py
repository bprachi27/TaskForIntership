class cal3:
    p=0
    r=0
    t=0
    def __init__(self):
        print('Enter values of p,r,t(time in year)')
        self.p=int(input())
        self.r=float(input())
        self.t=int(input())

    def cllinterest(self):
        i= (self.p*self.r*self.t)/100
        self.display(i)
        
    def display(self,ans):
        print('Area of circle is ',ans)
        
c1=cal3()
c1.cllinterest()
