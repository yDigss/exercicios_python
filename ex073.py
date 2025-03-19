times = (
    "Botafogo",
    "Palmeiras",
    "Flamengo",
    "Fortaleza",
    "Internacional",
    "São Paulo",
    "Corinthians",
    "Bahia",
    "Cruzeiro",
    "Vasco da Gama",
    "Vitória",
    "Atlético Mineiro",
    "Fluminense",
    "Grêmio",
    "Juventude",
    "Red Bull Bragantino",
    "Athletico Paranaense",
    "Criciúma",
    "Atlético Goianiense",
    "Cuiabá"
)
print("-="*15)
for t in times:
    print(t)
print("-="*15)
print(f"Os 5 primeiros colocados são {times[0:5]}")
print("-="*15)
print(f"Os quatro ultimos são {times[-4:]}")
print("-="*15)
print(f"Times em ordem alfabetica {sorted(times)}")