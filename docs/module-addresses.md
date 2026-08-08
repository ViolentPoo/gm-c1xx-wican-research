# Module Address Research

Confirmed on this 2022 Enclave project:

| Module | Request ID | Response ID | Bus | CAN Speed | Evidence | Confidence |
|---|---:|---:|---|---:|---|---|
| ECM/PCM standard OBD | `7E0` physical or `7DF` functional | `7E8` | HS-CAN/OBD | 500K | Existing working standard/enhanced WiCAN PIDs | Confirmed |
| BCM diagnostic route | `241` | `641` | GM diagnostic route via WiCAN | Unknown | `ATSH241;ATCRA641;` + `1A90` returned VIN prefix `5GAE` | Confirmed |

Likely or candidate routes:

| Module | Request ID | Response ID | Bus | CAN Speed | Evidence | Confidence |
|---|---:|---:|---|---:|---|---|
| RFA/RCDLR/TPMS candidate | `258` | `658` | Body/RFA candidate | Unknown | Public GM convention/project note, not verified | Experimental |
| TCM | unknown | unknown | HS-CAN/OBD | 500K | Transmission data may be exposed through ECM/gateway or passive frames | Possible |
| EBCM/ABS | unknown | unknown | HS-CAN | 500K | OpenDBC broadcasts wheel speed/brake signals on GM Global A | Strongly likely for passive only |
| K9 BCM passive broadcast | no request | no response | HS-CAN | 500K candidate | OpenDBC `BCMDoorBeltStatus` and `BCMTurnSignals` | Strongly likely for C1XX-related testing |
| K84 Keyless Entry Control Module | unknown | unknown | Low-speed GMLAN/module diagnostic | varies | C1XX-adjacent service-info scan-tool parameters include door ajar/open and liftgate ajar/handle; 2024 Enclave parts data shows K84 family on 2019-2024 Enclave | Strongly likely as body-alert module target; route unknown |
| K39 Liftgate Control Module | unknown | unknown | Low-speed GMLAN/module diagnostic | varies | C1XX-adjacent service-info scan-tool parameters and connector evidence include liftgate latch/switch/status and low-speed GMLAN | Strongly likely as liftgate module target; route unknown |
| Low-speed/SW-CAN GMLAN | no request | no response | SW-CAN/low-speed | varies | OpenDBC `gm_global_a_lowspeed.dbc`; WiCAN Pro supports SW-CAN pin 1 | Possible |

Notes:

- Do not assume every GM module uses the same request/response offset.
- Negative response from one module only proves that module does not support the DID under the current conditions.
- Body, TPMS, liftgate, windows, and locks may require passive capture or a different bus rather than ECM `7E0` polling.
- K84/K39 scan-tool parameter names are validation targets. They are not confirmed WiCAN request headers or DIDs.
