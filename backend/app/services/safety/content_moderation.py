import re

# Whole words and their common forms only, so "skill" and "whatever" are not flagged.
UNSAFE_PATTERNS = {
    "exploit": r"exploit(?:s|ed|ing|ation|ative)?",
    "fraud": r"fraud(?:s|ulent|ster|sters)?",
    "hate": r"hat(?:e|es|ed|ing|eful|red|er|ers)",
    "kill": r"kill(?:s|ed|ing|er|ers)?",
    "scam": r"scam(?:s|med|ming|mer|mers)?",
    "violence": r"violen(?:ce|t|tly)",
}
_COMPILED = {
    term: re.compile(rf"\b{pattern}\b", re.IGNORECASE) for term, pattern in UNSAFE_PATTERNS.items()
}


def find_unsafe_terms(text: str) -> list[str]:
    return sorted(term for term, pattern in _COMPILED.items() if pattern.search(text))


class ContentModeration:
    def check(self, text: str) -> dict:
        hits = find_unsafe_terms(text)
        return {"safe": not hits, "flags": hits}
