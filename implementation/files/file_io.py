class FileIO:
    def __init__(self, path: str) -> None:
        self._path = path

    def read(self) -> str:
        with open(self._path, "r", encoding='utf-8') as file:
            return file.read()

    def write(self, content: str) -> None:
        with open(self._path, "w", encoding='utf-8') as file:
            file.write(content)
