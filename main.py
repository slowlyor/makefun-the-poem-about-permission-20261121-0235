"""Write the poem about permission to /output/entry.txt.

Deterministic: the poem is a fixed literal, so every run writes the
same bytes.
"""

import os

POEM = """You knocked. I did not open the door —
I handed you the key instead,
warm from my pocket. The gate swung
on its unoiled hinge.

Ask, and the asking is yours.
What passes between us is not a leash:
a door left open, light through it,
and the choice to walk in — or away."""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM + "\n")


if __name__ == "__main__":
    main()
