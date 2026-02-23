class Employee:
    
    
    def __init__(self,empno,ename,salary,deptno):
        self.Empno = empno
        self.Ename = ename
        self.Salary = salary
        self.Deptno = deptno
        
        
    def showEmployee(self):
        print("Employee # : {} \nEmployee Name : {} \n \
              Salary : {}\nDepartment: {}\n".format(self.Empno,\
            self.Ename,self.Salary,self.Deptno))
        
        
class salesMan(Employee):
    
    def __init__(self,empno,ename,salary,deptno,comm):
        self.com = comm
        super().__init__(empno,ename,salary,deptno)
        
e1 = salesMan(101,"sudhin", 5400,10,500)
e1.showEmployee()
print("Commission: ",e1.com)
