from implementation.files.file_io import FileIO
from implementation.subtitles.content.subtitle_content_generator import SubtitleContentGenerator


class SubtitleContentRetriever:
    def __init__(self, reader: FileIO) -> None:
        self._reader = reader

    def retrieve(self) -> SubtitleContentGenerator:
        reader = self._reader
        read = reader.read()
        split = read.splitlines()
        return SubtitleContentGenerator(split)
