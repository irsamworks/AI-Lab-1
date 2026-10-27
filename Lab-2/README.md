# Lab 2: Intelligent Agents

## Overview

This lab explores intelligent-agent design using PEAS specifications, environment classification, and a stateful classroom temperature-control agent.

## Files

* `lab2_percepts.py` — Implements the original reflex classroom agent.
* `lab2_model.py` — Implements a stateful agent that remembers its previous mode and avoids repeated commands.
* `lab2_check.py` — Tests the stateful agent using seven test cases.
* `outputs/percepts_output.txt` — Output from the original reflex agent.
* `outputs/stateful_output.txt` — Output from the stateful agent.
* `outputs/test_results.txt` — Test results for the stateful agent.
* `Lab2_Report.docx` — Written report covering PEAS specifications, environment classifications, implementation, testing, and reflection.

## Requirements

* Python 3
* No external Python packages are required.

## How to Run

Open a terminal in the project directory and run:

```bash
python Lab-2/lab2_percepts.py
python Lab-2/lab2_model.py
python Lab-2/lab2_check.py
```

## Expected Results

The original reflex agent should produce the modes `COOL`, `COOL`, `IDLE`, `IDLE`, `WARM`, and `ECO` for the supplied percept sequence.

The stateful agent should send a command when the target mode changes and avoid sending a duplicate command when the target mode remains unchanged.

The test script currently passes all seven test cases.

## Assumptions and Limitations

The classroom is simulated. Temperature is measured in degrees Celsius, and occupancy is represented by a Boolean value. The agent selects a target mode but does not control real HVAC hardware. The current implementation uses fixed thresholds and does not include sensor-failure detection, physical comfort measurements, or hysteresis.

## Academic Integrity

The implementation and report should reflect the student's own understanding. Any external sources or borrowed code should be acknowledged in the report.
