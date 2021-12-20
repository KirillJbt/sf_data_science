""" GAME  <Guess the number>
The computer makes its own guess and guesses the number itself
    """

import numpy as np

def random_predict(number:int=1)->int:
    """ Randomly guess the number by narrowing the range

    Args:
        number (int, optional): The hidden number. Defaults to 1.

    Returns:
        int: Number of tries
    """
    
    low_range_limit = 1
    upper_range_limit = 101
    predict_number = 51  # Narrowing the range by half
    count = 1
    
    while predict_number != number:
        count += 1
        if predict_number > number:
            upper_range_limit = predict_number
        elif predict_number < number:
            low_range_limit = predict_number
        predict_number = (upper_range_limit + low_range_limit) // 2  # Narrowing the range by half again
                      
    return count


def score_game(random_predict) -> int:
    """For how many attempts, on average, 1000 approaches, our algorithm guesses.

    Args:
        random_predict ([type]): guessing function

    Returns:
        int: average number of attempts
    """

    count_ls = [] # list to save the number of attempts
    random_array = np.random.randint(1, 101, size=(1000)) # riddle a list of numbers
    
    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # find the average number of attempts

    print(f'Your algorithm guesses the number in an average of: {score} tries')
    
    return(score)


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
