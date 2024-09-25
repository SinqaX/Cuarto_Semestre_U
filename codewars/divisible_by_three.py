"""
A trick I learned in elementary school to determine whether or not a number was divisible by three is to add all of the integers 
in the number together and to divide the resulting sum by three. If there is no remainder from dividing the sum by three, then the 
original number is divisible by three as well.

Given a series of digits as a string, determine if the number represented by the string is divisible by three.

Example:

"123"      -> true
"8409"     -> true
"100853"   -> false
"33333333" -> true
"7"        -> false
"""
# def divisible_by_three(st): 
#     result = sum(int(num) for num in st)
#     while result > 10:
#         result = sum(int(num) for num in str(result))
#     if result == 3 or result == 6 or result == 9:
#         return True
#     else:
#         return False
    

# print(divisible_by_three('123'))
# print(divisible_by_three('19254'))
# print(divisible_by_three('88'))
# print(divisible_by_three('1'))



def format_duration(seconds):
    if seconds == 0:
        return "now"
    else:
        if seconds > 60:
            minutes = seconds / 60
            print(f"minutes {minutes}")
            if minutes > 60:
                hours = minutes / 60
                print(f"hours {hours}")
                if hours > 24:
                    days = hours / 24
                    print(f"days {days}")
                    if days > 365:
                        years = days / 365
                        print(f"years {years}")
    
format_duration(0)
format_duration(1)
format_duration(62)
format_duration(120)
format_duration(3600)
format_duration(3662)
format_duration(15731080)
format_duration(132030240)
format_duration(205851834)
format_duration(253374061)
format_duration(242062374)
format_duration(101956166)
format_duration(33243586)