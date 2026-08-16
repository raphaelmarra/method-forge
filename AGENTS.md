# Agent contribution rules

Treat `skills/select-methodologies` as the installable product and its `references/` directory as the canonical catalog.

Before editing, route the change to the canonical domain owner defined by the taxonomy. Do not create a second definition of a method when domain tailoring is sufficient.

For volatile standards, regulations, software specifications, and jurisdictional claims, verify the current primary source and record the check date. Preserve the distinction between what an owner defines and what independent evidence supports.

Keep repository documentation in English. Keep the skill identifier `select-methodologies` stable unless a compatibility plan is accepted through an ADR.

Run `python tools/validate_repository.py` before handing off changes. Record durable architectural, licensing, taxonomy, or governance decisions in `docs/adr/` without rewriting accepted history.
