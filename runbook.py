#!/usr/bin/env python3
"""Convert a structured incident timeline into an executable runbook draft."""
import argparse
import json
from pathlib import Path


def extract(incident):
    symptoms = [event["text"] for event in incident.get("events", []) if event.get("type") == "symptom"]
    checks = [event["text"] for event in incident.get("events", []) if event.get("type") == "check"]
    actions = [{"command": event["text"], "approval_required": bool(event.get("destructive"))} for event in incident.get("events", []) if event.get("type") == "action"]
    return {"title": incident.get("title", "Incident runbook"), "symptoms": symptoms, "checks": checks, "actions": actions}


def markdown(runbook):
    lines = [f"# {runbook['title']}", "", "## Symptoms"]
    lines += [f"- {item}" for item in runbook["symptoms"]] or ["- None recorded"]
    lines += ["", "## Checks"] + [f"- {item}" for item in runbook["checks"]]
    lines += ["", "## Actions"] + [f"- {'[Approval required] ' if item['approval_required'] else ''}`{item['command']}`" for item in runbook["actions"]]
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("incident")
    args = parser.parse_args()
    print(markdown(extract(json.loads(Path(args.incident).read_text()))))


if __name__ == "__main__":
    main()
