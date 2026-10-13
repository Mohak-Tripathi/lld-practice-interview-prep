# LLD Master Plan

Prepare for the hardest version: **full working compiled code, every time.**
If a round turns out to be discussion-only or pseudocode, that is a scale-down from
something already built. You can always do less. You cannot scale up from only ever
having drawn boxes.

---

## The method — one pipeline, every problem

```
requirements  ->  entities  ->  class design  ->  working code  ->  extend it
```

A machine-coding round walks the whole pipeline. A discussion round stops at class design
and asks you to talk instead of type. **Same work, truncated.** No second track.

Not separate formats:
- **API design** = the public method list. Already produced at class design.
- **Schema design** = the entity list written as tables. Already produced at entities.
- **Concurrency** = the same code with a lock where two things touch the same state.

**Narrate out loud on every rep, recorded.** Narration is graded in every format and is
the part not yet practised at all.

---

## The real end goal

> An interviewer gives you an unfamiliar problem. You clarify requirements, model the
> domain, implement a clean working core, explain trade-offs, and extend it without
> losing control of the code.

That capability — not a count of problems solved — is what the preparation must produce.
There is no credible published pass-rate data for LLD rounds, so no percentage target is
used here.

---

## What each rep must PROVE

| Rep | Proves | Conditions |
|---|---|---|
| **R1 — learning** | you can build a correct runnable implementation and explain the design | 2-3 h, full checkpoints, learning doc written after |
| **R2 — independent** | you can reconstruct it from a blank file with no notes | 45 min, timer, recorded, no notes |
| **R3 — transfer** | you can solve it under time pressure AND handle a requirement you have not practised | timer + unseen extension, recorded |

**A rep that reproduces memorised code is not a rep.** Every rep is solved as if the
problem were new, including R3. Roughly half of real rounds will be a problem on no list
— what covers you there is the method, not recall.

### The readiness bar
Not "30 minutes." The bar is: **inside the real round's time limit (60-90 min), deliver a
correct core flow, demonstrate it running, and make a meaningful extension.** Some
problems legitimately need more time even with a sound design.

---

## The problems

### Core 12 — three reps each
| # | Problem | Skeleton | R1 | R2 | R3 |
|---|---|---|----|----|----|
| 1 | Parking Lot | allocation | ☑ | ☐ | ☐ |
| 2 | LRU Cache | data-structure | ☐ | ☐ | ☐ |
| 3 | Vending Machine | state machine | ☐ | ☐ | ☐ |
| 4 | Elevator System | state machine | ☐ | ☐ | ☐ |
| 5 | Splitwise | ledger | ☐ | ☐ | ☐ |
| 6 | Movie Booking | allocation | ☐ | ☐ | ☐ |
| 7 | Rate Limiter | data-structure | ☐ | ☐ | ☐ |
| 8 | Logging Framework | pipeline | ☐ | ☐ | ☐ |
| 9 | Notification Service | pipeline | ☐ | ☐ | ☐ |
| 10 | Ride-hailing | allocation | ☐ | ☐ | ☐ |
| 11 | Tic-Tac-Toe | game | ☐ | ☐ | ☐ |
| 12 | ATM | state machine | ☐ | ☐ | ☐ |

### Next 10 — two reps each; third rep only where timed performance shows a gap
| # | Problem | Skeleton | R1 | R2 |
|---|---|---|----|----|
| 13 | Hit Counter | data-structure | ☐ | ☐ |
| 14 | HashMap | data-structure | ☐ | ☐ |
| 15 | Trie / Autocomplete | data-structure | ☐ | ☐ |
| 16 | Text Editor | data-structure | ☐ | ☐ |
| 17 | File System | data-structure | ☐ | ☐ |
| 18 | Task Scheduler | pipeline | ☐ | ☐ |
| 19 | Inventory + stock blocking | allocation | ☐ | ☐ |
| 20 | URL Shortener | data-structure | ☐ | ☐ |
| 21 | Snake & Ladder | game | ☐ | ☐ |
| 22 | Digital Wallet | ledger | ☐ | ☐ |

**22 problems, ~56 reps.** No additions until timed performance shows a genuine gap.

### Optional 10 — one rep, only if time allows
Snake Game · LFU Cache · Chess · Meeting Room Scheduler · Coffee Machine ·
Locker Management · Library Management · Stock Portfolio Tracker ·
**File Adapter / Converter Framework** · **In-memory Document Search & Filtering**

The last two came from an external review. Low evidence of being commonly asked, so
optional rather than core — but both exercise useful muscle: Adapter/Strategy for the
converter, and indexing + filter composition for document search. Document search is
also a reported Razorpay problem, so it doubles as company-layer prep for that style.

### Excluded from the core (company layer only)
In-memory RDBMS, in-memory pub-sub, git-lite. Razorpay-style "build a mini-system"
problems. Prepare only if such a round is actually scheduled.

---

## The six skeletons

| Skeleton | Core move |
|---|---|
| **Resource allocation + lifecycle** | find available -> assign -> release |
| **State machine** | states + legal transitions |
| **Data-structure design** | pick 2 structures, make ops O(1) |
| **Game / board** | board, players, turn order, win rule |
| **Transaction / ledger** | balances, splits, settlement |
| **Pipeline / dispatch** | route a thing through handlers |

Parking lot and hotel booking are the SAME problem. Vending machine and ATM are the SAME
problem. After three reps of a skeleton, a new costume costs ~5 minutes of extra
requirements gathering, not a new skill.

---

## Curveball bank — rotate, never predictable

Do NOT use the same extension twice on one problem. Pick from the bank at random, sealed
until the agreed moment.

| Problem | Extensions |
|---|---|
| Parking Lot | nearest spot, then cheapest spot; multi-floor; pricing varies by vehicle type |
| Movie Booking | **expiring seat holds**; competing booking attempts on one seat |
| Digital Wallet / ATM | failure recovery mid-transaction; transaction history; **duplicate requests (idempotency)** |
| Task Scheduler | task dependencies; retries; recurring tasks; cancellation |
| Notification Service | multiple channels; retry with backoff; per-user preferences |
| LRU Cache / Rate Limiter | time complexity of every op; time-window semantics; thread safety |
| File System / HashMap | edge cases; what is in memory vs persisted; collision handling |
| Splitwise | unequal splits; multi-currency; settlement simplification |
| Elevator | multiple lifts + dispatch strategy; priority/express requests |
| Vending Machine | cannot make change; refund mid-transaction; restock during a sale |
| Ride-hailing | surge pricing; driver cancellation; matching strategy change |
| Inventory | oversell under concurrency; partial fulfilment; reservation expiry |

### Mid-round requirement injection
Some companies (Razorpay style) add requirements **at minute 40, while you are still
building** — not at the end. From problem 5 onward, practise this: the extension arrives
mid-build and must be absorbed without restarting.

---

## Concurrency layer

A second pass after R2, not new problems.

| Problem | The race |
|---|---|
| Parking Lot | two threads occupy one spot between `can_fit` and `occupy` (check-then-act) |
| Movie Booking | two users book the same seat |
| Inventory | oversell when stock is blocked concurrently |
| Digital Wallet | double-spend / concurrent debit on one balance |
| Rate Limiter | concurrent counter increments |
| Task Scheduler | concurrent workers pulling the same task |

**Say even without implementing:** where the race is, what the lock protects, lock
granularity (per-spot vs whole-lot) and why a coarse lock kills throughput, how deadlock
is avoided. Seeing the race and naming the fix scores most of the marks.

---

## Rep schedule — ROLLED, not batched

Do NOT finish all 22 first reps before starting second reps — six weeks between building
and revisiting loses most of it.

**Rule: when starting problem N, do R2 of problem N-4 and R3 of problem N-10.**

---

## Python friction — fix it actively, do not wait it out

Current bottleneck is mechanical, not design: bracket placement, `__init__`, dict vs list
access, import paths. Zero design errors so far. In a timed round this costs ~20 minutes
that do not exist.

1. **Every build starts from the same minimal project skeleton**, typed from memory in
   under 10 minutes: enums, exception hierarchy, frozen dataclasses for value objects,
   ABC for the varying behaviour, dict-backed storage, thin orchestrator, `main.py`
   driver. (`reference/skeleton.py` in the repo — written by hand, never copied.)
2. **Run the program throughout, not at the end.** Compilation is not a final step. After
   every class, run something.

---

## Recovery protocol — when a round is going badly

Neither panic nor silence. Both are scored down.

- **Wrong design spotted mid-build:** say it out loud and fix it.
  *"I've realised Ticket shouldn't own this — I'm moving it to the lot, costs me five
  minutes."* Catching your own error and correcting it is a POSITIVE signal.
- **Behind on time at minute 75:** stop adding features. Make what exists run, write the
  driver, demo it. *A partial solution with good design beats a messy complete one.*
- **Stuck on a requirement:** state the assumption out loud and move on.
  *"I'll assume X for now and flag it as an open question."*
- **Never go silent.** Narrate the stuck-ness itself.

---

## Learning doc — one per problem, written after R1 only

- Requirements and assumptions
- Class responsibilities and public methods
- The most important invariant
- Why the chosen abstractions are justified
- Tests, edge cases, and the main extension
- One thing to do differently next time

**R2 and R3 are attempted WITHOUT consulting it.** Review it only after the rep.

---

## Mocks — three, one of them early

- **Mock 1, after problem 8-10.** An **unfamiliar prompt**, not one from the list. Ask for
  concrete feedback on five axes: requirements gathering, code completeness, OO design,
  time management, communication. Feedback arriving here can still change 12+ problems of
  practice.
- **Mock 2, after problem 22 — machine coding.** Blank editor, strict timer, runnable
  code, tests, unseen extension, no hints.
- **Mock 3, after problem 22 — discussion / hybrid.** Another unfamiliar design. The
  interviewer should challenge class boundaries, ask why a pattern is warranted, and
  introduce a change forcing a partial redesign.

**Ask for specific observations, not a pass/fail verdict.** You need to know whether the
weakness was design, implementation speed, requirements clarification, or communication.

Known delivery faults to watch for in transcripts: numbers move when speeding up; answers
trail into vague summaries instead of stopping on the concrete fact.

---

## Daily load

**LLD is the priority this month.** DSA stays in the loop but yields on collision.

| Day type | LLD | DSA |
|---|---|---|
| Normal weekday | 1 hour (checkpoints or an R2/R3) | 5 revision + 2 new/DP |
| Full-build day | the full rep | **revision only** |
| Weekend | one full rep + one timed rep | 90-min virtual contest |

Applications and referrals run daily throughout. They do not pause for prep.

---

## Evaluation bar

**See `lld_design_rubric.md`** for the full principles / OOP / patterns checklist and the
CP7 review list. Headline: in India, interviewers ask about patterns directly — so design
cleanly first and name precisely WHEN ASKED, never as running commentary. Interview-ready
designs use none, one or two patterns; three or more reads as over-engineering.

1. **Working code** — must compile and run. *A partial solution with good design beats a
   messy complete one.*
2. **OO design** — classes, interfaces, encapsulation, separation of concerns. Heavily weighted.
3. **Extensibility** — how much code changes when a requirement is added.
4. **Patterns** — where they fit naturally. Where none is warranted, SAY SO and name the
   seam: *"no Strategy yet because nothing varies; if selection becomes configurable,
   `_find_available` is the seam."*
5. **Readability**, then **edge cases / validation**.

---

## What closes LLD

1. 22 problems, all reps, every rep solved as process rather than recall
2. The last 10 done solo under the clock — no help, no lookups
3. Three mocks with a human — one mid-way, two at the end
4. Python friction gone — actively fixed, not waited out

---

## Company layer — only when a round is scheduled

Generic prep above is the bulk of it. Do not prepare company-specific material
speculatively. Once a round IS booked, two weeks:

1. Search company + role + "interview experience", last 2-3 months. Determine format,
   duration, whether code must run.
2. Any problems named in recent reports get a dedicated rep.
3. Map their problem to one of the six skeletons; re-rep that skeleton in their format.
4. Learn their domain vocabulary — fintech: settlement, reconciliation, idempotency,
   double-entry. Commerce: SKU, fulfilment, blocking vs reserving. Devtools: webhook,
   retry, backoff.
5. Book mocks: one technical with an SDE2+ person, one behavioural with an EM-level person.

Interview-experience reports are self-reported and companies rotate problems. Treat any
problem-to-company mapping as a probability, never a guarantee.
