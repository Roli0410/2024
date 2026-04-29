szelesseg = float(input("Kérem a szoba szélességét: "))
magassag = float(input("Kérem a szoba hosszúságát: "))
parketta  = int(input("Hány csomag parketta van: "))
terulet = szelesseg * magassag
parketta_terulet = parketta * 2
print(f"A szoba területe {terulet:.2f} négyzetméter.") #terulet:.2f = 2 tizedes jegyre kerekítés




if parketta_terulet >= terulet:
    print("Van elegendő parketta!")
else:
    print("Szükséges még parkettát vásárolni!")

