import sys


def crisis_manager(filename, routine=False) -> None:
    """Handles access to cyber archives with error management."""
    header = "ROUTINE ACCESS" if routine else "CRISIS ALERT"
    print(f"{header}: Attempting access to '{filename}'...")
    try:
        with open(filename, "r") as f:
            content = f.readline().strip()
            print(f"SUCCESS: Archive recovered - ``{content}''")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    except Exception as e:
        print(f"RESPONSE: Unexpected system anomaly - {type(e).__name__}")
    if routine:
        print("STATUS: Normal operations resumed")
    elif "PermissionError" in sys.exc_info():
        print("STATUS: Crisis handled, security maintained")
    else:
        print("STATUS: Crisis handled, system stable")
    print()


def ft_crisis_response() -> None:
    """Simulates a crisis response system for cyber archives."""
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    crisis_manager("lost_archive.txt")
    crisis_manager("/root/classified_vault.txt")
    crisis_manager("standard_archive.txt", routine=True)
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    ft_crisis_response()
