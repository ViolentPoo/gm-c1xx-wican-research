# Research Summary

This research package documents known, likely, and experimental OBD-II PIDs, GM enhanced DIDs, passive CAN messages, and module addresses for a 2022 Buick Enclave and related GM C1XX vehicles.

Tools used:

- Built-in OpenCode file/search tools
- `webfetch` for public URLs
- Subagent research pass over public OpenDBC and web-accessible sources
- Existing shell utilities available in the workspace

Tools installed:

- No new external packages were required for this first evidence package.
- General web search was limited by unauthenticated API/CAPTCHA blocks; this limitation is documented in `docs/sources.md`.

Most useful sources:

- WiCAN firmware repository and documentation links
- OpenDBC GM Global A/C1XX-supported vehicle files
- OpenDBC GM fingerprints and public routes for C1XX-related Acadia/Traverse vehicles
- OpenDBC generated GM powertrain DBC and expanded low-speed GM Global A DBC
- Public GM HS-CAN DBC
- RealDash GM LS OBD2 XML
- SimpleOBDII default GM user PID definitions
- Public forum threads for GM/Torque/ScanGauge PID formulas and headers
- GM service-info mirrors for door ajar, keyless-entry, TPMS, liftgate, GMLAN/LIN topology, and XT5/LGX/9T65 scan-tool parameter names
- SAE J1979 standard PID references
- Project-specific WiCAN test observations

Confirmed findings:

- The target vehicle is C1XX, not Lambda.
- ECM/PCM standard OBD route `7E0`/`7E8` works.
- BCM route `241`/`641` is confirmed by VIN response to `1A90`.
- Existing WiCAN standard PIDs for RPM, speed, fuel, voltage, fuel rate, and related basics are working with caveats for sleeping/off-state data.
- Existing `01A6` odometer is verified against the dash.
- `221940` transmission temperature and `221154` oil temperature are plausible/working existing WiCAN entries, but still benefit from independent scan-tool validation.
- `221155` oil life is untrusted/rejected for dashboard use because it did not match the dash oil-life value.
- Live Enclave testing on 2026-08-06 confirmed active oil life `1A6D` via `7E0`/`7E8`; response `7E8 03 5A 6D 57` decoded to `33.98%` and matched the dash value `34%`.
- Live Enclave testing confirmed air filter life `2236A7`; response `7E8 05 62 36 A7 55 10` matched the dash value `85%` using raw byte `0x55` as percent.
- Live Enclave testing confirmed `221940` responds on both `7E0`/`7E8` and `7E2`/`7EA` with close transmission-temperature values.
- Passive HS-CAN testing confirmed PRNDL/manual range on `0x1F5`; WiCAN filters use `PRNDL_RANGE_CODE = B3` and `PRNDL_MANUAL_FLAG = B5`. Observed values: Park `1/0`, Reverse `2/0`, Neutral `3/0`, Drive `4/0`, and manual L ranges use flag `2` with codes `12..4` for L1..L9.
- Passive HS-CAN testing confirmed park brake on `0x1F1`; WiCAN filter `PARK_BRAKE_SET = (B4&16)/16` exposes `1` when set and `0` when released.
- WiCAN passive CAN-filter webhook consumers can lag. In one test WiCAN direct `/autopid/test_can_filter` saw Park immediately while the downstream state changed from Drive to Park after about 3 minutes 30 seconds. Treat passive gear and park-brake values as current/last state for display/research, not low-latency automation triggers.

Strongly likely findings:

- Standard PIDs indicated by supported-PID bitmaps should be safe first additions.
- OpenDBC has explicit C1XX-related vehicle support for GMC Acadia and Chevrolet Traverse public routes/fingerprints, increasing confidence in reused GM Global A frames.
- OpenDBC GM Global A broadcasts including `0x12A BCMDoorBeltStatus` and `0x140 BCMTurnSignals` are strong passive-capture candidates for C1XX-related vehicles. `0x1F1 BCMGeneralPlatformStatus` park brake and `0x1F5 ECMPRDNL2` PRNDL are now Enclave-confirmed on HS-CAN.
- Independent GMLAN forum evidence also points to `0x1F5` carrying PRNDL/range values, strengthening passive gear validation.
- 2022 XT5 service-info mirrors for K20 ECM and K71 9T65 TCM confirm that C1XX/LGX/9T65 scan-tool data includes oil life remaining, measured/calculated oil pressure, measured/calculated oil temperature, transmission fluid temperature, current gear, gear command, TCC slip, ISS/OSS, and range sensor data. These pages do not provide raw DID IDs.
- GM bulletin `20-NA-136` directly covers 2018-2022 Enclave 9T65 applications and confirms scan-tool validation targets including TFT, ISS, OSS, command gear, TCC pressure command, and TCC slip speed. It does not provide raw DIDs.
- OBDb's 2023 Chevrolet Traverse raw test cases provide direct C1XX-sibling evidence for `7E2`/`7EA` `221940` transmission-fluid temperature with `A-40`, `7E0`/`7E8` `221154` engine-oil temperature with `A-40`, and `7E0`/`7E8` `2211A6` knock retard. These are still not Enclave-confirmed until live-tested.
- OBDb's Chevrolet Impala command database provides structured modern GM leads for `221470` oil pressure, `221940` TFT, `221B30` current gear, `221991` TCC slip/VSS, and `22295A` filtered TFT. Its `DA18` route syntax is not directly WiCAN-ready and is not Enclave-specific.
- K84 Keyless Entry Control Module service-info pages for C1XX-adjacent Acadia list scan-tool parameters for driver/passenger/rear door ajar/open state plus liftgate ajar/handle state. 2024 Enclave parts data shows the keyless-entry module family applies to 2019-2024 Enclave, increasing relevance of K84 as a body-alert target. These sources do not provide raw DIDs.
- K39 Liftgate Control Module service-info pages list liftgate latch pawl/ratchet/sector, handle switch, close switch, mode switch, object sensor, and open/closed learned state parameters. K39 connector evidence shows low-speed GMLAN serial data and rear-closure switch/status circuits.
- GM LIN bus bulletin PIT5698C applies to Enclave through 2022 and explains that door ajar can be hard-wired to a window motor, then sent by LIN to the BCM. This supports passive/module-level capture over blind BCM DID guessing for door/window status.
- Passive `0x3F9 Engine_General_Status_3` oil-life signal from public GM HS-CAN DBC is a high-value oil-life candidate.
- The 2022 Enclave owner manual and GM OLM bulletin `18-NA-125` confirm the DIC Remaining Oil Life value is the validation target; they do not expose a raw PID. Any oil-life candidate must match the DIC exactly before being trusted.

Experimental findings:

- `22119F` and `22119F01` rejected for oil life on this Enclave; use confirmed `1A6D` instead.
- `222122` as a possible BCM door-status DID.
- Oil pressure DIDs `22115C`, `221470`, `221C1B`, `222344`, and `222345` were implausible while running and are rejected for this route on the Enclave.
- Additional OBDb Traverse raw test cases expose longer-test ECM diagnostics including current misfire counters, injector duty cycle, total knock retard, fan commands, oil-pressure control solenoid command, and enhanced runtime. These are read-only service `22` candidates for staged diagnostics, not quick-test or alert priorities.
- RealDash-sourced shift/gear leads `221951` and `22199A`.
- `221949` as a weak GM/Torque fallback transmission-temperature candidate only if `221940` fails.
- OBDb-sourced `221B30`, `221991`, and `22295A` as route-unknown TCM research leads, not quick-test candidates.
- Knock retard/runtime/airflow/pedal DIDs `2211A6`, `2211A1`, `2211AC`, `2212B4`.
- RFA/RCDLR route `258`/`658` for TPMS-related research.
- Generic GM low-speed body leads for windows, liftgate, hood, TPMS, lighting, battery state, and RFA/key status. These require SW-CAN/low-speed passive capture and are not yet Enclave-confirmed.
- 2024 Enclave is considered same-generation/high-relevance evidence; 2025+ Enclave is redesigned and excluded unless explicitly labeled as non-comparable.

Major unknowns:

- Exact C1XX Enclave door/liftgate/window/lock/TPMS DIDs.
- Whether K84/K39 scan-tool parameters are exposed through a WiCAN-accessible diagnostic route, passive low-speed GMLAN frame, or only dealer scan-tool abstraction.
- Whether `0x12A` appears on the Enclave's currently configured HS-CAN bus.
- Whether oil pressure comes from `22115C`, `221470`, passive `0x4D1`, or none of those on this vehicle.
- Which diagnostic request/header exposes the K71 TCM scan-tool values, if any are available through WiCAN without broader probing.
- Exact WiCAN raw-capture workflow for this installed firmware/configuration.
- C1XX-specific passive liftgate/window/TPMS frames.
- Passive oil life `0x3F9` remains unconfirmed, but active oil life `1A6D` is confirmed.

Next action:

- When the vehicle is awake, first query supported-PID bitmaps and preserve `/load_auto_pid`.
- For body alerts, prioritize passive capture for `0x12A` and low-speed body frames before testing the experimental `222122` DID. `0x1F1` park brake and `0x1F5` PRNDL are confirmed and can be used as passive WiCAN filters with the timing caveat above.
