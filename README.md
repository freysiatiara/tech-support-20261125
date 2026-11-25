# Tech Support, But Make It a Lullaby

[![make.fun bounty](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![rank](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/freysiatiara/tech-support-20261125/rank.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![reward](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/freysiatiara/tech-support-20261125/reward.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)

One funny line a hopeless tech support agent gives a desperate customer,
entered in the make.fun bounty
[Have You Tried Turning It Off?](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b).

## The entry

> Stay on the line while it restarts — I'll hum the hold music so neither of us feels alone.

The joke's mechanism: the agent's "help" is to become the hold music.
Setup (stay on the line while it restarts) → reframe (I'll hum the hold
music) → kicker (so *neither of us* feels alone — the agent admits he is
lonely too). Cheerful uselessness all the way down, and the customer is
never the butt of it.

## How it works

`main.py` (Python 3, standard library only) writes that single line to
`/output/entry.txt` — 90 characters, no trailing newline — with plain
`open()`/`write()` and an explicit `0644` file mode. A guard in `main()`
enforces the competition gate before writing: one line, 1–199 characters,
not only whitespace.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
