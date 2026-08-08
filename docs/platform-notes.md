# Platform Notes

Primary vehicle:

- 2022 Buick Enclave Essence
- GM C1XX platform
- 3.6L LGX V6
- 9T65 nine-speed automatic transmission
- WiCAN Pro / WiCAN-OBD-PRO

Closest research relatives:

- 2018-2024 Buick Enclave, second generation C1XX. The 2022 Enclave remains the target vehicle; 2024 Enclave evidence is high relevance because it is pre-redesign.
- 2018-2023 Chevrolet Traverse, C1XX
- 2017-2023 GMC Acadia, C1XX
- 2017-2023 Cadillac XT5, C1XX
- 2020-2023 Cadillac XT6, C1XX
- 2025 and newer Buick Enclave is redesigned and should not be mixed into this dataset unless explicitly labeled non-comparable.

OpenDBC C1XX-adjacent public support observed:

- `GM.GMC_ACADIA` public test route `7cc2a8365b4dd8a9/2018-12-02--12-10-44`
- `GM.CHEVROLET_TRAVERSE` public test route `a40976dc9f28ba62/0000001f--160e210119`
- Fingerprints include C1XX-related Acadia/Traverse CAN IDs such as `0x12A`, `0x140`, `0x1F1`, and `0x1F5`.

Lower-priority legacy leads:

- First-generation Buick Enclave
- First-generation Chevrolet Traverse
- First-generation GMC Acadia
- Saturn Outlook

Legacy Lambda findings can suggest reused GM DIDs or formulas, but they are not treated as confirmed for the 2022 Enclave.

Evidence classification used in this package:

- Confirmed: observed on this project, standard OBD support concept, or directly supported by credible source and matching vehicle/family.
- Strongly likely: confirmed on closely related C1XX/GM Global A source or same LGX/9T65 system.
- Possible: credible GM source or repeated enhanced-PID list, but not vehicle-specific.
- Experimental: weak source, uncertain equation, uncertain module, or unresolved conflict.
- Rejected/incorrect: disproven by testing or incompatible source.
