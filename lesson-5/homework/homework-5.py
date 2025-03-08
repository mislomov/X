# 1. Modify String with Underscores
def add_underscores(txt):
    result = ""
    count = 0
    i = 0
    while i < len(txt):
        result += txt[i]
        count += 1
        if count == 3 and i < len(txt) - 1:
            if txt[i] in 'aeiouAEIOU' or (i + 1 < len(txt) and txt[i+1] in 'aeiouAEIOU'):
                count = 0
            else:
                result += '_'
                count = 0
        i += 1
    return result

# 2. Integer Squares
def print_squares(n):
    for i in range(n):
        print(i ** 2)

# 3. Loop-Based Exercises
def print_natural_numbers():
    i = 1
    while i <= 10:
        print(i)
        i += 1

def print_pattern():
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def calculate_sum(n):
    return sum(range(1, n + 1))

def print_multiplication_table(n):
    for i in range(1, 11):
        print(n * i)

def filter_numbers(numbers):
    for num in numbers:
        if num <= 150 and num % 5 == 0:
            print(num)

def count_digits(n):
    return len(str(abs(n)))

def print_reverse_pattern():
    for i in range(5, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

def print_reverse_list(lst):
    for i in range(len(lst)-1, -1, -1):
        print(lst[i])

def print_negative_numbers():
    for i in range(-10, 0):
        print(i)

def print_with_done():
    for i in range(5):
        print(i)
    print("Done!")

def print_primes(start, end):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)

def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 4. Return Uncommon Elements
def uncommon_elements(list1, list2):
    count1 = {}
    count2 = {}
    
    for item in list1:
        count1[item] = count1.get(item, 0) + 1
    for item in list2:
        count2[item] = count2.get(item, 0) + 1
    
    result = []
    for item in count1:
        if item not in count2:
            result.extend([item] * count1[item])
    for item in count2:
        if item not in count1:
            result.extend([item] * count2[item])
            
    return result

# Test examples
if __name__ == "__main__":
    print("Testing add_underscores:")
    print(add_underscores("hello"))  # hel_lo
    print(add_underscores("assalom"))  # ass_alom
    
    print("\nTesting uncommon_elements:")
    print(uncommon_elements([1, 1, 2], [2, 3, 4]))  # [1, 1, 3, 4]
    print(uncommon_elements([1, 2, 3], [4, 5, 6]))  # [1, 2, 3, 4, 5, 6]