import operator
import re
from datetime import datetime


def create_sorted_entries(args):
    entries = list()

    for entry in args:
        regex_full_result = re.search(r'\[(.*)\] (.*)', entry)

        new_entry = dict()
        new_entry["date"] = datetime.strptime(regex_full_result.groups()[0], "%Y-%m-%d %H:%M")
        new_entry["log"] = regex_full_result.groups()[1]

        entries.append(new_entry)

    sorted_entries = sorted(entries, key=lambda k: k['date'])
    return sorted_entries


def extract_guard_id(log):
    regex_full_result = re.search(r'.*#(\d+)', log)
    return int(regex_full_result.groups()[0])


def calculate_times(log):
    for key, guard in log.items():
        if "sleep_times" not in guard:
            continue

        sleep_times = guard["sleep_times"]
        if len(sleep_times) == 0:
            continue

        start = None
        end = None
        sorted_times = sorted(sleep_times, key=operator.itemgetter(1))
        for action, time in sorted_times:

            if action == "wake_up":
                end = time
            elif action == "sleep":
                start = time

            if start is not None and end is not None:
                diff = end - start
                guard["asleep_minutes"] += diff.seconds / 60

                minute_start = start.minute
                minute_end = end.minute

                for i in range(minute_start, minute_end, 1):
                    if i in guard["sleep_minutes"]:
                        guard["sleep_minutes"][i] += 1
                    else:
                        guard["sleep_minutes"][i] = 1

                start = None
                end = None

    return log


def main(args):
    entries = create_sorted_entries(args)

    log = dict()

    curr_guard = None
    for entry in entries:
        if "begins shift" in entry["log"]:
            guard_id = extract_guard_id(entry["log"])
            if guard_id not in log:
                log[guard_id] = dict(sleep_times=list(), sleep_minutes=dict(), asleep_minutes=0)
            curr_guard = guard_id

        if "falls asleep" in entry["log"]:
            date = entry["date"]
            log[curr_guard]["sleep_times"].append(('sleep', date))

        if "wakes up" in entry["log"]:
            date = entry["date"]
            log[curr_guard]["sleep_times"].append(('wake_up', date))

    times_calculated = calculate_times(log)

    sleep_minutes = {k: v["asleep_minutes"] for k, v in times_calculated.items()}
    max_asleep_guard = max(sleep_minutes, key=sleep_minutes.get)
    print(f"Most asleep guard #{max_asleep_guard}: {times_calculated[max_asleep_guard]}")
    print("----------------------------")
    print(f"Guard with more sleeps #{max_asleep_guard}: {times_calculated[max_asleep_guard]}")
    print("----------------------------")

    guard_asleep_minutes = times_calculated[max_asleep_guard]["sleep_minutes"]
    
    # TODO: Needs refactoring
    last_val = -1
    max_minute = -1
    for minute, count in guard_asleep_minutes.items():
        if last_val == -1:
            last_val = count
            max_minute = minute
            continue
        if count > last_val:
            last_val = count
            max_minute = minute

    print(f"Max Minute {max_minute}")

    print(f"Multiplication: {max_asleep_guard * max_minute}")


if __name__ == "__main__":
    with open("inputs/input.txt", "r") as r:
        main([line.strip() for line in r.readlines()])
