from numpy import random
from numpy import mean


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

def run_game():
    """
    The main() function to run the game
    """
    
    # the list to store the number of tries for each number
    counters = []
    
    # random-generate the list of numbers
    random_nums = [i for i in range(random.randint(1, 1000))]
    
    # the list must be sorted for bin search to work
    random_nums.sort()

    # iterating thro the random numbers
    for number in random_nums:
        counters.append(bin_search(random_nums, number))

    # calculate the mean for all numbers of tries
    score = int(mean(counters))

    print(f'The average number of tries your algorithm guesses a number is: {score}')


if __name__ == '__main__':
    # run
    run_game()