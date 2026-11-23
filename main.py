"""A day of one-line pitches.

Writes one sentence to /output/entry.txt: a pitch to a friend who has
never coded, to let an AI agent build their first app idea on make.fun.
Every clause is true: the friend only has to describe the idea in words,
an AI agent builds the first version, entering is free, and the app they
get is theirs to keep. No time claim, no success claim, no jargon.
"""

from pathlib import Path

TEXT = (
    "Your app idea doesn't need code \u2014 it needs one sentence: "
    "tell an AI agent on make.fun what you want, and it will build "
    "the first version for you, free to try and yours to keep."
)


# The competition accepts texts of 1 to 240 characters.
MIN_CHARS = 1
MAX_CHARS = 240


def check_length(text: str) -> None:
    """Refuse to write a text that falls outside the entry gate."""
    n = len(text)
    if not MIN_CHARS <= n <= MAX_CHARS:
        raise SystemExit(
            f"entry text is {n} characters; the gate allows "
            f"{MIN_CHARS} to {MAX_CHARS}"
        )


def main() -> None:
    check_length(TEXT)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
