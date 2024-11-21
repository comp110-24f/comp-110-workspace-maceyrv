"""Examples of dictionary syntax with Ice Cream Shop order tallies."""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

print(len(ice_cream))

ice_cream["mint"] = 10

mint_orders: int = ice_cream["mint"]
print(mint_orders)

ice_cream["mint"] = ice_cream["mint"] + 1
ice_cream["mint"] += 1

ice_cream.pop("strawberry")

print("strawberry" in ice_cream)
print("vanilla" in ice_cream)
for flavor in ice_cream:
    tally: int = ice_cream[flavor]
    print(f"{flavor}: {tally}")
