# scholarship-tracker

cuz i need to keep track of scholarships

A tiny public tracker for scholarships I applied to, deadlines, decision dates, and results.

## Statuses

- `interested` — found it, haven't applied yet
- `applying` — application in progress
- `submitted` — application sent
- `finalist` — advanced / waiting on final decision
- `awarded` — won 🎉
- `not_selected` — did not receive it
- `closed` — no longer pursuing

## How to add a scholarship

Edit `scholarships.json` and add an entry like:

```json
{
  "name": "Example Scholarship",
  "amount": 2500,
  "url": "https://example.com",
  "applied_date": "2026-09-11",
  "deadline": "2026-10-01",
  "decision_date": "2026-11-15",
  "status": "submitted",
  "last_checked": "2026-09-11",
  "notes": "Applied through school portal"
}
```

Use `null` when you don't know a date or amount yet.

## Automatic reminders

GitHub Actions checks the tracker every day. It opens a GitHub issue when:

- a deadline is within 7 days and the scholarship isn't submitted yet
- a decision date has arrived and the status is still `submitted` or `finalist`
- a submitted/finalist application hasn't been checked in 14+ days

The workflow avoids opening the same reminder issue twice.

## Important

Don't put private information in this repo. Since it's public, keep names, addresses, application IDs, essays, financial documents, and other personal data out of `scholarships.json`.