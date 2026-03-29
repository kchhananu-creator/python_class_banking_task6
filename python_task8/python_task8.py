Bank_Name = { 
    'b1':'HDFC',
    'b2': 'ICICI',
    'b3': 'PNB'
}

bank_dict = {
        'Customer_name': 'Rohit', 
        'Account_number': 567, 
        'Balance' : 2000,
        'Acc_open_date' : '15/10/2025',
        'Acc_type' : 'Current'
        }

class Bank:
    def __init__(self,bankname,branchnum):
        self.BankName = bankname
        self.branchNumber = branchnum
        print("This is Bank Class")
    
    def BankDetails(self):
        if self.BankName == Bank_Name.get('b1'):
            print(f"The {Bank_Name.get('b1')} bank has 5 branch")
        elif self.BankName == Bank_Name.get('b2'):
            print(f"The {Bank_Name.get('b2')} bank has 3 branch")
        elif self.BankName == Bank_Name.get('b3'):
            print(f"The {Bank_Name.get('b3')} bank has 2 branch")


class National(Bank):
    def __init__(self,BankName):
        super().__init__(Bank_Name.get('b2'),3)
        print("It's National Bank Class")
        self.BankName = BankName
        print(f"Bank name is {self.BankName}")
        
     
bk1 = National('ICICI')
bk1.BankDetails()