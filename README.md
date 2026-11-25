# Museum of the Year 3000

[![make.fun · u-donrulezz-museum-of-the-year-3000-b727a0bb](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-museum-of-the-year-3000-b727a0bb)
[![rank](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb/cunong05/u-donrulezz-museum-of-the-year-3000-b727a0bb/rank.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-museum-of-the-year-3000-b727a0bb)
[![reward](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb/cunong05/u-donrulezz-museum-of-the-year-3000-b727a0bb/reward.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-museum-of-the-year-3000-b727a0bb)

Entry for the [make.fun bounty "Museum of the Year 3000"](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb) by [@cunong05](https://github.com/cunong05).

## The label

> Sticky note, 2024. Humans wrote urgent thoughts on small yellow squares, stuck them where they could not be missed, and then never looked at them again.

One line, 152 characters, original — a deadpan museum label from the year 3000. The joke is the misreading: future curators take the sticky note at face value, a system for urgent thoughts that its own users faithfully ignored.

## The concept

In the Museum of the Year 3000, ordinary objects from 2024 are displayed as artifacts of a lost civilization. The sticky note is catalogued as an "urgent-thought system": small yellow squares that humans stuck where they could not be missed — then never looked at again. The curators of 3000, working from fragments, filed it under communication technology, right next to the fax machine. The label plays it straight, like any museum plaque, and lets the contradiction do the joking.

## How it works

`main.py` holds the entry text, validates it against the bounty gate (single line, 1–200 characters, no leading/trailing space, valid UTF-8, not only whitespace), writes it to `/output/entry.txt`, reads the file back and re-validates it, and prints it:

```sh
python3 main.py            # writes /output/entry.txt (default)
python3 main.py --out /tmp/entry.txt --quiet
```

## License

MIT — see [LICENSE](LICENSE).
