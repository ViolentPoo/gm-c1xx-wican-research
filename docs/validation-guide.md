# Validation Guide

Validate every sensor against expected physical behavior before using it for alerts.

Coolant temperature:

- Cold engine should be close to ambient temperature.
- Warm engine should rise smoothly into normal range.
- Implausible jumps indicate bad byte mapping or stale data.

Transmission temperature:

- Cold start should be near ambient.
- Temperature should rise more slowly than coolant.
- Existing candidate `221940` should be compared against any scan tool value if possible.

Oil temperature:

- Test standard `015C` first.
- Enhanced `221154` should be used only if it tracks realistic warm-up behavior.

Oil life:

- Compare against the dashboard oil-life display.
- Existing `221155` mapping is rejected/untrusted because it did not match the dash.
- Test `22119F`, `22119F01`, and passive `0x3F9` only while the vehicle is awake.
- If dash shows 34%, raw byte for `raw * 100 / 255` should be near `0x56` or `0x57`.

Fuel level:

- Use guarded/last-known-good derived values for parked state.
- Raw standard `012F`/`2F` can drop to invalid zero while modules sleep.
- Validate against the dash gauge and refill events.

Odometer:

- Compare `01A6` against cluster mileage.
- Existing `ODOMETER_MI` is verified as matching dash in this project.

Vehicle speed:

- Validate only while awake/running.
- Raw off-state values such as 255 km/h / 158 mph are invalid and must be guarded.

Torque and gear:

- `0161`, `0162`, `0163`, and `01A4` require supported-PID confirmation.
- Gear/PRNDL should match selected range at rest and behavior while driving only after stationary validation.

Door states:

- Open one door at a time.
- Record all-closed, driver, passenger, left rear, right rear, and liftgate states.
- Confirm bit changes repeat after closing/reopening.
- Do not enable alerts until all bits are mapped.

TPMS:

- Compare each tire pressure against the cluster TPMS screen.
- Verify tire location mapping after a pressure difference is visible.

Battery/voltage:

- Guard raw module voltage while vehicle is off.
- Running voltage should usually be in the normal charging range.
