# LLD Gym — one month, Python, machine-coding rounds

Target: Razorpay / Meesho / Swiggy / CRED machine-coding and LLD rounds.
Format being trained for: build a **working program with a driver, inside 90 minutes**,
absorbing new requirements thrown mid-round. Not a class diagram. Not a discussion.

## Rules of the gym

- Python only. No framework, no DB, dicts for storage.
- It must run at the timer. Unfinished but running beats complete but broken.
- Never watch a video or open a reference solution for a problem before attempting it.
- Every problem ends with `learnings.md` written by Mohak, refined with Claude.

## Levels

### Week 1 — skeleton and simple entities (full hand-holding)
1. Parking Lot  *(session 1 also builds the reusable skeleton)*
2. Tic-Tac-Toe
3. Vending Machine
4. Elevator System

### Week 2 — multi-entity, state machines, locking (less hand-holding)
5. Splitwise
6. Snake and Ladder
7. Movie Ticket Booking  *(concurrency: seat locking)*

### Week 3 — timed machine-coding simulation, 90 min strict (hints only)
8. In-memory SQL database  *(reported at Razorpay)*
9. Ride-sharing, two features  *(reported at Meesho)*
10. Rating system  *(reported at Razorpay)*

### Week 4 — company-shaped, interview conditions (near-silent)
11. Inventory with stock blocking  *(Meesho's most reported)*
12. Payment processing package  *(CRED-shaped)*
13. Top-K restaurant discovery  *(Swiggy-shaped)*
14. Git-like version control  *(reported at Razorpay SDE2)*

Weeks 3 and 4 are aspirational on volume. Finishing 10 levels properly beats 14 half-done.

## Scoring

Three stars per level:
- it runs and the driver demonstrates every flow
- no business rule leaked into the orchestrator, no infra leaked into entities
- the curveball needed no edit to existing working classes

Two stars minimum to advance. One star means repeat the level later in the week.

## Weekly rhythm

- Weekdays: ~1 hour LLD (checkpoints 1-3 of the next problem, or finishing the previous), ~45 min DSA.
- One weekend day: the full 90-minute uninterrupted build, plus review.
- Daily, separately: applications and referral outreach. This does not pause.

## Folders

- `weekN/<problem>/` — one folder per level: `requirements.md`, `src/`, `main.py`, `learnings.md`
- `reference/skeleton.py` — the reusable machine-coding skeleton. **Mohak writes this**, in session 1.
- `docs/` — rubric, rejection list, pattern triggers
- `progress.md` — the scoreboard
