"""
Exercise-1: Find missing elements
Write a function "missing_elements(my_list: list) -> list" that takes a
sorted list of integers and returns a list of missing integers in the range of the list.
"""

def missing_elements(my_list: list) -> list:
    if not my_list:
        return []

    my_set = set(my_list)
    return [i for i in range(my_list[0], my_list[-1]) if i not in my_set]


"""
Exercise-2: Count occurrences
Write a function "count_occurrences(my_list: list) -> dict" that takes a
list of integers and returns a dictionary where keys are unique integers
from the list and values are their counts in the list.
"""

def count_occurrences(my_list: list) -> dict:
    result = {}
    for num in my_list:
        result[num] = result.get(num, 0) + 1
    return result


"""
Exercise-4: Common elements
Write a function "common_elements(list1: list, list2: list) -> list" that takes two
lists of integers and returns a list of unique common elements.
"""

def common_elements(list1: list, list2: list) -> list:
    return list(set(list1) & set(list2))


"""
Exercise-5: Character frequency
Write a function "char_frequency(my_string: str) -> dict" that takes a
string and returns a dictionary with the frequency of each character in the string.
"""

def char_frequency(my_string: str) -> dict:
    result = {}
    for char in my_string:
        result[char] = result.get(char, 0) + 1
    return result


"""
Exercise-6: Unique words
Write a function "unique_words(my_string: str) -> int" that takes a
string and returns the number of unique words in the string.
"""

def unique_words(my_string: str) -> int:
    return len(set(my_string.split()))


"""
Exercise-7: Word frequency
Write a function "word_frequency(my_string: str) -> dict" that takes a
string and returns a dictionary with the frequency of each word in the string.7
"""

def word_frequency(my_string: str) -> dict:
    result = {}
    for word in my_string.split():
        result[word] = result.get(word, 0) + 1
    return result


"""
Exercise-8: Count elements in range
Write a function "count_in_range(my_list: list, start: int, end: int) -> int" that
takes a list of integers and two integers as range boundaries and
returns the count of unique elements within that range in the list.
"""

def count_in_range(my_list: list, start: int, end: int) -> int:
    return len({x for x in my_list if start <= x <= end})


"""
Exercise-9: Swap dictionary keys and values
Write a function "swap_dict(d: dict) -> dict" that takes a dictionary
and returns a new dictionary where keys become values and values become keys.
If duplicates appear, the first key should be saved.
"""

def swap_dict(d: dict) -> dict:
    result = {}
    for key, value in d.items():
        if value not in result:
            result[value] = key
    return result


"""
Exercise-10: Subset check
Write a function "is_subset(set1: set, set2: set) -> bool" that takes two
sets and returns True if set2 is a subset of set1, and False otherwise.
"""

def is_subset(set1: set, set2: set) -> bool:
    return set2.issubset(set1)


"""
Exercise-11: Intersection of lists
Write a function "list_intersection(list1: list, list2: list) -> list" that takes two
lists and returns a list of unique elements that are in both lists.
"""

def list_intersection(list1: list, list2: list) -> list:
    return list(set(list1) & set(list2))


"""
Exercise-12: Union of lists
Write a function "list_union(list1: list, list2: list) -> list" that takes two
lists and returns a list of unique elements that are in either of the lists.
"""

def list_union(list1: list, list2: list) -> list:
    return list(set(list1) | set(list2))


"""
Exercise-13: Most frequent element
Write a function "most_frequent(my_list: list) -> int" that takes a
list of integers and returns the most frequent element in the list.
"""

def most_frequent(my_list: list) -> int:
    counts = {}
    for x in my_list:
        counts[x] = counts.get(x, 0) + 1
    return max(counts, key=counts.get)


"""
Exercise-14: Least frequent element
Write a function "least_frequent(my_list: list) -> int" that takes a
list of integers and returns the least frequent element in the list.
"""

def least_frequent(my_list: list) -> int:
    counts = {}
    for x in my_list:
        counts[x] = counts.get(x, 0) + 1
    return min(counts, key=counts.get)