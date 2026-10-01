# CyberSentinel

CyberSentinel is a beginner-friendly defensive cybersecurity project built with Python.

The project combines several security-monitoring features to help identify potentially suspicious processes and detect changes to monitored files.

It was created as a learning project to explore Python programming while developing an understanding of basic cybersecurity concepts.

## Features

### 1. Process Scanner

CyberSentinel scans running processes and analyzes them for potentially suspicious characteristics.

The project uses `psutil` to gather process information and a risk-analysis system to assign a risk score.

Some indicators can increase the risk score, such as:

- An executable being located in the Downloads folder
- A process being registered as a startup program

The scanner then assigns a risk level based on the score:

- **LOW**
- **MEDIUM**
- **HIGH**

### 2. Startup Scanner

CyberSentinel checks the Windows user's startup entries using the Windows Registry.

It specifically checks the user's `Run` registry location for programs configured to start automatically.

A process being registered as a startup program can contribute to its risk score.

### 3. File Integrity Monitor

CyberSentinel can monitor selected files for unexpected changes.

The project uses **SHA-256 hashing** to create a baseline for monitored files.

The program can identify files that are:

- Unchanged
- Modified
- New
- Deleted

A `baseline.json` file is used to store the baseline information.

### 4. Security Event Logging

CyberSentinel records important events in a local log file.

The logging system records events with timestamps using the following format:

```text
YYYY-MM-DD HH:MM:SS
```

The generated log file is called:

```text
CyberSentinel.log
```

This file is intentionally excluded from the GitHub repository using `.gitignore`.

## Technologies Used

- Python
- `psutil`
- `hashlib`
- `winreg`
- `json`

## Python Concepts Practiced

This project helped me practice several Python concepts, including:

- Functions
- Variables
- Lists
- Dictionaries
- Conditional statements
- Loops
- String methods
- File handling
- JSON files
- Modules and imports
- Exception handling
- Working with external libraries
- SHA-256 hashing

## Cybersecurity Concepts

Through this project, I explored:

- Process monitoring
- Basic risk scoring
- Suspicious-process indicators
- Startup-program monitoring
- File integrity monitoring
- Cryptographic hashing
- Security event logging
- Defensive security

## How the Risk Scoring Works

CyberSentinel assigns points when certain indicators are detected.

For example, an executable located in the Downloads folder can add to the risk score, while a program registered as a startup entry can add another risk indicator.

The final score is then used to determine the risk level.

The project uses the following levels:

```text
LOW       → 0
MEDIUM    → 1–25
HIGH      → Above 25
```

The score is intended as a simple educational risk indicator rather than a definitive determination that a process is malicious.

## How to Run

1. Make sure Python is installed.
2. Install the required dependency:

```bash
pip install psutil
```

3. Clone or download this repository.
4. Open the project in PyCharm or another Python IDE.
5. Run the main Python file.
6. Use the menu to select the available scanning and monitoring options.

## Project Structure

```text
CyberSentinel/
│
├── cybersentinel.py
├── risk_analyzer.py
├── startup_scanner.py
├── baseline.json
├── README.md
└── .gitignore
```

`CyberSentinel.log` is generated while the program runs and is excluded from the repository.

## Example

CyberSentinel can produce results such as:

```text
Risk Score: 25
Risk Level: MEDIUM

Reasons:
- Executable is located in Downloads
- Registered as startup program
```

The File Integrity Monitor can also report results such as:

```text
Unchanged: 1
Modified: 1
New: 0
Deleted: 0
```

## Limitations

CyberSentinel is an educational project and should not be considered a complete antivirus, EDR, or malware-detection system.

Its risk indicators are intentionally simple and can produce false positives or miss sophisticated threats.

The project is designed to demonstrate fundamental defensive-security concepts rather than provide comprehensive real-world threat detection.

## What I Learned

Building CyberSentinel helped me connect Python programming concepts with cybersecurity.

I learned how to work with running processes, Windows startup entries, file hashes, JSON data, and security logs.

The project also helped me understand how multiple smaller security features can be combined into one defensive monitoring tool.

## Future Improvements

Possible future improvements could include:

- More process-risk indicators
- Additional startup locations
- A more detailed reporting system
- A graphical user interface
- More advanced file-monitoring options

These features are outside the scope of the current beginner version of CyberSentinel.

---

**Educational defensive cybersecurity project built with Python. 🐍🛡️**
