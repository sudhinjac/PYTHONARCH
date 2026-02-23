class Employee:
    totalEmployees = 0
    
    def __init__(self,empno,ename,salary,deptno):
        self.Empno = empno
        self.Ename = ename
        self.Salary = salary
        self.Deptno = deptno
        Employee.totalEmployees +=1
        
    def showEmployee(self):
        print("Employee # : {} \nEmployee Name : {} \n \
              Salary : {}\nDepartment: {}\n".format(self.Empno,\
            self.Ename,self.Salary,self.Deptno))
        
        
e1 = Employee(101, "Sudhin", 4500, 10)
e2 = Employee(101, "Jacob", 8500, 20)
print("Total Employees: ",Employee.totalEmployees)
e1.showEmployee()
e2.showEmployee()
print("Total Employees: ",Employee.totalEmployees)


        
        