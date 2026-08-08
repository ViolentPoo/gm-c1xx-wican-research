# OpenDBC Source Index

Files inspected:

- `opendbc/car/gm/values.py`
- `opendbc/car/gm/fingerprints.py`
- `opendbc/car/tests/routes.py`
- `opendbc/dbc/generator/gm/gm_global_a_powertrain.dbc`
- `gm_global_a_lowspeed.dbc`
- `cadillac_ct6_powertrain.dbc`
- `gm_global_a_lowspeed_1818125.dbc`
- OpenDBC repository tree and GM C1XX support references through subagent research

C1XX-related vehicle evidence:

- `GMC_ACADIA` appears in GM platform values and fingerprints.
- `CHEVROLET_TRAVERSE` appears in GM platform values and fingerprints.
- Public routes include `7cc2a8365b4dd8a9/2018-12-02--12-10-44` for `GM.GMC_ACADIA` and `a40976dc9f28ba62/0000001f--160e210119` for `GM.CHEVROLET_TRAVERSE`.

Important extracted signals:

- `0x12A BCMDoorBeltStatus`
- `0x140 BCMTurnSignals`
- `0x1F1 BCMGeneralPlatformStatus`
- `0x1F5 ECMPRDNL2`
- `0x10630000 DriverDoorStatus`
- Generic low-speed body, lighting, hood, RFA, TPMS, remote-start, battery, and oil-life leads from `gm_global_a_lowspeed_1818125.dbc`

Limitations:

- CT6 is not C1XX, so CT6-only frames are same-era GM leads, not direct confirmation.
- Openpilot support for C1XX Acadia/Traverse increases confidence in GM Global A frame reuse, but vehicle-local passive capture is still required.
