#Vytvořte pole, které bude mít 5 stringových hodnot
array = ["fotbal", "balón", "hřiště", "rozhodčí", "hráči"]
print("Základní pole:", array)
#Přidejte pomocí metody append() jeden prvek. - "vítr"
array.append("vítr")
print("Pole po přidání pomocí append:", array)
#Odstraňte pomocí metody remove() druhý prvek z pole
array.remove(array[1])
print("Pole po odstranění pomocí remove:", array)
#Zaměňte 5 hodnotu z pole za: "slunce"
array[4] = "slunce"
print("Pole po zaměnění 5 hodnoty z pole:", array)
#Přidejte 2 stringové hodnoty pole pomocí metody extend()
array.extend(["trenér", "penalta"])
print("Pole po přídání 2 stringových hodnot:", array)
#Vypište základní vytvořené pole a potom každé pole, ve kterém uděláte změnu

