'''
ВНИМАНИЕ! Правильного решения нет, но есть приблизительный ход решения.
Данная задача оптимальным способом решается с применением методов
динамического программирования, однако я буду использовать в процессе
решения жадный алгоритм ввиду простоты его понимания
'''
def getIndexesThatSumOfTarget(nums, target):
    '''
    так как дано условие, что массив из целых чисел, а также target также целое число,
    то в массиве могут быть как отрицательные, так и положительные числа, а также ноль
    '''

    #если target == 0, то просто находим индекс нуля, иначе сообщаем о том, что удовлетворяющих индексов нет
    if target == 0:
        return nums.index(0)

    '''
    если target != 0 и в массиве присутствуют нулевые элементы, то их необходимо удалить,
    так как они лишь удлинняют ответ, а также увеличивают время работы алгоритма; к тому же и так понятно, что эти
    элементы можно включить в конечный ответ, но в рамках задачи эти значения не имеют смысла
    '''
    nums = list(filter(lambda a: a != 0, nums))
    print(nums)

    
    sorted_nums = sorted(nums)
    print(sorted_nums)
    i = len(nums) - 1
    indexes = []
    sum = 0
    for num in sorted_nums:
        if num == target:
            indexes.append(num)
            return indexes
    while i >= 0:
        if (sorted_nums[i] <= target):
            indexes.append(i)
            target -= nums[i]
            if target == 0:
                    return indexes
            print(target)
        i -= 1
    return indexes
print(getIndexesThatSumOfTarget([-1, -3, 0], 0))