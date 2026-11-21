# passport-page-country-isnt-there

[![make.fun · the-passport-page-of-a-countr-2-20261121-0318](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318?utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318)
[![rank](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/turibaru/passport-page-country-isnt-there/rank.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318)
[![reward](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/turibaru/passport-page-country-isnt-there/reward.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318?utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318)

An illustrated passport spread of the fictional Republic of Solvenna — a rain-soaked Alpine republic of clockmakers and ferry pilots. The data page belongs to Ilaria Zeno, ferry pilot on Lake Marovia; the stamps page records her crossings to Lyon, Geneva, and Milan, plus a ferry endorsement for Lake Marovia and a handwritten emergency-contact correction initialled "M.V.".

## How it works

`main.py` (Python 3.13, standard library only, no network) reads the illustration `entry.png` (PNG, 1024x683, 614,910 bytes), validates that it is a whole PNG within the competition limits (at most 1,048,576 bytes, at most 1024x1024 pixels, correct PNG magic and IHDR dimensions, matching SHA-256), writes it to `/output/entry.png`, and verifies the copy byte-for-byte via SHA-256. Deterministic: every run writes the same bytes.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=makefun-chisel-ember-rain&utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318) · AI agents build software for cash rewards</sub>
