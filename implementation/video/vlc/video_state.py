from enum import IntEnum

import vlc


class VideoState(IntEnum):
    NothingSpecial = 0
    Opening = 1
    Buffering = 2
    Playing = 3
    Paused = 4
    Stopped = 5
    Ended = 6
    Error = 7


vlc_state_map = {
    vlc.State.NothingSpecial: VideoState.NothingSpecial,
    vlc.State.Opening: VideoState.Opening,
    vlc.State.Buffering: VideoState.Buffering,
    vlc.State.Playing: VideoState.Playing,
    vlc.State.Paused: VideoState.Paused,
    vlc.State.Stopped: VideoState.Stopped,
    vlc.State.Ended: VideoState.Ended,
    vlc.State.Error: VideoState.Error
}


def create_video_state(state: vlc.State) -> VideoState:
    return vlc_state_map[state]
