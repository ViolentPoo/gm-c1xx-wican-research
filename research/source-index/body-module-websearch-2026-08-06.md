# Body Module Websearch 2026-08-06

Scope:

- Target remains 2022 Buick Enclave.
- 2018-2024 Buick Enclave is treated as same-generation C1XX evidence.
- 2025+ Buick Enclave is excluded by default because it is redesigned.
- C1XX relatives are used when direct Enclave data is unavailable: Traverse, Acadia, XT5, XT6.

Key findings:

- No public raw DID was found for Enclave door, liftgate, window, lock, or TPMS status.
- GM PIT5698C applies to 2013-2022 Enclave and explains that LIN buses are not wired directly to the DLC. It specifically says a driver door ajar switch can be hard-wired to the driver window motor, then sent by LIN to the BCM, which wakes modules and broadcasts door-open state.
- C1XX-adjacent K84 Keyless Entry Control Module scan-tool data lists driver door ajar/open/unlock, passenger door ajar/open, left/right rear door ajar, liftgate ajar, liftgate handle, and exterior door handle parameters.
- K84 connector evidence shows low-speed GMLAN serial data plus driver/passenger/rear door handle and passive-entry antenna circuits.
- 2024 Enclave parts evidence shows the keyless-entry module family applies to 2019-2024 Enclave, supporting 2024 Enclave as high-relevance same-generation evidence.
- C1XX-adjacent K39 Liftgate Control Module scan-tool data lists liftgate latch pawl/ratchet/sector, handle switch, rear close switch, mode switch, object sensor, open/closed learned state, and liftgate open/close command state.
- K39 connector evidence shows low-speed GMLAN serial data plus rear-closure latch/status/handle/switch circuits.
- Enclave/Traverse bulletins for door-lock faults and water intrusion reinforce that door/lock issues are BCM/K84/body-harness concerns, but they still do not provide read-only DIDs.

Interpretation:

- For body-state research, the best evidence path remains passive capture or targeted module-level diagnostics, not broad BCM DID scanning.
- `0x12A` remains the first HS-CAN passive door/belt candidate.
- If low-speed capture is available, K84/K39-related low-speed GMLAN traffic is now the best body-alert research target.
- `222122` remains experimental and weaker than the K84/K39/passive evidence.

Limitations:

- Scan-tool parameter names do not prove WiCAN-accessible request headers or UDS DIDs.
- The K84/K39 pages are C1XX-adjacent, not directly 2022 Enclave service pages.
- Door/window/liftgate LIN details may be abstracted by BCM/K84/K39 before appearing on GMLAN.
