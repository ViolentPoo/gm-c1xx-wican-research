# WiCAN User Guide For GM C1XX Research

This guide explains how to use the data in this repository with WiCAN while keeping testing read-only and repeatable. It is written for WiCAN users researching GM C1XX vehicles such as Buick Enclave, Chevrolet Traverse, GMC Acadia, Cadillac XT5, and Cadillac XT6.

## Safety Scope

Use this repository for passive monitoring and read-only diagnostics only.

Allowed service families for this project:

| Service | Purpose |
|---|---|
| `01` | Standard OBD-II current data. |
| `09` | Vehicle information where supported. |
| `22` | Read data by identifier, one DID at a time. |
| `1A` | GM read data by packet identifier where supported. |

Avoid service families that can clear data, run controls, change coding, request security access, or program modules.

## First Steps With WiCAN

Before editing anything permanent:

1. Confirm the vehicle is awake/running.
2. Save the current `/load_auto_pid` response.
3. Test one known-good PID such as RPM before testing unknown values.
4. Add or change only a few entries at a time.
5. Reboot WiCAN after saving AutoPID or CAN-filter changes.
6. Keep raw responses and validation notes.

Useful WiCAN endpoints:

| Endpoint | Use |
|---|---|
| `/load_auto_pid` | Read current AutoPID configuration before editing. |
| `/store_auto_data` | Save AutoPID/custom PID/CAN-filter configuration. |
| `/autopid/test_pid` | One-off test for OBD PID or enhanced DID definitions. |
| `/autopid/test_can_filter` | One-off test for passive CAN filter expressions. |
| `/api/webhook` | Inspect webhook delivery state and interval. |
| `/system_reboot` | Reboot after saving configuration or leaving monitor/capture mode. |

## Reading The Data Tables

Start with these files:

| File | What It Contains |
|---|---|
| `data/pids.csv` | Standard OBD-II PIDs and live validation status. |
| `data/dids.csv` | GM enhanced DIDs and one-off diagnostic results. |
| `data/broadcast-signals.csv` | Passive CAN signals and confidence/status. |
| `data/module-addresses.csv` | Known or candidate request/response routes. |
| `output/wican-candidate-config.example.json` | WiCAN-ready confirmed entries and examples. |

Status meanings:

| Status | Meaning |
|---|---|
| `confirmed` / `confirmed_live` | Observed on the target vehicle and matched expected behavior. |
| `existing` | Already working in the project but still worth independent validation. |
| `candidate` / `passive_test_candidate` | Evidence exists, but the signal is not confirmed on the target vehicle. |
| `rejected` / `no_data_live` | Tested and should not be trusted for this route/vehicle. |

## WiCAN Byte Expressions

Many internet formulas use `A`, `B`, `C`, and `D` for response bytes. WiCAN expressions in this project usually use `B3`, `B4`, or byte ranges such as `[B3:B6]` because the response includes service/PID/DID bytes before the data byte.

Example active DID response:

```text
7E8 04 62 11 54 4C
```

For this response:

| Byte | Meaning |
|---|---|
| `62` | Positive response to service `22`. |
| `11 54` | Echoed DID. |
| `4C` | First data byte. In WiCAN formulas here, this is `B4`. |

That is why confirmed oil temperature `221154` uses:

```text
((B4-40)*1.8)+32
```

## Confirmed WiCAN Entries

### Oil Life

| Field | Value |
|---|---|
| Request header | `7E0` |
| Response filter | `7E8` |
| PID/request | `1A6D` |
| Expression | `B3*100/256` |
| Unit | `%` |

Validation: matched the dash oil-life display at about 34%.

### Air Filter Life

| Field | Value |
|---|---|
| Request header | `7E0` |
| Response filter | `7E8` |
| PID/request | `2236A7` |
| Expression | `B4` |
| Unit | `%` |

Validation: matched the dash air-filter-life display at 85%.

### Transmission Temperature

Confirmed request:

| Field | Value |
|---|---|
| PID/request | `221940` |
| Expression | `((B4-40)*1.8)+32` |
| Unit | `F` |

Observed routes:

| Request Header | Response Header | Notes |
|---|---|---|
| `7E0` | `7E8` | ECM/gateway-style route responded. |
| `7E2` | `7EA` | TCM-style route also responded with close value. |

### Engine Oil Temperature

| Field | Value |
|---|---|
| Request header | `7E0` |
| Response filter | `7E8` |
| PID/request | `221154` |
| Expression | `((B4-40)*1.8)+32` |
| Unit | `F` |

Standard OBD PID `015C` returned no data on the tested vehicle.

## Confirmed Passive CAN Filters

WiCAN stores passive CAN filters in top-level `can_filters` inside `/load_auto_pid` / `/store_auto_data` JSON.

Schema:

```json
{
  "frame_id": 501,
  "parameters": [
    {
      "name": "PRNDL_RANGE_CODE",
      "expression": "B3",
      "unit": "",
      "class": "none",
      "period": "1000",
      "min": "1",
      "max": "12",
      "type": "Default",
      "send_to": "",
      "enabled": true
    }
  ]
}
```

### PRNDL / Manual Range: `0x1F5`

| Name | Expression | Meaning |
|---|---|---|
| `PRNDL_RANGE_CODE` | `B3` | Selected PRNDL/manual range code. |
| `PRNDL_MANUAL_FLAG` | `B5` | `0` normal PRND, `2` manual L range. |

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

| Name | Expression | Meaning |
|---|---|---|
| `PARK_BRAKE_SET` | `(B4&16)/16` | `1` set, `0` released. |

## Passive Filter Timing Caveat

WiCAN direct `/autopid/test_can_filter` can see passive frames immediately, but downstream webhook consumers can lag. In one observed test, direct WiCAN testing saw Park immediately while the downstream state updated several minutes later.

Treat passive CAN-filter values as display/research values unless you have independently measured update latency for your setup.

## Validation Workflow

For each new PID, DID, or passive frame:

1. Save raw response or raw CAN frame.
2. Record vehicle state: off, accessory, running, parked, driving, gear, temperature, or physical switch state.
3. Decode with the smallest possible expression.
4. Compare against the dash, a scan tool, or a deliberate physical action.
5. Repeat after returning to baseline.
6. Mark as confirmed only when the value repeats and matches expected behavior.

## Troubleshooting

| Symptom | Likely Cause | Action |
|---|---|---|
| `NO DATA` for known PIDs | Vehicle/modules asleep | Wake vehicle and re-test a known-good PID first. |
| `7F 22 31` | DID not supported on that route | Record as rejected for that route; do not scan blindly. |
| AutoPID test stays busy | Previous request or route wedged WiCAN | Reboot WiCAN and avoid broad probing. |
| Passive filter returns `No frame` | Frame not seen during short test window | Repeat with the vehicle awake and the relevant action occurring. |
| Value matches once but not later | Bad byte mapping or stale state | Capture raw frames/responses and validate again. |

## Contributing New Findings

When adding findings, include:

- Vehicle year/model/trim if known.
- Engine/transmission if known.
- Request header and response header for active diagnostics.
- Raw response or raw CAN frame.
- WiCAN expression used.
- Physical validation target.
- Whether the result was confirmed, rejected, or only a candidate.

Do not include private network addresses, device IDs, passwords, VINs, or account-specific paths in public notes.
