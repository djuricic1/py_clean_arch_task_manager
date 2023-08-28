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
        index_to_change = None
        for index, d in enumerate(self.data):
            if d.id == arg.id:
                index_to_change = index

        if index_to_change is not None:
            self.data[index_to_change] = arg
        else:
            # add some custom exception here
            raise Exception("Not found error")

        return T

    def delete(self, id_: K) -> bool:
        index_to_remove = None
        for index, obj in enumerate(self.data):
            if obj.id == id_:
                index_to_remove = index
                break
        if index_to_remove is not None:
            del self.data[index_to_remove]
            return True

        return False
