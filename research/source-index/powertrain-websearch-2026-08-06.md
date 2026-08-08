# Powertrain Websearch 2026-08-06

Scope:

- Target remains 2022 Buick Enclave LGX/9T65.
- Same-generation 2018-2024 Enclave evidence is high relevance.
- Related C1XX/9T65 vehicles are used when direct Enclave evidence is unavailable.

Key findings:

- GM bulletin `20-NA-136` directly covers 2018-2022 Enclave 9T65 and related C1XX 9T65 vehicles.
- `20-NA-136` confirms scan-tool validation targets: transmission fluid temperature, transmission ISS, transmission OSS, command gear, TCC pressure command, and TCC slip speed.
- The bulletin describes TCC slip expectations: below 100 RPM when applied and steady, with electronically controlled capacity clutch behavior allowing small slip around 20 RPM in some gears/applications.
- Public Torque/GM discussions continue to support `221940` as the primary GM transmission-fluid-temperature candidate with `A-40` style formulas and Auto or `7E2` headers.
- Some broad GM/Torque lists include `221949` as transmission-fluid-temperature method 3 with `(A-40)/0.75`. This is weaker than `221940` and is fallback-only.
- OBDb's Chevrolet Impala structured command database maps `221470` to oil pressure, `221940` to TFT, `221B30` to current gear/gear, `221991` to TCC slip/VSS, and `22295A` to filtered TFT. It uses `DA18` route syntax that is not directly WiCAN-ready.
- OBDb's Chevrolet Traverse 2023 raw command test cases are stronger C1XX-sibling evidence and use directly translatable routes:
- `7E2.7EA.221940` returns `7EA0462194040` decoded as 24 C and `7EA046219408E` decoded as 102 C, confirming `A-40` on the response byte.
- `7E0.7E8.221154` returns `7E80462115441` decoded as 25 C and `7E8046211548E` decoded as 102 C, confirming `A-40` on the response byte.
- `7E0.7E8.221C1B` returns `7E804621C1B00` decoded as `CHEVROLET_EOP_CALC` 0.
- `7E0.7E8.222344` returns `7E80462234400` decoded as `CHEVROLET_EOP_ABS` 0.
- `7E0.7E8.222345` returns `7E80462234500` decoded as `CHEVROLET_EOP` 0.
- `7E0.7E8.2211A6` returns `7E8046211A600` decoded as 0 degrees and `7E8046211A647` decoded as 15.62 degrees.
- Additional Traverse-supported raw pulls for extended testing include current misfire counters `221200`, `221206`, `221205`, `221207`, `221208`, `2211EA`, `2211EB`; injector duty `2212C3` and `2212C4`; total knock retard `2212D9`; cooling-fan commands `2213AF` and `223812`; oil-pressure control solenoid raw `223318`; and enhanced runtime `2211A1`.
- The 2022 Enclave owner manual confirms the DIC Remaining Oil Life display/reset workflow, and GM bulletin `18-NA-125` explains OLM calculation pathways. Neither source publishes a raw oil-life PID.

Interpretation:

- Do not add `221949` to the quick 5-10 minute test by default.
- Keep `221940` as the primary test because it already exists in the project and has stronger public evidence.
- Prefer a one-off `7E2`/`7EA` route for `221940` during live testing because the Traverse raw case uses that TCM-style route. If the existing WiCAN `7E0`/`7E8` entry also responds, record both.
- Use `221949` only after a clean negative or implausible result from `221940`, and validate against cold-start/warm-up behavior.
- Add `221C1B`, `222344`, and `222345` as low-cost one-off oil-pressure candidates after `22115C`/`221470`, but do not trust them without engine-off/running behavior and a formula/scan-tool comparison.
- Keep the extra Traverse ECM diagnostics in a longer test tier. They are useful for raw response validation and diagnostics, but they are not quick-run priorities and should not become alert signals without repeated validation.
- Treat `221B30`, `221991`, and `22295A` as follow-up research leads only after the route/header mapping is understood.
- Treat the DIC Remaining Oil Life value as the authority for oil-life validation. Reject any candidate that does not match it exactly.
- No WiCAN-ready public raw DID was found for TCC slip, ISS, OSS, or command gear on the Enclave/9T65.

Limitations:

- Service bulletins and service-info pages confirm scan-tool parameters but do not publish raw WiCAN request headers or UDS DIDs.
- Broader GM/Torque PID lists often span older platforms and should not be treated as direct Enclave support.
