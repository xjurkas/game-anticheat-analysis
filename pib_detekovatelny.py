import pymem
def open_game_process(process_name):   # Otvorí herný proces
    try:
        pm = pymem.Pymem(process_name)
        print(f"Herný proces {process_name} bol úspešne otvorený.")
        return pm
    except Exception as e:
        print(f"Chyba pri otváraní procesu: {e}")
        return None
def modify_memory_value(pm, address, new_value):   # Pokusí sa zmeniť hodnotu na pamäťovej adrese
    try:
        pm.write_int(address, new_value)
        print(f"Hodnota na adrese {hex(address)} bola úspešne zmenená na {new_value}.")
    except Exception as e:
        print(f"Chyba pri zápise do pamäte na adrese {hex(address)}: {e}")
def main():
    process_name = input("Zadajte názov herného procesu (napr. 'valorant.exe'): ")      # Zadanie názvu herného procesu
    pm = open_game_process(process_name)    # Otvorí proces
    if pm is None:
        return
    try:
        memory_address = int(input("Zadajte pamäťovú adresu (hexadecimálne, napr. '0x17CA0'): "), 16)   # Zadanie pamäťovej adresy
    except ValueError:
        print("Zadaná adresa je neplatna.")
        return
    try:
        new_value = int(input("Zadajte novú hodnotu (celé číslo): "))   # Zadanie novej hodnoty
    except ValueError:
        print("Neplatná hodnota.")
        return
    modify_memory_value(pm, memory_address, new_value)  # Pokus o zmenu hodnoty na pamäťovej adrese
if __name__ == "__main__":
    main()
