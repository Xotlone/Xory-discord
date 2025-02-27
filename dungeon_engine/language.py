__all__ = (
    'Language'
)


class Language:
    """Class for storing language parameters"""

    def __init__(self, name: str, speakers, script: str = None):
        self.name = name
        self.speakers = speakers
        self.script = name if script is None else script

    def __str__(self): return self.name
