# Check My Passh

```text
  ____ _               _           __  __             ____               _     
 / ___| |__   ___  ___| | __      |  \/  |_   _      |  _ \ __ _ ___ ___| |__  
| |   | '_ \ / _ \/ __| |/ /      | |\/| | | | |     | |_) / _` / __/ __| '_ \ 
| |___| | | |  __/ (__|   <       | |  | | |_| |     |  __/ (_| \__ \__ \ | | |
 \____|_| |_|\___|\___|_|\_\      |_|  |_|\__, |     |_|   \__,_|___/___/_| |_|
                                          |___/                                 
                                Password Defense Kit


Check My Passh is a defensive utility built to audit password integrity through two lenses: mathematical entropy and known-breach correlation.


Defensive Auditing
The suite calculates entropy to determine a string's resistance to brute force attacks. Following NIST 800-63B guidelines, the tool mandates a 60-bit entropy floor for "Strong" verdicts. Any string found within the local blacklist.txt is automatically flagged as "Weak," as its effective entropy in a targeted attack is zero.

CSPRNG Password Generation

Unlike standard pseudo-random generators (PRNG) which can be deterministic, this tool utilises pythons secrets module. By tapping into OS-level hardware entropy, it ensures generated passwords are cryptographically secure and mathematically unpredictable.

Hash Crack

The cracker acts as a pre-image attack simulation. Because cryptographic hashes are one way fingerprints, the tool generates digests for every entry in a wordlist to find a collision. It includes built-in bit-length validation to filter inputs before processing:

MD5: 128-bit / 32 characters (Legacy)
SHA-1: 160-bit / 40 characters (Deprecated)
SHA-256: 256-bit / 64 characters (Current standard)
