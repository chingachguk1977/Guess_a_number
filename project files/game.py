import numpy as np


def bin_search(range_: list, num2guess: int) -> int:
    """Implements the binary search algorithm on the given sequence. This algorithm
    guarantees the number being guessed will be found in no more than log2 of the 
    number of elements in the given sequence.

    Args:
        range_ (list): A list in which to search the number being guessed.
        num2guess (int): The number to be guessed.

    Returns:
        [int]: How many tries it took to guess the number correctly.
    """
    
    lower_bound = 0
    upper_bound = len(range_) - 1
    count = 0

    while lower_bound <= upper_bound:
        count += 1
        guess = (lower_bound + upper_bound) // 2
        if guess == num2guess:
            break
        elif guess > num2guess:
            upper_bound = guess - 1
        else:
            lower_bound = guess + 1
    return count

def run_game():
    """
    The main() function to run the game
    """
    
    # the list to store the number of tries for each number
    counters = []
    
    # random-generate the list of numbers
    random_nums = list(set(np.random.randint(1, 101, size=1000)))

    # iterating thro the random numbers
    for number in range(100):
        predict_number = np.random.randint(1, 101) 
        counters.append(bin_search(random_nums, predict_number))

    # calculate the mean for all numbers of tries
    score = int(np.mean(counters))

    print(f'The average number of tries your algorithm guesses a number is: {score}')


if __name__ == '__main__':
    # run
    run_game()