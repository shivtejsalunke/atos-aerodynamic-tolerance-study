# ATOS — Aerodynamic Tolerance Optimization System

ATOS is a calculation scaffold for double-eccentric offset geometry, simplified tolerance-stack calculations, and drag-force sensitivity scenarios.

## Current scope
- Double-eccentric offset vector calculations.
- Worst-case and root-sum-square tolerance stack estimates.
- Drag equation calculations and user-specified drag-coefficient sensitivity scenarios.
- CLI, tests, and GitHub Actions.
- Documentation describing a future CAD/CFD validation protocol.

## Quick start
```bash
python -m venv .venv
# Activate the environment, then:
python -m pip install -e '.[test]'
pytest -q
```

## Important limitations
The 0.5 mm gap and 4.5% drag-reduction figures mentioned in the original project description are unverified hypotheses, not reproduced results. This repository does not contain a SolidWorks model, a validated Ansys Fluent case, mesh-independence evidence, wind-tunnel data, or airworthiness approval. Do not use this scaffold to authorize flight-critical modifications.
