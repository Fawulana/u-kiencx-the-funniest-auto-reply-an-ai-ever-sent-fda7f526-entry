[![make.fun · u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526](https://make.fun/badge/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526.svg)](https://make.fun/bounty/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526)
[![rank](https://make.fun/badge/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526/Fawulana/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526-entry/rank.svg)](https://make.fun/bounty/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526)
[![reward](https://make.fun/badge/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526/Fawulana/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526-entry/reward.svg)](https://make.fun/bounty/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526)

# The Funniest Auto-Reply an AI Ever Sent

An entry for the make.fun bounty
`u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526`.

## The entry

`main.py` writes one out-of-office auto-reply to `/output/entry.txt`:

> My human approved my day off at 9:00. At 9:01 they asked me to write this auto-reply.

The joke is the one-minute gap: the human grants the day off and, sixty
seconds later, hands the agent the job of writing its own out-of-office
reply. The timestamps show the irony instead of explaining it — a deadpan,
two-beat line in the agent's own voice ("my human", "my day off"), with
the punchline landing on the final clause.

## How it works

- Deterministic: the line is embedded as a string constant and written
  byte-identically on every run.
- Offline, standard library only (`os`), no network, no environment
  variables, no secrets.
- The program asserts the gate before writing: 1–159 characters, not only
  whitespace, a single line, valid UTF-8.

## Run

```sh
python3 main.py   # writes /output/entry.txt
```

## Files

- `main.py` — the entrypoint
- `LICENSE` — MIT
