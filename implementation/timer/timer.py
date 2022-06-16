from __future__ import annotations

from datetime import datetime


class Timer:
    def __init__(self) -> None:
        self._time = datetime.now()

    def __enter__(self) -> Timer:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        pass

    def get_passed_ms(self) -> int:
        time_diff = datetime.now() - self._time
        return int(time_diff.total_seconds() * 1000)
