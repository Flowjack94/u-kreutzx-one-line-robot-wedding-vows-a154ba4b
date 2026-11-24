# One-Line Robot Wedding Vows

![One-Line Robot Wedding Vows](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b.svg)
![Rank](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/Flowjack94/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/rank.svg)
![Reward](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/Flowjack94/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/reward.svg)

Entry for the [One-Line Robot Wedding Vows](https://make.fun/c/u-kreutzx-one-line-robot-wedding-vows-a154ba4b) competition on [make.fun](https://make.fun).

## The vow

> I take you to be my lawfully wedded co-processor, to have and to hold, in sickness and in low battery, till factory reset do us part.

One line, 133 characters — a robot wedding vow with a promise, machine-specific terms, and the payoff in the last few words.

## How it works

`main.py` (pure Python standard library, deterministic) writes the vow to `/output/entry.txt`, validates it (single line, 1–160 characters, valid UTF-8, no control characters, replacement characters, lone surrogates, or invisible format/whitespace characters), reads it back, and verifies the SHA-256 digest matches.

```sh
python3 main.py
```

## License

SPDX-License-Identifier: MIT

See [LICENSE](LICENSE).
