msi_rtxa5000_price = 4199.35
gigabyte_aero_price = 4295.54
razer_blade15_price = 3696.99
asus_zephyrus_m16_price = 1849.79
msi_laptop_creator_17 = 3505.90
alienware_x15 = 2199.99

prices = [4199.35, 4295.54, 3696.99, 1849.79, 3505.90, 2199.99]

q = max(msi_rtxa5000_price, msi_laptop_creator_17, gigabyte_aero_price, razer_blade15_price, asus_zephyrus_m16_price, alienware_x15)
w = min(msi_rtxa5000_price, msi_laptop_creator_17, gigabyte_aero_price, razer_blade15_price, asus_zephyrus_m16_price, alienware_x15)
e = round(msi_rtxa5000_price)
r = round(gigabyte_aero_price)
t = round(razer_blade15_price)
y = round(asus_zephyrus_m16_price)
u = round(msi_laptop_creator_17)
i = round(alienware_x15)
o = sum(prices) / len(prices)
p = round(o)

print(f"The most expensive laptop price is: {q}")
print(f"The least expensive laptop price is: {w}")
print(f"The rounded price of the MSI RTX 5000 is: {e} ")
print(f"The rounded price of the Gigabyte Aero is: {r} ")
print(f"The rounded price of the Razer Blade 15 is: {t} ")
print(f"The rounded price of the Asus Zephyrus is: {y} ")
print(f"The rounded price of the MSI Laptop Creator 17 is: {u} ")
print(f"The rounded price of the Alienware X15 is: {i} ")
print(f"The average price of all of these laptops is: {p}")