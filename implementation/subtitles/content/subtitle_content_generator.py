from typing import List

from implementation.subtitles.subtitle import EMPTY_SUBTITLE


class SubtitleContentGenerator:
    def __init__(self, subtitle_contents: List[str]) -> None:
        self._subtitles_contents = subtitle_contents
        self._current_index = 0

    def get_current(self) -> str:
        if self._current_index < len(self._subtitles_contents):
            return self._subtitles_contents[self._current_index]
        else:
            return EMPTY_SUBTITLE

    def advance(self) -> None:
        self._current_index += 1
