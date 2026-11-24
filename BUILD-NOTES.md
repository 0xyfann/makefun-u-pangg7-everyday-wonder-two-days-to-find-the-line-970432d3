# Build notes

- Competition: u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3
  ("Everyday Wonder, Two Days to Find the Line"), $2, closes 26 Nov 2026
  18:35 WIB. Free entry, escrowed.
- Read `RULES.txt` / `competition.yaml` in the kit first. Judge criteria,
  in order: small everyday moment; unseen angle; surprise lands in one
  read; grounded in something real and specific; no filler, no worn phrase.
- Idea: a vending machine giving two bars for one coin — a tiny, concrete
  everyday "miracle" — with the twist that being chosen by the universe
  is flattering until you notice which god did the choosing.
- v1: "...chosen by a god with very low standards." — 127 characters.
  Ran locally, valid (1 line, 1-200 chars, not whitespace-only).
- Revision (v2): dropped the filler word "very" — "chosen by a god with
  low standards." — 122 characters. Tighter, same joke, every word works.
- Local test (v2): `mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py`
  then read `out/entry.txt`: 122 chars / 122 bytes, 1 line, non-whitespace,
  valid 1-200. Test output dir removed afterwards.
- `main.py` is stdlib only (`os`), honours `MAKEFUN_OUTPUT_DIR`,
  defaults to `/output`, writes the sentence with no trailing newline.
- Not submitted; no repo created; make.fun not contacted.
