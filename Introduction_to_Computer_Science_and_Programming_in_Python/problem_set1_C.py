#Part C Finding the right amount to save away 
#bisection search 

print("Enter you annual salary:")
salary = int(input())


def get_annual_salary(num_months, annual_salary = salary, increase_rate = 0.07):
    """
    Return the realtime annual salary, accounting for increase every 6 months
    """
    time_tracker = num_months//6 
    salary = annual_salary * (1 + increase_rate) ** time_tracker
    return salary

def get_savings(saving_rate_input, months = 36, 
                current_savings = 0, r = 0.04, 
                increase_rate = 0.07):
    """
    Return the amount of savings after the expected number of months given the savings rate
    """ 
    savings = current_savings
    saving_rate = saving_rate_input/10000

    for i in range(months):
        annual_salary = get_annual_salary(i)
        monthly_increase = annual_salary/12 * saving_rate + savings * (r/12)
        savings += monthly_increase

    return savings 

epsilon = 100 
num_steps = 0 
down_payment = 1000000 * 0.25
low = 0 
high = 10000
ans = (low + high)/2
solution_possible = True 

savings = get_savings(ans)

while abs(savings - down_payment) >= epsilon and solution_possible:
    num_steps += 1 
    #print('low ', low/10000, ' high ', high/10000, ' ans ', ans/10000)
    if savings > down_payment:
        high = ans 
    else:
        low = ans 

    if high > low:
        ans = (high + low)/2
        savings = get_savings(ans)

    else:
        solution_possible = False
        print("It is not possible to pay the down payment in three years.")
        break 

if solution_possible:   
    print(f"Best savings rate: {ans/10000}")
    print(f"Steps in bisection search: {num_steps}")
