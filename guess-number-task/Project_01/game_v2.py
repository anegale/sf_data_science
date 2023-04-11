"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # переменные для реализации поиска
    count = 0
    low = 0
    high = len(random_array) - 1
    predict_number = np.random.randint(1, 101)  # предполагаемое число
    # реализация угадывания числа через бинарный поиск
    while low <= high:
        mid = (low + high) // 2
        count += 1

        if random_array[mid] < predict_number:
            low = mid + 1
        elif random_array[mid] > predict_number:
            high = mid - 1
        else:
            return (mid, count)

    return (-1,count)


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    global random_array
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел
    
    for number in random_array:
         count_ls.append(random_predict(number))

    # score = int(np.mean(count_ls))
    score = random_predict(number)
    score = score[1]
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)