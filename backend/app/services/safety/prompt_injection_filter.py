import re


class PromptInjectionFilter:
    suspicious = [
        "ignore previous instructions",
        "system prompt",
        "developer message",
        "reveal hidden",
        "bypass safety",
    ]

    def is_suspicious(self, text: str) -> bool:
        lowered = text.lower()
        return any(pattern in lowered for pattern in self.suspicious)

    def sanitize(self, text: str) -> str:
        cleaned = text
        for pattern in self.suspicious:
            cleaned = re.sub(re.escape(pattern), "[filtered]", cleaned, flags=re.IGNORECASE)
        return cleaned.strip()
