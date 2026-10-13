# LLD Design Rubric — principles, OOP, patterns

Source: Hello Interview "Low Level Design in a Hurry" — design-principles, oop-concepts,
patterns. Apply on every problem; use as the CP7 review checklist.

---

## The India posture

> "In US interviews, you're generally evaluated on design quality rather than on naming
> patterns. In other regions, such as India, interviewers are more likely to ask about
> patterns directly."

**So: design cleanly first, then name precisely when asked.** Naming happens at the end
of a section or in answer to a question — NOT as running commentary while coding.

Two failure modes, both real:
- **Silent** — used Strategy, never said so, interviewer assumes you got there by luck.
- **Over-naming** — announcing a pattern every two minutes. Hello Interview is explicit:
  *interview-ready designs use none, one, or two patterns. Three or more suggests
  over-engineering.*

On OOP vocabulary specifically: *"You don't need to name these concepts in an interview.
The concepts show through in how you design, not in what you name."* Be ready to answer
"why is this encapsulated?" — don't volunteer "here I am applying encapsulation."

**The sentence that scores, when no pattern is warranted:**
> "No Strategy here yet — nothing varies. If spot selection becomes configurable,
> `_find_available` is the seam."

---

## 1. General design principles

| Principle | Definition | Self-check |
|---|---|---|
| **KISS** | Pick the straightforward approach; add complexity only when simplicity stops working. | Is any class here earning its existence? |
| **DRY** | Consolidate logic that is *conceptually* the same. Do NOT force unrelated code to share an abstraction. | Is this duplication real, or coincidental similarity? |
| **YAGNI** | Implement what current requirements call for. Design for extension, don't BUILD for hypothetical futures. | Did I add anything no requirement asked for? |
| **Separation of Concerns** | Different responsibilities in different parts, each changeable and testable independently. | Can I unit-test this class with zero other objects? |
| **Law of Demeter** | A method's dependencies stay to nearby objects — no navigating chains of other objects' internals. Chaining that returns the same object type is fine. | Any `a.b.c()` in my code? |

**Law of Demeter is the one most likely to appear in this code.** `ticket.spot.release()`
is a violation — `spot` is a stranger reached through `ticket`. Options: have `close()`
return the spot, or accept it and *name the tradeoff out loud*. Not noticing is the
only wrong answer.

## 2. SOLID

| | Definition | Self-check |
|---|---|---|
| **SRP** | A class should have one reason to change. | Can I name this class's single reason to change? |
| **OCP** | Open for extension, closed for modification. New behaviour from new classes, not edits. | Does the curveball force me to edit a working class? |
| **LSP** | A subclass must be usable anywhere its base is, without breaking what the base promises. | Does any subclass throw or no-op on an inherited method? |
| **ISP** | Small focused interfaces over large ones. No class implementing methods it doesn't need. | Does any implementer leave a method empty? |
| **DIP** | Depend on abstractions, not concretions. (Dependency injection is a *technique* for this, not the principle.) | Does the orchestrator hardcode a concrete rule it should receive? |

Caution from the source: don't over-apply SOLID outside Java/C#. Modern Python favours
**composition over class hierarchies, functions over interfaces.**

## 3. OOP concepts

| Concept | Definition | Interview advice |
|---|---|---|
| **Encapsulation** | Keeping an object's data private and letting the object control how it's used. | Basic hygiene. Private fields, expose methods. **Returning a collection? Return a copy or unmodifiable view.** |
| **Abstraction** | Exposing only what's essential, hiding implementation behind clear interfaces. | Trigger: tangled logic, or requirements with multiple variations. Pick the right level — `doWork()` is meaningless; too specific abstracts nothing. |
| **Polymorphism** | Objects respond to the same call in their own way; replaces type checks and switches on type. | Use when behaviour varies by type. **Be ready to state the tradeoff:** more flexible and extensible, but control flow is harder to trace and debug. |
| **Inheritance** | One class as a more specific version of another. Shares implementation, creates tight coupling. | Only for stable shared implementation. Avoid for behaviour variation. Default to interfaces + composition. **"In most LLD interviews, you don't need inheritance at all."** |

The encapsulation detail is a cheap, concrete win: if a getter returns a list, return
`list(self._spots)` not `self._spots`.

## 4. Patterns — triggers

| Pattern | Kind | Trigger |
|---|---|---|
| **Strategy** | behavioral | Interchangeable ways of doing the same thing, swapped at runtime. Replaces if/else or switch on type. **The most common pattern in LLD interviews.** |
| **Observer** | behavioral | Multiple components must react to one change. Signal words: "notify", "update multiple components". |
| **State Machine** | behavioral | Behaviour depends on current state with complex transitions. Signal: "state" repeated in requirements. Vending machines, document workflows. |
| **Factory** | creational | Callers shouldn't know which concrete class to create. "Support different notification types", multiple payment methods. |
| **Builder** | creational | Many optional parts or config choices. Unnecessary for simple objects with a few required fields. |
| **Singleton** | creational | Only when exactly one shared instance is genuinely needed. Passing shared objects through constructors is usually clearer. |
| **Decorator** | structural | Layering optional, combinable behaviours at runtime (logging, encryption). Signals: "optional features", "stack behaviors". If the variation is fixed at design time, use subclasses instead. |
| **Facade** | structural | A coordinator hiding complexity behind a simple interface — e.g. a `Game` class orchestrating board and players. **Naming it is optional; no need to announce.** |

**Your orchestrators are Facades.** `ParkingLot` is one. Don't announce it.

**A pattern is earned only when a requirement has VARIED.** No variation, no pattern.

## 5. Per-problem pattern map

Expected, not mandatory — the requirements decide.

| Problem | Likely |
|---|---|
| Parking Lot | Strategy (spot selection, pricing) |
| Vending Machine / ATM / Elevator | State Machine |
| Notification Service | Strategy (channels) + Factory + Observer |
| Logging Framework | Chain of Responsibility *(not in HI's list — Decorator or Strategy also defensible)* |
| Rate Limiter | Strategy (token bucket vs sliding window) |
| Movie Booking | Strategy (seat allocation) + State (hold -> booked -> expired) |
| Splitwise | Strategy (split type: equal / exact / percentage) |
| Ride-hailing | Strategy (matching, pricing) + Observer (trip status) |
| Task Scheduler | Strategy (scheduling policy) + Observer (completion) |
| LRU / HashMap / Trie | usually NONE — say so and name the seam |

Several of these need **zero** patterns. Saying "none is warranted here, and here's the
seam if it changes" scores better than inventing one.

## 6. CP7 review checklist

Run on every rep, in order:

1. **Does it run?** Driver demonstrates every flow with asserts.
2. **SRP** — each class's single reason to change, nameable in one sentence.
3. **Anemic check** — did a business rule leak into the orchestrator? Did infra leak into
   an entity? *(The known reflex: router -> controller -> service -> repository producing
   a fat orchestrator with dumb data bags.)*
4. **Encapsulation** — private fields; collections returned as copies.
5. **Law of Demeter** — any `a.b.c()`? Named, if accepted.
6. **OCP via the curveball** — did it force an edit to a working class?
7. **Patterns** — used where earned; where none, is the seam named?
8. **Inheritance** — any used? Is it for *shared implementation* rather than *behaviour
   variation*? Could composition replace it?
9. **YAGNI** — anything built that no requirement asked for?
10. **Three questions an interviewer would ask**, with what a weak answer looks like.
