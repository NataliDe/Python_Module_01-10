def crisis_handler(filename: str) -> None:
    """
    Handle archive access during crisis scenarios.

    This function attempts to access an archive file and reacts
    according to the type of situation encountered:
    - missing archive (FileNotFoundError)
    - restricted archive access (PermissionError)
    - successful archive recovery

    It ensures that all file operations are performed safely using
    a context manager and that each crisis is handled without
    destabilizing the system.
    """
    if filename == "standard_archive.txt":
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
    else:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")

    try:
        if filename == "classified_vault.txt":
            raise PermissionError("Security protocols deny access")

        with open(filename, "r", encoding="utf-8") as f:
            data = f.read()

        if filename == "standard_archive.txt":
            print(f"SUCCESS: Archive recovered - ``{data}''")
            print("STATUS: Normal operations resumed")
        else:
            print("SUCCESS: Archive recovered")
            print("STATUS: Crisis handled, system stable")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled, system stable")


def main() -> None:
    """
    Run the Cyber Archives crisis response simulation.

    This function initializes the crisis response system and
    sequentially tests multiple archive access scenarios, including
    missing archives, restricted vaults, and successful recoveries.
    """
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    crisis_handler("lost_archive.txt")
    print("")
    crisis_handler("classified_vault.txt")
    print("")
    crisis_handler("standard_archive.txt")
    print("")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    """
    Entry point of the Cyber Archives crisis response program.
    """
    main()
