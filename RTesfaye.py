#ACME payroll
i = 0
while i != 5:
    Name = input("Enter employee name :")
    Hours = float(input("enter hours worked :"))
    Rate = float(input("hourly pay : "))

    grosspay = Hours * Rate
    fed_tax = grosspay * 0.1
    state_tax = grosspay * 0.03
    fica = round(grosspay * 0.07)
    overtime= Hours * 1.5
    print(f"grosspay  {Rate * Hours: }")
    print(f"Fed Tax  {fed_tax: }")
    print(f"state tax {state_tax: }")
    print(f"fica {fica: }")
    print(f"net_pay $ {grosspay - fed_tax - state_tax - fica} ")
    if Hours < 40:
        overtime = 0
    elif Hours == 40:
        overtime = 0
    else:
        overtime = (Hours - 40) * 1.5 * Rate
    print(i)
    i += 1

