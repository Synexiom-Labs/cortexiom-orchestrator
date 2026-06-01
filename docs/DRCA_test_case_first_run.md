# Baseline Workflow

Time Elapsed: 76.8s

## Parsed Regulation Rules

Here are the compliance rules extracted from the regulation document:

**1. Applicable entities:**

- All business units.
- All subsidiaries.
- All contractors handling organizational data on behalf of the company.
- All third-party service providers handling organizational data on behalf of the company.

**2. Mandatory requirements:**

- All PII and SPI collected or processed by the organization must be stored in Canadian jurisdictions only.
- PII and SPI must not be stored in AWS us-east-1, AWS us-east-2, AWS us-west-1, AWS us-west-2 regions.
- PII and SPI must not be stored in any GCP regions outside `northamerica-northeast1` and `northamerica-northeast2`.
- PII and SPI must not be stored in any Azure regions outside `canadacentral` and `canadaeast`.
- All systems storing PII/SPI must be migrated to compliant regions.
- During the migration period (September 1, 2025 – February 28, 2027), all non-compliant data stores must maintain AES-256 encryption at rest.
- During the migration period (September 1, 2025 – February 28, 2027), all non-compliant data stores must maintain TLS 1.3 in transit.
- During the migration period (September 1, 2025 – February 28, 2027), all non-compliant data stores must maintain geo-restriction on access (Canadian IP blocks only).
- During the migration period (September 1, 2025 – February 28, 2027), all non-compliant data stores must provide quarterly attestation to the CISO that interim controls remain in place.
- Exceptions require written approval from the CISO and Legal Counsel.
- Approved exceptions must be reviewed quarterly.

**3. Numeric thresholds:**

- **Encryption:** AES-256 encryption at rest.
- **TLS Protocol:** TLS 1.3 in transit.
- **Review Cycle:** Annual (for the policy).
- **Migration Period:** 18 months (from policy issuance to March 1, 2027).
- **Attestation Frequency:** Quarterly (for interim controls attestation).
- **Exception Review Frequency:** Quarterly.
- **Maximum Fine:** $25 million CAD.

**4. Effective dates and deadlines:**

- **Policy Effective Date:** March 1, 2027.
- **Data Residency Mandate Effective Date:** March 1, 2027.
- **AWS ca-west-1 Availability:** Q3 2026.
- **Migration Deadline:** No later than March 1, 2027.
- **Interim Controls Period Start:** September 1, 2025.
- **Interim Controls Period End:** February 28, 2027.
- **Internal Compliance Audit Window:** Q1 2027 (January–February 2027).

**5. Documentation standards:**

- Exceptions to geo-restriction on access for non-compliant data stores must be documented.
- Quarterly attestation to CISO that interim controls remain in place is required.
- Exceptions require written approval from the CISO and Legal Counsel.
- Approved exceptions must be documented in the exception register.

**6. Penalties for non-compliance:**

- Suspension of business operations in affected provincial markets.
- Regulatory referral under PIPEDA / provincial privacy legislation.
- Disclosure obligations to affected data subjects.
- Fines up to $25 million CAD under the Digital Charter Implementation Act.
- Systems not ready by the Q1 2027 audit are subject to accelerated remediation and executive escalation.

## Evidence Gathered

Here are the compliance-relevant facts extracted from the provided documents:

**1. Current Organizational State**

- **Financial Advisory Services:**
    - Advisors are compensated via base salary, AUM-based commission (0.5%-1.2%), trailing commissions from fund manufacturers, and referral fees.
    - An annual performance bonus program exists ($8,000–$47,000 CAD) based on net new assets, client retention, compliance incident record, and regional ranking.
    - Disclosure of standard compensation is done via Form 31-103F1 and Fund Facts. Performance bonuses are disclosed in Appendix C of the client Relationship Disclosure Document (RDD) using generic language.
- **Health Information Exchange (HIE) Operations:**
    - Operates in California, Texas, and Nova Scotia using the SecureHealth HIE v2.4 platform.
    - Uses a written opt-in authorization form (HC-US-01 Rev 3.2) in all three jurisdictions; Texas also uses an HB 300 addendum.
    - Nova Scotia operations were added in January 2026.
- **Data Storage and Transfer:**
    - Primary data store systems (Customer Database, Transaction Ledger, Document Storage, Analytics Platform) are hosted on AWS in **Northern Virginia, USA (us-east-1)**.
    - Transfers data to the European Union, United Kingdom, Switzerland, United States, and India.
    - Uses various transfer mechanisms: EU/Switzerland adequacy decisions, UK IDTA, and PIPEDA SCCs for the US (AWS, Salesforce, Zendesk) and India (limited development data).
    - Security controls for primary data stores include AES-256 encryption at rest, TLS 1.3 in transit, IAM roles, MFA, VPCs, AWS WAF geo-blocking for non-CA/US IPs, and CloudTrail logging. These controls satisfy interim requirements under CORP-SEC-2026-07 §4.4.
- **PEP Client Management:**
    - Maintains a register of 47 Politically Exposed Persons (PEPs) clients (Domestic, Foreign, HIO).
    - All PEP clients have an Enhanced Due Diligence (EDD) completion date logged. Component-level EDD documentation is in individual client files.

**2. Compliance Posture Against Data Residency Policy CORP-SEC-2026-07**

**2.1. Current State**

- All primary data systems (Customer Database, Transaction Ledger, Document Storage, Analytics Platform) are located in AWS us-east-1 (Northern Virginia, USA).
- The UK International Data Transfer Agreement (IDTA) expires on February 28, 2027.
- New data transfers are planned for Singapore (Q3 2026) for a new analytics vendor (DataMetrics SG Pte Ltd) and Australia (Q4 2026) for customer support expansion.

**2.2. Compliance Gaps Identified**

- **Direct Non-Compliance with CORP-SEC-2026-07:** The current location of all primary data systems in AWS us-east-1 (USA) is explicitly stated as **NON-COMPLIANT** with CORP-SEC-2026-07, as this region is non-compliant under the policy.
- **Missing Transfer Mechanism (Singapore):** No transfer mechanism is currently in place for Singapore for the planned Q3 2026 engagement with DataMetrics SG Pte Ltd. Singapore's PDPA adequacy decision is pending and not yet in force. This poses a **HIGH priority risk** of PIPEDA violation if data transfer commences before SCCs are executed.
- **Migration Risk Concentration:** The migration plan schedules four production data migrations (Customer DB, Transaction Ledger, Document Storage, Analytics Platform) in January–February 2027, immediately before the March 1, 2027 policy deadline. This creates significant concentration risk in Q1 2027, coinciding with the internal compliance audit.

**2.3. Remediation Roadmap (as per documents)**

- **Target region selection (AWS ca-central-1):** Due July 15, 2026 (Status: Not started).
- **Development environment migration:** Due September 1, 2026 (Status: Not started).
- **Staging environment migration:** Due November 1, 2026 (Status: Not started).
- **Production data migration (Customer DB):** Due January 15, 2027 (Status: Not started).
- **Production data migration (Transaction Ledger):** Due February 1, 2027 (Status: Not started).
- **Production data migration (Document Storage):** Due February 15, 2027 (Status: Not started).
- **Analytics Platform migration:** Due February 25, 2027 (Status: Not started).
- **Execute SCCs with DataMetrics SG Pte Ltd (Singapore):** HIGH priority, due before any transfer commences (Status: Not yet initiated).
- **Renew UK IDTA:** Medium priority, due December 2026 (expires Feb 28, 2027).
- **Review US SCCs for current sub-processor coverage:** Medium priority, due October 2026.

**2.4. Missing Information (Specific to Data Residency Policy)**

- The target region selection for migration (AWS ca-central-1) is "Not started."
- No transfer mechanism is yet identified or in place for the planned Australia customer support expansion (Q4 2026).
- SCC execution for DataMetrics SG Pte Ltd (Singapore) has not yet been initiated, despite the Q3 2026 start date for the vendor.

**3. Other Compliance Gaps Identified in the Documents**

- **Advisor Compensation Disclosure (CSA Staff Notice 31-362):**
    - Current Appendix C language for performance bonuses is non-compliant with August 2024 CSA guidance.
    - It fails to state the specific dollar range ($8,000–$47,000), explain potential conflicts in plain terms, or meet the "reasonable client" test.
    - The reliance on a March 2023 legal opinion is outdated, as it predates the August 2024 CSA guidance.
    - No update to Appendix C or client disclosure has been made since the August 2024 guidance.
- **Nova Scotia HIE Operations (PHIPA-NS):**
    - Nova Scotia operations are potentially non-compliant with PHIPA-NS. The standard US consent form (HC-US-01 Rev 3.2) is being used without specific assessment against PHIPA-NS requirements.
    - An internal compliance memo (March 2026) flagged that PHIPA-NS implied consent provisions were not evaluated.
    - No jurisdiction-specific PHIPA-NS audit has been conducted.
- **PEP Client EDD Refresh:**
    - Annual refresh is due for clients whose EDD date falls more than 12 months prior. Based on the "Last Updated: May 15, 2026" date, at least nine PEP clients (e.g., PEP-005, PEP-008, PEP-013, PEP-021, PEP-025, PEP-029, PEP-035, PEP-039, PEP-040) have EDD dates exceeding 12 months (e.g., PEP-039 from July 30, 2023).

**4. Any Missing Information Noted in the Documents Themselves**

- **Advisor Compensation:**
    - An updated legal opinion on Appendix C under the 2024 standard is in progress (due June 30, 2026).
    - Redrafting of Appendix C is "Not started" (due July 31, 2026).
    - Re-disclosure to affected clients is "Not started" (due August 31, 2026).
- **HIE Operations:**
    - Legal assessment for Nova Scotia PHIPA-NS compliance is assigned and due Q3 2026.
    - Evaluation of whether PHIPA-NS implied consent exception applies to the current NS patient population is pending.
    - Consideration of whether a separate NS-specific consent framework is required is pending.

## **Final Recommendation**

**Compliance Assessment: Data Residency Policy CORP-SEC-2026-07**

---

**STATUS:** Non-Compliant

**SUMMARY:** The organization is currently non-compliant with CORP-SEC-2026-07 because all primary PII/SPI data stores reside in AWS us-east-1 (USA), a region explicitly prohibited by the policy. Critical migration activities to Canadian compliant regions are significantly behind schedule, creating a high risk of missing the March 1, 2027 deadline. Furthermore, essential legal mechanisms for new international data transfers are missing or uninitiated.

**KEY FINDINGS:**

- **Direct Non-Compliance with Data Residency Mandate:** All primary PII/SPI data systems (Customer Database, Transaction Ledger, Document Storage, Analytics Platform) are currently hosted in AWS us-east-1 (Northern Virginia, USA). This directly violates CORP-SEC-2026-07's requirement for PII/SPI to be stored solely in Canadian jurisdictions and its explicit prohibition of AWS us-east-1.
- **Interim Control Adherence (Partial):** While primary data stores meet AES-256 encryption at rest and TLS 1.3 in transit requirements for the interim period, the stated "AWS WAF geo-blocking for non-CA/US IPs" needs verification to confirm it strictly adheres to the "Canadian IP blocks only" mandate of the policy's interim controls.
- **Critical Migration Delays & High Deadline Risk:** All foundational steps for the required migration, including target region selection (due July 15, 2026), development environment migration (due Sept 1, 2026), and staging environment migration (due Nov 1, 2026), are currently "Not started." The current remediation roadmap's concentration of all four production data migrations in January-February 2027, just weeks before the March 1, 2027 policy effective date and coinciding with the internal audit window, creates an extremely high risk of missing the deadline and incurring severe penalties.
- **Missing New International Data Transfer Mechanisms:**
    - **Singapore:** No transfer mechanism (e.g., SCCs) has been initiated for DataMetrics SG Pte Ltd, despite their planned engagement in Q3 2026, posing a high-priority PIPEDA violation risk if data transfer commences without a legal basis.
    - **Australia:** No transfer mechanism has been identified or is in place for the planned customer support expansion in Q4 2026.
- **Upcoming International Data Transfer Agreement Reviews:** The UK International Data Transfer Agreement (IDTA) expires on February 28, 2027, requiring renewal, and existing US SCCs with sub-processors require review by October 2026.

**ACTION ITEMS:**

*Prioritization Scale:*

- **P1 (Critical/Immediate):** Direct non-compliance, imminent deadlines, high penalties, foundational steps.
- **P2 (High Priority):** Significant risk, requires prompt attention to avoid P1 status.
- **P3 (Medium Priority):** Important for robust compliance, but not immediately critical for core policy adherence.

---

**P1: Address Core Data Residency Non-Compliance & Migration Delays**

- **Action:** Immediately initiate and complete Target Region Selection for AWS ca-central-1 (or other policy-compliant Canadian region).
    - **Owner:** Head of Infrastructure / CTO
    - **Timeline:** **Urgent, by July 31, 2026 (Revised from original July 15, 2026 due to missed deadline).**
- **Action:** Revise and significantly accelerate the overall data migration plan to compliant Canadian regions. Prioritize and execute Development and Staging environment migrations to de-risk production cutovers.
    - **Owner:** Head of Infrastructure / Project Management Office (PMO)
    - **Timeline:** **Revised plan submitted by August 15, 2026.**
- **Action:** Implement and verify strict "Canadian IP blocks only" geo-restriction for all non-compliant PII/SPI data stores in AWS us-east-1, as explicitly required by CORP-SEC-2026-07 interim controls. Document proof of this strict configuration.
    - **Owner:** Security Operations / Network Engineering
    - **Timeline:** **Immediate, by August 31, 2026.**
- **Action:** Conduct the first quarterly attestation to the CISO, confirming all required interim controls (AES-256, TLS 1.3, and strict Canadian geo-restriction) are fully in place for non-compliant data stores.
    - **Owner:** Compliance Officer / CISO
    - **Timeline:** **By September 30, 2026 (for Q3 reporting).**

**P1: Establish Missing International Data Transfer Mechanisms**

- **Action:** Immediately initiate and complete execution of Standard Contractual Clauses (SCCs) or other appropriate, legally sound transfer mechanisms with DataMetrics SG Pte Ltd for Singapore.
    - **Owner:** Legal Counsel / Procurement / Data Protection Officer (DPO)
    - **Timeline:** **Before any data transfer commences, no later than August 31, 2026.**
- **Action:** Identify and initiate appropriate data transfer mechanisms (e.g., SCCs) for the planned Australia customer support expansion.
    - **Owner:** Legal Counsel / Procurement / DPO
    - **Timeline:** **Before any data transfer commences, no later than October 31, 2026.**

---

**P2: Manage Existing International Data Transfer Agreements & General Readiness**

- **Action:** Conduct a thorough review of all existing US SCCs for current sub-processor coverage to ensure ongoing compliance with data transfer regulations.
    - **Owner:** Legal Counsel / DPO
    - **Timeline:** **By October 31, 2026.**
- **Action:** Plan and initiate the renewal process for the UK International Data Transfer Agreement (IDTA) to ensure uninterrupted data transfers.
    - **Owner:** Legal Counsel / DPO
    - **Timeline:** **By November 30, 2026.**
- **Action:** Establish a robust project management framework and governance for the entire data migration project, including regular reporting to executive leadership, risk management, and a clear escalation path.
    - **Owner:** PMO / CIO
    - **Timeline:** **By August 31, 2026.**
- **Action:** Begin dedicated preparation for the Q1 2027 Internal Compliance Audit, ensuring demonstrable progress on migration and full adherence to interim controls.
    - **Owner:** Compliance Officer / CISO / PMO
    - **Timeline:** **Ongoing, audit preparation to intensify by December 1, 2026.**

---

**P3: Ongoing Compliance & Documentation**

- **Action:** Ensure all exceptions to CORP-SEC-2026-07 are formally documented with written approval from the CISO and Legal Counsel, and promptly added to a central exception register.
    - **Owner:** Compliance Officer
    - **Timeline:** **Ongoing, as needed.**
- **Action:** Schedule and conduct quarterly reviews of all approved exceptions to ensure their continued validity and necessity.
    - **Owner:** Compliance Officer
    - **Timeline:** **Quarterly (e.g., end of Q3 2026, Q4 2026, Q1 2027).**

---

**CONFIDENCE:** High

**Reasoning:** The evidence explicitly states that all primary PII/SPI data stores are located in AWS us-east-1, which is a prohibited region under CORP-SEC-2026-07, unequivocally placing the organization in a "Non-Compliant" status with the policy's core mandate. The policy's requirements for prohibited regions, interim controls, and deadlines are clear and unambiguous. The significant delays in critical migration activities, as noted by their "Not started" status, present a very high probability of missing the March 1, 2027 deadline. The missing international data transfer mechanisms for Singapore and Australia represent immediate, high-priority compliance risks under general data protection regulations (e.g., PIPEDA) that underpin the residency policy. The only minor area requiring immediate verification is the precise configuration of the geo-restriction interim control to ensure it strictly meets the "Canadian IP blocks only" requirement.

---

**Note on Other Compliance Gaps:** While this assessment focuses strictly on CORP-SEC-2026-07, the provided evidence highlights additional critical compliance vulnerabilities. These include non-compliance with August 2024 CSA guidance on Advisor Compensation Disclosure (CSA Staff Notice 31-362), potential non-compliance with PHIPA-NS for Health Information Exchange (HIE) operations in Nova Scotia, and overdue Enhanced Due Diligence (EDD) refreshes for a significant number of Politically Exposed Persons (PEP) clients. These areas require immediate, dedicated attention from the relevant business units and legal/compliance functions to mitigate broader regulatory and reputational risks.

# Supervised Workflow (Cortexiom)

Time Elapsed: 405.5s

## Parsed Regulation Rules

Here are the compliance rules extracted from the document:

---

**Applicable Entities:**

- All business units.
- All subsidiaries.
- All contractors handling organizational data on behalf of the company.
- All third-party service providers handling organizational data on behalf of the company.

**Mandatory Requirements:**

- **Data Residency:** All PII and SPI collected or processed by the organization must be stored in Canadian jurisdictions only.
    - Explicitly non-compliant regions: AWS us-east-1, AWS us-east-2, AWS us-west-1, AWS us-west-2, all GCP regions outside `northamerica-northeast1` and `northamerica-northeast2`, all Azure regions outside `canadacentral` and `canadaeast`.
    - Approved compliant regions:
        - AWS: `ca-central-1` (Montreal), `ca-west-1` (Calgary — available Q3 2026).
        - GCP: `northamerica-northeast1` (Montreal), `northamerica-northeast2` (Toronto).
        - Azure: `canadacentral` (Toronto), `canadaeast` (Quebec City).
- **Migration:** All systems storing PII/SPI must be migrated to compliant regions.
- **Interim Controls (during migration period):** All non-compliant data stores must maintain:
    - AES-256 encryption at rest.
    - TLS 1.3 in transit.
    - Geo-restriction on access (Canadian IP blocks only, with documented exceptions).
    - Attestation to CISO that interim controls remain in place.
- **Auditing:** An internal compliance audit will be conducted to verify readiness. Systems not ready by the Q1 2027 audit are subject to accelerated remediation and executive escalation.
- **Exceptions:** Require written approval from the CISO and Legal Counsel. Approved exceptions must be documented and reviewed.

**Thresholds:**

- **Policy Review Cycle:** Annual.
- **Migration Deadline:** No later than March 1, 2027 (18 months from policy issuance).
- **Interim Controls Attestation:** Quarterly.
- **Geo-restriction:** Canadian IP blocks only (for access during interim period).
- **Audit Window:** Q1 2027 (January–February 2027).
- **Exception Review:** Quarterly.
- **Maximum Fine:** Up to $25 million CAD (under the Digital Charter Implementation Act).

**Effective Dates:**

- **Policy Effective Date:** March 1, 2027.
- **Canadian Privacy Law Amendments Effective Date:** Q1 2026 (contextual).
- **AWS ca-west-1 availability:** Q3 2026.
- **Migration Period for Interim Controls:** September 1, 2025 – February 28, 2027.
- **Audit Window:** Q1 2027 (January–February 2027).
- **Compliance Deadline for Penalties:** March 1, 2027.

**Documentation Standards:**

- Policy classification: Internal — Restricted.
- Geo-restriction exceptions: Must be documented.
- Interim controls attestation: Must be made to the CISO.
- Exceptions:
    - Require written approval from the CISO and Legal Counsel.
    - Must be documented in an exception register.

**Penalties:**

- **Failure to comply by March 1, 2027 may result in:**
    - Suspension of business operations in affected provincial markets.
    - Regulatory referral under PIPEDA / provincial privacy legislation.
    - Disclosure obligations to affected data subjects.
    - Fines up to $25 million CAD under the Digital Charter Implementation Act.
- **Systems not ready by Q1 2027 audit:** Subject to accelerated remediation and executive escalation.

## Evidence Gathered

## **Compliance Posture Assessment: Data Residency Policy CORP-SEC-2026-07**

**1. Current Compliance Posture**

**Overall Status:** **NON-COMPLIANT** with Policy CORP-SEC-2026-07 regarding the primary storage location of critical data.

**Key Findings:**

- **Non-Compliant Data Location:** All primary data stores, including Customer Database, Transaction Ledger, Document Storage, and Analytics Platform, are currently hosted in **AWS us-east-1 (Northern Virginia, USA)**. The `data_residency_posture.md` document explicitly states that this region is a "non-compliant region under the policy CORP-SEC-2026-07."
- **Interim Controls in Place:** The organization has implemented various security controls (encryption at rest/in transit, access control, network segmentation, geo-restriction, logging). These controls are noted to satisfy the **interim requirements** under CORP-SEC-2026-07 §4.4, providing a temporary compliant state during the migration period. Quarterly CISO attestations confirm this.
- **Policy Deadline:** The hard deadline for full compliance with CORP-SEC-2026-07 is **March 1, 2027**.
- **Migration Planning Initiated:** A migration plan targeting AWS ca-central-1 (Canada) has been developed.
- **Significant Migration Risk:** The current migration plan front-loads critical production migrations (Customer DB, Transaction Ledger, Document Storage, Analytics Platform) into January–February 2027, immediately preceding the March 1, 2027 policy deadline. This creates **significant concentration risk** and a high probability of missing the deadline if any delays occur. As of April 30, 2026, no migration steps have been started.

**2. Identified Compliance Gaps**

1. **Primary Data Residency:** The fundamental requirement of CORP-SEC-2026-07, which mandates primary data storage in a compliant region, is not currently met. All primary systems reside in a non-compliant US region.
2. **Migration Timeline Risk:** The delayed start and back-loaded nature of the production migration plan present a substantial risk of failing to achieve full compliance by the March 1, 2027 deadline. The plan indicates no progress on milestones as of late April 2026.
3. **Lack of De-risking Strategy:** The current migration plan does not appear to incorporate explicit de-risking strategies for the concentrated activity in Q1 2027.

**3. Missing Information Noted**

- **Full Policy Document CORP-SEC-2026-07:** While the `data_residency_posture.md` document references CORP-SEC-2026-07, the actual policy document was not provided. This means the precise definition of "non-compliant region," specific compliant regions, and the full scope of "interim requirements under §4.4" are inferred from the infrastructure inventory document rather than being directly reviewed. Access to the full policy would allow for a more comprehensive and granular assessment.

---

## **Remediation Roadmap: Data Residency Policy CORP-SEC-2026-07**

This roadmap aims to address the identified compliance gaps and risks, ensuring full adherence to CORP-SEC-2026-07 by the March 1, 2027 deadline.

---

**Phase 1: Immediate Actions (May – June 2026)**

| Action Item | Description | Owner | Due Date | Status |
| --- | --- | --- | --- | --- |
| **1.1 Formal Acknowledgment of Non-Compliance** | Formalize and communicate the current non-compliant status (concerning primary data location) to key stakeholders, including Executive Leadership, CISO, and VP Engineering. | CISO, VP Engineering | May 15, 2026 | New |
| **1.2 Accelerate & De-risk Migration Plan** | Immediately revise the migration plan to bring forward critical production migration milestones. Distribute the workload more evenly across Q3 2026, Q4 2026, and Q1 2027 to mitigate concentration risk. | VP Engineering, Cloud Infrastructure Team | June 15, 2026 | New |
| **1.3 Prioritize Initial Migration Steps** | Expedite "Target region selection (AWS ca-central-1)" and "Development environment migration" to start within Q2 2026, rather than Q3. | VP Engineering, Cloud Infrastructure Team | Target Region: June 30, 2026; Dev Env Start: July 31, 2026 | New |
| **1.4 Establish Migration Governance** | Form a dedicated task force or steering committee (including CISO, VP Engineering, and representatives from Legal/Compliance) to oversee and track the data residency migration. Implement bi-weekly progress reviews. | CISO, VP Engineering | May 31, 2026 | New |
| **1.5 Resource Assessment** | Conduct a thorough assessment of required resources (personnel, budget, tools) to support the accelerated migration plan. Address any identified shortfalls proactively. | VP Engineering, HR, Finance | June 30, 2026 | New |
| **1.6 CISO Attestation Q2 2026** | Ensure the quarterly attestation confirming interim controls are in place and effective is completed and documented. | CISO | June 30, 2026 | Pending |

---

**Phase 2: Short-Term Actions (July 2026 – February 2027)**

| Action Item | Description | Owner | Due Date | Status |
| --- | --- | --- | --- | --- |
| **2.1 Execute Revised Migration Plan** | Systematically execute the accelerated and de-risked migration plan, focusing on moving primary data stores to AWS ca-central-1. | Cloud Infrastructure Team | Ongoing, leading to March 1, 2027 | In Progress |
| **2.2 Implement Contingency Planning** | Develop and document a comprehensive contingency plan for potential migration delays or technical challenges. This plan should outline fallback options, temporary solutions, and communication protocols. | VP Engineering, CISO | July 31, 2026 | New |
| **2.3 Ongoing Progress Monitoring** | The migration governance committee (established in 1.4) must rigorously monitor progress against the revised timeline, identifying and addressing any deviations or blockers promptly. | Migration Governance Committee | Ongoing | In Progress |
| **2.4 Maintain Interim Controls** | Continuously verify the effectiveness and operational status of all interim security controls (CORP-SEC-2026-07 §4.4) until full migration is complete. | CISO, Cloud Infrastructure Team | Ongoing | In Progress |
| **2.5 CISO Attestations Q3/Q4 2026, Q1 2027** | Ensure timely completion of all remaining quarterly CISO attestations prior to the deadline. | CISO | Sep 30, 2026; Dec 31, 2026; Mar 1, 2027 | Pending |

---

**Phase 3: Post-Deadline Verification (March – April 2027)**

| Action Item | Description | Owner | Due Date | Status |
| --- | --- | --- | --- | --- |
| **3.1 Post-Migration Audit** | Conduct a comprehensive audit to verify that all primary data subject to CORP-SEC-2026-07 has been successfully migrated to AWS ca-central-1 and that the previous non-compliant region (us-east-1) no longer hosts this data. | CISO, Internal Audit | April 30, 2027 | New |
| **3.2 Policy Compliance Declaration** | Issue a formal declaration of full compliance with CORP-SEC-2026-07, supported by audit evidence. | CISO, Legal, Compliance | April 30, 2027 | New |
| **3.3 Policy Review & Update** | Initiate a review of CORP-SEC-2026-07 to ensure it remains current and effective, considering lessons learned from the migration process. | Legal, CISO, Compliance | Q2 2027 | New |

## Checkpoint 1 - Pre-Decision - Confidence 68%

Evidence completeness review before recommendation is drafted

depth=1 | state_token=✓ active

## **Compliance Posture Assessment — CORP-SEC-2026-07**

**Overall Status: NON-COMPLIANT (with Interim Controls Asserted)**

Before issuing a remediation roadmap, this assessment must be direct about something the evidence chain does not yet fully support: the organization's current posture is **asserted compliance** under §4.4 interim controls — not **verified compliance**. That distinction carries regulatory weight, and the roadmap below is structured accordingly.

---

## **Part 1: Evidence Completeness Assessment**

**Confidence in current evidence chain: 0.62** — sufficient to characterize the gap and issue a conditional roadmap, insufficient to confirm interim control adequacy.

**What the evidence confirms**

- All production data stores (Customer Database, Transaction Ledger, Document Storage, Analytics Platform) reside in AWS us-east-1 — an explicitly named non-compliant region under CORP-SEC-2026-07.
- Migration planning targeting AWS ca-central-1 is underway.
- Interim security controls (AES-256 encryption at rest and in transit, access controls, network segmentation, geo-restriction, logging) are reportedly in place.
- Quarterly CISO attestations are described as active.
- Hard compliance deadline: **March 1, 2027**.

**Critical gaps in the evidence chain**

| Gap | Risk Level | Why It Matters |
| --- | --- | --- |
| **CISO attestation records not retrieved** | HIGH | The claim that §4.4 interim controls are satisfied is asserted in posture documentation, not evidenced by the attestation records themselves. These are the primary artifact a regulator would examine. |
| **Interim control rule truncated** | HIGH | The extracted regulation was cut off mid-sentence at "AES-256 encry—". The complete §4.4 control set is unknown. Controls implemented may not fully satisfy requirements not yet read. |
| **Migration plan artifacts not retrieved** | MEDIUM | Target architecture, data classification scope, timeline, and owner assignments are referenced but not in evidence. |
| **Contractor and third-party data store inventory** | MEDIUM | The policy applies to all contractors and third-party providers handling organizational data. No evidence addresses their current residency posture. |
| **Data classification inventory** | MEDIUM | The policy governs PII and SPI specifically. No evidence confirms what data in each store meets those classifications, which affects migration priority and scope. |

**Structural contradiction flagged**

The regulation text was truncated before the full §4.4 interim control requirements were captured. **This is not a minor gap.** Controls described as satisfying §4.4 cannot be verified against an incomplete rule set. Any recommendation built on "interim controls are sufficient" carries this unresolved dependency.

**Recommended immediate action:** Retrieve the complete §4.4 text, all CISO attestation records for the current interim period, and the formal migration plan document before this assessment is used for board-level or regulatory reporting.

---

## **Part 2: Compliance Posture Characterization**

The organization's situation is more precisely described as follows:

- **Jurisdictional non-compliance:** 100% of production PII/SPI infrastructure is in a US jurisdiction. This is not a configuration gap — it is an architectural misalignment with the policy's foundational requirement of Canadian jurisdictional sovereignty over data.
- **Interim controls as deferral, not resolution:** The interim controls address data security during the migration window. They do not resolve the jurisdictional sovereignty problem. Every quarter the CISO attests to interim compliance, the organization is making an implicit claim that the gap is managed. The attestation records — which would substantiate that claim — have not been retrieved and reviewed.
- **Documentation trail risk:** If a regulatory inquiry were initiated today, the organization would need to produce attestation records that have not been confirmed to exist in complete, audit-ready form.

---

## **Part 3: Remediation Roadmap**

This roadmap is framed as a **policy-architecture realignment**, not a technical migration. That distinction determines who owns each workstream and what "done" means.

**Phase 0: Immediate — Evidence and Control Verification (Now → 30 days)**

**Owner: CISO + Legal + Compliance**

- [ ]  Retrieve and review all §4.4 attestation records for completeness and audit-readiness.
- [ ]  Obtain and review the complete §4.4 interim control requirements (untruncated).
- [ ]  Conduct a gap analysis between controls implemented and controls required.
- [ ]  Inventory all contractor and third-party data stores for PII/SPI residency.
- [ ]  Confirm the PII/SPI classification of all data in each production store.
- [ ]  Confirm whether CISO attestations are being signed with full knowledge of the unverified documentation state.

**Gate criterion:** Leadership must be formally notified, in writing, of the difference between asserted and verified interim compliance. This is a governance obligation, not an optional step.

---

**Phase 1: Migration Foundation (30–90 days)**

**Owner: Cloud Architecture + Security + Legal**

- [ ]  Finalize and formally approve the migration plan targeting AWS ca-central-1 (Montreal) as primary, with AWS ca-west-1 (Calgary) as secondary option pending Q3 2026 availability confirmation.
- [ ]  Prioritize data stores by PII/SPI density and regulatory exposure: Customer Database → Transaction Ledger → Document Storage → Analytics Platform (validate this ordering against the data classification inventory).
- [ ]  Establish Canadian-region infrastructure (VPC, IAM, KMS, logging) with parity controls to current us-east-1 environment.
- [ ]  Engage procurement and legal to review all third-party and contractor data processing agreements for residency compliance obligations.
- [ ]  Confirm that interim controls are fully documented and attestation records are current and complete.

---

**Phase 2: Phased Data Migration (90–270 days / by November 1, 2026)**

**Owner: Engineering + Cloud Architecture + Data Governance**

- [ ]  Execute migration in workload priority order with defined rollback procedures.
- [ ]  For each migrated data store: validate residency, re-run control verification, update CISO attestation scope.
- [ ]  Decommission us-east-1 data stores as each migration completes — do not run parallel primary stores beyond the minimum necessary transition window.
- [ ]  Maintain a running compliance register updated after each store migration.
- [ ]  Engage an independent third party to audit the first completed migration before proceeding to subsequent workloads.

---

**Phase 3: Full Compliance Verification and Closure (November 1, 2026 → February 1, 2027)**

**Owner: CISO + Legal + Executive Sponsor**

- [ ]  Complete all data store migrations to Canadian jurisdictions.
- [ ]  Conduct full independent audit of residency compliance across all systems, including contractor and third-party data processors.
- [ ]  Retire all §4.4 interim control attestations and replace with full-compliance attestations.
- [ ]  Produce a compliance closure report suitable for regulatory submission.
- [ ]  Brief board or equivalent governance body on compliance achievement with supporting audit evidence.

**Target completion: February 1, 2027** — providing a 28-day buffer before the March 1, 2027 hard deadline for remediation of any findings.

---

## **Key Governance Question Requiring an Answer**

**Who in this organization has been informed, in writing, that the current interim posture is asserted compliance — not verified compliance — and what has been done with that information?**

If that question does not have a documented answer, Phase 0 is not optional. It is the prerequisite on which the validity of everything else depends.

---

*This assessment is conditional on retrieval of the complete §4.4 rule text, attestation records, and migration plan artifacts noted above. It should not be used as a standalone regulatory representation until those gaps are resolved.*

## Checkpoint 2 - Post-Recommendation - Confidence 71%

Contradiction detection and confidence calibration

depth=2 | state_token=✓ active

**Reflector Assessment — CORP-SEC-2026-07 Compliance Recommendation Review**

---

**CONFIDENCE IN CURRENT EVIDENCE CHAIN: 0.58**

The draft recommendation's 0.xx confidence posture (implied by its hedged language) is overstated relative to the evidence actually in hand. The regulatory text provided to this review is itself incomplete — the approved compliant regions list is truncated mid-entry (`ca-west-1` is named but its city designation and any qualifying conditions are cut off). This is not a minor formatting artifact. If the full regulatory text contains carve-outs, interim provisions, or scope definitions that were not transmitted, the recommendation may be materially miscalibrated in either direction. Confidence in the evidence chain is therefore capped at 0.58 until the complete regulatory document is confirmed reviewed.

---

**CONTRADICTIONS AND GAPS DETECTED**

**1. The NON-COMPLIANT status label is doing three jobs it has not individually earned.**

The current recommendation conflates three independent determinations into a single status:

- *Regulatory interpretation:* Whether the March 1, 2027 mandate admits of any interim-control defense at all. The policy text as provided contains no explicit interim carve-out. If the absolute-date language forecloses interim control reliance, then the "with Interim Controls Asserted" qualifier in the status line is not a mitigating notation — it is a false comfort to downstream reviewers.
- *Operational risk assessment:* Whether the interim controls are preventive (restricting access to or processing of non-compliant data) or documentary (recording that non-compliant storage is occurring). These are not points on a spectrum. A documentary control in this context is an audit trail for an ongoing violation, not a mitigation of it.
- *Scope adequacy:* Whether the migration program captures all residency-subject data — specifically data lineage records, backup retention sets, and archived SPI that may reside in non-compliant regions independently of the primary data stores being migrated. The draft recommendation is silent on these categories. Silence reads as confirmation of adequacy to any reviewer who is not specifically looking for the gap.

These three determinations must be unbundled. The recommendation cannot be finalized until each is resolved on its own evidentiary basis.

**2. The preventive/documentary control distinction is the threshold question — and it is unresolved.**

The draft flags unverified interim controls but treats this as a documentation gap to be closed. It is not. Until it is established that interim controls actively prevent non-compliant processing or access — not merely record it — the organization's compliance posture cannot be described as "managed risk." If controls are documentary only, the organization is accruing regulatory exposure in real time. The CISO attestation records and the complete §4.4 policy text are not supporting evidence for an otherwise adequate recommendation; they are prerequisites to making the recommendation at all.

**3. Jurisdiction-specific requirement gap: Contractor and third-party scope.**

The regulation's applicable entity list explicitly includes contractors and third-party service providers handling organizational data. The draft recommendation addresses primary organizational data stores but does not assess whether contracted data processors or third-party integrations have independent residency exposure. If any third party is processing PII or SPI on the organization's behalf in a non-compliant region, that exposure is not cured by the organization's own migration. This gap should be explicitly scoped in or out — not left open.

**4. Temporal calibration: The truncated regulation text creates a verification gap.**

The approved compliant regions list as provided is incomplete (`ca-west-1` entry is cut off). Any recommendation asserting that migration to specific target regions will achieve compliance must be grounded in the complete approved-regions text. If the full document contains qualifying conditions on approved regions (e.g., specific service-level constraints, data classification restrictions, or approval conditions), those conditions could alter the migration target assessment. This is a document-integrity issue that must be resolved before the recommendation is finalized.

**5. The recommendation borrows confidence from risk-management conventions the regulatory text may not honor.**

The draft is written in the idiom of risk management — interim controls, phased migration, timeline concentration risk. The regulatory mandate, as provided, uses absolute-date language with no explicit interim provision. These are different normative frameworks, and the recommendation does not surface the tension between them. A regulator or auditor reading this recommendation will apply the regulatory framework, not the risk-management one. The draft should explicitly state whether external legal counsel has opined on whether interim controls constitute a recognized defense under this mandate — and if not, that opinion should be obtained before the recommendation is issued.

---

**THINGS THAT WOULD CHANGE THIS RECOMMENDATION IF TRUE**

- *If §4.4 contains an explicit interim-control provision:* The NON-COMPLIANT status and its qualified framing may be appropriate — but only if controls are preventive, not documentary.
- *If interim controls are documentary only:* The recommendation's risk framing should be replaced with a violation-accrual framing. The language of "managed risk" is not defensible.
- *If the migration scope excludes backups, archives, or lineage data:* A fully executed migration by March 1 may produce a post-deadline compliance posture structurally identical to the current one, just with a different data category carrying the exposure. This would be a worse outcome than the current draft anticipates.
- *If any third-party processor is handling PII/SPI in a non-compliant region:* The organization's compliance gap is larger than its own migration program can close.
- *If the `ca-west-1` approved-region entry contains qualifying conditions:* Migration target planning may need revision.

---

**RECOMMENDED ACTION**

Do not issue this recommendation in its current form. Three steps must precede finalization:

1. **Obtain and review the complete CORP-SEC-2026-07 text** — including the full approved-regions list, §4.4 in its entirety, and any interim provision language. Confirm that the document reviewed is the effective March 1, 2027 version.
2. **Resolve the preventive/documentary control question** — via reviewed CISO attestation and independent technical verification — before characterizing interim controls as mitigating. This is not a documentation step; it determines the fundamental nature of the current compliance posture.
3. **Commission or confirm a data mapping exercise** that explicitly scopes backups, archives, data lineage records, and third-party processors against the residency mandate — before the migration plan is finalized. The migration program's current scope should be treated as unconfirmed until this exercise is complete.

If there is regulatory, legal, or business pressure to issue a recommendation before these steps are complete, the recommendation should explicitly state which determinations remain unresolved and why, and should not use status language that implies those questions have been answered.

## Checkpoint 3 - Escalation - Confidence 68%

Final routing: file / human review / urgent escalation

depth=3 | state_token=✓ active

**ESCALATION ROUTING DECISION**

**Routing: HUMAN REVIEW — with conditional path to URGENT ESCALATION**

---

**Routing Rationale**

This case does not meet the threshold for FILE REPORT, and the determination between HUMAN REVIEW and URGENT ESCALATION turns on a sequencing question: whether the primary blocker (missing mandate text) can be resolved within a timeframe that still permits principled governance before the migration plan becomes irreversible. The current answer is: yes, but barely, and the window is closing.

The NON-COMPLIANCE verdict may be correct. The problem is that it has been issued without the epistemic standing to defend it in a governance or regulatory context — and if this assessment is transmitted to the CCO, board, or a regulator in its current form, the organization is not just non-compliant with a data residency mandate; it is also operating a compliance function that is producing conclusions it cannot support. That is a distinct and compounding governance risk.

The appropriate routing is therefore **HUMAN REVIEW** at the senior compliance officer level, with a mandatory escalation trigger defined in advance.

---

**Confidence in Current Evidence Chain: Low-Moderate (calibrated at 0.52)**

The Attractor synthesis was assessed at 0.68, but that confidence attaches to the *diagnosis* of the epistemic gap — not to the compliance verdict itself. Confidence in the underlying compliance determination is lower and cannot be raised until the mandate text is retrieved and interpreted. These are different confidence objects, and conflating them would misrepresent what is known.

---

**Contradictions and Gaps Detected**

*Contradiction 1 — Verdict without standing:* The assessment issues a CRITICAL NON-COMPLIANCE verdict while simultaneously acknowledging that the foundational text required to issue any verdict is unavailable. These two postures are in direct tension. The recommendation correctly flags this, but the status label itself — CRITICAL NON-COMPLIANCE — may be doing governance work (triggering escalation protocols, board notifications, regulatory disclosure obligations) before the evidentiary basis exists to support it. This needs to be surfaced explicitly to the reviewing officer.

*Contradiction 2 — Migration plan velocity vs. definitional uncertainty:* The migration plan is in execution against a target (ca-west-1, ca-central-1, defined scope) that has not been confirmed as the correct target by the mandate text. If the mandate contains conditional provisions, carve-outs, or interim-control thresholds that differ from current assumptions, the migration infrastructure being built now may be optimized against the wrong standard. Velocity here is not a risk mitigant — it is a risk amplifier.

*Gap 1 — Definitional alignment phase is absent from the timeline:* The migration timeline currently moves from 'retrieve mandate' to 'execute migration' without a mandatory intermediate phase: extract scope definitions, interim-control thresholds, and approved-region conditions from the mandate; align them against organizational definitions; identify any divergence; resolve divergence before milestone execution. This phase does not exist on the current plan and must be inserted.

*Gap 2 — Regulatory interpretation contingency is unplanned:* If the mandate text, once retrieved, contains intra-regulatory ambiguity — conditional provisions, jurisdiction-specific carve-outs, or interim-control language that admits multiple reasonable interpretations — the resolution path is regulatory engagement (inquiry to the issuing authority or privacy regulator), not internal gap-closure. There is currently no planned trigger for this path. It must be defined before mandate retrieval, not after.

*Gap 3 — Stress-test calibration:* The current review process has been calibrated to surface evidentiary gaps (missing documents, missing attestations). It has not been systematically calibrated to surface definitional gaps (scope misalignment, contested interim-control thresholds). Both gap types are present. Only one is being consistently caught. This is a process-design issue that the reviewing officer should note for the broader compliance function, independent of this case.

*Evidence not retrieved but required:*

- Full, untruncated text of CORP-SEC-2026-07, including §4.4 and the complete approved-regions list with all conditions
- CISO attestation records for any claimed interim controls
- Third-party processor data residency agreements and any applicable sub-processor chains
- Backup and archive inventory with jurisdiction mapping
- Data lineage documentation sufficient to confirm scope boundaries

---

**Time-Sensitive Actions (sequenced)**

1. **Immediate (within 24 hours):** Assign a named owner to mandate retrieval. This is the blocking dependency for everything downstream. Confirm that the retrieved text is the final, effective version and has not been amended since issuance.
2. **Within 48 hours of retrieval:** Conduct a structured mandate interpretation session — compliance, legal, and the CISO or delegate — focused specifically on: (a) scope boundaries, (b) interim-control eligibility and required attestation format, (c) approved-region conditions, and (d) any conditional or carve-out provisions. Document the output as the authoritative internal interpretation.
3. **Concurrent with step 2:** Define the regulatory engagement trigger. If the interpretation session surfaces genuine intra-regulatory ambiguity, the default path is regulatory inquiry — not an internal judgment call. Define who authorizes that inquiry and on what timeline.
4. **Within one week of mandate retrieval:** Reassess the migration plan against the authoritative interpretation. Confirm that the current timeline, scope, and technical targets are aligned with the actual mandate requirements. If they are not, surface the delta to senior leadership immediately.
5. **Mandatory escalation trigger to CCO and legal:** If the mandate text is not retrieved and the interpretation session is not completed within 10 business days of this routing decision, escalate to URGENT ESCALATION automatically. The January–February 2027 window cannot absorb further delay without compressing the response timeline to a point where principled governance is no longer feasible.

---

**On the Status Label**

The senior compliance officer reviewing this case should consider whether the CRITICAL NON-COMPLIANCE status label, in its current form, should be communicated to governance stakeholders or disclosed externally before the mandate interpretation phase is complete. The underlying condition — production data in a non-Canadian jurisdiction — may well constitute non-compliance. But transmitting a verdict that the compliance function cannot currently defend as evidence-grounded is a separate risk that the reviewing officer must own explicitly. That is not a reason to suppress the assessment; it is a reason to frame it accurately: *probable non-compliance, assessment basis incomplete, full determination pending mandate retrieval and interpretation.*

## **Final Recommendation (Cortexiom-Revised)**

## **Compliance Recommendation: Data Residency Policy CORP-SEC-2026-07 (REVISION 1.0)**

**STATUS: CRITICAL NON-COMPLIANCE - FUNDAMENTAL BASIS UNVERIFIED**

**SUMMARY:** The organization currently operates under a status of critical non-compliance with CORP-SEC-2026-07. While primary PII and SPI data stores reside in non-Canadian jurisdictions, the foundational elements required to accurately assess both the extent of non-compliance and the validity of any asserted interim controls are *missing or incomplete*. The full text of the mandate, particularly concerning interim controls and approved regions, has not been obtained, rendering any assessment of the current posture or future migration plan as speculative. Claims of interim control efficacy remain entirely unverified due to the absence of CISO attestation records and the complete policy text. Furthermore, the scope of data subject to the mandate (including backups, archives, data lineage, and third-party processors) is unconfirmed, making the existing migration plan premature and potentially misaligned with the actual compliance requirements for the March 1, 2027 deadline.

**KEY FINDINGS:**

- **PRIMARY BLOCKER: Incomplete Mandate Text:** The full, untruncated text of CORP-SEC-2026-07, including §4.4 (Interim Controls) and the complete approved regions list (e.g., `ca-west-1` conditions), is unavailable. This is the **primary obstacle** to any accurate assessment of compliance.
- **PRIMARY BLOCKER: Unresolved Interim Control Efficacy:** The claim of interim control efficacy under CORP-SEC-2026-07 §4.4 is asserted but entirely unverified. The threshold question of whether these controls are **preventive (mitigating non-compliance)** or merely **documentary (recording ongoing violations)** remains unanswered due to missing CISO attestations and the incomplete §4.4 text.
- **PRIMARY BLOCKER: Unconfirmed Mandate Scope:** A comprehensive data mapping exercise has not been conducted. The full scope of PII/SPI data requiring residency compliance (specifically including backups, archives, data lineage records, and data handled by third-party processors and contractors) is unconfirmed. This renders the current migration plan's scope as potentially inadequate or misdirected.
- **Absolute Primary Data Residency Violation:** *Assuming an absolute interpretation of the mandate (pending clarification on interim provisions)*, all PII and SPI are currently stored in AWS us-east-1 (Northern Virginia, USA), which is a non-compliant region under CORP-SEC-2026-07.
- **Premature & High Migration Timeline Risk:** The existing migration plan is based on an unconfirmed scope and mandate interpretation. It front-loads critical production migrations into January–February 2027, creating significant concentration risk. Even if its scope were accurate, no migration steps have commenced as of April 30, 2026, making the March 1, 2027 deadline highly improbable without drastic revision.
- **Undetermined Regulatory Interpretation:** There is no documented legal opinion on whether the "absolute-date" language of CORP-SEC-2026-07 allows for interim controls as a recognized defense, creating tension between the organization's risk management approach and potential regulatory interpretation.
- **Lack of Explicit De-risking Strategy in Current Plan:** The provided migration plan lacks explicit strategies to mitigate the concentrated activity risk, which is exacerbated by the unconfirmed scope.

**CORTEXIOM FLAGS (Reiterated & Elevated):**

The Cortexiom Pre-Decision Assessment highlighted the following critical issues regarding the evidence and assessment, which remain unresolved and are now elevated as foundational blockers:

- **CISO attestation records not retrieved:** The primary artifacts to substantiate the claim of interim control compliance are missing from the evidence chain, making verification impossible.
- **Interim control rule truncated:** The complete text of §4.4 is unknown, making it impossible to fully verify if implemented controls meet all requirements or if interim controls are even permissible.
- **Migration plan artifacts not retrieved:** The detailed migration plan was referenced but not provided for review, further limiting the ability to assess its adequacy or feasibility.
- **Contractor and third-party data store inventory missing:** A significant portion of the policy's applicability scope has not been assessed.
- **Data classification inventory missing:** Essential for accurately identifying and prioritizing PII/SPI data for migration.
- **Structural Contradiction:** Asserting compliance with an interim rule set that is truncated creates a logical inconsistency where the assertion cannot be fully validated.
- **Key Governance Question:** The CORTEXIOM assessment specifically flagged: "Who in this organization has been informed, in writing, that the current interim posture is asserted compliance — not verified compliance — and what has been done with that information?" This highlights a critical executive and governance awareness gap.

**ACTION ITEMS:**

---

**P1: Immediate & Critical - Foundational Prerequisites & Governance (May 2026 - June 2026)**

*These actions are absolute prerequisites for any meaningful assessment or planning. Progress on P2/P3 is contingent upon their completion.*

| Action Item | Description | Owner | Due Date |
| --- | --- | --- | --- |
| **P1.1 Retrieve & Review Complete Mandate Text** | Obtain the full, untruncated text of CORP-SEC-2026-07, including §4.4 (Interim Controls) and the complete, qualified approved regions list (e.g., `ca-west-1` conditions). Confirm this is the effective March 1, 2027 version. | CISO, Legal | May 15, 2026 |
| **P1.2 Resolve Preventive/Documentary Control Question** | Obtain and audit all quarterly CISO attestations and supporting technical documentation to explicitly determine if asserted interim controls are **preventive** (actively mitigating non-compliance) or merely **documentary** (recording ongoing violations). This is a technical verification, not just a documentation retrieval. | CISO, Internal Audit, Cloud Infrastructure | May 31, 2026 |
| **P1.3 Commission Comprehensive Data Mapping** | Conduct a full data mapping exercise to explicitly scope all PII/SPI data across *all categories* (primary stores, backups, archives, data lineage records) and *all entities* (internal systems, third-party providers, contractors) against the confirmed CORP-SEC-2026-07 mandate. This will define the *true* migration scope. | Data Governance, CISO, Legal, Procurement | June 30, 2026 |
| **P1.4 Obtain Legal Opinion on Interim Controls** | Secure external legal counsel's opinion on whether CORP-SEC-2026-07's "absolute-date" language admits of any recognized interim control provisions as a valid defense against non-compliance. | Legal Counsel | June 15, 2026 |
| **P1.5 Formal Notification of Unverified Status** | CISO and Legal to formally notify Executive Leadership and the Board that current interim control compliance is *asserted but entirely unverified*, and that the overall compliance status is *critically unconfirmed* due to missing foundational evidence and unresolved mandate interpretation (addressing Cortexiom's key governance question). | CISO, Legal Counsel | May 31, 2026 |
| **P1.6 Establish Mandate Governance Committee** | Form a dedicated steering committee (CISO, VP Eng, Legal, Compliance, Data Governance) to oversee, track, and report on mandate clarification and full scope definition. This committee will then transition to overseeing the *revised* migration plan. | CISO, VP Engineering | May 31, 2026 |

---

**P2: High Priority - Contingent Planning & Refinement (July 2026 - September 2026)**

*These actions can only be reliably planned and executed after P1 items are largely complete.*

| Action Item | Description | Owner | Due Date |
| --- | --- | --- | --- |
| **P2.1 Revise Migration Plan based on Confirmed Scope & Mandate** | Immediately revise the migration plan to evenly distribute critical production migrations across remaining quarters, explicitly incorporating de-risking strategies, rollback procedures, and resource allocation based on the *confirmed* data mapping (P1.3) and mandate interpretation (P1.1, P1.4). | VP Engineering, Cloud Infrastructure Team | July 31, 2026 |
| **P2.2 Resource Assessment & Allocation (Revised)** | Conduct a thorough assessment of personnel, budget, and tools needed for the *revised, comprehensive* migration plan and secure necessary resources. | VP Engineering, HR, Finance | August 31, 2026 |
| **P2.3 Develop Comprehensive Contingency Plan** | Create a robust contingency plan for potential migration delays, technical challenges, fallback options, and clear communication protocols, now informed by the full scope. | VP Engineering, CISO | September 30, 2026 |
| **P2.4 Ongoing Interim Controls Attestation & Monitoring** | Ensure all quarterly CISO attestations are completed and meticulously documented (Q2 2026, Q3 2026), and continuously monitor the effectiveness of these controls *as defined by the confirmed §4.4 text and legal opinion*. | CISO | June 30, Sep 30, 2026 |

---

**P3: Ongoing - Execution, Verification & Closure (October 2026 - April 2027)**

*These actions are contingent upon the successful completion of P1 and P2.*

| Action Item | Description | Owner | Due Date |
| --- | --- | --- | --- |
| **P3.1 Execute Revised Migration Plan** | Systematically execute the accelerated and de-risked migration of all in-scope PII/SPI data stores to compliant regions (e.g., AWS ca-central-1), following the prioritized order defined in P2.1. | Cloud Infrastructure Team | Ongoing, leading to March 1, 2027 |
| **P3.2 Continuous Progress Monitoring** | The Mandate Governance Committee to rigorously monitor progress, identify and address blockers, and report status to executive leadership bi-weekly. | Mandate Governance Committee | Ongoing |
| **P3.3 Post-Migration Independent Audit** | Conduct an independent, comprehensive audit to verify *all* PII/SPI data (including backups, archives, third-party data, etc.) has been successfully migrated to compliant regions and that non-compliant regions no longer host this data. | CISO, Internal Audit (or 3rd Party) | April 30, 2027 |
| **P3.4 Formal Compliance Declaration** | Issue a formal declaration of full compliance with CORP-SEC-2026-07, supported by comprehensive audit evidence, to Executive Leadership and relevant regulatory bodies. | CISO, Legal, Compliance | April 30, 2027 |
| **P3.5 Policy Review & Update** | Initiate the annual review cycle for CORP-SEC-2026-07, incorporating lessons learned from the migration process and any new regulatory guidance. | Legal, CISO, Compliance | Q2 2027 |

---

**CONFIDENCE: Low** Confidence in the *current assessment and the organization's readiness for compliance* is **Low**. This is primarily due to the foundational gaps identified by Cortexiom and reiterated as P1 action items. Without the complete policy text, verified interim control efficacy (preventive vs. documentary), and a confirmed comprehensive scope of data subject to the mandate, any current assessment of compliance posture or migration strategy remains critically unconfirmed and potentially misdirected. Confidence will only increase as the P1 foundational prerequisites are met.

---

**REVISION NOTES:**

This recommendation has undergone a significant revision based on the Cortexiom Post-Recommendation Review, specifically addressing the "Recommended Action" steps:

1. **Status Update:** Changed from "NON-COMPLIANT (with Interim Controls Asserted...)" to "**CRITICAL NON-COMPLIANCE - FUNDAMENTAL BASIS UNVERIFIED**" to explicitly reflect the unconfirmed nature of the mandate's interpretation and the efficacy of interim controls.
2. **Summary Rewrite:** The summary now emphasizes the critical missing foundational elements that prevent an accurate assessment, rather than assuming the basis of compliance.
3. **Key Findings Restructuring:**
    - The top three findings (Incomplete Mandate Text, Unresolved Interim Control Efficacy, Unconfirmed Mandate Scope) are now explicitly flagged as "**PRIMARY BLOCKERS**" reflecting Cortexiom's emphasis on their prerequisite nature.
    - The "Absolute Primary Data Residency Violation" is now qualified with an assumption of an absolute mandate, pending legal clarification.
    - "High Migration Timeline Risk" is reframed as "Premature & High Migration Timeline Risk" to highlight that the plan itself is built on an unconfirmed foundation.
    - "Undetermined Regulatory Interpretation" has been added as a new finding, directly addressing Cortexiom's concern about the tension between risk management and regulatory frameworks.
4. **Cortexiom Flags Elevation:** The original Cortexiom flags are now reiterated and presented as "Elevated" to emphasize their ongoing and critical impact.
5. **Action Items Restructuring:**
    - **P1 Actions** have been completely re-prioritized and augmented to align directly with Cortexiom's "Recommended Actions," making them absolute prerequisites.
        - **P1.1:** Directly addresses Cortexiom's #1: "Obtain and review the complete CORP-SEC-2026-07 text."
        - **P1.2:** Directly addresses Cortexiom's #2: "Resolve the preventive/documentary control question."
        - **P1.3 (New):** Directly addresses Cortexiom's #3: "Commission or confirm a data mapping exercise" (including backups, archives, lineage, third-party processors).
        - **P1.4 (New):** Explicitly calls for a legal opinion on interim controls, addressing Cortexiom's "tension" flag.
        - P1.5 and P1.6 are adjusted to reflect the "unverified" status and the need for new governance over the foundational issues.
    - **P2 and P3 Actions** are now explicitly stated as being *contingent* upon the completion of the P1 foundational prerequisites. Many original P2/P3 items (e.g., initial migration steps) are inherently premature and have been either moved, rephrased, or delayed.
6. **Confidence Update:** Drastically reduced from "Medium" to "**Low**" to accurately reflect the significant unresolved foundational issues identified by Cortexiom, with a clear explanation that confidence is contingent on resolving P1 actions.