def archive_creation() -> None:
    """Simulates a data archiving system that creates and writes contents"""
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    try:
        with open("new_discovery.txt", "w") as f:
            print(f"Initializing new storage unit: {f.name}")
            print("Storage unit created successfully...\n")
            print("Inscribing preservation data...")
            f.write("{[}ENTRY 001{]} New quantum algorithm discovered\n")
            f.write("{[}ENTRY 002{]} Efficiency increased by 347%\n")
            f.write("{[}ENTRY 003{]} Archived by Data Archivist trainee\n")
        with open("new_discovery.txt", "r") as f:
            for line in f:
                print(line.strip())
            print()
            print("Data inscription complete. Storage unit sealed.")
            print(f"Archive '{f.name}' ready for long-term preservation.")
    except IOError:
        print("ERROR: Unable to create storage unit. "
              "Check system permissions.")


if __name__ == "__main__":
    archive_creation()
