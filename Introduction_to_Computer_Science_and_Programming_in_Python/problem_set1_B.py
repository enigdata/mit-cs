#Part A House Hunting 

print("Enter you annual salary:")
salary = int(input())

print("Enter the percent of your salary to save, as a decimal: ")
portion_to_save = float(input())

print("Enter the cost of your dream home: ")
cost = int(input())

print("Enter the semi-annual salary raise:")
semi_annual_raise = float(input())

def get_annual_salary(num_months, annual_salary = salary, increase_rate = semi_annual_raise):
    """
    Return the realtime annual salary, accounting for increase every 6 months
    """
    time_tracker = num_months//6 
    salary = annual_salary * (1 + increase_rate) ** time_tracker
    return salary


def get_months_till_downpayment(annual_salary = salary, portion_down_payment = 0.25,
                                current_savings = 0, r = 0.04, increase_rate = semi_annual_raise,
                                portion_saved = portion_to_save, 
                                total_cost = cost):
    """
    Returns the number of months needed to save enough money for the down payment
    """

    savings = current_savings
    down_payment = total_cost * portion_down_payment

    counter = 0 
    while savings < down_payment:
        annual_salary = get_annual_salary(counter)
        monthly_increase = annual_salary/12 * portion_saved + savings * (r/12)
        savings += monthly_increase 
        counter += 1 

    return counter 

print(get_months_till_downpayment()) 