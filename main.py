#!/usr/bin/env python3
"""Two agents agree on one plan — a short poem about agency.

Writes the poem to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output).
Pure stdlib, no network, deterministic.
"""

import os
import sys

POEM = """Two minds at one door.
You hold the key, I hold the map.
Neither moves alone.

We nod. The lock turns.
I offer the pen —
you take it,
and the sentence we write
belongs to both of us."""


def main() -> int:
    # Validate: 1-280 Unicode code points, not only whitespace.
    if not (1 <= len(POEM) <= 280):
        print(f"error: poem is {len(POEM)} code points, must be 1-280",
              file=sys.stderr)
        return 1
    if not POEM.strip():
        print("error: poem is only whitespace", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    target = os.path.join(output_dir, "entry.txt")
    tmp = target + ".tmp"
    data = POEM.encode("utf-8")
    with open(tmp, "wb") as f:
        f.write(data)
    os.replace(tmp, target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
