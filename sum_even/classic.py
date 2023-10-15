from typing import Iterable

def sum_even(nums:Iterable[int]) -> int:
    acc=0

    for n in nums:
        if (n%2) == 0:
            acc+=n

    return acc


print(sum_even(range(1,11)))