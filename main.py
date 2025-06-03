max_cas = int(input("Maximální čas (min): "))
odehrano = int(input("Odehráno (min): "))
if input("Úkoly hotové? (ano/ne): ") != "ano":
    print("Nejdřív úkoly.")
elif input("Bylo hodné? (ano/ne): ") != "ano":
    print("Dnes ne.")
elif odehrano >= max_cas:
    print("Čas vyčerpán.")
else:
    print(f"Zbývá {max_cas - odehrano} min.")