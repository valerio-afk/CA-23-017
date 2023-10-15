from typing import Iterable,Callable
from numbers import Number

def apply_fn(nums:Iterable[int],even=Callable[[int],Number], odd=Callable[[int],Number]) -> Iterable[Number]:
    result = []

    for n in nums:
        is_odd = n % 2

        r = (is_odd * odd(n)) + ((1-is_odd) * even(n))

        result.append(r)

    return result


print(apply_fn(range(1,11),even=lambda x: x/2, odd=lambda x:x*2))