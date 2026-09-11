import json
from datetime import date, datetime
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "scholarships.json"
TODAY = date.today()


def parse_date(value):
    if not value:
        return None
    return datetime.strptime(value, "%Y-%m-%d").date()


def days_since(value):
    parsed = parse_date(value)
    return None if parsed is None else (TODAY - parsed).days


def main():
    scholarships = json.loads(DATA.read_text())
    reminders = []

    for item in scholarships:
        name = item.get("name", "Unnamed scholarship")
        status = item.get("status", "interested")
        deadline = parse_date(item.get("deadline"))
        decision = parse_date(item.get("decision_date"))
        last_checked_age = days_since(item.get("last_checked"))

        if deadline and status in {"interested", "applying"}:
            days_left = (deadline - TODAY).days
            if 0 <= days_left <= 7:
                reminders.append({
                    "kind": "deadline",
                    "name": name,
                    "title": f"Deadline reminder: {name}",
                    "body": f"**{name}** is due on **{deadline.isoformat()}** ({days_left} day(s) away). Current status: `{status}`."
                })

        if decision and status in {"submitted", "finalist"} and decision <= TODAY:
            reminders.append({
                "kind": "decision",
                "name": name,
                "title": f"Check decision: {name}",
                "body": f"The listed decision date for **{name}** was **{decision.isoformat()}**. Current status: `{status}`. Check the scholarship portal/email and update the tracker."
            })

        if status in {"submitted", "finalist"} and last_checked_age is not None and last_checked_age >= 14:
            reminders.append({
                "kind": "stale",
                "name": name,
                "title": f"Follow up: {name}",
                "body": f"**{name}** hasn't been checked in **{last_checked_age} days**. Current status: `{status}`."
            })

    print(json.dumps(reminders))


if __name__ == "__main__":
    main()
