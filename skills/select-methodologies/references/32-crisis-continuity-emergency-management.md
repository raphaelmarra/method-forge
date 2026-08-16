# Crisis, continuity, emergency, incident, and recovery management

Use this catalog when the primary decision concerns organizational resilience, what must continue or recover, active incident coordination, executive crisis leadership, emergency/disaster management, ICT recovery, exercising, or post-incident improvement. Use `13-legal-policy-ethics.md` for legal authority, compliance, rights, ethics, and public-policy analysis; use `27` for crisis communication and `06` for specialist technical safety/security assurance.

## Capability boundaries

| Capability | Primary method | Output | Do not confuse with |
| --- | --- | --- | --- |
| Disaster-risk reduction | Sendai Framework 2015–2030 + local law/strategy | prevention, vulnerability/exposure reduction, preparedness, resilient recovery | one organization's continuity plan |
| Organizational resilience | ISO 22316 | cross-capability adaptive-resilience principles and portfolio | incident playbook or certifiable requirements |
| Business continuity | ISO 22301 + BIA | BCMS, prioritized services, strategies, plans, exercises, improvement | immediate incident command or ICT-only recovery |
| Business Impact Analysis — BIA | ISO/TS 22317 method | impacts over time, priorities, minimum capacity, dependencies, recovery requirements | generic risk register or technology-chosen RTO |
| Crisis management | ISO 22361 | executive crisis team, strategic decisions, legitimacy, values, communication, learning | tactical incident management or media relations alone |
| Incident/emergency management | ISO 22320 / locally authorized ICS | command, objectives, common operating picture, resources, incident action | strategy, continuity, or routine tickets |
| Cyber incident response | NIST SP 800-61 Rev. 3 / sector process | integrated preparation, detection, response, recovery, and improvement | all-hazards crisis/BCMS or one universal forensic runbook |
| ICT readiness / disaster recovery | ISO/IEC 27031:2025 + tested recovery architecture | backups, failover/rebuild, runbooks, integrity, RTO/RPO evidence | continuity of people, facilities, suppliers, and non-ICT work |
| Exercise and improvement program | ISO 22398 / HSEEP-style process | objectives, scenario, observations, AAR, owned improvement and retest | scripted demonstration or plan review without performance evidence |
| After-Action Review / incident learning | learning method | observations, explanations, decisions, actions, owners, and effectiveness checks | blame session or action closure without retest |

Continuity asks what must continue or recover and by when. Incident management coordinates active response. Crisis management governs strategic legitimacy and executive decisions. Disaster recovery restores ICT. They interact but are not synonyms.

## Composition patterns

### Crisis and continuity stack

`risk/dependency context → ISO 22316 frame → ISO 22301 BCMS → BIA → continuity/ICT strategies → exercises → ISO 22320/ICS incident activation + ISO 22361 strategic crisis leadership → recovery → AAR, remediation, and retest`

### Active incident stack

`detection/notification → authority and incident classification → command + safety objectives → common operating picture → incident action/resource plan → executive escalation triggers → public/risk communication in 27 → stabilization → recovery transition → evidence preservation → AAR and retest`

Do not let the same active-response team independently certify readiness or closure when consequences are material.

## Research anchors and status

Status checked 2026-08-12. Verify local emergency authority, sector rules, and current owner editions before implementation.

- [ISO 22301:2019](https://www.iso.org/standard/75106.html) plus Amendment 1:2024 remains current; a later committee draft is not a published replacement.
- [ISO/TS 22317:2021](https://www.iso.org/standard/79000.html), [ISO 22320:2018](https://www.iso.org/standard/67851.html), and [ISO 22361:2022](https://www.iso.org/standard/50267.html) distinguish BIA, incident management, and crisis management.
- [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) is the final 2025 cyber-incident-response publication; it supersedes Rev. 2.
- ISO/IEC 27031:2025 is the current ICT-readiness/continuity edition and replaces 2011.
- [Sendai Framework 2015–2030](https://www.undrr.org/publication/sendai-framework-disaster-risk-reduction-2015-2030) remains active through 2030.
