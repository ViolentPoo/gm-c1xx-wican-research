# Sources

Access date: 2026-08-05.

Additional websearch pass: 2026-08-06.

Primary sources used:

- WiCAN firmware repository: `https://github.com/meatpiHQ/wican-fw`
- WiCAN firmware releases: `https://github.com/meatpiHQ/wican-fw/releases`
- WiCAN documentation link from repository: `https://meatpihq.github.io/wican-fw/`
- MeatPi programming examples link from repository: `https://github.com/meatpiHQ/programming_examples/tree/master/CAN`
- OpenDBC repository tree: `https://github.com/commaai/opendbc`
- OpenDBC GM values: `https://github.com/commaai/opendbc/blob/master/opendbc/car/gm/values.py`
- OpenDBC GM fingerprints: `https://github.com/commaai/opendbc/blob/master/opendbc/car/gm/fingerprints.py`
- OpenDBC routes: `https://github.com/commaai/opendbc/blob/master/opendbc/car/tests/routes.py`
- OpenDBC generated GM powertrain DBC: `https://github.com/commaai/opendbc/blob/master/opendbc/dbc/generator/gm/gm_global_a_powertrain.dbc`
- OpenDBC GM low-speed DBC: `https://raw.githubusercontent.com/commaai/opendbc/master/opendbc/dbc/gm_global_a_lowspeed.dbc`
- OpenDBC Cadillac CT6 powertrain DBC: `https://raw.githubusercontent.com/commaai/opendbc/master/opendbc/dbc/cadillac_ct6_powertrain.dbc`
- OpenDBC GM Global A low-speed expanded DBC: `https://raw.githubusercontent.com/commaai/opendbc/master/opendbc/dbc/gm_global_a_lowspeed_1818125.dbc`
- Public GM HS-CAN DBC: `https://raw.githubusercontent.com/pddenhar/gm_dbc/master/GM%20HS-CAN.dbc`
- RealDash GM LS profile: `https://raw.githubusercontent.com/janimm/RealDash-extras/master/OBD2/realdash_obd2_gm_ls.xml`
- SimpleOBDII default user PIDs: `https://raw.githubusercontent.com/MOtterbine/SimpleOBDII/master/SimpleOBDII/ViewModels/UserPIDSViewModel.cs`
- Harry's GPS Suite GM PID thread: `https://forum.gps-laptimer.de/viewtopic.php?t=2292`
- GMTNation Torque App thread: `https://gmtnation.com/forums/threads/torque-app.4761/`
- Traverse Forum transmission-temperature thread: `https://www.traverseforum.com/threads/obdii-transmission-temp.4033/`
- GMTNation oil-life PID thread: `https://gmtnation.com/forums/threads/2008-envoy-sle-oil-life-monitor-pid.14559/`
- Torque ScanGauge OLM thread: `https://torque-bhp.com/community/main-forum/scangauge-2-pid-input-for-olm/`
- Torque GM oil-pressure thread: `https://torque-bhp.com/community/main-forum/gm-oil-pressure-in-versoin-1-10-258/`
- HP Tuners GMLAN PRNDL thread: `https://forum.hptuners.com/showthread.php?77170-GM-PID-s-for-Gear-Indicate-P-N-R=`
- GM service-info mirrors for door ajar, GMLAN topology, and liftgate module wiring.
- LEMON Manuals 2022 XT5 K20 ECM and K71 9T65 TCM scan-tool information pages.
- GM 9T65 diagnostic bulletin `20-NA-136` from NHTSA service-bulletin mirror.
- OBDb Chevrolet Impala structured command database commit with modern GM enhanced command mappings.
- OBDb Chevrolet Traverse raw 2023 command test cases for C1XX-sibling `7E2`/`7EA` `221940` and `7E0`/`7E8` `221154`, `221C1B`, `222344`, `222345`, and `2211A6`.
- 2022 Enclave owner manual oil-life page and GM `18-NA-125` OLM operation bulletin.
- GM PIT5698C LIN Bus Diagnostic Information covering 2013-2022 Enclave and related GM vehicles.
- LEMON Manuals C1XX-adjacent K84 Keyless Entry Control Module scan-tool and connector pages.
- LEMON Manuals/Mitchell-style C1XX-adjacent K39 Liftgate Control Module scan-tool and connector pages.
- 2024 Enclave parts listings showing same-generation keyless-entry module fitment.
- Tire Review GM TPMS service article: `https://www.tirereview.com/servicing-gm-tpms/`
- SAE J1979 standard PID summaries, including `https://en.wikipedia.org/wiki/OBD-II_PIDs`
- Project-specific WiCAN observations from this workspace conversation.

Search limitations encountered:

- GitHub code search API returned unauthenticated `401` responses.
- Google challenged automated search. DuckDuckGo HTML/lite and native `websearch` worked after opencode config was corrected, but searches must be rate-limited to avoid provider `429` responses.
- No private forum, commercial scan-tool, HP Tuners, EFILive, Torque Pro, or Car Scanner proprietary database access was used.

Source-quality notes:

- OpenDBC is credible for broadcast CAN signals used by openpilot-supported GM vehicles, including C1XX Acadia/Traverse entries, but a signal is still not confirmed for this exact Enclave until observed.
- OpenDBC Acadia/Traverse support and routes are C1XX-adjacent evidence, not proof that every signal is present on the Enclave's OBD-accessible HS-CAN bus.
- RealDash and SimpleOBDII provide useful public GM enhanced-PID leads, but their equations and headers must be translated to WiCAN response-byte conventions and validated against dash/scan-tool behavior.
- Forum posts are useful for candidate formulas and headers, but many are older GM platforms. They increase test priority; they do not confirm Enclave/C1XX behavior.
- Broad GM forum/Torque candidates such as `221949` are fallback-only unless confirmed by Enclave raw response and behavior.
- OBDb command mappings are useful because they are structured and test-backed for modern Chevrolet models. Traverse commands listed as `7E0.7E8.x` or `7E2.7EA.x` are directly translatable to WiCAN one-off header/filter/request tests; Impala `DA` route syntax must still be understood before translating to WiCAN.
- Owner-manual and OLM-operation sources define validation targets, not PID identifiers.
- Service-info scan-tool pages confirm that parameters exist and give expected behavior/ranges, but they do not identify WiCAN request headers or UDS DIDs.
- 2024 Buick Enclave evidence is treated as high relevance because it is still second-generation C1XX. 2025+ Enclave evidence is excluded by default because of the redesign.
- AI-generated search summaries are not used as evidence. The `222122` BCM door DID remains an experimental lead only.
- Forum/PID-list style enhanced GM DIDs are treated as possible or experimental unless validated by a real response and behavior.
