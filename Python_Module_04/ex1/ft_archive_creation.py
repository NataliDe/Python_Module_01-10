FILENAME = "new_discovery.txt"


def main() -> None:
    """
    Create and populate a new archive file.

    This function opens (or creates) the file `new_discovery.txt`
    in write mode and inscribes three preservation entries into it.
    Each entry represents critical archival information intended
    for long-term digital preservation.

    If the storage unit cannot be created or accessed, an error
    message is displayed and the operation is safely aborted.
    """
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print(f"Initializing new storage unit: {FILENAME}")

    try:
        f = open(FILENAME, "w", encoding="utf-8")
    except OSError:
        print("ERROR: Could not create storage unit.")
        return

    try:
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")

        lines = [
            "[ENTRY 001] New quantum algorithm discovered",
            "[ENTRY 002] Efficiency increased by 347%",
            "[ENTRY 003] Archived by Data Archivist trainee",
        ]

        for line in lines:
            f.write(line)

        for line in lines:
            print(line)

    finally:
        f.close()

    print("\nData inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    """
    Entry point of the Cyber Archives preservation program.
    """
    main()
