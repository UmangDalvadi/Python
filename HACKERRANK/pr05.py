# false for 2100 as an input

def is_leap(year):
    if year % 4 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 400 == 0:
        leap = True
    else:
        leap = False
    return leap


year = int(input())
print(is_leap(year))


# true for all inputs

# def is_leap(year):
#     leap = False
#     if year%400 == 0:
#         leap = True
#     else:
#         if year%100 ==0:
#             leap = False
#         else:
#             if year%4 == 0:
#                 leap = True
#             else:
#                 leap = False
#     return leap

# year = int(input())
# print(is_leap(year))
