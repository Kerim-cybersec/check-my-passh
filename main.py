from logic import PasswordTool
import os

def draw_box(title, content_list):
    width = 60
    print("\n┌" + "─" * (width - 2) + "┐")
    print(f"│ {title.center(width - 4)} │")
    print("├" + "─" * (width - 2) + "┤")
    for line in content_list:
        print(f"│ {line.ljust(width - 4)} │")
    print("└" + "─" * (width - 2) + "┘")

ASCII_ART = """
  ____ _               _           __  __             ____               _     
 / ___| |__   ___  ___| | __      |  \/  |_   _      |  _ \ __ _ ___ ___| |__  
| |   | '_ \ / _ \/ __| |/ /      | |\/| | | | |     | |_) / _` / __/ __| '_ \ 
| |___| | | |  __/ (__|   <       | |  | | |_| |     |  __/ (_| \__ \__ \ | | |
 \____|_| |_|\___|\___|_|\_\      |_|  |_|\__, |     |_|   \__,_|___/___/_| |_|
                                          |___/                                  
               Check My Passh: Password Defense Kit
"""

def run_suite():
    tool = PasswordTool()
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(ASCII_ART)
        print(" [1] Strength Checker")
        print(" [2] Secure Password Generator")
        print(" [3] Hash Cracker")
        print(" [Q] Quit")
        
        choice = input("\nSelect an option: ").lower().strip()

        if choice == "1":
            print("\n--- TOOL DEFINITIONS ---")
            print("ENTROPY: A score of randomness. Above 60 is strong.")
            print("PWNED STATUS: Checks if your password is in a known data breach list.")
            while True:
                pwd = input("\nEnter password to test (or 'b' for menu): ").strip()
                if pwd.lower() == 'b': break
                
                entropy = tool.get_entropy(pwd)
                pwned = pwd in tool.blacklist
                
                results = [
                    f"Password: {pwd}",
                    f"Entropy Score: {entropy} bits",
                    f"Pwned Before? {'YES' if pwned else 'NO'}",
                    f"Verdict: {'STRONG' if entropy > 60 and not pwned else 'WEAK'}"
                ]
                draw_box("SECURITY ASSESSMENT", results)
                
                print("\n[!] Ready for next input...")
        
        elif choice == "2":
            print("\nThis tool generates cryptographically strong passwords.")
            while True:
                print("\nChoose a length: [A] 8 | [B] 12 | [C] 16 | [M] Menu")
                len_choice = input("Selection: ").lower().strip()
                if len_choice == 'm': break
                
                lengths = {'a': 8, 'b': 12, 'c': 16}
                if len_choice in lengths:
                    l = lengths[len_choice]
                    pwd = tool.generate_secure(l)
                    draw_box("SECURE GENERATION", [f"Password: {pwd}", f"Entropy: {tool.get_entropy(pwd)} bits"])
                else:
                    print("Invalid choice.")

        elif choice == "3":
            while True:
                print("\n--- HASH CRACKER MENU ---")
                print(" [A] MD5 | [B] SHA-1 | [C] SHA-256 | [M] Menu")
                algo_choice = input("Select algorithm: ").lower().strip()
                if algo_choice == 'm': break
                
                algos = {'a': 'md5', 'b': 'sha1', 'c': 'sha256'}
                expected_lengths = {'md5': 32, 'sha1': 40, 'sha256': 64}
                
                if algo_choice not in algos:
                    print("Invalid selection.")
                    continue
                
                selected_algo = algos[algo_choice]
                target = input(f"Paste {selected_algo.upper()} hash: ").strip()
                
                if len(target) != expected_lengths[selected_algo]:
                    print(f"\nERROR: Invalid {selected_algo.upper()} length.")
                    continue

                show_live = input("Show live crack? (y/n): ").lower() == 'y'
                print(f"\n[*] Scanning for match...")
                result = tool.crack_hash(target, algo=selected_algo, verbose=show_live)
                
                if result:
                    draw_box("CRACK SUCCESSFUL", [f"Plaintext: {result}", f"Algo: {selected_algo.upper()}"])
                else:
                    print("\n[-] No match found.")
                
                input("\nPress Enter to return to cracker menu...")

        elif choice == "q":
            print("Exiting Check My Passh...")
            break

if __name__ == "__main__":
    run_suite()