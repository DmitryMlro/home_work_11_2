from inspect import isgenerator


def generate_cube_numbers(end):
    """
    Генератор, який створює числа у кубі, починаючи з 2, поки значення менше або дорівнює end

    Args:
        end (int): верхня межа генерації чисел у кубі

    Yields:
        int: куб числа, якщо він <= end
    """
    number = 2
    while True:
        cub = number ** 3
        if cub > end:
            return
        yield cub
        number += 1


gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'

print('Ok')
