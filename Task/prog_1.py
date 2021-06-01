class MyClass:
    n1=0
    n2=0
    n3=0
    def setdata(self,n1,n2,n3):
        self.n1=n1
        self.n2=n2
        self.n3=n3
        self.display()
        
    def display(self):
        ans = self.n1+ self.n2+ self.n3
        print('n1+n2+n3=',ans)
        
c1=MyClass()
print('Enter 3 value')
n1=int(input())
n2=int(input())
n3=int(input())
c1.setdata(n1,n2,n3)

    
