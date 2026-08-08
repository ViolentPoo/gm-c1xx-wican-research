# GM C1XX WiCAN Research

Research package for WiCAN OBD-II PID, GM enhanced DID, and passive CAN discovery on GM C1XX vehicles, focused on the 2022 Buick Enclave and related Chevrolet Traverse, GMC Acadia, Cadillac XT5, and Cadillac XT6 models.

It includes confirmed examples for oil life, air filter life, transmission temperature, engine oil temperature, odometer, passive PRNDL/range on CAN `0x1F5`, and park brake state on CAN `0x1F1`.

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

## Confirmed Live Findings

These values were confirmed on a 2022 Buick Enclave C1XX with WiCAN. See the linked data files and notes for raw responses, caveats, and rejected alternatives.

| Signal | Route / CAN ID | WiCAN Expression | Status | Notes |
|---|---:|---|---|---|
| Oil life | `1A6D`, `7E0`/`7E8` | `B3*100/256` | Confirmed | Matched dash oil life at about 34%. |
| Air filter life | `2236A7`, `7E0`/`7E8` | `B4` | Confirmed | Matched dash air filter life at 85%. |
| Transmission temperature | `221940`, `7E0`/`7E8` and `7E2`/`7EA` | `((B4-40)*1.8)+32` | Confirmed | Both ECM/gateway and TCM-style routes responded with close values. |
| Engine oil temperature | `221154`, `7E0`/`7E8` | `((B4-40)*1.8)+32` | Confirmed | Standard `015C` returned no data on this vehicle. |
| Odometer | `01A6`, `7DF`/`7E8` | `[B3:B6]*0.0621371` | Confirmed | Matched cluster mileage. |
| PRNDL / selected range | Passive CAN `0x1F5` | `B3`, `B5` | Confirmed | Park, Reverse, Neutral, Drive, and L1-L9 observed. |
| Park brake set | Passive CAN `0x1F1` | `(B4&16)/16` | Confirmed | `1` means set, `0` means released. |

## Confirmed Passive CAN Mappings

### PRNDL / Manual Range: `0x1F5`

WiCAN CAN-filter parameters:

| Parameter | Expression | Meaning |
|---|---|---|
| `PRNDL_RANGE_CODE` | `B3` | Selected PRNDL/manual range code. |
| `PRNDL_MANUAL_FLAG` | `B5` | `0` for normal PRND, `2` for manual L range. |

Observed mapping:

| Range | `B3` | `B5` |
|---|---:|---:|
| Park | `1` | `0` |
| Reverse | `2` | `0` |
| Neutral | `3` | `0` |
| Drive | `4` | `0` |
| L1 | `12` | `2` |
| L2 | `11` | `2` |
| L3 | `10` | `2` |
| L4 | `9` | `2` |
| L5 | `8` | `2` |
| L6 | `7` | `2` |
| L7 | `6` | `2` |
| L8 | `5` | `2` |
| L9 | `4` | `2` |

### Park Brake: `0x1F1`

WiCAN CAN-filter parameter:

| Parameter | Expression | Meaning |
|---|---|---|
| `PARK_BRAKE_SET` | `(B4&16)/16` | `1` when park brake is set, `0` when released. |

## Data Layout

| Path | Purpose |
|---|---|
| `data/pids.csv` | Standard OBD-II PID candidates, confirmed values, and rejected values. |
| `data/dids.csv` | GM enhanced DID candidates and live validation status. |
| `data/broadcast-signals.csv` | Passive CAN broadcast signals and confidence levels. |
| `data/module-addresses.csv` | Known and candidate module routes. |
| `output/wican-candidate-config.example.json` | Confirmed WiCAN candidate snippets, including passive CAN filters. |
| `docs/wican-configuration-guide.md` | WiCAN endpoint and configuration notes. |
| `docs/wican-user-guide.md` | Practical workflow for using this research with WiCAN. |
| `docs/validation-guide.md` | Validation workflow for new signals. |
| `research/raw-notes/live-session-2026-08-06.md` | Raw live-session observations and caveats. |

## Important Caveats

- This is vehicle-observed research, not official GM service data.
- Confirm every signal on your vehicle before trusting it.
- Passive CAN-filter webhook consumers can lag; use confirmed passive gear and park-brake values for display/research rather than immediate-response automation.
- Avoid broad scans. Use read-only diagnostics and passive capture first.

Safety rule: this project is for passive monitoring and read-only diagnostics only. Do not use it for vehicle control, actuator tests, coding, programming, security access, or unsafe experimentation.
