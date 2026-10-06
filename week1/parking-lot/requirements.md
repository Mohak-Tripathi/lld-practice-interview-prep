<!-- 

## They're not competing. One is the output, one is the input.

**Hello Interview's four themes are the buckets your answer lands in.** Capabilities,  errors, rules, scope. That's a checklist for *verifying you covered everything* at the end.

**My six moves are how you generate the questions** that fill those buckets. That's the *procedure*.

Themes = what the finished spec must contain. Moves = what you actually do with your mouth in those ten minutes. You were trying to use the themes as a procedure. They don't work that way, which is exactly why you sat there unable to think of questions.

---

## The one checklist. Six moves, in order.

**Move 1 — State the operations, invite correction.** → fills *Capabilities*

Don't ask open-ended. State and invite.

> "I'm assuming three operations: park a vehicle, exit with a ticket, and query availability. Am I missing any?"

Open-ended ("what should it support?") reads lost. Stating reads senior. If you're wrong, he corrects you, which costs nothing.

**Move 2 — Invert each operation to find failures.** → fills *Errors*

Mechanical. Take each operation. Ask: what makes this not work?

Park → lot full / no spot of that type / vehicle already inside.
Exit → ticket doesn't exist / ticket already used.

You said "I don't know what failure means." You never have to know. You derive it. One operation at a time, ask what breaks it.

**Move 3 — Find every place the system makes a choice.** → fills *Rules*

Anywhere the system picks one thing out of many.

> "When a vehicle arrives and several spots fit, how do I pick one? First available, nearest, cheapest?"

This is the highest-value question in any LLD problem. A choice is where behaviour varies. Varying behaviour is where the pattern goes, and where the curveball lands at minute 50.

**Move 4 — Ask what varies by type.** → fills *Rules*

> "Does pricing differ by vehicle type, or is it one flat rate?"

Same logic as move 3. Variation by type is the other seam.

**Move 5 — Trace the lifecycle of the main entity.** → fills *Rules*

> "A ticket goes from active to used. Can it ever be reissued or cancelled?"

State transitions are where the bugs and the interviewer's follow-ups live.

**Move 6 — Declare out of scope, get confirmation.** → fills *Scope*

> "I'm excluding payment gateway, UI, persistence, and reservations. Tell me if any of those are actually in."

Volunteer it. Don't wait to be asked. This protects your clock and reads as senior.

**Then sweep the four themes as a final check.** Capabilities covered? Rules? Errors? Scope? If a bucket is empty, a move got skipped.

Save this:

```bash
# in docs/requirements_checklist.md
```

```markdown
# Requirement gathering — 6 moves, every problem

1. STATE the operations, invite correction.    -> Capabilities
2. INVERT each operation to find failures.      -> Errors
3. FIND every choice the system makes.          -> Rules  ← highest value
4. ASK what varies by type.                     -> Rules  ← second highest
5. TRACE the main entity's lifecycle.           -> Rules
6. DECLARE out of scope, get confirmation.      -> Scope

Final sweep: Capabilities / Rules / Errors / Scope — any bucket empty means a move was skipped.

Ask what the system MUST DO. Never ask how YOU should build it.
"Should this support cancellation?" = good.
"Should I use a Strategy pattern here?" = you just asked the interviewer to design it.
```

---

## Now map the spec into your file

The flat list I gave you isn't the answer sheet. It's raw material. Sorting it into the four sections *is* the exercise.

Two worked, so you see the shape:

**Clarifying questions I asked** — this section is your record of moves 1 to 6. Write the questions as questions:

```
1. (M1) Operations: park, exit, query availability. Missing any? → no, that's all three.
2. (M3) When several spots fit, how is one chosen? → first available matching spot.
```

**Functional requirements** — numbered, each one a behaviour the system does. Not a fact about the domain.

```
1. The system accepts a vehicle of type motorcycle, car or truck and assigns it the
   first available spot matching its type, issuing a ticket.
2. The system rejects parking when no matching spot is free.
```

Notice: "three vehicle types" is **not** a functional requirement. It's a domain fact that feeds requirement 1. That distinction is the thing to learn here. Requirements are verbs.

Your turn for the rest. Sort these yourself:

- single floor, capacity fixed at construction
- flat hourly rate, rounded up to the full hour
- exit fails on unknown or already-used ticket
- ticket: active → used; spot: free → occupied → free
- payment gateway, UI, persistence, reservations, multi-floor

Three go in functional requirements as verbs. One is an assumption. One is out of scope. One is a domain fact that belongs inside a requirement rather than standing alone.

Paste the finished file. Before checkpoint 2, I'll give you a 60-second drill on a different problem to confirm the six moves actually stuck. If they didn't, we stay here. You're right not to move forward until they do. -->


# Parking Lot — requirements

## Clarifying questions I asked
1. (M1) Operations are park, exit, query availability. Am I missing any? → No.
2. (M3) When several spots fit a vehicle, how is one chosen? → First available matching spot.
3. (M4) Does anything vary by vehicle type — pricing, spot size? → Spot size yes, pricing no.
4. (M2) What makes parking fail? → No free spot of that vehicle's type.
5. (M2) What makes exit fail? → Ticket unknown, or ticket already used.
6. (M5) Ticket lifecycle — can it be reissued or cancelled? → No. Active → used, once.
7. (M5) Spot lifecycle — anything between free and occupied? → No. Free → occupied → free.
8. (M6) Excluding payment gateway, UI, persistence, reservations, multi-floor. Confirm? → Confirmed.

## Domain facts
- Vehicle types: motorcycle, car, truck.
- A spot is sized for exactly one vehicle type and fits only that type.
- Single floor. Capacity is fixed when the lot is constructed.
- Pricing: one flat hourly rate for all vehicle types.

## Functional requirements
1. The system parks a vehicle by assigning the first available spot matching the
   vehicle's type, and issues a ticket recording the spot and the entry time.
2. The system rejects a park request when no spot matching that vehicle's type is free.
3. The system exits a vehicle against its ticket, computes the fee, and frees the spot.
4. The system computes the fee as the hourly rate times the parked duration,
   rounded up to the next full hour.
5. The system rejects an exit when the ticket is unknown or has already been used.
6. The system marks a ticket used on exit; a ticket is never reissued or cancelled.
7. The system reports how many spots are currently free, per vehicle type.

## Out of scope
- Payment gateway and money movement
- UI / rendering
- Persistence / networking
- Reservations and pre-booking
- Multiple floors

## Assumptions I am stating out loud
- Single-threaded. No concurrent park/exit; I'll note where a lock would go.
- Ticket IDs are unique opaque strings; I'm not designing an ID scheme.
- A vehicle is identified by a licence plate and cannot be parked twice at once.
- Time is supplied to the system, not read from a global clock, so fees are testable.

