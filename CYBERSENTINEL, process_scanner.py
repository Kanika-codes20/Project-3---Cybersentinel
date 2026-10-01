import psutil
import risk_analyzer
import startup_scanner

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




