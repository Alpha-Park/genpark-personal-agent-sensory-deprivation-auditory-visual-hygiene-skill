---
name: genpark-personal-agent-sensory-deprivation-auditory-visual-hygiene-skill
version: "1.0.0"
description: "Zero-dependency Sensory Overload Index (SOI) quantifier, thalamocortical sensory gating modeler, and Restricted Environmental Stimulation Therapy (REST) protocol prescriptor."
license: MIT
dependencies:
  - python>=3.10
  - mcp>=1.0.0
entrypoint: client.py
---

# Personal Agent Sensory Deprivation Auditory Visual Hygiene Skill

Designed for **OpenClaw**, **Hermes**, and sovereign personal AI health agents to quantify thalamocortical sensory gating fatigue, synthesize multi-modal sensory inputs (photopic flux, ambient acoustic decibels, notification interrupts) into the Sensory Overload Index (SOI), and prescribe customized Restricted Environmental Stimulation Therapy (REST) doses.

## Agent In-Context Capabilities

- **Sensory Overload Index (SOI)**: Combines logarithmic decibel burden, retinal high-contrast blue light irradiance, and task-switching notification interrupts into a 0-100 index.
- **REST Protocol Dosing**: Prescribes structured sensory blackout regimes (Flotation REST, Chamber REST, or Micro Sensory Hiatus).
- **Cognitive Attenuation Forecasting**: Predicts percentage reduction in prefrontal cortex neural gating strain.

## Tools Summary

1. `calculate_sensory_overload_burden`: Returns SOI score, saturation tier, and component breakdown.
2. `prescribe_sensory_deprivation_rest_dose`: Outlines environmental specifications and duration for neuro-sensory de-escalation.
