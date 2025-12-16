def parse_recommendation(text: str) -> tuple[str, str]:
    lines = [line.strip() for line in text.strip().splitlines() if line.strip()]

    if not lines:
        return "", ""

    name = lines[0]
    explanation = "\n\n".join(lines[1:])

    return name, explanation