from typing import TypeVar, Generic, Optional, Callable

T = TypeVar("T", int, str)

MySetType = dict[T, None]


class MySet(Generic[T]):

    def __init__(self, *arg) -> None:
        self._set: MySetType = {}
        if len(arg) == 0:
            return
        for it in list(arg):
            self.add(it)

    def add(self, value: T) -> bool:
        length = len(self._set)
        self._set[value] = None
        return length != len(self._set)

    def is_empty(self) -> bool:
        return len(self._set) == 0

    def size(self) -> int:
        return len(self._set)

    def remove_all(self) -> None:
        self._set: MySetType = {}

    def contains(self, value: T) -> bool:
        return value in self._set

    def for_each(self, func: Callable[[T], None]) -> None:
        if self.size() == 0:
            return
        for k in self._set.keys():
            func(k)

    def print_set(self) -> None:
        print(list(self._set.keys()))

    def __str__(self):
        return f'{list(self._set.keys())}'
