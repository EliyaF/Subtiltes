from implementation.files.file_io import FileIO

from configuration.configuration import FileConfig

from implementation.subtitles.content.subtilte_conent_retriever import SubtitleContentRetriever
from implementation.subtitles.srt.srt_creator import SrtCreator
from implementation.subtitles.srt.srt_writer import SrtWriter
from implementation.subtitles.subtitle import Subtitle
from implementation.subtitles.subtitles import Subtitles
from implementation.user_input.timed_input import TimedInput
from implementation.user_input.input_timeout_exception import InputTimeoutException

from implementation.video.stream.video_streamer import VideoStreamer
from implementation.video.vlc.vlc_video_player import VlcVideoPlayer


def run_vlc() -> None:
    input_text_file = FileIO(FileConfig.Input.input_subtitle_path)
    output_subtitles_file = FileIO(FileConfig.Output.output_subtitle_path)

    subtitles_generator = SubtitleContentRetriever(input_text_file).retrieve()
    srt_writer = SrtWriter(SrtCreator(), output_subtitles_file)
    subtitles = Subtitles()

    timed_input = TimedInput()

    with VlcVideoPlayer(FileConfig.Input.input_video_path) as video_player:
        input("Enter to start the video")
        print("")
        video_player.play()
        video_length = video_player.get_length()
        timed_out = False
        while not timed_out:
            current_time = video_player.get_time()
            srt_writer.write(subtitles.create_copy().add_subtitle(Subtitle(subtitles_generator.get_current(),
                                                                           current_time,
                                                                           video_length)))
            video_player.set_subtitles(FileConfig.Output.output_subtitle_path)
            previous_time = current_time
            try:
                timed_input.try_timed_input(subtitles_generator.get_current(), video_length - current_time)
            except InputTimeoutException:
                timed_out = True
            subtitles.add_subtitle(Subtitle(subtitles_generator.get_current(), previous_time, video_player.get_time()))
            subtitles_generator.advance()

    print(f"Converting file: {FileConfig.Input.input_video_path} -> {FileConfig.Output.output_video_path}")
    VideoStreamer(FileConfig.Input.input_video_path).with_subtitles(FileConfig.Output.output_subtitle_path) \
        .stream(FileConfig.Output.output_video_path)
    print("Convert finished!")
    print("")
    input("Press any key to continue...")


if __name__ == '__main__':
    run_vlc()
