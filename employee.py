"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract_type, monthly_contract = None, hourly_wage = None,
                 hours_worked = None, fixed_bonus_commission= None,  contracts_landed=None, 
                 commission_per_contract = None,):
        self.name = name
        self.contract_type = contract_type
        self.monthly_contract = monthly_contract
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        self.fixed_bonus_commission = fixed_bonus_commission
        self.contracts_landed = contracts_landed
        self.commission_per_contract = commission_per_contract
    
    def calculate_contract_pay(self):
        if self.contract_type == 'monthly':
            return self.monthly_contract
        elif self.contract_type == 'hourly':
            return self.hours_worked*self.hourly_wage
        else:
            raise ValueError("Invalid contract")
    
    def calculate_commission(self):
        if self.fixed_bonus_commission is not None:
            return self.fixed_bonus_commission
        elif self.contracts_landed is not None and self.commission_per_contract is not None:
            return self.contracts_landed*self.commission_per_contract
        else:
            return 0



    def get_pay(self):
        contractPay = self.calculate_contract_pay()
        commissionPay = self.calculate_commission()
        total_pay = contractPay + commissionPay
        return total_pay

    def __str__(self):
        employeeName = self.name
        return f"{employeeName} {self.pay_description()}"
    
    def pay_description(self):
        #contractPay = self.calculate_contract_pay
        #commissionPay = self.calculate_commission
        #total_pay = contractPay + commissionPay
        monthlySalary = self.monthly_contract
        hoursWorked = self.hours_worked
        hourlyWage = self.hourly_wage
        bonusCommission = self.fixed_bonus_commission
        contractsLanded = self.contracts_landed
        commisionPerContract = self.commission_per_contract
        if self.commission_per_contract is not None and self.contracts_landed is not None:
            if self.contract_type == 'hourly':
                return f"works on a contract of {hoursWorked} hours at {hourlyWage}/hour and receives a commission for {contractsLanded} contract(s) at {commisionPerContract}/contract. Their total pay is {self.get_pay()}."
            elif self.contract_type == 'monthly':
                return f"works on a monthly salary of {monthlySalary} and receives a commission for {contractsLanded} contract(s) at {commisionPerContract}/contract. Their total pay is {self.get_pay()}."

        elif self.fixed_bonus_commission is not None:
            if self.contract_type == 'hourly':
                return f"works on a contract of {hoursWorked} hours at {hourlyWage}/hour and receives a bonus commission of {bonusCommission}. Their total pay is {self.get_pay()}."
            elif self.contract_type == 'monthly':
                return f"works on a monthly salary of {monthlySalary} and receives a bonus commission of {bonusCommission}. Their total pay is {self.get_pay()}."

        else:
            if self.contract_type == 'hourly':
                return f"works on a contract of {hoursWorked} hours at {hourlyWage}/hour. Their total pay is {self.get_pay()}."
            elif self.contract_type == 'monthly':
                return f"works on a monthly salary of {monthlySalary}. Their total pay is {self.get_pay()}."


            
#Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.

        


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee(name ='Billie', contract_type='monthly', monthly_contract=4000)
charlie = Employee(name ='Charlie', contract_type='hourly', hours_worked=100, hourly_wage=25)
renee = Employee(name ='Renee', contract_type='monthly', monthly_contract=3000, contracts_landed=4, commission_per_contract=200)
jan = Employee(name ='Jan', contract_type='hourly', hours_worked=150, hourly_wage=25, contracts_landed=3, commission_per_contract=220)
robbie = Employee(name ='Robbie', contract_type='monthly', monthly_contract=2000, fixed_bonus_commission=1500)
ariel = Employee(name ='Ariel', contract_type='hourly', hours_worked=120, hourly_wage=30, fixed_bonus_commission=600)
print (str(jan))
print (str(renee))
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
#charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
#renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
#jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
#robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
#ariel = Employee('Ariel')
