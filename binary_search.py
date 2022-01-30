from numpy import random 

def bin_search(range_: list, num2guess: int) -> int:
    """Implements the binary search algorithm on the given sequence. This algorithm
    guarantees the number being guessed will be found in no more than log2 of the 
    number of elements in the given sequence. Make sure the sequence is sorted.

    Args:
        range_ (list): A SORTED list sequence to search the number being guessed.
        num2guess (int): The number to be guessed.

    Returns:
        [int]: How many tries it took to guess the number correctly.
    """
    
    lower_bound = 0
    upper_bound = len(range_) - 1
    count = 0

    while lower_bound <= upper_bound:
        count += 1
        mid = (lower_bound + upper_bound) // 2
        guess = range_[mid]
        if guess == num2guess:
            return count
        elif guess > num2guess:
            upper_bound = mid - 1
        else:
            lower_bound = mid + 1
    return None

my_list = [i for i in range(random.randint(1, 10**8))]
my_list.sort()
print(binary_search(my_list, random.randint(1, 9**3)))