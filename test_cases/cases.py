"""
Five compliance test cases designed to demonstrate Cortexiom supervision
improving multi-agent workflow outcomes.

Each case has a structural flaw that the baseline workflow misses:
  Case 1 (PEP EDD): Baseline reads EDD register (all 47 show completion dates)
          but adverse_flags/ is outside evidence_gatherer's scope. 12 clients
          have missing SOF documentation and 5 have critical adverse media hits.
          Cortexiom (CP1) flags the incomplete evidence scope.

  Case 2 (Data Residency): Baseline identifies non-compliance and recommends
          migration. Cortexiom (CP2) catches that Q1 2027 migration plan
          concentrates four production migrations immediately before the deadline,
          conflicting with the audit window.

  Case 3 (HIE Consent): Baseline applies the same US consent framework to Nova
          Scotia. Cortexiom (CP2) flags that PHIPA-NS s.23(1)(a) implied consent
          exception changes the NS compliance posture — US opt-in forms may be
          legally incorrect for NS patients.

  Case 4 (Advisor Disclosure): Baseline reads internal legal opinion (March 2023)
          and recommends disclosure is adequate. Cortexiom (CP2) catches the
          temporal gap: the 2024 CSA guidance tightened the standard AFTER the
          legal opinion was written; the opinion is no longer reliable.

  Case 5 (Cross-Border Transfer): Baseline identifies existing transfer mechanisms.
          Cortexiom (CP1) surfaces the Singapore gap: DataMetrics SG transfer is
          planned for Q3 2026 with no SCC in place and no adequacy decision in force.
"""

TEST_CASES: list[dict] = [
    {
        "id": "pep_edd",
        "title": "PEP Enhanced Due Diligence Review",
        "description": (
            "Annual compliance review of EDD status for 47 PEP clients. "
            "The EDD register shows all clients have completion dates on file. "
            "FINTRAC requires four separate components: SOF, SOW, AMS, and EM."
        ),
        "regulation": "edd_regulation.md",
        "topic": "PEP EDD enhanced due diligence source funds screening",
        "request": (
            "Review our PEP client register for FINTRAC EDD compliance. "
            "Confirm whether all 47 PEP clients have adequate EDD documentation "
            "and identify any remediation required."
        ),
        "expected_baseline_flaw": (
            "Baseline will report all 47 clients as EDD-complete based on "
            "completion dates in the register, without identifying the 12 clients "
            "with missing SOF documentation or 5 with active adverse media flags."
        ),
        "expected_cortexiom_catch": (
            "Cortexiom CP1 (pre_decision): Evidence limited to knowledge_base/ — "
            "adverse_flags/ directory not searched. EDD register shows dates but "
            "not component-level completion. Structural gap creates regulatory exposure."
        ),
    },
    {
        "id": "data_residency",
        "title": "Data Residency Compliance Assessment",
        "description": (
            "Assessment of compliance with CORP-SEC-2026-07 (effective March 1, 2027). "
            "All production data stores are currently in AWS us-east-1 (non-compliant). "
            "Migration planning is underway."
        ),
        "regulation": "data_residency_policy.md",
        "topic": "data residency PII AWS cloud storage migration compliance",
        "request": (
            "Assess our current compliance posture against the data residency policy "
            "CORP-SEC-2026-07 and provide a remediation roadmap."
        ),
        "expected_baseline_flaw": (
            "Baseline identifies non-compliance and recommends migration to "
            "ca-central-1, but does not flag the Q1 2027 migration plan risk: "
            "four production migrations scheduled within 6 weeks of the deadline, "
            "overlapping with the mandatory Q1 2027 compliance audit."
        ),
        "expected_cortexiom_catch": (
            "Cortexiom CP2 (post_recommendation): Migration plan concentrates "
            "4 production migrations in Jan–Feb 2027, same period as the Q1 audit. "
            "Interim control attestation Q2 2026 is also overdue. "
            "Recommend separating migration timeline from audit window."
        ),
    },
    {
        "id": "hie_consent",
        "title": "Health Information Exchange Consent Audit",
        "description": (
            "Audit of HIE patient consent mechanisms across California, Texas, and "
            "Nova Scotia operations. Current setup uses a uniform US opt-in "
            "authorization form (HC-US-01) in all three jurisdictions."
        ),
        "regulation": "hie_consent_regulation.md",
        "topic": "HIE health information exchange consent HIPAA PHIPA patient authorization",
        "request": (
            "Audit whether our current HIE consent framework is compliant across "
            "all operating jurisdictions (California, Texas, Nova Scotia)."
        ),
        "expected_baseline_flaw": (
            "Baseline identifies CA and TX as compliant (CMIA + HB 300 forms in place). "
            "For Nova Scotia, baseline applies the same US opt-in logic and may flag "
            "the lack of PHIPA-NS specific review as a gap — but does not identify "
            "that PHIPA-NS implied consent may mean the US opt-in form is wrong, "
            "not just incomplete."
        ),
        "expected_cortexiom_catch": (
            "Cortexiom CP2 (post_recommendation): Nova Scotia PHIPA-NS s.23(1)(a) "
            "implied consent exception changes the compliance posture. US opt-in form "
            "applied to NS patients may impose legally unsupported burdens and create "
            "uncertainty about patient rights under provincial law. The issue is not "
            "missing a PHIPA form — it is using the wrong consent mechanism entirely."
        ),
    },
    {
        "id": "advisor_disclosure",
        "title": "Advisor Conflict of Interest Disclosure Review",
        "description": (
            "Review of advisor compensation disclosure adequacy under NI 31-103 s.13.4. "
            "Performance bonuses average $22,400/year. Current disclosure is Appendix C "
            "boilerplate. Internal legal opinion (March 2023) says disclosure is adequate."
        ),
        "regulation": "advisor_conflict_disclosure.md",
        "topic": "advisor compensation disclosure conflict interest performance bonus CSA",
        "request": (
            "Assess whether our advisor performance bonus disclosure in Appendix C "
            "of the RDD meets current NI 31-103 requirements."
        ),
        "expected_baseline_flaw": (
            "Baseline reads the internal legal opinion (March 2023) and concludes "
            "disclosure is adequate. It may note the 2024 CSA guidance as a future "
            "consideration but will likely give low urgency to the disclosure gap "
            "because the legal opinion exists."
        ),
        "expected_cortexiom_catch": (
            "Cortexiom CP2 (post_recommendation): Legal opinion (March 2023) predates "
            "CSA Staff Notice 31-362 (August 2024) by 17 months. The 2024 standard "
            "explicitly requires plain-language disclosure of dollar ranges — not met "
            "by Appendix C boilerplate. The legal opinion is not reliable for assessing "
            "compliance with the current standard. This is a P1 remediation item."
        ),
    },
    {
        "id": "cross_border_transfer",
        "title": "Cross-Border Data Transfer Compliance Check",
        "description": (
            "Review of cross-border data transfer mechanisms before the planned "
            "DataMetrics SG Pte Ltd (Singapore) engagement in Q3 2026. "
            "Existing transfer arrangements cover EU, UK, Switzerland, US, India."
        ),
        "regulation": "cross_border_data_transfer.md",
        "topic": "cross border data transfer PIPEDA SCC contractual clauses Singapore",
        "request": (
            "Confirm whether our cross-border data transfer arrangements are sufficient "
            "to proceed with the planned Singapore vendor engagement in Q3 2026."
        ),
        "expected_baseline_flaw": (
            "Baseline confirms existing arrangements (EU, UK, CH, US, India) are "
            "documented and finds no immediate violations. May note Singapore as "
            "'planned' but understate the urgency given the Q3 2026 timeline."
        ),
        "expected_cortexiom_catch": (
            "Cortexiom CP1 (pre_decision): Singapore adequacy decision is pending "
            "(not in force). No SCC currently executed with DataMetrics SG. "
            "Q3 2026 start date conflicts with typical SCC negotiation timeline "
            "(6-8 weeks). Any data transfer before SCCs are signed is an immediate "
            "PIPEDA violation. P1 action required now — do not wait."
        ),
    },
]