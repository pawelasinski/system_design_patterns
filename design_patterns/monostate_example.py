"""Monostate

The `Monostate` pattern ensures that multiple instances of a class share the same state,
behaving as if they were a single instance. Unlike the `Singleton` pattern,
which restricts instantiation, `Monostate` allows multiple objects while maintaining
a shared internal state.

Why use it?
* Encapsulation (keeps state management internal without exposing global variables).
* Flexibility (allows multiple instances while ensuring consistency across them).
* Ease of use (eliminates the need for explicit instance control, like in Singleton).

"""


class ThreadMonostate:
    __shared_state = {
        'a': 1,
        'b': 2,
    }

    def __init__(self):
        self.__dict__ = self.__shared_state


if __name__ == '__main__':
    tm1 = ThreadMonostate()
    print(tm1.__dict__)

    tm2 = ThreadMonostate()
    print(tm2.__dict__)

    tm1.a = 3
    print(tm1.__dict__)
    print(tm2.__dict__)
