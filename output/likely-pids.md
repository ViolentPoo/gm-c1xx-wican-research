# Likely PIDs, DIDs, And Broadcast Signals

High-value standard PID tests:

| Name | Request | Confidence | Validation |
|---|---:|---|---|
| STFT Bank 1 | `0106` | Strongly likely | Supported bitmap, idle behavior |
| LTFT Bank 1 | `0107` | Strongly likely | Supported bitmap, plausible trim |
| MAP | `010B` | Strongly likely | KOEO near barometric, lower at idle |
| Timing advance | `010E` | Strongly likely | Plausible idle/load values |
| Barometric pressure | `0133` | Strongly likely | Compare local pressure |
| Relative accelerator position | `015A` | Possible | Pedal sweep |
| Engine oil temperature | `015C` | Possible | Warm-up behavior |
| Engine fuel rate | `015E` | Possible | Idle/load behavior |
| Driver demand torque | `0161` | Possible | Pedal/load behavior |
| Actual engine torque | `0162` | Possible | Load behavior |
| Engine reference torque | `0163` | Possible | Supported response |
| Transmission gear/ratio | `01A4` | Experimental | Response inspection and PRNDL comparison |

Strong passive CAN candidates:

| Name | CAN ID | Confidence | Source |
|---|---:|---|---|
| BCM door/belt status | `0x12A` | Strongly likely | OpenDBC GM Global A / C1XX-related GM data |
| BCM turn signals | `0x140` | Strongly likely | OpenDBC |
| BCM ignition/platform status | `0x1F1` | Strongly likely | OpenDBC GM Global A / C1XX fingerprints |
| Engine oil life remaining | `0x3F9` | Strongly likely | Public GM HS-CAN DBC |
| Transmission status/gear | `0x1F5` | Strongly likely | Public GM HS-CAN DBC/OpenDBC/independent GMLAN post |
| Engine fuel/oil status | `0x4D1` | Possible | Public GM HS-CAN DBC |

Likely enhanced DIDs:

| Name | Request | Confidence | Notes |
|---|---:|---|---|
| Transmission fluid temperature | `221940` | Strongly likely | OBDb Traverse raw evidence uses `7E2`/`7EA`; validate against warm-up/scan tool |
| Enhanced oil temperature | `221154` | Strongly likely | OBDb Traverse raw evidence uses `7E0`/`7E8`; compare standard `015C` if supported |
| Oil life | `1A6D` | Confirmed | Live Enclave response `5A6D57` matched dash `34%` using `B3*100/256` |
| Air filter life | `2236A7` | Confirmed | Live Enclave response byte `0x55` matched dash `85%` |
| Knock retard | `2211A6` | Possible | OBDb Traverse raw evidence confirms scale; low priority for display use |

Low-speed passive candidates for later SW-CAN work:

| Name | CAN ID | Confidence | Notes |
|---|---:|---|---|
| Window positions | `0x8064A000` | Possible | Generic GM Global A low-speed DBC |
| Rear closure ajar | `0x806AA000` | Possible | Generic GM Global A low-speed DBC |
| Power liftgate status | `0x805A0000` | Possible | Passive only; do not transmit controls |
| TPMS pressures | `0x803D4000` | Possible | kPaG scale 4 in low-speed DBC |
| Hood status | `0x80728000` | Possible | Generic GM Global A low-speed DBC |
| Lighting/brake/reverse status | `0x8020C000` | Possible | Useful for validation captures |
