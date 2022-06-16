from __future__ import annotations

from typing import Optional

from vlc import Instance, MediaPlayer, Media

from implementation.video.video_player import VideoPlayer
from implementation.video.vlc.video_state import create_video_state, VideoState


class VlcVideoPlayer(VideoPlayer):
    def __init__(self, path: str) -> None:
        self._path = path
        self._media_player: Optional[MediaPlayer] = None

    def play(self) -> None:
        self._media_player.play()

    def pause(self) -> None:
        self._media_player.pause()

    def set_time(self, time_ms: int) -> None:
        self._media_player.set_time(time_ms)

    def get_time(self) -> int:
        return self._media_player.get_time()

    def get_length(self) -> int:
        return self._media_player.get_length()

    def set_subtitles(self, subtitles_path: str) -> None:
        self._media_player.video_set_subtitle_file(subtitles_path)

    def get_state(self) -> VideoState:
        return create_video_state(self._media_player.get_state())

    def __enter__(self) -> VlcVideoPlayer:
        vlc_instance: Instance = Instance()
        vlc_instance.log_unset()
        self._media_player = vlc_instance.media_player_new()
        media: Media = vlc_instance.media_new(self._path)
        self._media_player.set_media(media)
        self.play()
        self._media_player.set_pause(True)
        self.set_time(0)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._media_player.stop()


