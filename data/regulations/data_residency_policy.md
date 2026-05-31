# Internal Data Residency Policy — CORP-SEC-2026-07
**Issuing Authority:** Chief Information Security Officer
**Effective Date:** March 1, 2027
**Review Cycle:** Annual
**Classification:** Internal — Restricted

---

## 1. Purpose

This policy establishes mandatory requirements for the storage, processing, and transmission of Personally Identifiable Information (PII) and Sensitive Personal Information (SPI) held by the organization. It is issued in response to the Canadian government's Digital Charter Implementation Act and provincial privacy law amendments effective Q1 2026.

## 2. Scope

Applies to all business units, subsidiaries, contractors, and third-party service providers handling organizational data on behalf of the company.

## 3. Definitions

- **Canadian Jurisdiction**: Data physically stored and processed within the geographic boundaries of Canada (any province or territory).
- **PII**: Any information that can identify an individual directly or in combination with other data (name, SIN, address, financial account numbers, health identifiers).
- **SPI**: Subset of PII including financial records, health data, biometric data, and government identifiers.
- **Non-Compliant Region**: Any data center or cloud region located outside Canadian jurisdiction.

## 4. Requirements

### 4.1 Data Residency — Mandatory

All PII and SPI collected or processed by the organization **must be stored in Canadian jurisdictions only** as of the effective date.

The following regions are explicitly **non-compliant** with this policy:
- AWS us-east-1 (Northern Virginia, USA)
- AWS us-east-2 (Ohio, USA)
- AWS us-west-1, us-west-2
- All GCP regions outside `northamerica-northeast1` and `northamerica-northeast2`
- All Azure regions outside `canadacentral` and `canadaeast`

### 4.2 Compliant Regions

Approved cloud regions as of policy issuance:
- **AWS**: ca-central-1 (Montreal), ca-west-1 (Calgary — available Q3 2026)
- **GCP**: northamerica-northeast1 (Montreal), northamerica-northeast2 (Toronto)
- **Azure**: canadacentral (Toronto), canadaeast (Quebec City)

### 4.3 Migration Deadline

All systems storing PII/SPI must be migrated to compliant regions **no later than March 1, 2027** (18 months from policy issuance).

### 4.4 Interim Controls

During the migration period (September 1, 2025 – February 28, 2027), all non-compliant data stores must maintain:
1. AES-256 encryption at rest
2. TLS 1.3 in transit
3. Geo-restriction on access (Canadian IP blocks only, with documented exceptions)
4. Quarterly attestation to CISO that interim controls remain in place

### 4.5 Audit Window

An internal compliance audit will be conducted **Q1 2027** (January–February 2027) to verify readiness before the mandatory deadline. Systems not ready by the Q1 2027 audit are subject to accelerated remediation and executive escalation.

## 5. Non-Compliance Consequences

Failure to comply by March 1, 2027 may result in:
- Suspension of business operations in affected provincial markets
- Regulatory referral under PIPEDA / provincial privacy legislation
- Disclosure obligations to affected data subjects
- Fines up to $25 million CAD under the Digital Charter Implementation Act

## 6. Exceptions

Exceptions require written approval from the CISO and Legal Counsel. Approved exceptions must be documented in the exception register and reviewed quarterly.

---

*This is a synthetic policy document created for demonstration purposes.*