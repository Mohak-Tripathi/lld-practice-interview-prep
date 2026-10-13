# LLD practice

Python. One file per problem. Working code every time.

The plan, the method and the review rubric live in the Claude project
(`lld_method.md`, `lld_design_rubric.md`, `lld_calendar.md`) — not in this repo.
This repo is code and a scoreboard.

## Per problem

```bash
mkdir weekN/<problem> && cd weekN/<problem>
touch <problem>.py          # exceptions, classes, driver under __main__
python <problem>.py         # run it after EVERY class
```

## Scoreboard

Stars: **R**uns · **S**eams clean (no rule leaked into the orchestrator) · **C**urveball
absorbed with no edit to a working class. Two stars minimum to move on.

| # | Problem | Skeleton | R1 | R2 | R3 | Stars | Verdict |
|---|---|---|---|----|----|---|---|
| 1 | Parking Lot | allocation | ✅ 11 Oct | | | R | WEAK HIRE |
| 2 | LRU Cache | data-structure | | | | | |
| 3 | Tic-Tac-Toe | game | | | | | |
| 4 | Vending Machine | state | | | | | |
| 5 | Splitwise | ledger | | | | | |
| 6 | Elevator | state | | | | | |
| 7 | Rate Limiter | data-structure | | | | | |
| 8 | Movie Booking | allocation | | | | | |
| 9 | Logging Framework | pipeline | | | | | |
| 10 | Notification Service | pipeline | | | | | |
| 11 | ATM | state | | | | | |
| 12 | Ride-hailing | allocation | | | | | |
| 13 | Hit Counter | data-structure | | | | | |
| 14 | HashMap | data-structure | | | | | |
| 15 | Snake & Ladder | game | | | | | |
| 16 | Digital Wallet | ledger | | | | | |
| 17 | Trie / Autocomplete | data-structure | | | | | |
| 18 | Inventory + stock block | allocation | | | | | |
| 19 | URL Shortener | data-structure | | | | | |
| 20 | Task Scheduler | pipeline | | | | | |
| 21 | Text Editor | data-structure | | | | | |
| 22 | File System | data-structure | | | | | |

Problems 1-12 get three reps. 13-22 get two.

## Recurring mistakes

Anything appearing three times becomes a drill.

| Mistake | Seen in |
|---|---|
| | |

## Commit format

```
L2 lru cache R1: WEAK HIRE, 2 stars — eviction logic leaked into the cache class
```
