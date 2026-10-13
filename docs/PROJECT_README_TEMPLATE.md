# ATOS — Aerodynamic Tolerance Optimization System

> A mechanical design and simulation study exploring geometry/tolerance considerations and aerodynamic performance.

![SolidWorks](https://img.shields.io/badge/SolidWorks-3D%20CAD-DA291C?style=flat-square)
![Ansys Fluent](https://img.shields.io/badge/Ansys%20Fluent-CFD-CF5C20?style=flat-square)
![CFD](https://img.shields.io/badge/CFD-Flow%20Simulation-795548?style=flat-square)
![Status](https://img.shields.io/badge/status-in%20development-orange?style=flat-square)

## Overview

Describe the component or assembly, its operating conditions, the aerodynamic problem, and the engineering constraints. Clarify whether the work is a preliminary concept, CAD study, simulated analysis, or experimentally validated design.

## Objectives

- Establish a documented baseline geometry and performance metric.
- Model the modified geometry and relevant tolerance constraints.
- Set up CFD with defensible boundary conditions and convergence checks.
- Perform stress/FEA analysis where applicable and report limitations.

## Design Context

Describe the assembly, materials, coordinate system, units, key dimensions, tolerance stack, and operating conditions. Explain why the considered tolerance or geometry change matters.

![CAD model](docs/images/cad-model.png)

## Tools & Methods

- CAD: SolidWorks [version]
- CFD: Ansys Fluent [version]
- Structural analysis: [solver, material model, assumptions]
- Post-processing: [plots/scripts/tools]

## Repository Layout

```text
.
├── cad/
│   ├── native/
│   └── neutral-exports/
├── simulation/
│   ├── geometry/
│   ├── mesh/
│   ├── solver-settings/
│   └── post-processing/
├── analysis/
│   ├── drag-calculations/
│   └── fea/
├── results/
│   ├── figures/
│   └── reports/
├── docs/
│   ├── images/
│   └── reports/
├── references/
└── README.md
```

Include native and neutral files only when licensing and file-size constraints permit. Avoid committing temporary solver caches and huge intermediate files without a clear reason.

## Simulation Setup

Document the assumptions needed to interpret the result:

| Parameter | Value |
|---|---|
| Geometry revision | [identifier] |
| Fluid / material properties | [values and source] |
| Inlet / outlet / wall conditions | [values] |
| Turbulence / physical model | [model and rationale] |
| Mesh type and element count | [details] |
| Convergence criteria | [residuals and monitored quantities] |
| Solver version and precision | [details] |

Provide mesh images, boundary-condition screenshots, and solver convergence histories.

## Governing Equations & Calculations

State the equations used, define every variable and unit, and cite the source. For example, when appropriate, the drag relation may be written as:

`F_D = \frac{1}{2}\rho v^2 C_D A`

Explain the assumptions and how `C_D`, reference area, density, and velocity were established. Do not compare values if the reference areas or boundary conditions differ without explaining the difference.

## Results

| Metric | Baseline | Modified case | Difference | Evidence |
|---|---:|---:|---:|---|
| Drag force / coefficient | [value] | [value] | [value] | [report/plot] |
| Peak stress | [value] | [value] | [value] | [report/plot] |
| Maximum displacement | [value] | [value] | [value] | [report/plot] |

A 4.5% drag-reduction figure has appeared in project materials. Treat it as a **reported result pending substantiation** until the baseline, mesh, solver setup, convergence, and comparison data are included.

## Verification & Sensitivity

- Include a mesh-independence or mesh-sensitivity study.
- Show convergence of relevant monitors, not only residual plots.
- Check mass balance and boundary-condition plausibility.
- Document material model, contacts, loads, constraints, and mesh quality for FEA.
- Compare to an analytical estimate, published benchmark, or experiment where feasible.

## Limitations

- CFD/FEA results depend on modeling choices and idealized conditions.
- State any missing validation, simplified geometry, or uncertain material properties.
- Do not present a simulated gain as experimentally proven performance.

## Reproduce the Study

Document software versions, case files, parameter settings, mesh generation procedure, solver steps, and post-processing commands. State any proprietary-tool requirements.

## Roadmap

- [ ] Publish geometry and boundary-condition diagrams.
- [ ] Add convergence and mesh-sensitivity evidence.
- [ ] Include baseline and modified-case result tables.
- [ ] Document structural assumptions and tolerance stack.
- [ ] Compare simulation results against an independent reference where possible.

## References & License

Cite equations, standards, datasheets, material properties, and third-party models. State license/redistribution limits for CAD, solver, and project files.

## Contact

**Shivtej Salunke · SAL Dynamics**  
[GitHub](https://github.com/shivtejsalunke) · [LinkedIn](https://www.linkedin.com/in/shivtejsalunke) · [Email](mailto:shivtejsalunke23@gmail.com)
