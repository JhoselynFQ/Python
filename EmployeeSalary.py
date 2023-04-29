class Employee:
    def __init__(self, name, experience, base_salary, monthly_hr_worked, total_hr_worked):
        self.name = name
        self.experience = experience
        self.base_salary = base_salary
        self.monthly_hr_worked = monthly_hr_worked
        self.total_hr_worked = total_hr_worked

    def calculate_salary(self):
        if self.experience < 8:
            salary = self.base_salary * self.monthly_hr_worked
        elif self.experience > 15:
            salary = (self.base_salary * self.monthly_hr_worked) + 3500 # bonus of 3500
        else:
            salary = self.base_salary * self.monthly_hr_worked
        return salary

    def calculate_tax(self):
        salary = self.calculate_salary()
        tax = salary * 0.13 # 13% tax deduction
        return tax

    def calculate_net_salary(self):
        salary = self.calculate_salary()
        tax = self.calculate_tax()
        net_salary = salary - tax
        return net_salary

# Example usage:
employee1 = Employee("Mirella", 7, 25, 160, 2000) # Mirella has 7 years of experience
print(f"{employee1.name}'s salary is {employee1.calculate_salary()} per month.")
print(f"{employee1.name}'s tax deduction is {employee1.calculate_tax()} per month.")
print(f"{employee1.name}'s net salary is {employee1.calculate_net_salary()} per month.")