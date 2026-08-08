# WiCAN Configuration Guide

Current known WiCAN state from this project:

- Model: WiCAN Pro / WiCAN-OBD-PRO
- Firmware reported by device: `4.50`
- Latest checked WiCAN Pro release: `WiCAN-PRO v4.50`, tag `v4.50p`
- CAN bitrate: 500K
- CAN mode: normal
- Protocol: auto_pid
- MQTT: disabled
- Webhook: enabled
- Sleep enabled, `sleep_volt: 12.8`, `sleep_time: 5`
- Webhook post interval observed through `/api/webhook`: `15` seconds

Important endpoints:

- `/load_config`
- `/load_auto_pid`
- `/store_auto_data`
- `/autopid/test_pid`
- `/autopid/test_can_filter`
- `/api/webhook`
- `/system_reboot`

Working approach:

1. Load `/load_auto_pid` before editing.
2. Preserve existing entries.
3. Add small batches only.
4. Use known-good `010C` RPM as the awake sanity check.
5. If `010C` returns no data, stop PID testing because the vehicle/modules are asleep.
6. Restart/reboot only when needed.

WiCAN formula caution:

- Internet formulas often use `A`, `B`, `C`, `D` for OBD payload bytes.
- Existing WiCAN custom DID formulas in this project use `B3`, `B4`, or ranges such as `[B3:B6]`.
- Validate response layout before converting formulas.

Passive capture:

- WiCAN Pro documentation indicates support for RealDash CAN protocol, slcan/SocketCAN, TCP/UDP, SD card logging, multiple buses, GM HS J1962 pins 12/13, MS-CAN pins 3/11, and SW-CAN/GMLAN pin 1.
- Passive capture may require temporarily leaving the current `auto_pid` + webhook mode.
- Save the current config before switching modes.

Confirmed passive CAN filters for this Enclave:

- `0x1F5` PRNDL/range:
  - `PRNDL_RANGE_CODE`: expression `B3`, period `1000`, range `1..12`.
  - `PRNDL_MANUAL_FLAG`: expression `B5`, period `1000`, range `0..2`.
  - Observed mapping: Park `1/0`, Reverse `2/0`, Neutral `3/0`, Drive `4/0`, L1 `12/2`, L2 `11/2`, L3 `10/2`, L4 `9/2`, L5 `8/2`, L6 `7/2`, L7 `6/2`, L8 `5/2`, L9 `4/2`.
- `0x1F1` park brake:
  - `PARK_BRAKE_SET`: expression `(B4&16)/16`, period `1000`, `1` set and `0` released.

Passive CAN-filter timing caveat:

- WiCAN direct `/autopid/test_can_filter` can see confirmed frames immediately, but downstream webhook state can lag for passive CAN-filter values. A Park update was observed taking about 3 minutes 30 seconds even though `/api/webhook` showed successful 15-second posts. Use these values for display state and research, not immediate-response automations.
