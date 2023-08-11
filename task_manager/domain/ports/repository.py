from typing import Protocol, TypeVar

T = TypeVar("T")
K = TypeVar("K")


class IRepository(Protocol[T, K]):
    def save(
        self,
        arg: T,
    ) -> T:
        ...

    def get_all(self) -> list[T]:
        ...

    def get_by_id(self, id_: K) -> T:
        ...

    def update(self, arg: T) -> T:
        ...

    def delete(self, id_: K) -> bool:
        ...
