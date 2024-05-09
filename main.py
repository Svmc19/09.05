# Task1
# def sums_array(lst):
#         if sum(lst) > 1:
#             return str(f"{sum(lst)} ohms")
#         else:
#             return str(f"{sum(lst)} ohm")
#
# print(sums_array([1,5,6,3]))
# print(sums_array([16,3.5,6]))
# print(sums_array([0.5,0.5]))

# Task2

# def asc_des_none(lst):
#     string = input("3 ta shartdan birini kiriting -- > Asc/Des/None:")
#     if string == "Asc":
#         return sorted(lst)
#     elif string == "Des":
#         sorting = lst.sort(reverse=True)
#         return sorting
#     elif string == "None":
#         return lst
#     else:
#         return f"Make sure you entered one of the three options above!"
#
# print(asc_des_none([7,69,11,66]))

# Task3
# def nums(numbers):
#     lst = []
#     func = numbers[0] // 2
#
#     d = numbers[0] - func
#
#     lst.append(func)
#     lst.append(d)
#
#     return lst
#
# print(nums([4]))
# print(nums([10]))
# print(nums([11]))
# print(nums([-9]))