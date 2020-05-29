count = 1 
while True:
    s = input()
    if s== "#":
        break
    else:
        if s.upper() == "HELLO":
            print(f"Case {count}: ENGLISH")
        elif s.upper() == "HOLA":
            print(f"Case {count}: SPANISH")
        elif s.upper() == "HALLO":
            print(f"Case {count}: GERMAN")
        elif s.upper() == "BONJOUR":
            print(f"Case {count}: FRENCH")
        elif s.upper() == "CIAO":
            print(f"Case {count}: ITALIAN")
        elif s.upper() == "ZDRAVSTVUJTE":
            print(f"Case {count}: RUSSIAN")
        else:
            print(f"Case {count}: UNKNOWN")

        count +=1