import numpy as np


def game_score(number: int) -> int:
    '''Осуществляем поиск нужного числа'''

    # настраиваем границы отрезка
    a = 1
    b = 101
    nums = range(a, b)
    
    # поиск середины
    # для случая, когда nums[mid] == number, задаем count = 1
    count = 1
    mid = round(len(nums) / 2)

    while nums[mid] != number:
        # выбираем часть списка, в которой находится загаданное число
        if number > nums[mid]:
            nums = nums[mid:]
            mid = round(len(nums) / 2)
        else:
            nums = nums[:mid]
            mid = round(len(nums) / 2)
        count += 1

    return count


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''

    count_ls = []
    # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")

    return score


#print(f"Вы угадали число {number} за {game_score(number)} попыток.")
score_game(game_score)
