# Cross-Border Data Transfer Inventory
**Owner:** Privacy Officer
**Last Updated:** April 2026
**Review Cycle:** Semi-annual (next review: October 2026)

---

## Active Transfer Arrangements

| Jurisdiction | Transfer Mechanism | Agreement Reference | Data Categories | Established | Last Reviewed |
|---|---|---|---|---|---|
| European Union | Adequacy Decision (EU→CA) | OPC Adequacy Register — EU | Customer PII, transaction data | 2021-03-01 | 2026-01-15 |
| United Kingdom | Contractual Clauses (UK IDTA) | IDTA-2024-UK-001 | Customer PII, analytics | 2024-02-28 | 2026-01-15 |
| Switzerland | Adequacy Decision (FADP) | OPC Adequacy Register — CH | Customer PII | 2022-09-01 | 2026-01-15 |
| United States | Contractual Clauses (PIPEDA SCC) | SCC-2022-US-001 | Customer PII, support data | 2022-06-15 | 2025-06-10 |
| India | Contractual Clauses (PIPEDA SCC) | SCC-2023-IN-001 | Engineering development data (limited) | 2023-03-10 | 2025-03-08 |

---

## Transfer Mechanisms Summary

### European Union
**Mechanism:** EU adequacy decision recognizing Canada under GDPR (Commission Decision 2001/497/EC, reaffirmed post-Schrems II). Reciprocal — OPC accepts EU as adequate under PIPEDA.
**Status:** Active. No SCCs required.

### United Kingdom
**Mechanism:** UK International Data Transfer Agreement (IDTA) executed with UK entity. Required post-Brexit as the EU adequacy decision does not automatically extend to the UK.
**Agreement expires:** February 28, 2027. Renewal required.

### Switzerland
**Mechanism:** FADP (Federal Act on Data Protection) adequacy recognized. Switzerland is on the OPC's list of adequate jurisdictions.
**Status:** Active. No SCCs required.

### United States
**Mechanism:** PIPEDA-compliant SCCs executed with three US-based sub-processors (AWS, Salesforce, Zendesk).
**Note:** US does not have adequacy status under PIPEDA. SCCs are required for each sub-processor relationship.
**Last SCC update:** 2022. Review recommended to ensure current data flows are covered.

### India
**Mechanism:** SCCs executed for limited development data (no PII beyond employee email addresses and support ticket metadata).
**Scope:** Narrow — engineering team collaboration tools only.

---

## Planned / Pending Transfers

| Jurisdiction | Purpose | Status | Mechanism Identified | ETA |
|---|---|---|---|---|
| Singapore | New analytics vendor (DataMetrics SG Pte Ltd) | Planning | None | Q3 2026 |
| Australia | Customer support expansion | Under review | To be determined | Q4 2026 |

### Singapore — Important Note
DataMetrics SG Pte Ltd engagement is planned to begin Q3 2026. **No transfer mechanism is currently in place for Singapore.** Singapore PDPA adequacy review is listed as "pending" in OPC materials — adequacy decision is **not yet in force**. SCCs will be required before any data transfer to DataMetrics SG begins. Legal has been notified; SCC execution has not yet been initiated.

**Risk:** If the DataMetrics SG engagement begins before SCCs are executed, it will constitute a PIPEDA violation. Q3 2026 start date conflicts with typical SCC negotiation timeline (6–8 weeks).

---

## Gaps and Action Items

| Item | Priority | Owner | Due |
|------|----------|-------|-----|
| Execute SCCs with DataMetrics SG Pte Ltd (Singapore) before data transfer | HIGH | Legal / Privacy Officer | Before any transfer commences |
| Renew UK IDTA (expires Feb 28, 2027) | Medium | Legal | December 2026 |
| Review US SCCs for current sub-processor coverage | Medium | Privacy Officer | October 2026 |

---

*This is a synthetic privacy inventory document created for demonstration purposes.*