from datetime import date, timedelta
# from dateutil.relativedelta import relativedelta

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def compound_interest(principle, rate, time): 
    Amount = principle * (pow((1 + rate / (365 * 100)), time)) 
    CI = round(Amount - principle, 2)
    return CI

if __name__ == '__main__':

    p = 4000
    r = 10
    t = 1
    print(compound_interest(p,r,t))
    # print(calculate_age())



