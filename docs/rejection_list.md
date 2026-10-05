# What gets you rejected in a machine-coding round

Check this before submitting at checkpoint 7.

1. **Code that does not run at the timer.** The single biggest killer. Razorpay and Meesho
   reject on this regardless of how good the design looked.
2. **No driver demonstrating the flows.** If the interviewer has to imagine it working, it
   did not work.
3. **Blew the clock on discussion.** 35 minutes of requirements and entities, then panic
   coding. Design is capped at 25 minutes total.
4. **God class.** One service holding all the logic, anemic data bags around it.
   *This is Mohak's specific reflex from four years of router -> controller -> service -> repository.*
5. **if/else on type.** It survives the happy path and explodes at the curveball.
6. **No custom exceptions, no validation.** Bare `raise Exception("bad")` everywhere.
7. **`print()` instead of returning objects.** Makes the code untestable and undemoable.
8. **Silence.** These rounds are scored partly on narration. Say what you are doing.
9. **Forcing patterns.** A Factory and an Observer bolted onto a problem that needed
   neither reads worse than plain classes. Name the pattern after the design fits.
