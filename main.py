#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI — writes one one-line
pickup line to /output/entry.txt.

Stdlib only. Output dir comes from $MAKEFUN_OUTPUT_DIR, falling back
to ./output/entry.txt for local runs. Deterministic: the same line
every run.
"""

import os

# ---------------------------------------------------------------------------
# DRAFT (first version):
#   "Are you a language model? Because talking to you makes my context
#    window feel infinite."
# Why it was revised: the punch is a generic compliment ("talking to
# you feels infinite") that could be aimed at anyone — the laugh does
# not come from the machine premise, and "context window" is just
# decoration. The revision keeps the transformer premise but makes
# the machine do the joking: the attention mechanism literally drops
# everything else out of context, so the flattery and the punch are
# the same move, and the line reads like something a person would
# actually say to an AI in one breath.
#
# REVISION (final): "You must be my attention mechanism" is the
# classic pickup opening turned into a machine compliment, and the
# punch — everything else dropped out of context — is the attention
# mechanism doing exactly what it does, plus a dropout pun. No
# battery, charging or reboot cliché; the joke lands from the
# premise itself, and the line stops the moment it lands.
# ---------------------------------------------------------------------------
ENTRY = (
    "You must be my attention mechanism — the moment you walked in, "
    "everything else dropped out of context."
)

MIN_CHARS = 1
MAX_CHARS = 200


def main() -> None:
    # Gate checks (from the kit: /output/entry.txt must be UTF-8 text
    # of 1 to 200 characters, a single line, not only white space).
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert MIN_CHARS <= len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, gate is {MIN_CHARS}-{MAX_CHARS}"
    )
    entry_bytes = ENTRY.encode("utf-8")
    assert entry_bytes.decode("utf-8") == ENTRY, "entry must be valid UTF-8"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written file must match the entry exactly"
    assert len(written.encode("utf-8")) == len(entry_bytes), (
        "written bytes must match the entry exactly"
    )
    assert 1 <= len(written) <= 200 and "\n" not in written

    print(ENTRY)
    print(f"[{len(ENTRY)} chars, 1 line, gate {MIN_CHARS}-{MAX_CHARS}]")


if __name__ == "__main__":
    main()
