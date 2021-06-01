class cal4:
    n=0
    def setdata(self,n):
        self.n=n
        ans=self.display()
        print('Area of circle is ',ans)
                
    def display(self):
        ans= n*n
        return ans
        
        
c1=cal4()
print('Enter value')
n=int(input())
c1.setdata(n)
