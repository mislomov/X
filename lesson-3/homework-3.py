# 1. Create and Access List Elements
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[2])

# 2. Concatenate Two Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print(concatenated_list)

# 3. Extract Elements from a List
numbers = [10, 20, 30, 40, 50]
first_element = numbers[0]
middle_element = numbers[len(numbers) // 2]
last_element = numbers[-1]
extracted_elements = [first_element, middle_element, last_element]
print(extracted_elements)

# 4. Convert List to Tuple
favorite_movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight", "Pulp Fiction"]
movies_tuple = tuple(favorite_movies)
print(movies_tuple)

# 5. Check Element in a List
cities = ["New York", "London", "Paris", "Tokyo", "Sydney"]
is_paris_in_list = "Paris" in cities
print(is_paris_in_list)

# 6. Duplicate a List Without Using Loops
numbers_list = [1, 2, 3, 4, 5]
duplicated_list = numbers_list * 2
print(duplicated_list)

# 7. Swap First and Last Elements of a List
numbers_to_swap = [1, 2, 3, 4, 5]
numbers_to_swap[0], numbers_to_swap[-1] = numbers_to_swap[-1], numbers_to_swap[0]
print(numbers_to_swap)

# 8. Slice a Tuple
numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sliced_tuple = numbers_tuple[3:8]
print(sliced_tuple)

# 9. Count Occurrences in a List
colors = ["red", "blue", "green", "blue", "yellow", "blue"]
blue_count = colors.count("blue")
print(blue_count)

# 10. Find the Index of an Element in a Tuple
animals = ("cat", "dog", "lion", "tiger", "elephant")
lion_index = animals.index("lion")
print(lion_index)

# 11. Merge Two Tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print(merged_tuple)

# 12. Find the Length of a List and Tuple
sample_list = [1, 2, 3, 4, 5]
sample_tuple = (1, 2, 3, 4, 5)
print(len(sample_list))
print(len(sample_tuple))

# 13. Convert Tuple to List
numbers_tuple_to_list = (10, 20, 30, 40, 50)
converted_list = list(numbers_tuple_to_list)
print(converted_list)

# 14. Find Maximum and Minimum in a Tuple
numbers_for_min_max = (5, 10, 15, 20, 25)
max_value = max(numbers_for_min_max)
min_value = min(numbers_for_min_max)
print(max_value)
print(min_value)

# 15. Reverse a Tuple
words_tuple = ("hello", "world", "python", "programming")
reversed_tuple = words_tuple[::-1]
print(reversed_tuple)