class cal2:
    n1=0
    def setdata(self):
        print('Enter radius value')
        self.n1=int(input())
        self.area()

    def area(self):
        ans=3.14*(self.n1)*(self.n1)
        self.display(ans)
        
    def display(self,ans):
        print('Area of circle is ',ans)
        
c1=cal2()
c1.setdata()
