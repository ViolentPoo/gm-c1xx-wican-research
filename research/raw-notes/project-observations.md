# Project Observations

- Vehicle: 2022 Buick Enclave Essence, C1XX, LGX V6, 9T65.
- WiCAN Pro firmware reports `4.50`; latest checked release tag was `v4.50p`.
- WiCAN currently uses `auto_pid`, webhook enabled, MQTT disabled.
- ECM route `7E0`/`7E8` is working.
- BCM route `241`/`641` was confirmed by `1A90` returning VIN prefix `5GAE`.
- Broad BCM scanning previously wedged WiCAN until reboot; avoid blind scans.
- Existing `01A6` odometer matches dash.
- Raw speed/fuel/voltage can be invalid while asleep.
- Existing `221155` oil life did not match dash and is untrusted.
