# Websearch Pass 2026-08-06

Native `websearch` became available during the research pass.

Search approach:

- Searched exact Enclave/C1XX terms first.
- Broadened to related C1XX vehicles: Chevrolet Traverse, GMC Acadia, Cadillac XT5, Cadillac XT6.
- Broadened again to public GM enhanced PID/Torque/ScanGauge/RealDash references.
- Avoided using AI summaries as source evidence; used result pages, forum text, DBCs, or source snippets with concrete IDs/formulas.

Key findings:

- Direct Enclave-specific PID tables were not found publicly.
- Traverse forum evidence indicates transmission temperature is available to capable scan tools on Traverse and that Torque GM PID sets worked on at least one 2013 Traverse, but this is pre-C1XX and not direct Enclave confirmation.
- `221940` has repeated public GM/Torque evidence with equation `A-40`, using either `Auto` or `7E2` header. Other threads also report vehicle-dependent failures, so Enclave `7E0` behavior remains project-specific until retested.
- `221154` has public GM/Torque evidence with equation `A-40` for oil temperature.
- `22115C` has repeated public oil-pressure formula evidence: `(A*0.65)-17.5` psi. This now deserves a one-off test alongside `221470`.
- `22119F` and `22119F01` are supported by Torque/ScanGauge oil-life discussions, but vehicle support varies and `221155` remains rejected from project observation.
- `22199A` has public GM current-gear discussion but may need correct byte selection from multi-line responses.
- `0x1F5` passive PRNDL evidence was strengthened by an independent HP Tuners/GMLAN forum post in addition to OpenDBC/public DBC sources.
- Public service-info mirrors support BCM/DDM/PDM door ajar scan-tool parameters, BCM gateway behavior, low-speed GMLAN body modules, K39 liftgate module on low-speed GMLAN, and TPMS receiver/BCM/DIC data flow. They did not reveal a confirmed C1XX door/liftgate/window/TPMS DID.
- 2022 XT5 K20 ECM and K71 TCM service-info pages confirm C1XX/LGX/9T65 scan-tool parameters for oil life, oil pressure, oil temperature, transmission fluid temperature, current gear, gear command, TCC slip, ISS/OSS, and transmission range data. They do not publish raw diagnostic IDs.

Limitations:

- Parallel native `websearch` calls can return provider `429`; use sequential/rate-limited queries.
- Google still challenges automated search.
- Some forum pages are only available via websearch excerpts or JavaScript-rendered access; prefer direct page text when available.
- Older GM platform PID evidence increases test priority but does not confirm C1XX/2022 Enclave support.
- Service-info parameter names are validation targets only unless matched to a raw WiCAN response.
