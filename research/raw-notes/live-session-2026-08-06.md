# Live WiCAN Session 2026-08-06

Vehicle: 2022 Buick Enclave, parked, started then later shut off by user.

WiCAN: reachable before testing. `/load_auto_pid` was saved before testing. WiCAN initially showed 500K CAN bitrate and Silent mode in the status page, but `/autopid/test_pid` active one-off requests worked.

## Confirmed

- RPM sanity: `010C` returned `7E8 04 41 0C 0C A0`, decoded `808 rpm`; after WiCAN reboot returned `708.5 rpm`.
- Voltage: `0142` returned `7E8 04 41 42 34 BA` and `7EA 04 41 42 34 C9`, decoded about `13.5 V`; user reported `13.8 V` then `13.4 V` on dash.
- Odometer: `01A6` returned `7E8 06 41 A6 00 0E A4 0C`, decoded `59620.55 mi` with existing formula.
- Barometric pressure: `0133` returned `101 kPa`.
- STFT/LTFT bank 1: `0106` returned `1.56%`; `0107` returned `-3.91%`.
- Timing advance: `010E` returned `13 degrees`.
- Actual/reference torque: `0162` returned `19%`; `0163` returned `322 Nm`.
- Transmission temperature `221940`: `7E0/7E8` returned `7E8 04 62 19 40 46`, decoded `86 F`; `7E2/7EA` returned `7EA 04 62 19 40 47`, decoded `87.8 F`.
- Enhanced oil temperature `221154`: returned `7E8 04 62 11 54 4C`, decoded `96.8 F`.
- Oil life `1A6D`: returned `7E8 03 5A 6D 57`, decoded `33.98%`; user confirmed dash oil life `34%`.
- Air filter life `2236A7`: returned `7E8 05 62 36 A7 55 10`; raw `0x55` = `85`, matching user-reported dash air filter life `85%`.
- Passive PRNDL/range `0x1F5`: confirmed on HS-CAN. Captures included Park `F0 F0 00 01 00 00 08 00`, Reverse `E0 E0 00 02 00 00 0A 00`, Neutral `D0 D0 00 03 00 00 08 00`, Drive `01 01 00 04 00 00 09 00`, and L1-L9 using byte 3 values `0C..04` with byte 5 `02`. WiCAN filters use `PRNDL_RANGE_CODE = B3` and `PRNDL_MANUAL_FLAG = B5`.
- Passive park brake `0x1F1`: confirmed on HS-CAN. ON baseline `A2 12 00 00 18 00 40 7A`; OFF `A2 12 00 00 08 00 40 7A`. WiCAN filter uses `PARK_BRAKE_SET = (B4&16)/16`.
- Extended diagnostics: cylinders 2-6 misfire counters returned zero, injector duty `2212C3`/`2212C4` returned `1.52%`, total knock retard `2212D9` returned zero, fan commands `2213AF`/`223812` returned about `20%`, and oil-pressure control solenoid raw `223318` returned `0x11`.

## Rejected Or Not Useful From This Session

- Standard PIDs `015C`, `015E`, `01A4`, `015A`, `010B`, and `0161` returned `NO DATA`.
- Oil life `22119F` returned `7E8 03 7F 22 31`.
- Oil life `22119F01` returned `7E8 03 7F 22 12`.
- Oil pressure candidates `22115C`, `221470`, `221C1B`, `222344`, and `222345` returned zero or implausible running values; do not use them for oil pressure.
- Gear candidates `221951` and `22199A` returned `7E8 03 7F 22 31` in Park.
- BCM door candidate `222122` on confirmed route `241/641` returned `641 03 7F 22 31`.
- ECM TPMS candidates `22248E`, `22248F`, `222490`, `222491`, `22C901`, and `22C902` returned `7F 22 31` on `7E0/7E8`.
- RFA route `258/658` TPMS attempts produced `NO DATA`, timeouts, and `AutoPID busy`; stop using this route until stronger evidence exists.

## Operational Notes

- Passive CAN filter tests through `/autopid/test_can_filter` returned `No frame`/`STOPPED` for `0x3F9`, `0x1F5`, `0x12A`, `0x1F1`, `0x4D1`, and `0x4C9`. Treat this as endpoint/tooling inconclusive, not proof that frames are absent.
- Later testing confirmed `/autopid/test_can_filter` can intermittently see `0x1F5` and evaluate the same B-byte expressions used by configured CAN filters. A direct WiCAN test saw Park immediately with raw `1F5 0F 0F 00 01 00 00 08 00` and `B3=1`, while the downstream webhook consumer still showed Drive for about 3 minutes 30 seconds before updating. WiCAN `/api/webhook` remained healthy with interval `15` seconds during this test.
- WiCAN AutoPID top-level `can_filters` schema is confirmed: each filter uses `{"frame_id": number, "parameters": [{"name", "expression", "unit", "class", "period", "min", "max", "type", "send_to", "enabled"}]}` and is saved through `/store_auto_data`; reboot is required for the new filters to take effect.
- RFA-route TPMS attempts wedged the AutoPID test endpoint busy. WiCAN recovered after `POST /system_reboot` with body `reboot`.
- User also reported TPMS dash values: LF `33 psi`, RF `34 psi`, LR `34 psi`, RR `34 psi`; and compass heading `North`. No validated PID/DID found for either in this session.
