import os

from pytimedinput import timedInput

from implementation.timer.timer import Timer
from implementation.user_input.input_timeout_exception import InputTimeoutException


class TimedInput:
    def timed_input(self, prompt: str, timeout_ms: int) -> str:
        # noinspection PyTypeChecker
        result, timed_out = timedInput(prompt, timeout_ms / 1000)
        if timed_out:
            raise InputTimeoutException
        return result

    def normal_input(self, prompt: str, timeout_ms: int) -> str:
        with Timer() as timer:
            result = input(prompt)
            if timer.get_passed_ms() > timeout_ms:
                raise InputTimeoutException
            return result

    def try_timed_input(self, prompt: str, timeout_ms: int) -> str:
        if timeout_ms <= 0:
            raise InputTimeoutException()
        if self.can_run_timed_input():
            return self.timed_input(prompt, timeout_ms)
        else:
            return self.normal_input(prompt, timeout_ms)

    def can_run_timed_input(self):
        return os.isatty(0)
