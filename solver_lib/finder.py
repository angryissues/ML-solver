from difflib import SequenceMatcher

class ProblemFinder:
    def __init__(self, problems: list[dict]):
        self.problems = problems

    def _score(self, query: str, keywords: list[str]) -> float:
        """Оцениваем, насколько query близок к keyword-сету."""
        best = 0.0
        q = query.lower()
        for kw in keywords:
            # сравниваем с каждым ключевым словом
            ratio = SequenceMatcher(None, q, kw.lower()).ratio()
            best = max(best, ratio)
        return best

    def find(self, query: str, threshold: float = 0.5) -> dict | None:
        """
        Ищет задачу с максимальным сходством query→keywords.
        Если совпадение ниже threshold, вернёт None.
        """
        best_prob = None
        best_score = threshold
        for prob in self.problems:
            sc = self._score(query, prob.get("keywords", []))
            if sc > best_score:
                best_score = sc
                best_prob = prob
        return best_prob