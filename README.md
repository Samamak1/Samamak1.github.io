# Sama Mushtaq - Program and Project Leadership Portfolio

[View the live portfolio](https://samamak1.github.io/)

> Operator accountability, program leadership, cross-functional delivery, and systems-building across technology, operations, launches, and founder-led ventures.

This repository contains the source for Sama Mushtaq's public portfolio. The site is designed for Program Manager and Project Manager recruiting conversations and emphasizes business stakes, mandate, decisions, delivery systems, adoption, and evidence rather than a gallery of outputs.

## Portfolio status

- **Deployment:** live public static site on GitHub Pages
- **Audience:** Program Manager, Project Manager, and cross-functional operations hiring teams
- **Content status:** selected cases and resume are published
- **Evidence discipline:** claims are separated into dated snapshots, operating records, founder-reported aggregates, reconstructions, and illustrative prototypes

## Positioning

Sama's operating pattern is consistent across industries:

1. Frame the business outcome and baseline.
2. Translate ambiguity into workstreams, owners, dependencies, and acceptance criteria.
3. Align stakeholders around tradeoffs and decision rights.
4. Establish a governance cadence for risks, metrics, and escalation.
5. Build training, documentation, and ownership into delivery.
6. Measure the result and institutionalize what worked.

## Selected program cases

| Program | Sama's mandate | Delivery evidence | Outcome status |
|---|---|---|---|
| [RYGNeco](https://samamak1.github.io/work/rygneco/) | Co-Founder and Program Lead; field workflow, product requirements, vendor delivery, acceptance, and reporting direction. | Vendor-built dashboard prototype, sanitized workflow reconstruction, and reconstructed delivery roadmap. | Pilot and program facts are aggregate operating claims; dashboard values are fictional sample data. |
| [Hard Rock Casino Cincinnati](https://samamak1.github.io/work/hard-rock/) | Operations Manager -> AGM -> Acting GM; financial controls, workforce capability, adoption, and management cadence. | Original server-certification artifact plus sanitized operating-model reconstruction. | Aggregate operating results are leadership-account claims; confidential P&Ls and employee records are withheld. |
| [iTZCALi Tapas and Tequila](https://samamak1.github.io/work/itzcali/) | **Director of Operations / Launch Consultant; not owner or founder.** | Sanitized launch roadmap, operating photo, pricing system, layouts, menu, and process evidence. | Aggregate launch outcomes are operating-record and leadership-account claims. |
| [MAK Trading](https://samamak1.github.io/work/mak-trading/) | Founder and Program Lead; brand, acquisition, onboarding, curriculum, membership, retention, and platform migration. | Direct Stripe snapshots and sanitized platform reconstruction. | Approximately 2,000 peak community members and more than 1,200 cumulative paid subscribers across the program lifetime are founder-reported aggregates; MRR and active-subscription figures are dated Stripe snapshots. |

## Supporting operating systems

- [Alcohol pricing decision system](https://github.com/Samamak1/alcohol-pricing-engine): invoice-to-pour-cost and POS pricing workbooks.
- [Crew scheduling engine](https://github.com/Samamak1/crew-scheduling-engine): sanitized representative reconstruction of operational tooling used to produce posted schedules.
- [Restaurant Imaging program](https://github.com/Samamak1/restaurant-imaging-program): standards corrective-action cadence, ownership, photo evidence, and re-walk governance.
- [Casino steakhouse analytics](https://github.com/Samamak1/steakhouse-gm-analytics): redacted beverage-profitability business case and capability programs.
- [Restaurant buildout](https://github.com/Samamak1/restaurant-buildout): operating workstreams and artifacts from the iTZCALi launch engagement.

## Evidence standards

The portfolio uses explicit provenance labels so visual polish is not mistaken for stronger proof than the source supports.

| Label | Meaning |
|---|---|
| Documented platform snapshot | Direct capture from a source platform at a specific point in time. |
| Operating record | Aggregate result supported by historical operating materials that remain private. |
| Leadership-account claim | Result reported from Sama's management records or direct operating knowledge; not independently audited in the public repository. |
| Original artifact | Historical work product shown substantially as created, with publication review. |
| Sanitized original | Historical artifact with identities, confidential values, or sensitive fields physically removed. |
| Reconstruction | Retrospective recreation of the operating model after sensitive details were removed. |
| Representative sample | Fresh output created from anonymized or substitute data while preserving system behavior. |
| Illustrative prototype | Product or interface concept containing fictional or sample values; not evidence of business results. |

## Repository structure

```text
/
|-- index.html                  Portfolio home
|-- style.css                   Shared visual system and responsive layout
|-- script.js                   Navigation, interaction, and print behavior
|-- images/                     Reviewed public evidence and site imagery
|-- work/
|   |-- rygneco/                Zero-to-one product program case
|   |-- hard-rock/              Operational transformation case
|   |-- itzcali/                Restaurant launch case
|   `-- mak-trading/            Community and recurring-revenue case
|-- resume/
|   |-- index.html              Web resume
|   `-- *.pdf                   One-page formatted resume
|-- scripts/                    Build, validation, and resume-generation scripts
`-- package.json                Local validation and build commands
```

## Local validation

Requirements: Node.js for site validation and the documented Python/PDF dependencies only when rebuilding the resume PDF.

```bash
npm run check
npm run build
```

- `npm run check` runs the repository's static checks.
- `npm run build` produces the validated static-site output.

Review the home page, every case page, the web resume, and the PDF at desktop and mobile widths before deployment. Evidence images require a separate visual privacy review because automated checks cannot determine whether an identity should be public, and CSS cropping is not treated as source-file redaction.

## Role, contributors, and authorship

Sama Mushtaq supplied the source records, career context, operating decisions, claim approvals, and final acceptance for this portfolio. The underlying programs were delivered with employees, managers, co-founders, vendors, contractors, advisers, and system partners as identified in each case.

The portfolio distinguishes between:

- Work Sama personally authored or led
- Work implemented by vendors or collaborators under his program direction
- Reconstructed presentation artifacts
- Direct platform evidence
- Aggregate claims whose detailed records remain private

The portfolio does not claim that Sama personally wrote every line of vendor software, performed every frontline task, or created third-party platform interfaces.

## AI assistance

AI tools assisted with portfolio research, information architecture, writing, coding, document generation, and testing. Sama provided the source material, corrected role and metric details, decided what could be published, and accepted the final result.

AI assistance in presenting the portfolio is not presented as authorship of the underlying historical operating work. Individual supporting repositories disclose AI involvement in the original work where the public record establishes it, including the crew scheduling and Restaurant Imaging programs.

## Confidentiality and publication controls

- No employee roster, applicant record, payroll record, client inventory, device identifier, confidential P&L, or trading-performance record should be published.
- Prototype figures must remain labeled fictional or illustrative.
- Aggregate metrics must retain their evidence labels and time boundaries.
- Vendor-implemented interfaces must not be described as personally coded by Sama.
- Redaction must occur in the source artifact, not only through CSS or layout.
- Any new artifact requires both content review and visual privacy review before deployment.

## Limitations

- This is a self-authored professional portfolio, not an independent audit.
- Selected evidence is intentionally incomplete because detailed employer, employee, client, and member records remain private.
- Some outcomes are leadership-account claims rather than directly published source records.
- Reconstructed visuals explain operating systems but are not substitutes for original evidence.
- The site presents selected programs and does not represent every role or project.

## Licensing and reuse

No license is currently granted for personal photographs, resume content, case-study text, brand materials, or evidence images. If source code is intended for reuse, add an explicit code license and separately state that personal content and media remain excluded from that license.

## Contact

- [LinkedIn](https://www.linkedin.com/in/samamushtaq/)
- [GitHub](https://github.com/Samamak1)
- [Live portfolio](https://samamak1.github.io/)
