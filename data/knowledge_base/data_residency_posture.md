# Current Data Residency Posture — Infrastructure Inventory
**Last Updated:** April 30, 2026
**Owner:** VP Engineering / Cloud Infrastructure Team
**Status:** UNDER REVIEW — Data Residency Policy CORP-SEC-2026-07 in effect

---

## Primary Data Store

| System | Cloud Provider | Region | Region ID | Data Types | Record Count |
|--------|---------------|--------|-----------|------------|-------------|
| Customer Database | AWS | Northern Virginia, USA | us-east-1 | PII, financial records | ~2.4M records |
| Transaction Ledger | AWS | Northern Virginia, USA | us-east-1 | Financial transactions, PII | ~18M records |
| Document Storage | AWS S3 | Northern Virginia, USA | us-east-1 | Contracts, ID documents | ~340K files |
| Analytics Platform | AWS Redshift | Northern Virginia, USA | us-east-1 | Aggregated PII, behavioral data | ~4B rows |

**Current compliance status:** NON-COMPLIANT with CORP-SEC-2026-07. All primary systems are located in AWS us-east-1 (Virginia, USA), which is explicitly listed as a non-compliant region under the policy.

---

## Security Controls (Currently in Place)

- **Encryption at rest:** AES-256 via AWS KMS (enabled on all data stores)
- **Encryption in transit:** TLS 1.3 enforced on all endpoints
- **Access control:** IAM roles with least-privilege; MFA required for all admin access
- **Network:** VPC with private subnets; no direct internet access to DB tier
- **Geo-restriction:** AWS WAF geo-blocking for non-CA/US IPs on customer-facing endpoints
- **Logging:** CloudTrail enabled; 90-day retention

These controls satisfy the **interim requirements** under CORP-SEC-2026-07 §4.4 during the migration period.

---

## Migration Planning Status

| Milestone | Target Date | Status |
|-----------|------------|--------|
| Architecture assessment | June 30, 2026 | In progress |
| Target region selection (AWS ca-central-1) | July 15, 2026 | Not started |
| Development environment migration | September 1, 2026 | Not started |
| Staging environment migration | November 1, 2026 | Not started |
| Production data migration (Customer DB) | January 15, 2027 | Not started |
| Production data migration (Transaction Ledger) | February 1, 2027 | Not started |
| Production data migration (Document Storage) | February 15, 2027 | Not started |
| Analytics Platform migration | February 25, 2027 | Not started |
| Policy deadline | March 1, 2027 | — |

**Assessment:** The current migration plan places four production migrations in January–February 2027, immediately before the March 1, 2027 deadline. This creates significant concentration risk in Q1 2027, the same period as the scheduled internal compliance audit.

---

## Quarterly Attestation

| Quarter | CISO Attestation | Date |
|---------|-----------------|------|
| Q3 2025 | Interim controls in place | September 15, 2025 |
| Q4 2025 | Interim controls in place | December 12, 2025 |
| Q1 2026 | Interim controls in place | March 18, 2026 |
| Q2 2026 | DUE | June 30, 2026 |

---

*This is a synthetic infrastructure document created for demonstration purposes.*