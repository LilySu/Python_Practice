from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def in_state(self):
        pass

class HappyState(State):
    def in_state(self):
        print("Happy State")

class SadState(State):
    def in_state(self):
        print("Sad State")


if __name__ == '__main__':
    s = HappyState()
    s.in_state()