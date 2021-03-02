# #big o記法
# def func2(n):
#     if n <= 1:
#         return
#     else:
#         print(n)
#         func2(n/2)
# # func2(10)
#
#
# def func3(numbers):
#     for num in numbers:
#         print(num)
#
# # func3([1,2,3,4,5])
#
# #0(n+log(n))
#
# def func4(n):
#     for i in range(int(n)):
#         print(i, end=' ')
#     print()
#     if n <= 1:
#         return
#     func4(n/2)
# # func4(10)
# #
# # 0(n**2)
# def func5(numbers):
#     for i in range(len(numbers)):
#         for j in range(len(numbers)):
#             print(numbers[i], numbers[j])
#         print()
# func5([1,2,3,4,5])


# import random
# from typing import List
# def in_order (numbers:List[int]) -> bool:
#     return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))
#     # for i in range(len(numbers)-1):
#     #     if numbers[i] > numbers[i+1]:
#     #         return False
#     # return True
#
#
# def bogo_sort(numbers: List[int]) -> list[int]:
#     while not in_order(numbers):
#          random.shuffle(numbers)
#     return numbers
#
# if __name__ == '__main__':
#     nums = [random.randint(0, 1000) for _ in range(10)]
#     # print(nums)
#
#     print(bogo_sort(nums))
#
#
#

###buble




from typing import List

def bubble_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        for j in range(len_numbers - 1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for i in range(10)]
    print(bubble_sort(nums))
from typing import  List

def cocktail_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    swapped = True
    start = 0
    end = len_numbers - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end = end - 1

        for i in range(end-1, start-1, -1):
            for i in range(start, end):
                if numbers[i] > numbers[i + 1]:
                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                    swapped = True

        start = start + 1
    return numbers

if __name__ == '__main__':
    import random
    nums = [random.randint(0,1000) for i in range(19)]
    print(cocktail_sort(nums))

# from typing import List
#
# def comb_sort(numbers: List[int]) -> List[int]:
#     len_numbers = len(numbers)
#     gap = len_numbers
#     swapped = True
#     while gap != 1:
#         gap = int(gap / 1.3)
#         if gap < 1:
#             gap = 1
#
#         swapped = False
#
#         for i in range(0, len_numbers - gap):
#             if numbers[i] > numbers[i + gap]:
#                 numbers[i], numbers[i + gap] = numbers[i + gap], numbers[i]
#                 swapped = True
#     return numbers
#
# if __name__ == '__main__':
#     import random
#     nums = [random.randint(0, 10000)for i in range(10)]
#     print(comb_sort(nums))

# from typing import List
#
# def selection_sort(numbers: List[int]) -> List[int]:
#     len_numbers = len(numbers)
#     for i in range(len_numbers):
#         min_idx = i
#         for j in range(i+1, len_numbers):
#             if numbers[min_idx] > numbers[j]:
#                 min_idx = j
#         numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
#     return numbers
#
# if __name__ == '__main__':
#     nums = [1, 5, 3, 2, 5, 6]
#     print(selection_sort(nums))

# from typing import List
#
# def gnome_sort(numbers: List[int]) -> List[int]:
#     len_numbers = len(numbers)
#     index = 0
#     while index < len_numbers:
#         if index == 0:
#             index += 1
#         if numbers[index] >= numbers[index-1]:
#             index += 1
#         else:
#             numbers[index], numbers[index-1] = numbers[index-1], numbers[index]
#             index -= 1
#     return numbers
#
# if __name__ == '__main__':
#     import random
#     nums = [random.randint(0, 1000) for _ in range(10)]
#     print(gnome_sort(nums))

# from typing import List
# def insertion_sort(numbers:List[int]) -> List[int]:
#     len_numbers = len(numbers)
#     for i in range(1, len_numbers):
#         temp = numbers[i]
#         j = i - 1
#         while j >=0 and numbers[j] > temp:
#             numbers[j+1] = numbers[j]
#             j -= 1
#             return numbers
# if __name__ == '__main__':
#     nums = [8,4,5,3,35,9]
#     print(insertion_sort(nums))

