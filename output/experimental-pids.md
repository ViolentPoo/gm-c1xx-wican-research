# Experimental Research Leads

These are not safe to treat as confirmed. Test one at a time only after supported-PID checks and known-good awake validation.

| Name | Request/ID | Module/Header | Why Experimental |
|---|---:|---|---|
| Oil life rejected | `22119F`, `22119F01`, `221155` | `7E0`/`7E8` | Rejected on live Enclave test; use confirmed `1A6D` instead |
| Oil pressure rejected set | `22115C`, `221470`, `221C1B`, `222344`, `222345` | `7E0`/`7E8` | Returned zero/implausible running values on live Enclave test |
| Transmission temp fallback | `221949` | `7E0`/`7E8` first; maybe Auto/7E2 in other tools | Weak GM/Torque method 3 lead; test only if `221940` fails |
| Shifter position rejected | `221951` | `7E0`/`7E8` | Rejected with `7F 22 31` in Park on live Enclave test |
| Current gear rejected | `22199A` | `7E0`/`7E8` | Rejected with `7F 22 31` in Park on live Enclave test |
| Current gear | `221B30` | Unknown / OBDb `DA18` | Structured OBDb Chevrolet lead; route not WiCAN-ready |
| TCC slip/VSS | `221991` | Unknown / OBDb `DA18` | Structured OBDb Chevrolet lead; route not WiCAN-ready |
| Filtered trans temp | `22295A` | Unknown / OBDb `DA18` | Structured OBDb Chevrolet lead; fallback research only |
| Knock retard | `2211A6` | `7E0`/`7E8` | RealDash scale found; byte mapping still uncertain |
| Enhanced runtime | `2211A1` | `7E0`/`7E8` | Prefer standard `011F` |
| Current misfire counters | `221200`, `221206`, `221205`, `221207`, `221208`, `2211EA`, `2211EB` | `7E0`/`7E8` | OBDb Traverse raw evidence; diagnostic only and longer-test scope |
| Injector duty cycle | `2212C3`, `2212C4` | `7E0`/`7E8` | OBDb Traverse raw evidence; validate behavior before any permanent sensor |
| Total knock retard | `2212D9` | `7E0`/`7E8` | OBDb Traverse raw evidence; diagnostic only |
| Cooling fan commands | `2213AF`, `223812` | `7E0`/`7E8` | OBDb Traverse raw evidence; longer warm-up or A/C validation |
| Oil pressure control solenoid raw | `223318` | `7E0`/`7E8` | OBDb Traverse raw evidence but formula is unclear |
| Calculated airflow | `2211AC` | `7E0`/`7E8` | Prefer standard `0110` |
| Accelerator pedal | `2212B4` | `7E0`/`7E8` | Prefer standard `015A` |
| BCM door DID rejected | `222122` | `241`/`641` | Rejected with `7F 22 31`; passive/low-speed capture is stronger |
| RFA/RCDLR route caution | `258`/`658` | candidate | TPMS probes caused `NO DATA`, timeouts, and AutoPID busy; do not retry without stronger evidence |
| Low-speed driver door | `0x10630000` | SW-CAN/low-speed | Requires bus/mode change and passive capture |
| Low-speed body set | `0x8020C000` etc. | SW-CAN/low-speed | Generic GM Global A body signals; not Enclave-confirmed |
