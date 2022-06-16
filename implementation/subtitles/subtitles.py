from __future__ import annotations

from typing import List

from implementation.subtitles.subtitle import Subtitle, EMPTY_SUBTITLE


class Subtitles:
    def __init__(self, subtitles: List[Subtitle] = None) -> None:
        self._subtitles = subtitles[:] if subtitles else []

    def get_subtitles(self) -> List[Subtitle]:
        return self._subtitles[:]

    def add_subtitle(self, subtitle: Subtitle) -> Subtitles:
        self._subtitles.append(subtitle)
        return self

    def create_copy(self) -> Subtitles:
        return Subtitles(self.get_subtitles())

    def find_content(self, time_ms: int) -> str:
        for subtitle in self._subtitles:
            if subtitle.start < time_ms < subtitle.end:
                return subtitle.content
        return EMPTY_SUBTITLE
