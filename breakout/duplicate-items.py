# given a list of n numbers, determine if it contains any duplicates

def duplicate(numbers):
    numbers.sort()
    for num in range(1, len(numbers)):
        if numbers[num] == numbers[num-1]:
            return numbers[num]

        