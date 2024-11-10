* Note you would need to Download BOTH "Dictionary_attack.py" & "XOR_KeyBrute.txt" for it to work. *
  
  How to use:
    1. Download Both files, Under "NationalCyberleague" folder from your linux VM, Make sure to place in a nice area.
    2. Modify the "Dictionary_attack.py" and change the value of " ciphertext = "'change-value'" " ,Located in line one, to one desired.
    3. Run this command, " python3 Dictionary_attack.py | grep -B 3 "Congratulations" "
