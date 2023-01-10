import numpy as np
def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0
    predict = np.random.randint(1, 101)
    n = 10
    while number != predict:
        if number > predict:
            n_pre = predict
            predict += n
            count += 1
            predict = np.random.randint(n_pre, predict)
        else:
            n_pre = predict
            predict -= n
            count += 1
            predict = np.random.randint(predict, n_pre)
    # Ваш код заканчивается здесь

    return count
#--------
def score_game(game_core_v3) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
#----------
print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)