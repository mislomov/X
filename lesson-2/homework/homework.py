# 1. Age Calculator
age = input("Year of birth: ")
print("Your age is: ", 2025-int(age))

# 2. Extract Car Names
txt = 'LMaasleitbtui'
car_name = txt[1] + txt[2] + txt[5] + txt[7] + txt[9] + txt[11]
print(car_name)

# # 3. Extract Car Names    
txt = 'MsaatmiazD'
car_name2 = txt[0] + txt[2] + txt[4] + txt[6] + txt[8] 
print(car_name2)

# 4. Extract Residence Area
txt = "I'am John. I am from London"
residence_area = txt[-6:]
print(residence_area)

# 5. Reverse String
user_input = input("Please enter: ")
print(user_input[::-1])


# 6. Count Vowels
txt = input("Please enter: ")
vowels = "aeiouAEIOU"
print("Number of vowels are: ", sum(txt.count(vowel)for vowel in vowels))

# 7. Find Maximum Value
numbers = list(map(int,(input("Enter numbers: ").split())))
find_max = max(numbers)
print("Max: ", find_max)

# # 8. Check Palindrome
txt = input("Please enter: ")
if txt == txt[::-1]:
    print("Palindrome")
else:
        print("not palindrome")

# 9. Extract Email Domain
txt = input("Enter email: ")
print("Domain is: ", txt.split("@")[-1])
