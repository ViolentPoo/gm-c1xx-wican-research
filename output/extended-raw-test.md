# Extended Raw WiCAN Test

Purpose: expand beyond the quick 5-10 minute run after the basic HS-CAN candidates are proven stable. Keep this read-only and staged. Do not run broad DID scans.

## Preconditions

- Complete `output/quick-live-test.md` first.
- Save `/load_auto_pid` before changes.
- Confirm `010C` returns live RPM.
- Keep the first extended pass on HS-CAN/500K.
- Stop if WiCAN becomes unreachable or responses become stale/repeated.

## Pass A: Longer HS-CAN Warm-Up

Use this pass to observe values over 15-30 minutes from cold or partially warm start.

```text
010C   RPM sanity
0105   coolant temperature
0110   MAF
011F   standard runtime
0142   module voltage
0146   ambient air temperature
221154 enhanced oil temperature
221940 transmission temperature on 7E2/7EA and optionally 7E0/7E8
1A6D   confirmed oil life
2236A7 confirmed air filter life
2211A1 enhanced runtime
```

Validation focus:

- Temperature values should rise smoothly.
- Standard `011F` and enhanced `2211A1` should agree or have an obvious unit relationship.
- Oil life and air filter life should match the dash exactly.
- Fuel-rate and MAF should move together with load if the configured fuel-rate sensor remains available.

## Pass B: Extended ECM Diagnostics

Set route:

```text
ATSH7E0;ATCRA7E8;
```

Run these one at a time at idle, then optionally after a brief light-throttle stationary blip:

```text
221200 total current misfires
221206 cylinder 1 current misfires
221205 cylinder 2 current misfires
221207 cylinder 3 current misfires
221208 cylinder 4 current misfires
2211EA cylinder 5 current misfires
2211EB cylinder 6 current misfires
2212C3 injector duty cycle bank 1
2212C4 injector duty cycle bank 2
2211A6 knock retard
2212D9 total knock retard
2213AF cooling fan motor command
223812 cooling fan command
223318 oil-pressure control solenoid raw
```

Validation focus:

- Misfire counters should stay at `0` on a healthy idle. Treat nonzero values as diagnostic evidence only, not alert triggers.
- Injector duty should be low at idle and rise with load.
- Fan command should increase only when coolant/A/C conditions justify it.
- Knock values may remain zero during a stationary test.
- `223318` is raw only until formula and behavior are understood.

## Pass C: HS-CAN Passive Capture

If raw/passive capture is available without permanent config changes, capture these while performing deliberate actions:

```text
0x12A doors and belts
0x140 turn signals and high beams
0x1F1 ignition and park brake
0x1F5 PRNDL and transmission state
0x3F9 oil life and generator duty
0x4C9 passive transmission oil temperature
0x4D1 fuel level oil temperature oil pressure
```

Actions:

- All doors closed baseline.
- Open and close one door at a time.
- Buckle and unbuckle driver belt while parked.
- Toggle turn signals and high beams.
- Toggle parking brake.
- PRNDL checkpoints only when explicitly prompted, brake applied, and vehicle stationary.

## Pass D: Low-Speed/SW-CAN Passive Session

Run this as a separate session only after HS-CAN is restored and saved. WiCAN cannot monitor HS-CAN/500K and low-speed/SW-CAN simultaneously with one adapter.

Candidate low-speed frames:

```text
0x8064A000 window positions
0x806AA000 rear closure ajar
0x805A0000 power liftgate status
0x803D4000 TPMS pressures
0x80728000 hood status
0x80390000 remote start status
0x80288000 RFA/key status
0x8020C000 lighting and brake/reverse status
0x80248000 battery state/current
```

Actions:

- Move one window at a time and record full-up/full-down/intermediate frames.
- Open/close liftgate only if safe and stationary.
- Compare TPMS values to the cluster.
- Move key inside/outside only while parked and secured.
- Press brake while parked.

## Notes

- One WiCAN means one bus configuration at a time.
- Two WiCANs on a fully wired OBD splitter can monitor HS-CAN and SW-CAN concurrently if the splitter exposes the needed pins.
- Keep low-speed body testing passive-first. Do not transmit lock, window, liftgate, or remote-start controls.
