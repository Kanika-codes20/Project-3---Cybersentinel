import hashlib
import json
from pathlib import Path
from datetime import datetime
import psutil
import risk_analyzer
import startup_scanner

def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("CyberSentinel.log", "a") as log_file:
        log_file.write("[" + timestamp + "] " + message + "\n")


def scan_processes():
    print("=" * 50)
    print("CYBERSENTINEL PROCESS SCANNER")
    print("=" * 50)

    startup_programs = startup_scanner.get_startup_programs()

    for process in psutil.process_iter():
        try:
            name = process.name()
            path = process.exe()

            score, reasons = risk_analyzer.calculate_risk(path, startup_programs)
            level = risk_analyzer.risk_level(score)

            print("Name:", name)
            print("Path:", path)
            print("Risk:", level)
            print("Score:", score)

            if reasons:
                print("Reasons:")

                for reason in reasons:
                    print("-", reason)

                print("-" * 50)

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

def scan_startup():
    print("="*50)
    print("CYBERSENTINEL STARTUP SCANNER")
    print("="*50)

    startup_programs = startup_scanner.get_startup_programs()
    for program in startup_programs:
        print(program)

def calculate_hash(filename):
    sha256 = hashlib.sha256()

    with open(filename, 'rb') as file:
        while True:
            chunk = file.read(4096)
            if not chunk:
                break
            sha256.update(chunk)
    return sha256.hexdigest()

def create_baseline(folder):
    baseline = {}
    for file in folder.iterdir():
        if file.is_file():
            file_hash = calculate_hash(file)
            baseline[str(file)] = file_hash

    with open("baseline.json", "w") as file:
        json.dump(baseline, file, indent=4)

    print("\n Baseline created!\n")

def scan_files(folder):
    log_event("Scan started.")

    with open("baseline.json", "r") as file:
        baseline = json.load(file)

    current_files = set()

    unchanged_count = 0
    modified_count = 0
    new_count = 0
    deleted_count = 0

    alerts = []

    for file in folder.iterdir():
        if file.is_file():
            file_path = str(file)
            current_files.add(file_path)
            current_hash = calculate_hash(file)

            if file_path not in baseline:

                print("NEW FILE:", file_path)
                new_count += 1
                alerts.append("New file detected: " + file_path)

            elif current_hash != baseline[file_path]:
                print("MODIFIED:", file_path)
                modified_count += 1
                alerts.append("Modified file detected:  " + file_path)

            else:
                print("UNCHANGED: ", file_path)
                unchanged_count += 1

    for file_path in baseline:
        if file_path not in current_files:
            print("DELETED:" , file_path)
            deleted_count += 1
            alerts.append("Deleted file detected: " + file_path)

    for alert in alerts:
        log_event(alert)

    print()
    print("="*40)
    print("SCAN SUMMARY")
    print("="*40)

    print("Unchanged files:", unchanged_count)
    print("Modified files:" , modified_count)
    print("Deleted files:", deleted_count)
    print("New files:" , new_count)

    log_event(
        f"Scan completed | Unchanged: {unchanged_count}"
        f" | Modified: {modified_count}"
        f"| New: {new_count}"
        f"| Deleted: {deleted_count}"
    )

    print()
    print("="*40)
    print("SECURITY ALERTS")
    print("="*40)

    if alerts:
        for alert in alerts:
            print("⚠", alert)
    else:
        print("No security relevant changes detected.")

folder = Path("monitored_files")

while True:

    print()
    print("=" * 50)
    print("CYBERSENTINEL")
    print("=" * 50)

    print("1. Process Scanner")
    print("2. Startup scanner")
    print("3. Create baseline")
    print("4. Scan Files")
    print("5. Exit")

    choice = input("Enter your choice:").strip().lower()


    if choice == "1":
        scan_processes()
    elif choice == "2":
        scan_startup()
    elif choice == "3":
        create_baseline(folder)
    elif choice == "4":
        scan_files(folder)
    elif choice == "5":
        print("Exiting Cybersentinel....")
        break
    else:
        print("Invalid Choice.")




