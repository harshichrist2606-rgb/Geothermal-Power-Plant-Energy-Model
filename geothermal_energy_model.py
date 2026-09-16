print("GEOTHERMAL POWER PLANT ENERGY MODEL")

thermal_power = float(input("Enter thermal power input (MW): "))
efficiency = float(input("Enter plant efficiency (%): "))
hours = float(input("Enter operating hours per day: "))
days = int(input("Enter number of operating days: "))

# Electrical power output
electrical_power = thermal_power * (efficiency / 100)

# Energy generation
daily_energy = electrical_power * hours
total_energy = daily_energy * days

# Heat rejected
heat_rejected = thermal_power - electrical_power

print("\n--- RESULTS ---")
print(f"Thermal Power Input : {thermal_power:.2f} MW")
print(f"Electrical Output   : {electrical_power:.2f} MW")
print(f"Daily Energy        : {daily_energy:.2f} MWh")
print(f"Total Energy        : {total_energy:.2f} MWh")
print(f"Heat Rejected       : {heat_rejected:.2f} MW")
print(f"Plant Efficiency    : {efficiency:.2f} %")

if efficiency >= 15:
    print("Plant Status        : GOOD")
else:
    print("Plant Status        : LOW EFFICIENCY")
