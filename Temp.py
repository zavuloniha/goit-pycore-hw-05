import re

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."


#def sum_profit(text: str, func: Callable):

n = []
pattern = r"\d{2,10}\.\d+"
total = 0
 
match = re.findall(pattern, text)
for item in match:
    print(item)
    total += float(item)
print(match)
print(total)

# match = re.search(pattern, text)
# if match: 
#     number = float(match.group())
#     print(number)
#     total += number
#     print(total)
# else:
#     print("not found")
    #number_f = re.sub()
    #n = n.append(number)
    
    #print(n)
    
    #yield number

    #total_sum += number    
#print(generator_numbers(text))


# pattern = r"\n"
# removing = ""

# def total_salary(path):
#     number_of_lines = 0
#     total_salaries = 0
#     try:
#         with open(path, "r", encoding='utf-8') as file:
#             text_in_file = file.readlines()
#             for ln in text_in_file:
#                 line_data = re.split(',', ln)
#                 number_in_line = int(re.sub(pattern, removing, line_data[1]))
#                 total_salaries += number_in_line