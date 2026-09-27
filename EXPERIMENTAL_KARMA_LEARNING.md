## Experimental Karma Learning

The `experiment/karma-learning` branch introduces a minimal persistent
conditioning layer without replacing the existing Digital Sangha architecture.

The learning loop is:

**present conditions → action → predicted consequences → actual consequences → Sangha reflection → conditioning → next present**

The experimental implementation deliberately separates:

- **recursive convergence** — stabilization of the current state within an encounter;
- **conditioning** — persistent change in dispositions across encounters;
- **prediction error** — difference between predicted and observed consequences.

The browser dashboard stores its experimental state in `localStorage`, so repeated
visits from the same browser continue the experimental history. This is a
developmental demonstration, not a claim that the system is sentient.

The Python reference implementation is `karma_learning.py`.
