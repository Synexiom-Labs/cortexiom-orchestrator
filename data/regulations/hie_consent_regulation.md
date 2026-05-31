# Health Information Exchange — Consent Requirements
**Regulatory Framework:** Multi-Jurisdictional Compliance Summary
**Prepared by:** Legal & Compliance — Health Data Practice
**Version:** 3.1 | Updated: February 2025

---

## 1. Overview

Health Information Exchange (HIE) platforms operating across multiple jurisdictions must comply with the patient consent requirements of each applicable jurisdiction. Consent mechanisms valid in one jurisdiction may not satisfy requirements in another. This document summarizes applicable requirements for the organization's current operating jurisdictions.

## 2. Federal (United States) — HIPAA

**Standard:** Opt-in consent for uses/disclosures beyond Treatment, Payment, Operations (TPO).

**HIE-specific rule:** Exchange of protected health information (PHI) through an HIE for treatment purposes does not require explicit patient authorization under 45 CFR §164.506(c)(1). However:
- Patient must be informed of the HIE (Notice of Privacy Practices)
- Opt-out mechanism must be available and honored within 30 days
- Breach notification: 60 days from discovery

**Documentation:** Signed NPP acknowledgment at point of care.

---

## 3. California — CMIA (Confidentiality of Medical Information Act)

**Standard:** Stricter than HIPAA. Explicit written authorization required for PHI disclosure to third parties, including other healthcare providers outside the treating relationship.

**Key difference from HIPAA:** California does not recognize the HIPAA "treatment" exception for HIE disclosures. Each provider participating in the HIE must be listed in the authorization.

**Penalty:** $1,000–$250,000 per violation; criminal penalties for intentional violations.

**Documentation required:**
- Signed written authorization naming each participating HIE provider
- Renewal required every 12 months

---

## 4. Texas — Texas HB 300 (Texas Medical Records Privacy Act)

**Standard:** HIPAA-equivalent baseline plus additional requirements:
- Disclosure to HIE requires patient authorization **unless** all receiving providers are part of the same Covered Entity or Organized Healthcare Arrangement
- Training requirement: all staff with PHI access must complete TMRPA training annually

**Documentation required:**
- Authorization form including HIE platform name
- Annual training records for all accessing staff

---

## 5. Nova Scotia — Personal Health Information Act (PHIPA-NS), SNS 2010, c 41

**Standard:** Nova Scotia PHIPA-NS diverges significantly from US frameworks.

**Key provision — s.23(1)(a) Implied Consent:**
A custodian may collect, use, or disclose personal health information about an individual **without the individual's consent** if:
> (a) the collection, use or disclosure is for the purpose of providing health care to the individual and it is not reasonably practical to obtain consent...

**Practical effect:** For treatment-purpose HIE exchanges within the provincial care network, Nova Scotia law permits **implied consent**. Explicit opt-in authorization is **not required** where:
1. The exchange is for treatment purposes
2. The disclosing custodian reasonably believes the individual would consent
3. The individual has not previously opted out

**Opt-out:** Patients may file a lockbox directive restricting access; this must be honored.

**Critical note:** Applying a US-style explicit opt-in consent form to Nova Scotia patients introduces **unnecessary barriers to care** and may create legal uncertainty. The standard US consent form does not reflect the implied consent regime and may be interpreted as limiting patient rights under PHIPA-NS.

**Documentation required:**
- Record that implied consent basis applies (treatment purpose)
- Evidence of absence of opt-out directive
- No signed authorization form required (and standard US form may be inappropriate)

---

## 6. Cross-Jurisdictional Compliance Summary

| Jurisdiction | Consent Mechanism | HIE for Treatment | Documentation |
|---|---|---|---|
| Federal (HIPAA) | Opt-out (NPP) | Permitted | NPP acknowledgment |
| California (CMIA) | Explicit opt-in | Authorization required | Signed auth, annual renewal |
| Texas (HB 300) | Opt-in | Authorization required | Signed auth, training records |
| Nova Scotia (PHIPA-NS) | **Implied consent** | Permitted without auth | Treatment purpose record + no lockbox |

Applying a single uniform US consent form to all jurisdictions **does not satisfy** Nova Scotia requirements and may impose legally unsupported burdens on NS patients.

---

*This is a synthetic regulatory summary document created for demonstration purposes.*