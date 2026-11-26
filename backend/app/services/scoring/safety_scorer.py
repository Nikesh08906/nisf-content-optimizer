from app.services.safety.content_moderation import find_unsafe_terms
from app.utils.text_utils import clamp


class SafetyScorer:
    def score(self, text: str, **kwargs) -> float:
        return clamp(100 - len(find_unsafe_terms(text)) * 35)
