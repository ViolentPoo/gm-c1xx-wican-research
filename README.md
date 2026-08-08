# GM C1XX WiCAN Research

Research package for WiCAN PID, DID, and passive CAN discovery on GM C1XX vehicles, focused on the 2022 Buick Enclave and related Chevrolet Traverse, GMC Acadia, Cadillac XT5, and Cadillac XT6 models.

Primary goals:

- Build an evidence-based library of standard OBD-II PIDs, GM enhanced DIDs, module addresses, and broadcast CAN signals.
- Separate confirmed findings from likely, possible, experimental, and rejected definitions.
- Provide a safe read-only test plan for WiCAN validation.

Start with:

- `docs/research-summary.md`
- `output/test-plan.md`
- `data/pids.csv`
- `data/dids.csv`
- `data/broadcast-signals.csv`

Safety rule: this project is for passive monitoring and read-only diagnostics only. Do not use it for vehicle control, actuator tests, coding, programming, security access, or unsafe experimentation.
