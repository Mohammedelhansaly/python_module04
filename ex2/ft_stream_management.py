import sys


def stream_management() -> None:
    """Simulates a communication system using standard input/output streams"""
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    sys.stdout.write("Input Stream active. Enter archivist ID:")
    sys.stdout.flush()
    archivist_id = sys.stdin.readline().strip()
    sys.stdout.write("Input Stream active. Enter status report:")
    sys.stdout.flush()
    status_id = sys.stdin.readline().strip()
    sys.stdout.write(f"\n[STANDARD] Archive status from "
                     f"{archivist_id}: {status_id}\n")
    sys.stderr.write("[ALERT] System diagnostic: "
                     "Communication channels verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")
    print()
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    stream_management()
