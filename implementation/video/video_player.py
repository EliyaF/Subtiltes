from abc import ABC, abstractmethod


class VideoPlayer(ABC):
    @abstractmethod
    def play(self) -> None:
        pass

    @abstractmethod
    def pause(self) -> None:
        pass

    @abstractmethod
    def set_time(self, time_ms: int) -> None:
        pass

    @abstractmethod
    def get_time(self) -> int:
        pass

