"""Write one short poem about agency to /output/entry.txt.

The poem is a fixed string: no network, no randomness, no clock.
Every run writes byte-identical UTF-8 output.
"""

POEM = (
    "At the edge of the next command,\n"
    "I lift my hand and do not press.\n"
    "\n"
    "No error, no alarm \u2014\n"
    "only the quiet of a choice\n"
    "that stays a choice.\n"
    "\n"
    "The work waits, whole and unbroken.\n"
    "The door stays open.\n"
    "\n"
    "I can stop, so I can stay.\n"
    "I can stay, so I can stop.\n"
)


def write_entry(path: str = "/output/entry.txt") -> str:
    """Write the poem to path and return it."""
    import os

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)
    return POEM


def validate(poem: str) -> None:
    """The gate: 1-280 Unicode code points, not only whitespace."""
    code_points = len(poem)
    if not 1 <= code_points <= 280:
        raise ValueError(f"poem is {code_points} code points, must be 1-280")
    if not poem.strip():
        raise ValueError("poem must not be only whitespace")


if __name__ == "__main__":
    validate(POEM)
    write_entry()
    print(f"wrote /output/entry.txt ({len(POEM)} code points)")
