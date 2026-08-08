# Quick Live WiCAN Test

Purpose: run the highest-value read-only tests in 5-10 minutes while the vehicle is awake. Do not change permanent AutoPID configuration during this pass.

## Setup

- Vehicle parked, parking brake applied.
- Any shift out of Park must be operator-directed: stay in Park until I explicitly ask for Reverse, Neutral, or Drive during the live session.
- WiCAN reachable before testing.
- Open the WiCAN PID test UI or API endpoint for one-off requests.
- Open `data/live-test-results-template.csv` for recording results.
- Record exact raw responses, including negative responses such as `7F`.

## Stop Conditions

- Stop if `010C` does not return live RPM.
- Stop if WiCAN becomes unreachable or responses become stale/repeated.
- Stop if any request causes warning lights, module errors, or unexpected behavior.
- Do not scan ranges and do not transmit control/write/clear/security services.

## Pass 0: Baseline

Run first:

```text
010C
```

Record RPM and vehicle state. Continue only if it is live and plausible.

Save current config for rollback reference:

```text
/load_auto_pid
```

## Pass 1: Supported Standard PID Bitmaps

Run these quickly and paste raw responses:

```text
0100
0120
0140
0160
0180
01A0
```

Do not spend time decoding during the vehicle session. The responses decide which standard PIDs are eligible later.

## Pass 2: Highest-Value Standard PIDs

Run only one-off tests:

```text
015C  engine oil temperature
015E  engine fuel rate
01A4  transmission gear/ratio
01A6  odometer
015A  relative accelerator position
010B  MAP
0133  barometric pressure
0106  STFT bank 1
0107  LTFT bank 1
010E  timing advance
0161  driver demand torque
0162  actual engine torque
0163  engine reference torque
```

Fast checks:

- `01A6` should match dash mileage.
- `015A` should move with a light pedal sweep while parked.
- `015C` should be plausible for engine temperature.
- `010B` KOEO should be near barometric pressure; running idle should be lower.

## Pass 3: ECM Enhanced DIDs

Set header/filter first:

```text
ATSH7E0;ATCRA7E8;
```

Run in this order:

```text
221940  transmission fluid temperature
221154  enhanced oil temperature
1A6D    confirmed oil life
2236A7  confirmed air filter life
2211A6  knock retard candidate
```

Also test the stronger Traverse/TCM route for transmission-fluid temperature as a one-off:

```text
ATSH7E2;ATCRA7EA;
221940  transmission fluid temperature via TCM-style route
ATSH7E0;ATCRA7E8;
```

Park-only gear baseline:

```text
skip 221951 and 22199A; both rejected in Park on live Enclave test
```

Do not repeat `221951` or `22199A` unless a stronger route/header is found.

Fast checks:

- `221940` should be plausible and near ambient on cold start, then slowly rise. XT5/9T65 service data shows typical TFT values around 41 C key-on/engine-off, 52 C running, 87 C at 48 km/h, and 94 C at 80 km/h.
- `221154` should be plausible and not conflict with `015C` if supported.
- `1A6D` is confirmed active oil life and should match the dash.
- `2236A7` is confirmed air filter life and should match the dash.
- `22119F`, `22119F01`, `221155`, `22115C`, `221470`, `221C1B`, `222344`, `222345`, `221951`, and `22199A` are rejected for this route/session and should not be retested in the quick run.

## Pass 3A: Optional 1-2 Minute Passive Check

Do this only if WiCAN raw/passive capture is already available without changing permanent configuration. Skip it if it would take time to set up.

Watch for these frames while parked:

```text
0x3F9  oil-life candidate
0x1F5  PRNDL/current gear candidate
0x12A  door/belt status candidate
0x1F1  ignition/platform status candidate
```

Fast checks:

- `0x3F9` is the best passive oil-life candidate; compare decoded value to dash before trusting.
- `0x1F5` has OpenDBC and independent GMLAN evidence for PRNDL/range; capture Park by default and only capture R/N/D if I explicitly ask for a brake-applied checkpoint.
- `0x12A` is the preferred door-status lead over experimental active BCM DIDs; record whether it appears at all.
- Do not spend the 5-10 minute session trying to solve raw-capture tooling if it is not immediately available.

## Pass 4: BCM One-Off Only If Time Allows

BCM `222122` rejected on the confirmed BCM route. Do not repeat in the quick run unless a stronger source is found:

```text
ATSH241;ATCRA641;
222122
```

Prefer passive/low-speed capture for doors instead. Do not scan nearby DIDs.

## After The 5-10 Minute Pass

- Paste the raw responses back into `data/live-test-results-template.csv` or send them for entry.
- Mark each row `Confirmed`, `Rejected`, or `Needs more testing`.
- Update `data/dids.csv`, `data/pids.csv`, `data/conflicts.csv`, and the output summaries.
- Only after these tests should we decide whether raw/passive CAN capture is needed.
