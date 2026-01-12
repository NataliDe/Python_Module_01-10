import sys


def main() -> None:
    """
    Demonstrate three-channel stream communication.

    This function collects archivist identification and status
    information via standard input, then sends messages through
    the appropriate system streams:
    - standard output for normal messages
    - standard error for alert messages

    This simulates the Cyber Archives communication protocol,
    where data channels must never be mixed.
    """
    sys.stdout.write("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n\n")

    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")

    sys.stdout.write(
        "{[}STANDARD{]} Archive status from "
        + archivist_id
        + ": "
        + status
        + "\n"
    )
    sys.stderr.write(
        "{[}ALERT{]} System diagnostic: "
        "Communication channels verified\n"
    )
    sys.stdout.write("{[}STANDARD{]} Data transmission complete\n")
    sys.stdout.write("Three-channel communication test successful.\n")


if __name__ == "__main__":
    """
    Entry point of the Cyber Archives communication system.
    """
    main()
