import json
from pathlib import Path

class ProblemDatabase:
    def __init__(self, path: str):
        self.path = Path(path)
        self._load()

    def _load(self):
        with open(self.path, encoding='utf-8') as f:
            self.problems = json.load(f)

    def all(self):
        return self.problems
