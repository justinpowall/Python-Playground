import os
import uuid
from datetime import datetime, timedelta
from modules.ui import c, header, divider, success, error, info, prompt, option_prompt
from modules.ui import CYAN, MAGENTA, YELLOW, GREEN, BOLD, DIM, RED

EVENTS_FILE = os.path.join(os.path.dirname(__file__), "..", "events.ics")


def _load_events():
    """Parse events from the .ics file, return list of dicts."""
    events = []
    if not os.path.exists(EVENTS_FILE):
        return events
    with open(EVENTS_FILE, "r") as f:
        lines = [l.rstrip("\n") for l in f]
    i = 0
    while i < len(lines):
        if lines[i] == "BEGIN:VEVENT":
            ev = {}
            i += 1
            while i < len(lines) and lines[i] != "END:VEVENT":
                if ":" in lines[i]:
                    key, _, val = lines[i].partition(":")
                    ev[key] = val
                i += 1
            events.append(ev)
        i += 1
    return events


def _save_events(events):
    """Write events list back to the .ics file."""
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Python Playground//Calendar//EN",
    ]
    for ev in events:
        lines.append("BEGIN:VEVENT")
        for key, val in ev.items():
            lines.append(f"{key}:{val}")
        lines.append("END:VEVENT")
    lines.append("END:VCALENDAR")
    with open(EVENTS_FILE, "w") as f:
        f.write("\n".join(lines) + "\n")


def _fmt_dt(dtstr):
    """Format a DTSTART/DTEND string like 20260311T130000 for display."""
    try:
        dt = datetime.strptime(dtstr, "%Y%m%dT%H%M%S")
        return dt.strftime("%Y-%m-%d %I:%M %p")
    except ValueError:
        return dtstr


def _list_events(events):
    if not events:
        info("No upcoming events.")
        return
    print()
    for idx, ev in enumerate(events, 1):
        title = ev.get("SUMMARY", "(no title)")
        start = _fmt_dt(ev.get("DTSTART", ""))
        end   = _fmt_dt(ev.get("DTEND", ""))
        print(f"  {c(f'[{idx}]', YELLOW, BOLD)}  {c(title, CYAN, BOLD)}")
        print(f"        {c('Start:', DIM)} {start}   {c('End:', DIM)} {end}")
    print()


def _add_event():
    header("Add Calendar Event")
    title     = prompt("Event title:").strip()
    if not title:
        error("Title cannot be empty.")
        return
    date_str  = prompt("Date (YYYY-MM-DD):").strip()
    start_str = prompt("Start time (HH:MM, 24h):").strip()
    end_str   = prompt("End time   (HH:MM, 24h):").strip()
    try:
        start_dt = datetime.strptime(f"{date_str} {start_str}", "%Y-%m-%d %H:%M")
        end_dt   = datetime.strptime(f"{date_str} {end_str}",   "%Y-%m-%d %H:%M")
    except ValueError:
        error("Invalid date/time format.")
        return
    ev = {
        "UID":     str(uuid.uuid4()),
        "SUMMARY": title,
        "DTSTART": start_dt.strftime("%Y%m%dT%H%M%S"),
        "DTEND":   end_dt.strftime("%Y%m%dT%H%M%S"),
    }
    events = _load_events()
    events.append(ev)
    _save_events(events)
    success(f'Event "{title}" saved to events.ics')


def run():
    header("Calendar Events")
    while True:
        divider()
        events = _load_events()
        _list_events(events)
        print(f"  {c('[a]', YELLOW, BOLD)}  Add event")
        print(f"  {c('[b]', YELLOW, BOLD)}  Back to main menu")
        choice = option_prompt()
        if choice == "a":
            _add_event()
        elif choice == "b":
            break
        else:
            print(c("  Invalid option.", DIM))
