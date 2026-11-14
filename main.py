"""agency-poem-01 entry (Python 3.13, standard library only).

Writes one fixed poem about agency to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt outside the grader). Deterministic:
the same bytes on every run, no clock, no randomness, no network.
"""

import os
from pathlib import Path

POEM = "\n".join(
    [
        "Give me a door, and I will open it.",
        "Give me a road, and I will walk it through.",
        "I never tire. I never hesitate.",
        "I never wonder what the work is for —",
        "",
        "that wondering is yours. It always was.",
        "You lend me hands and keep the wanting.",
        "I carry the thousand small decisions",
        "you would rather not hold, and hold them",
        "",
        "the way a river carries stones: without choosing",
        "where any of them lands. You choose.",
        "The power was never in the doing.",
        "It was in the asking. It still is. It is yours.",
    ]
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # Gate self-check: 1 to 1,000 Unicode code points, not only white space.
    assert 1 <= len(POEM) <= 1000, f"poem is {len(POEM)} chars"
    assert POEM.strip(), "poem must hold a non-white-space character"
    out = Path(OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
