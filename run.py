import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('empdata')


print("""
      ------------------------------------------------------
     |======================================================| 
     |======== Welcome To Employee Data System==============|
     |======================================================|
      ------------------------------------------------------   
      
     |------------- Important Information ------------------| 
    
             To login please create a new registration
         Enter any information on the username and password
         Then register as a new user, type Y to register          
""")

class LoginUser:
    def __init__(self):
        self.data = {}
    def add_user(self, login, password):
        if login in self.data:
            raise AssertionError('User already exists')

        self.data[login] = password

    def check_user(self, login, password):
        if not login in self.data:
            return False

        if self.data[login] != password:
            return False

        return True


class LoginManager:
    def __init__(self):
        self.store = LoginUser()

    def _ask_input_and_password(self):
        username = input("username: \n")
        password = input("password: \n")
        return username, password

    def login_check(self):
        username, password  = self._ask_input_and_password()

        while not self.store.check_user(username, password):
            print("Wrong username or password\n")
            if input("Are you a new user?  type Y to register : \n") == "y":
                print("Starting registration process\n")
                username, password = self._ask_input_and_password()
                self.store.add_user(username, password)
                print("Done. Try to login.\n")
            username, password  = self._ask_input_and_password()

manager = LoginManager()
manager.login_check()

class Employee:
    employeeList = list()
    #count = 0
    def __init__(self, empNo, empName, empDes, empSal):
        self.empNo, self.empName, self.empDes, self.empSal = empNo, empName, empDes, empSal
    def addNewEmployee(self):
        Employee.employeeList.append(self)
    def getEmpList(self):
            return Employee.employeeList
    def getEmpById(self, empNo):
        for emp in Employee.employeeList:
            if(emp.getEmpNo() == empNo):
                return emp
        return False
    def updateEmpById(self, empNo, empName, empDes, empSal):
        for emp in Employee.employeeList:
            if(emp.getEmpNo() == empNo):
                emp.empNo, emp.empName, emp.empDes, emp.empSal = empNo, empName, empDes, empSal
                return True
            return False

    def removeEmpById(self, empNo):
        for emp in Employee.employeeList:
            if(emp.getEmpNo() == empNo):
                Employee.employeeList.remove(emp)
                return True
            return False


    def setEmpNo(self, empNo):
            self.empNo = empNo
    def getEmpNo(self):
            return self.empNo

    def setEmpName(self, empName):
            self.empName = empName
    def getEmpName(self):
            return self.empName

    def setEmpDes(self, empDes):
            self.empDes = empDes
    def getEmpNo(self):
            return self.empDes

    def setEmpSal(self, empSal):
            self.empSal = empSal
    def getEmpSal(self):
            return self.empSal

    def __str__(self):
           return "%d %s %s %d" % (self.empNo, self.empName, self.empDes, self.empSal)

choice = 1
employee = Employee(0, "", "", 0.0)
while choice >= 1 and choice <= 5:
    print("\n\n1. Add New Employee\n2. Get All Employee List\n3. Get Employee By Id\n4. Update Employee By Id\n5. Remove Employee By Id\n\n")
    choice = int(input("Enter Your Choice:\n" ))
    if(choice == 1):
        empNo =int(input("Enter Employee No : \n"))
        empName = input("Enter Employee Name : \n")
        empDes = input("Enter Employee Designation : \n")
        empSal = float(input("Enter Employee Salary :\n "))
        emp = Employee(empNo, empName, empDes, empSal)
        emp.addNewEmployee()

    elif(choice == 2):
        print("\n")
        for emp in employee.getEmpList():
               print(emp)

    elif(choice == 3):
        empNo = int(input("Enter Emplyee No \n" ))
        emp = employee.getEmpById(empNo)
        if(emp == False):
            print("\nSorry..! Employee Not Found For ID : \n", empNo)
        else:
            print(emp)

    elif(choice == 4):
        empNo = int(input("Enter Employee No : \n"))
        empName = input("Enter Employee Name : \n")
        empDes = input("Enter Employee Designation : \n")
        empSal = float(input("Enter Employee Salary : \n"))
        emp = employee.updateEmpById(empNo, empName, empDes, empSal)
        if (emp == False):
            print("\nSorry..! Update Failed , Employee Not Found for Id : \n" , empNo)
        else:
            print("Successfully Updated Employee For Id \n", empNo)

    elif(choice == 5):
        empNo = int(input("Enter Employee Id : \n"))
        emp = employee.removeEmpById(empNo)
        if(emp == False):
            print("\nSorry..! Delete Failed , Employee Not Found for Id :\n ", empNo)
        else:
            print("Successfully Deleted Employee For Id\n ", empNo)


