# ATOS — Aerodynamic Tolerance Optimization System
### Geometry · Tolerance Analysis · Drag Sensitivity

<div align="center">

[![Python](https://img.shields.io/badge/Python-Calculation%20Tools-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Testing](https://img.shields.io/badge/Testing-pytest-0A9EDC?style=for-the-badge)](https://docs.pytest.org/)
[![Status](https://img.shields.io/badge/status-calculation%20scaffold-blue?style=for-the-badge)](#current-scope)

</div>

## Overview

ATOS is a calculation scaffold for double-eccentric offset geometry, simplified tolerance-stack calculations, and drag-force sensitivity scenarios. It provides a transparent software starting point for studying geometry and parameter sensitivity before any CAD/CFD validation is attempted.

## Current Scope

- Double-eccentric offset vector calculations.
- Worst-case and root-sum-square tolerance-stack estimates.
- Drag-equation calculations and user-specified drag-coefficient sensitivity scenarios.
- CLI, automated tests, and GitHub Actions.
- Documentation describing a future CAD/CFD validation protocol.

This repository currently documents a calculation workflow. It should not be described as a completed SolidWorks/Ansys Fluent CFD/FEA validation project unless those artifacts and reports are added.

## Quick Start

```bash
python -m venv .venv
# Activate the environment, then:
python -m pip install -e '.[test]'
pytest -q
```

Confirm the commands against the current package configuration and update if the project setup changes.

## Technical Notes

Document the governing equations, units, coordinate conventions, input constraints, tolerance assumptions, and meaning of each output. Include representative examples and tests for limiting cases.

## Validation Status

The **0.5 mm gap** and **4.5% drag-reduction** figures mentioned in the original project description are unverified hypotheses, not reproduced results. This repository does not contain a SolidWorks model, a validated Ansys Fluent case, mesh-independence evidence, wind-tunnel data, or airworthiness approval.

Do not use this calculation scaffold to authorize flight-critical modifications or replace engineering review.

## Suggested Structure

```text
.
├── src/                 # Calculation package
├── tests/               # Automated test cases
├── docs/
│   ├── images/          # Workflow / geometry diagrams
│   └── reports/         # Assumptions and validation plan
├── pyproject.toml
├── .github/workflows/   # Continuous integration
└── README.md
```

Keep the tree aligned with actual files and avoid adding empty folders solely for presentation.

## Roadmap

- [ ] Document units, coordinate conventions, assumptions, and equations.
- [ ] Add representative input/output examples and edge-case tests.
- [ ] Publish tolerance sensitivity plots with test data.
- [ ] Define a future CAD/CFD validation protocol, including boundary conditions, mesh sensitivity, and convergence criteria.
- [ ] Compare model outputs against an independent analytical or experimental reference if feasible.

## References & License

Cite the sources of equations, material/fluid properties, and relevant engineering standards. Specify the actual repository license.

## Contact

**Shivtej Salunke · SAL Dynamics**  
[GitHub](https://github.com/shivtejsalunke) · [LinkedIn](https://www.linkedin.com/in/shivtejsalunke) · [Email](mailto:shivtejsalunke23@gmail.com)
