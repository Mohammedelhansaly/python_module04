def vaul_security() -> None:
    """Simulates a vault security system that reads classified data"""
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    try:
        print("Initiating secure vault access...")
        print("Vault connection established with failsafe protocols\n")
        print("SECURE EXTRACTION:")
        with open("classified_data.txt", "r") as f:
            for line in f:
                print(line.strip())
        print()
        print("SECURE PRESERVATION:")
        with open("security_protocols.txt", "w") as f:
            f.write("[CLASSIFIED] New security protocols archived")
            print("[CLASSIFIED] New security protocols archived")
    except FileNotFoundError:
        print("ERROR: Vault access failed. Ensure all"
              " security files are present.")
    except IOError:
        print("ERROR: Unable to create storage unit. "
              "Check system permissions.")
    finally:
        print("Vault automatically sealed upon completion\n")
        print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    vaul_security()
