import winreg

def get_startup_programs():
    startup_programs = []

    key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"

    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            key_path
        )

        number_of_entries = winreg.QueryInfoKey(key)[1]

        for i in range(number_of_entries):
            name, value, _ = winreg.EnumValue(key, i)

            startup_programs.append(value)

        winreg.CloseKey(key)

    except (FileNotFoundError,PermissionError):
        pass
    return startup_programs





