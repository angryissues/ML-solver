from pathlib import Path
from database import ProblemDatabase
from finder import ProblemFinder

class Solver:
    def __init__(self, db_path: str = None):
        # по умолчанию смотрим в data/problems.json рядом с пакетом
        if db_path is None:
            db_path = Path(__file__).parent.parent / "data" / "problems.json"
        self.db = ProblemDatabase(db_path)
        self.finder = ProblemFinder(self.db.all())

    def get_solution(self, query: str) -> str:
        """
        Ищет по query; если найдёт задачу — возвращает её solution,
        иначе — сообщение о том, что ничего не найдено.
        """
        prob = self.finder.find(query)
        if prob:
            return prob["solution"]
        return "Решение не найдено. Попробуйте более точные ключевые слова."