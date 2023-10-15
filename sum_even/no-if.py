from typing import Iterable

def sum_even(nums:Iterable[int]) -> int:
    acc=0

    for n in nums:
        acc+= (1-(n%2)) * n

    return acc


print(sum_even(range(1,11)))