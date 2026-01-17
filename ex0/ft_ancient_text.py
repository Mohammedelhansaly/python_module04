def data_recovery() -> None:
    """Simulates a data recovery system that reads and displays contents"""
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    try:
        f = open("ancient_fragment.txt", "r")
        print(f"Accessing Storage Vault: {f.name}")
        print("Connection established...\n")
        print("RECOVERED DATA:")
        for line in f:
            print(line.strip())
        print()
        print("Data recovery complete. Storage unit disconnected.")
        f.close()
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    data_recovery()
