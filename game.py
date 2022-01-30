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


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    random.seed(1) # фиксируем сид для вопроизводимости
    random_array = random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':
    # RUN
    score_game(random_predict)