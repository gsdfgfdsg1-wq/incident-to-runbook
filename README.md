# incident-to-runbook

A dependency-free CLI that turns structured incident timelines into reviewable Markdown Runbook drafts.

## Quick start

```bash
python runbook.py incident.json
```

Incident events use `symptom`, `check`, or `action` types. The output extracts symptoms, verification checks, and mitigation commands. Actions flagged as destructive are explicitly marked as requiring approval.

## Test

```bash
python -m unittest discover -v
```

## License

MIT.
