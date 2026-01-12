FILENAME = "ancient_fragment.txt"


def main() -> None:
    """
    Recover and display data from an ancient archive file.

    This function opens the file `ancient_fragment.txt`, reads all
    preserved data, and prints it to the standard output following
    the Cyber Archives recovery protocol.

    If the file does not exist, an error message is displayed and
    the recovery process is aborted.
    """
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {FILENAME}")

    try:
        f = open(FILENAME, "r", encoding="utf-8")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
        return

    try:
        data = f.read()
    finally:
        f.close()

    print("Connection established...\n")
    print("RECOVERED DATA:")
    if data:
        print(data)
    print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    """
    Entry point of the Cyber Archives data recovery program.
    """
    main()
