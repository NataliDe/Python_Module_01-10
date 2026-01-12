#!/usr/bin/env python3

CLASSIFIED_FILE = "classified_data.txt"
PROTOCOLS_FILE = "security_protocols.txt"


def main() -> None:
    """
    Perform secure vault operations using context managers.

    This function demonstrates safe access to classified archival data
    by reading from a protected storage vault and writing new security
    protocols into a separate archive file.

    The `with` statement guarantees that all vault connections are
    automatically closed, even if an error occurs during the operation.
    Appropriate error handling is used to respond to missing or
    restricted archives.
    """
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")
    print("SECURE EXTRACTION:")

    try:
        with open(CLASSIFIED_FILE, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("ERROR: Classified vault missing. Run data generator first.")
        return
    except PermissionError:
        print("ERROR: Security protocols deny access")
        return

    if content:
        print(content)

    print("SECURE PRESERVATION:")
    try:
        with open(PROTOCOLS_FILE, "w", encoding="utf-8") as f:
            f.write("[CLASSIFIED] New security protocols archived\n")
    except PermissionError:
        print("ERROR: Security protocols deny access")
        return

    print("[CLASSIFIED] New security protocols archived")
    print("Vault automatically sealed upon completion")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    """
    Entry point of the Cyber Archives vault security program.
    """
    main()
