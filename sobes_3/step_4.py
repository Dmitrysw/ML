from collections import defaultdict


def maj_element(nums):
    """
    defaultdict - это тот же словарь, но при обращении к несуществующему элементу
    он не выбросит KeyError, а вызовет функцию, которую передали при создании этого
    defaultdict. В нашем случае - вызовет int() и получит 0 (так работает функция int()).
    """
    counters = defaultdict(int)
    for one_number in nums:
        # вариант без defaultdict
        # counters[one_number] = counters.get(one_number, 0) + 1
        counters[one_number] = counters[one_number] + 1
    for key in counters.keys():
        if counters[key] >= len(nums) // 2:
            return key