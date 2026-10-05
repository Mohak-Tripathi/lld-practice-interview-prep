# When each pattern is actually earned

Five patterns are in scope. Nothing else.

| Trigger you see in the requirements | Pattern |
|---|---|
| "behaviour differs by type" / if-else on an enum | **Strategy** |
| "pick nearest, then cheapest, then..." | **Strategy** (the selection rule is the strategy) |
| "object has states and legal transitions between them" | **State** |
| "when X happens, notify Y and Z" | **Observer** |
| "creation depends on a type code and may grow" | **Factory** |
| "exactly one instance, shared" | **Singleton** (rarely worth it; say why) |

**The rule:** a requirement must have *varied* before you reach for a pattern.
No variation, no pattern. Strategy, polymorphism, and the Open/Closed Principle are
one move, not three: replace if/else-on-type with objects sharing an interface.
