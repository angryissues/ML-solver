import json
from pathlib import Path

class ProblemDatabase:
    def __init__(self, db_path: Path = None):
        if db_path is None:
        # __file__ == .../solver_lib/database.py
            db_path = Path(__file__).parent / "data" / "problems.json"
        self.path = db_path
        self._load()

    def _load(self):
        with open(self.path, encoding='utf-8') as f:
            self.problems = json.load(f)

    def all(self):
        return self.problems
