from __future__ import annotations

import os
import subprocess
from typing import Optional


class VideoStreamer:
    def __init__(self, video_input_path: str) -> None:
        self._video_input_path = video_input_path
        self._subtitle_path: Optional[str] = None

    def with_subtitles(self, subtitles_path: str) -> VideoStreamer:
        self._subtitle_path = subtitles_path
        return self

    def stream(self, output_path: str) -> None:
        command = ["ffmpeg", "-y", "-i", self._video_input_path]
        if self._subtitle_path is not None:
            subtitle_full_path = os.path.join(os.getcwdb().decode("utf-8"), self._subtitle_path)
            subtitle_full_path = subtitle_full_path.replace("\\", "\\\\").replace(":", "\\:")
            command += ["-vf", f"subtitles=\'{subtitle_full_path}'"]
        command.append(output_path)
        subprocess.check_call(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
