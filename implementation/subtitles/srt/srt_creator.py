from datetime import timedelta

import srt

from srt import Subtitle as SrtSubtitle

from implementation.subtitles.subtitle import Subtitle
from implementation.subtitles.subtitles import Subtitles


class SrtCreator:
    def create_srt(self, subtitles: Subtitles) -> str:
        return srt.compose([self._convert_to_srt_subtitle(subtitle) for subtitle in subtitles.get_subtitles()])

    def _convert_to_srt_subtitle(self, subtitle: Subtitle) -> SrtSubtitle:
        return SrtSubtitle(index=None, start=timedelta(milliseconds=subtitle.start),
                          end=timedelta(milliseconds=subtitle.end), content=subtitle.content)
