"""Monostate is a pattern that allows multiple instances of a class to share the same state."""


class ThreadMonostate:
    __shared_state = {
        'a': 1,
        'b': 2,
    }

    def __init__(self):
        self.__dict__ = self.__shared_state


# The client's code.
if __name__ == '__main__':
    tm1 = ThreadMonostate()
    print(tm1.__dict__)

    tm2 = ThreadMonostate()
    print(tm2.__dict__)

    tm1.a = 3
    print(tm1.__dict__)
    print(tm2.__dict__)
