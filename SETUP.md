# Local setup

```bash
# 1. unzip wherever you keep code
cd ~/code && unzip ~/Downloads/lld-gym.zip && cd lld-gym

# 2. make it a repo
git init
git add -A
git commit -m "LLD gym: curriculum, session rules, templates"

# 3. create an EMPTY repo on github named lld-gym, then
git remote add origin git@github.com:<your-username>/lld-gym.git
git branch -M main
git push -u origin main

# 4. start a level
cp -r templates/problem week1/parking-lot
cd week1/parking-lot

# 5. open Claude Code from the repo root so it reads CLAUDE.md
cd ~/code/lld-gym && claude
```

Keep it **private**. Half-finished interview practice is not a portfolio.

Commit after every level with the verdict in the message:

```bash
git add -A && git commit -m "L1 parking lot: WEAK HIRE, 2 stars, leaked fee logic into orchestrator"
```

The commit log becomes the honest record of whether the month worked.
