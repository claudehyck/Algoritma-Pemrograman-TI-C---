# Program Perintah Robot (Arah, Langkah)

perintah = ("maju", 15)

match perintah :
    case ("diam", 0) | ("berhenti", 0):
        print("Robot tetap di tempat")
    
    case ("maju", langkah) if langkah > 10: # guard
        print(f"Robot maju cepat sejauh {langkah} meter")

    case ("mundur", _):
        print("Robot bergerak mundur")

    case _:
        print("Perintah tidak valid")
