# <Problem> — learnings

Written after the review, by Mohak first, then refined with Claude.

## Verdict received


## What I got structurally wrong
(not style differences — structure only)


## The rule I will carry to the next problem


## Where the curveball would have hurt


## Time split actual vs planned
| CP | Planned | Actual |
|----|---------|--------|
| requirements | 10 | |
| entities | 10 | |
| skeletons | 10 | |
| core code | 25 | |
| driver | 10 | |



## Field notes
- M1: operations are what an ACTOR asks for. Not internal steps. "Who stands in front
  of this and asks for it?" Returning change is a step inside dispense, not an operation.
- M2: invert ONE operation at a time, never the whole system. For each: what must be
  true before this succeeds? Each precondition is a failure. Invert the API call
  (any string can arrive), not the physical object.
- M3 and M4 sometimes point at the same seam. That's normal.
- M5 finds the entity you can't see: what exists only during the flow and vanishes after?
  Vending machine → the transaction. Parking lot → the ticket.