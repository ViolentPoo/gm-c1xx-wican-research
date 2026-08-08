# Confirmed And Existing Items

Confirmed on this project or through standard behavior plus observed working WiCAN entities:

| Item | Request/ID | Status | Notes |
|---|---:|---|---|
| ECM physical route | `7E0` -> `7E8` | Confirmed | Existing standard and enhanced WiCAN polling works |
| Functional OBD route | `7DF` -> `7E8` | Confirmed | Use for supported-PID bitmaps |
| BCM route | `241` -> `641` | Confirmed | `1A90` returned VIN prefix `5GAE` |
| Engine RPM | `010C` | Existing | Use as awake sanity check |
| Vehicle speed | `010D` | Existing | Guard off-state invalid values |
| Fuel tank level | `012F`/WiCAN `2F` | Existing | Guard zero/off-state values |
| Control module voltage | `0142`/WiCAN `42` | Existing | Guard off-state invalid values |
| Engine coolant temp | `0105` | Existing | Current WiCAN converts to Fahrenheit |
| Intake air temp | `010F` | Existing | Current WiCAN converts to Fahrenheit |
| MAF | `0110` | Existing | Standard PID |
| Throttle position | `0111` | Existing | Standard PID |
| Engine runtime | `011F` | Existing | Standard PID |
| Odometer | `01A6` | Verified | Existing expression matches dash |

Rejected from confirmed use:

| Item | Request | Reason |
|---|---:|---|
| Oil life candidate | `221155` | Returned data but did not match dash oil-life percentage |
