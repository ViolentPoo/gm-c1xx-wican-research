# WiCAN Vehicle Research Safety

This project is limited to passive monitoring and read-only diagnostics for a 2022 Buick Enclave and related GM C1XX vehicles.

Allowed diagnostic services for normal testing:

- `01` standard OBD-II current data
- `09` standard vehicle information
- `22` UDS/GM enhanced ReadDataByIdentifier

Do not test commands that can control actuators, change configuration, clear data, unlock security access, enter programming mode, or affect vehicle operation.

Off-limits unless explicitly requested with a separate safety review:

- `04` clear emissions DTCs
- `10` diagnostic session control beyond default read access
- `11` ECU reset
- `14` clear diagnostic information
- `27` security access
- `2E` write data by identifier
- `2F` input/output control
- `31` routine control
- Any lock, unlock, liftgate, window, brake, steering, throttle, shift, remote-start, or firmware programming request

Testing rules:

- Keep the vehicle parked.
- Apply the parking brake.
- Do not test while driving.
- Use conservative polling intervals.
- Stop testing a DID that repeatedly returns errors.
- Treat all body/TPMS/window/liftgate claims as unverified until validated on the vehicle.
- Prefer passive capture before unknown module probing.
