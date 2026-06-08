# Workflow Stage Contracts

In `create-academic-research` repositories, stage work starts with the matching
preflight command and prompt:

| Stage | Command | Primary contract |
|---|---|---|
| Literature | `npm run workflow:literature` | `sota/sota-claim-ledger.csv` |
| Survey | `npm run workflow:survey` | `survey/survey-claim-ledger.csv` |
| Agenda | `npm run workflow:agenda` | `research_agenda/opportunity-ledger.csv` |
| Contribution | `npm run workflow:contribution` | `contributions/contribution-ledger.csv` |
| Analysis | `npm run workflow:analysis` | contribution-local `analysis.yaml` |
| Frame | `npm run workflow:frame` | `paper_frames/frame-ledger.csv` |
| Release | `npm run workflow:release` | `paper_releases/release-ledger.csv` |
| Manuscript | `npm run workflow:manuscript` | `reports/paper/manuscript-ledger.csv` |
| Submission | `npm run workflow:submission` | `paper_submissions/submission-ledger.csv` |
| Response | `npm run workflow:response` | `paper_submissions/templates/review-rounds/` |

Every stage follows the same discipline:

1. Run the npm preflight when available.
2. Read the prompt in `docs/agent/workflow-prompts/`.
3. Read the local contract files before producing durable output.
4. Update ledgers and manifests instead of relying on prose-only memory.
5. Work in small slices.
6. Run adversarial review, fix, and re-review until no blocking issue remains.
7. Keep review history outside final artifacts.
8. Hand off only clean reviewed outputs.

If the repository does not contain the expected scaffold, report the missing
contract files and work conservatively instead of inventing alternate paths.
