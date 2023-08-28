from task_manager.domain.ports.repository import IRepository, T, K


class GenericMemRepo(IRepository[T, K]):
    def __init__(self, data: list[T]):
        self.data = data

    def save(
        self,
        arg: T,
    ) -> T:
        self.data.append(arg)

        return arg

    def get_all(self) -> list[T]:
        return self.data

    def get_by_id(self, id_: K) -> T:
        for d in self.data:
            if d.id == id_:
                return d

    def update(self, arg: T) -> T:
        # TODO add impl
        ...

    def delete(self, id_: K) -> bool:
        # TODO add impl
        ...
