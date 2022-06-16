from implementation.files.file_io import FileIO
from implementation.subtitles.srt.srt_creator import SrtCreator
from implementation.subtitles.subtitles import Subtitles


class SrtWriter:
    def __init__(self, srt_creator: SrtCreator, file_writer: FileIO) -> None:
        self._file_writer = file_writer
        self._srt_creator = srt_creator

    def write(self, subtitles: Subtitles):
        self._file_writer.write(self._srt_creator.create_srt(subtitles))
