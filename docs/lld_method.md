# LLD Method — the checkpoint protocol

The repeatable procedure. Applies to every problem, every rep. Design principles, OOP
concepts and patterns live in `lld_design_rubric.md`; the schedule lives in
`lld_calendar.md`.

---

## Setup — before CP0, every single build

```bash
mkdir weekN/<problem> && cd weekN/<problem>
touch <problem>.py
```

**One file.** Exceptions at the top, classes, then the driver at the bottom under
`if __name__ == "__main__":`. No packages, no `src/`, no import paths — that friction
cost 20 minutes in session 1 and buys nothing.

**Run the file after every class.** Compilation is not a final step.

## The checkpoints

| CP | What | Time |
|---|---|---|
| 1 | Requirements — the six moves | 10 min |
| 2 | Entities + relationships | 10 min |
| 3 | Class design — state + behaviour per class | 10 min |
| 4 | Code the core flow | 25 min |
| 5 | Driver with asserts | 10 min |
| 6 | Curveball — where does the change go? | 10 min |
| 7 | Review + verdict | — |

Design is capped at 25 minutes (CP1-CP3). Blowing the clock on discussion then
panic-coding is a top rejection cause.

---

## CP1 — requirements: the six moves

| # | Move | Fills |
|---|---|---|
| M1 | **STATE** the operations, invite correction | Capabilities |
| M2 | **INVERT** each operation to find failures | Errors |
| M3 | **FIND** every choice the system makes | Rules ← highest value |
| M4 | **ASK** what varies by type | Rules ← second highest |
| M5 | **TRACE** the main entity's lifecycle | Rules |
| M6 | **DECLARE** out of scope, get confirmation | Scope |

Final sweep: Capabilities / Rules / Errors / Scope. An empty bucket means a move was skipped.

**Ask what the system must DO. Never ask how YOU should build it.**
*"Should this support cancellation?"* = good. *"Should I use Strategy here?"* = you just
asked the interviewer to design it.

### Field notes
- **M1** — operations are what an ACTOR asks for, not internal steps. *"Who stands in
  front of this and asks for it?"* Returning change is a step inside dispense, not an
  operation. State and invite correction; open-ended reads lost, stating reads senior.
- **M2** — invert ONE operation at a time, never the whole system. *What must be true
  before this succeeds?* Each precondition is a failure. Invert the API call (any string
  can arrive), not the physical object.
- **M3** — anywhere the system picks one thing from many. *"When several spots fit, how do
  I pick?"* A choice is where behaviour varies; variation is where the pattern and the
  curveball live.
- **M4** — M3 and M4 sometimes point at the same seam. Normal.
- **M5** — finds the entity you can't see: what exists only during the flow and vanishes
  after? Vending machine → the transaction. Parking lot → the ticket.

### The three buckets
Every item lands in exactly one:

| Bucket | Test | Example |
|---|---|---|
| **Functional requirement** | the *system does* something; a verb; testable | "The system issues a ticket when a vehicle parks." |
| **Domain fact** | a noun, number or fixed list; just true; feeds a requirement | "Vehicle types are motorcycle, car, truck." |
| **Assumption** | *you* decided it; the interviewer never confirmed | "Ticket IDs are opaque strings." |

If the sentence can't start with "The system…", it is not a functional requirement.
**"Extensible to X" is never a functional requirement** — extensibility is a property of
the design, shown in code, not promised in a spec.

---

## CP2 — entities and relationships

### Entity filter
A noun becomes a **CLASS** if either is true:
1. its state changes over time
2. it enforces a rule about data it owns

Otherwise:
3. fixed label from a closed list → **enum**
4. values that travel together and never change after creation → **value object**

Then: who sequences the steps → **orchestrator**. Owns no business rules.

### Entity vs value object vs enum
- **Entity** — has identity. Two with identical fields are still two different things.
  Needs an id. (Ticket, ParkingSpot)
- **Value object** — NO identity. Two with identical fields are interchangeable. Frozen
  after creation. Exists so values travel together and can't be transposed at a call site.
  (Vehicle). **Embedded, never referenced** — in a DB they'd be columns, not a table.
- **Enum** — a single label from a closed list. (VehicleType)

### Relationships — 3 questions per arrow
1. Who holds a reference to whom?
2. Cardinality — one or many?
3. Direction — default ONE-WAY. Add the reverse only when a requirement forces it.

| Word | UML | Direction | The tell in the constructor |
|---|---|---|---|
| **contains** | composition | one → many | the owner **CREATES** the parts |
| **has-a** | aggregation | one → many | the owner **ACCEPTS** parts made elsewhere |
| **uses** | association | many → one | just **HOLDS A POINTER**, creates nothing |

**Test: does the child die when the parent dies?** Yes → composition. No, but still held →
aggregation. Just pointed at → association. **Lifecycle ownership decides direction, not
cardinality.**

**Hold the OBJECT, not an id.** `self._spot = spot`, never `self._spot_id = "A3"` —
holding an id forces a lookup through the owner on every use.

### The present-vs-history trap
> **The database models ALL OF TIME. The runtime object graph models THIS INSTANT.**

A DB has one mechanism — the foreign key, always on the many side. An object graph has
two, which is why `ParkingLot → ParkingSpot` (composition) runs *opposite* to the FK while
`Ticket → ParkingSpot` (association) matches it.

Ask **"at this instant, how many?"** — not "over time, how many?" Symptom of getting it
wrong: `self._tickets: list[Ticket]` on a spot, a scan on every exit, and an
impossible-by-design state you now have to defend.

### Derive relationships one operation at a time
Never map the whole graph at once.
> *"Exit computes the fee and frees the spot."* → exit receives a ticket id, so the lot
> must hold tickets; it must free a spot, so from the ticket it must reach a spot. Two
> arrows found.

### Why the arrows matter
1. `Ticket → ParkingSpot` makes exit O(1): `ticket.spot.release()`. Without it, exit scans.
2. `ParkingLot → Ticket (active only)` IS the storage decision: `dict[str, Ticket]`.
3. The arrow NOT drawn pays most — no reverse pointer means no circular import and the
   entity unit-tests alone.

---

## CP3 — class design

### The boundary rule
> If a step **decides something about the domain** → it belongs in the object.
> If a step **moves data across a boundary** → it belongs in the orchestrator.

- "Decides" = any `if` encoding a business rule.
- "Moves data" = fetch, hand off, return, store. Pure transport.

**Three-second test:** an `if` inside the orchestrator that reads a FIELD off another
object → that rule belongs in that object. An `if` about a COLLECTION the orchestrator
owns → it stays.

**The shape, every time: LOAD → TELL → SAVE.**

```python
# ANEMIC — orchestrator decides everything
for spot in self._spots:
    if not spot.is_occupied and spot.type == vehicle.type:   # DECIDES. wrong place.
        spot.is_occupied = True                              # mutates from outside

# RICH — orchestrator sequences, spot decides
spot = self._find_available(vehicle.type)   # transport
if spot is None: raise NoSpotAvailable()    # about MY collection — legitimately mine
spot.occupy(vehicle.type)                   # TELL — the spot guards itself
```

### Commands are not setters
A setter stores what it's given and asks nothing — which forces the CALLER to check first,
which rebuilds the fat orchestrator.

```python
def occupy(self, vehicle_type):      # a COMMAND that can REFUSE
    if not self.can_fit(vehicle_type):
        raise SpotNotAvailable()
    self._is_occupied = True
```

**Command-query separation:** queries return values (`can_fit → bool`); commands raise on
failure and return nothing (`occupy → None`). A command that always returns `True` carries
zero information and invites a meaningless `if`.

### Three more rules
- **Don't store what's derivable or owned elsewhere.** Two copies = two things to sync =
  a silent bug. Before adding a field: *does any requirement need it?*
- **Pass policy in, store facts.** A fact about this instance → store it (entry_time). A
  value that varies by policy → pass it in (hourly rate). Passed-in values become Strategy
  objects for free.
- **Entities never call each other in both directions.** The orchestrator calls entities.
  One direction along the arrow is fine; the reverse is a circular dependency.

### Start order
Hello Interview says start with the orchestrator. For an ex-fat-service dev that's a trap.
Instead: (1) orchestrator METHOD NAMES only, 1 minute; (2) design the entities fully,
pulling each decision down to the data owner; (3) return and write the bodies — now 3-4
lines each.

### Write the caller first
Stuck on "where would this get used?" → **write `main()` before the classes.** Three lines
of usage and every method you need falls out of them. That's where `ticket.id` came from.

---

## CP4-CP5 — code and driver

- Bottom-up: enums/value objects → entities → orchestrator → driver. Each class is
  runnable the moment it's finished.
- **The driver must demonstrate every flow and assert the outcome.** Print state
  before *and* after each action — `free: 2 → 1 → 2` proves the state changed. A demo that
  only prints the final answer proves nothing.
- A round where code runs but nothing is demonstrated scores the same as one where nothing
  runs.

---

## CP6 — curveball

Opened at the 2/3 mark, sealed until then. **Say where the change goes; don't implement
it.** The question being answered: did the design need an edit to a working class?

Some rounds inject the requirement at minute 40, mid-build, not at the end. Practise both.

---

## CP7 — review

Full checklist in `lld_design_rubric.md` §6. Verdict first: REJECT / WEAK HIRE / HIRE.

---

## Recovery protocol — when a round goes badly

- **Wrong design spotted mid-build:** say it out loud and fix it. *"I've realised Ticket
  shouldn't own this — moving it, costs five minutes."* Catching your own error is a
  POSITIVE signal.
- **Behind at minute 75:** stop adding features. Make what exists run, write the driver,
  demo it. *A partial solution with good design beats a messy complete one.*
- **Stuck on a requirement:** state the assumption out loud and move on.
- **Never go silent.** Narrate the stuck-ness itself.

---

## What gets you rejected

1. Code that doesn't run at the timer — the single biggest killer.
2. No driver demonstrating the flows.
3. Blew the clock on discussion, then panic-coded.
4. God class — one service holding all logic, anemic data bags around it.
   *(The known reflex: router → controller → service → repository.)*
5. `if/else` on type — survives the happy path, explodes at the curveball.
6. No custom exceptions, no validation.
7. `print()` instead of returning objects.
8. Silence.
9. Forcing patterns. Name the pattern after the design fits, never before.
