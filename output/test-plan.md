# Safe Vehicle Test Plan

Prerequisites:

- Vehicle parked.
- Parking brake applied.
- WiCAN reachable.
- Save current `/load_auto_pid` before changes.
- Verify `010C` returns RPM before testing additional PIDs.

For a fast vehicle-awake session, use `output/quick-live-test.md` and record into `data/live-test-results-template.csv`. For a longer staged session after the quick pass is stable, use `output/extended-raw-test.md`.

## Phase 1: Standard Supported-PID Discovery

Requests:

```text
0100
0120
0140
0160
0180
01A0
```

Goal:

- Build the actual supported standard-PID map for the Enclave.
- Do not add unsupported standard PIDs as permanent sensors.

## Phase 2: Standard PID Validation

Test in small batches:

```text
0106
0107
010B
010E
0133
015A
015C
015E
0161
0162
0163
01A4
01A6
```

Validation:

- Compare expected behavior to `docs/validation-guide.md`.
- Keep existing guarded logic for speed/fuel/voltage.

## Phase 3: Known ECM DIDs

Header/filter:

```text
ATSH7E0;ATCRA7E8;
```

Requests:

```text
221940
221154
22119F
22119F01
1A6D
22115C
221470
221C1B
222344
222345
221951
22199A
2211A6
2211A1
221200
221206
221205
221207
221208
2211EA
2211EB
2212C3
2212C4
2212D9
2213AF
223812
223318
```

Validation:
- `221940`: test both existing `7E0`/`7E8` and Traverse-backed `7E2`/`7EA` one-off routes if feasible; compare warm-up behavior and scan tool if available. XT5/9T65 service data shows typical TFT values around 41 C key-on/engine-off, 52 C running, 87 C at 48 km/h, and 94 C at 80 km/h.
- `221949`: fallback only if `221940` fails; do not include in the 5-10 minute quick test unless there is extra time and a clear negative result for `221940`.
- `221154`: compare with `015C` if supported.
- `22119F`: compare with dashboard oil life.
- `22119F01`: reject if `7F 22 13` or implausible.
- `1A6D`: reject unless it exactly tracks dashboard oil life.
- `22115C`: check engine-off baseline and running pressure behavior before converting units; public formula evidence is `(A*0.65)-17.5` psi.
- `221470`: check engine-off baseline and running pressure behavior before converting units.
- `221C1B`/`222344`/`222345`: Traverse-backed one-off oil-pressure candidates; check for zero or near-zero engine-off and rising running response but do not convert until formula is known.
- `221951`/`22199A`: compare to PRNDL and passive `0x1F5`; XT5/9T65 service data lists TCM Current Gear and Gear Command as P/R/N or 1-9 in D/L/M. Do not test while driving unless a helper records data safely.
- `2211A6`: compare only as a low-priority engine diagnostic value after basics are stable.
- Extended raw pulls: `221200`, `221206`, `221205`, `221207`, `221208`, `2211EA`, and `2211EB` are Traverse-backed misfire counters; `2212C3`/`2212C4` are injector duty; `2212D9` is total knock retard; `2213AF`/`223812` are fan commands; `223318` is oil-pressure control solenoid raw. These belong in `output/extended-raw-test.md`, not the quick run.

## Phase 4: Known TCM DIDs

No TCM physical request/response pair is confirmed yet.

Use standard `01A4`, passive `0x1F5`, and the existing `221940` candidate first before any TCM diagnostic probing. The K71 9T65 service page and GM bulletin `20-NA-136` confirm useful TCM scan-tool values but do not disclose DIDs or request headers.

## Phase 5: Other Confirmed Module Addresses

BCM route confirmed:

```text
ATSH241;ATCRA641;
```

Safe one-off candidate after passive tests:

```text
222122
```

Validation:

- Record all-closed response.
- Open one door at a time.
- Do not scan adjacent DIDs.

## Phase 6: Passive CAN Capture

Start with current HS-CAN/500K if WiCAN raw capture is available:

```text
0x12A BCMDoorBeltStatus
0x140 BCMTurnSignals
0x1F1 BCMGeneralPlatformStatus
0x3F9 Engine_General_Status_3
0x1F5 Transmission_General_Status_2
0x4D1 Engine_General_Status_5
```

If HS-CAN does not show door/window data, save config and investigate SW-CAN/low-speed mode as a separate session. One WiCAN cannot monitor HS-CAN/500K and low-speed/SW-CAN at the same time:

```text
0x10630000 DriverDoorStatus
0x8064A000 Window_Position_Status_LS
0x806AA000 Rear_Closure_Ajar_Switch_Status
0x805A0000 Control_Power_Liftgate_LS
0x803D4000 Tire_Pressure_Sensors_LS
0x80728000 Hood_Status_LS
0x8020C000 Lighting_Status_LS
0x80248000 Battery_Voltage
```

Do not transmit lock/window/liftgate control frames.

## Phase 7: Formula Validation

For each new response:

- Save raw response.
- Identify echoed service/PID/DID bytes.
- Map WiCAN byte references (`B3`, `B4`, ranges) from actual payload.
- Compare against dashboard or physical behavior.
- Record conflicts in `data/conflicts.csv`.

## Phase 8: WiCAN Configuration

Only after validation:

- Add permanent WiCAN AutoPID entries.
- Add downstream consumers only after stable sensor mapping.
- Do not create alerts for doors/liftgate/windows until all bits are repeatably mapped.
