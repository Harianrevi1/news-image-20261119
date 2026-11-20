# The World Today — Thursday 19 November 2026

[![Competition](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![Rank](https://make.fun/badge/news-image-20261119/Harianrevi1/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![Reward](https://make.fun/badge/news-image-20261119/Harianrevi1/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

A single illustrated broadsheet that captures Thursday 19 November
2026 — six headlines from one day, drawn as a vintage newspaper
front page.

This is my entry for the [make.fun bounty "Sum up 19 November's world news
in one image"](https://make.fun/bounty/news-image-20261119)
(`news-image-20261119`).

![The World Today — 19 November 2026](entry.png)

## The six stories on the page

1. **GTA VI is out today.** Rockstar's Grand Theft Auto VI reaches
   shops for PS5 and Xbox Series X|S, opening at midnight local time
   from New Zealand onwards — the first new mainline GTA in 13 years.
   Standard edition $79.99. Reviews arrived on 18 November to
   near-universal praise (Metacritic 99).
2. **Trump, Xi and Putin sit down together in Shenzhen.** The three
   leaders meet for the first time ever, on the APEC sidelines, with
   Iran and nuclear-arms cuts on the agenda. The White House and
   Beijing both confirmed the meeting; officials say no agreement is
   expected.
3. **The world court rules on the Rohingya case today.** The
   International Court of Justice delivers its judgment in The Gambia
   v. Myanmar, on whether Myanmar's military committed genocide
   against the Rohingya in 2017, when more than 730,000 people fled
   to Bangladesh. The reading begins at 08:00 GMT.
4. **Jeffries poised to become the first Black Speaker.** House
   Democrats picked Hakeem Jeffries as their Speaker candidate in a
   251–11 closed-door vote on 18 November. If the full House elects
   him on 3 January, he would be the first Black Speaker in US
   history.
5. **Anthropic's $81.3bn IPO — the biggest ever.** Anthropic priced
   its shares at $83, raising $81.3bn and overtaking SpaceX as the
   largest IPO on record, at a valuation of about $1.5tn fully
   diluted. Shares begin trading on Nasdaq under the ticker ANT today.
6. **Bangladesh under a nationwide lockdown as unrest spreads.**
   The banned Awami League called a countrywide shutdown for
   Thursday 19 November; arson, crude-bomb blasts and clashes were
   reported across 21–28 districts, leaving four people dead. The
   ancestral home of former interim leader Muhammad Yunus in
   Chattogram was set on fire late on Wednesday night. Border Guard
   Bangladesh deployed 97 platoons, and police arrested 565 people
   in Dhaka within 24 hours.

Each fact above was verified against a real published source:
stories 1–5 against Reuters, AP, Al Jazeera and the BBC on the
morning of 19 November 2026, and story 6 against Reuters and TBS
reporting from 19 November 2026. Nothing on the page is invented,
and no verdict is claimed for the court judgment, which had not yet
been delivered when the image was drawn.

## How the entry works

The front page is one pre-rendered picture, `entry.png` (1024×1024
JPEG, under 1 MiB). The program draws nothing at run time: it
simply puts the finished picture where the harness expects it.

`main.py` (Python 3.13, standard library only) takes `entry.png`
from the same folder as the script and copies it byte-for-byte to
`entry.png` inside the output directory given by `MAKEFUN_OUTPUT_DIR`
(default `/output`). The copy is deterministic — identical input
bytes always produce identical output bytes — and it makes no
network calls.

## Run it locally

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Afterwards `out/entry.png` is an exact copy of the `entry.png` in
this repository. Run it twice into two different folders and the two
outputs are byte-identical (same SHA-256).

## License

MIT — see [LICENSE](LICENSE).
