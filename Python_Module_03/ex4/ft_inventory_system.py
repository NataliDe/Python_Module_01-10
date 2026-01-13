#!/usr/bin/env python3
"""
Player Inventory System

This script demonstrates how to use Python dictionaries to manage
and analyze player inventories in a simple RPG-style scenario.
"""


def main() -> None:
    """
    Main entry point of the inventory system.
    Creates inventories, performs analytics, and prints results.
    """

    print("=== Player Inventory System ===")

    # Alice's inventory
    alice_inventory = {
        "sword": {
            "quantity": 1,
            "category": "weapon",
            "rarity": "rare",
            "value": 500,
        },
        "potion": {
            "quantity": 5,
            "category": "consumable",
            "rarity": "common",
            "value": 50,
        },
        "shield": {
            "quantity": 1,
            "category": "armor",
            "rarity": "uncommon",
            "value": 200,
        },
    }
    """Dictionary storing Alice's inventory items."""

    # Bob's inventory
    bob_inventory = {
        "potion": {
            "quantity": 0,
            "category": "consumable",
            "rarity": "common",
            "value": 50,
        },
        "magic_ring": {
            "quantity": 1,
            "category": "accessory",
            "rarity": "rare",
            "value": 300,
        },
    }
    """Dictionary storing Bob's inventory items."""

    print("=== Alice's Inventory ===")

    total_value = 0
    total_items = 0
    categories = {}

    # Display Alice's inventory
    for name, item in alice_inventory.items():
        qty = item.get("quantity")
        cat = item.get("category")
        rarity = item.get("rarity")
        value = item.get("value")

        item_total = qty * value
        total_value += item_total
        total_items += qty

        categories[cat] = categories.get(cat, 0) + qty

        print(
            f"{name} ({cat}, {rarity}): "
            f"{qty}x @ {value} gold each = {item_total} gold"
        )

    print(f"Inventory value: {total_value} gold")
    print(f"Item count: {total_items} items")

    # Print categories
    category_output = []
    for cat, qty in categories.items():
        category_output.append(f"{cat}({qty})")

    print("Categories: " + ", ".join(category_output))

    print("=== Transaction: Alice gives Bob 2 potions ===")

    # Transaction logic
    if alice_inventory["potion"]["quantity"] >= 2:
        alice_inventory["potion"]["quantity"] -= 2
        bob_inventory["potion"]["quantity"] += 2
        print("Transaction successful!")
    else:
        print("Transaction failed!")

    print("=== Updated Inventories ===")
    print(f"Alice potions: {alice_inventory['potion']['quantity']}")
    print(f"Bob potions: {bob_inventory['potion']['quantity']}")

    print("=== Inventory Analytics ===")

    # Calculate inventory values
    alice_value = 0
    for item in alice_inventory.values():
        alice_value += item.get("quantity") * item.get("value")

    bob_value = 0
    for item in bob_inventory.values():
        bob_value += item.get("quantity") * item.get("value")

    # Most valuable player
    if alice_value >= bob_value:
        print(f"Most valuable player: Alice ({alice_value} gold)")
    else:
        print(f"Most valuable player: Bob ({bob_value} gold)")

    # Count total items
    alice_items = 0
    for item in alice_inventory.values():
        alice_items += item.get("quantity")

    bob_items = 0
    for item in bob_inventory.values():
        bob_items += item.get("quantity")

    if alice_items >= bob_items:
        print(f"Most items: Alice ({alice_items} items)")
    else:
        print(f"Most items: Bob ({bob_items} items)")

    # Find rare items
    rarest = []

    for name, item in alice_inventory.items():
        if item.get("rarity") == "rare":
            rarest.append(name)

    for name, item in bob_inventory.items():
        if item.get("rarity") == "rare":
            rarest.append(name)

    print("Rarest items: " + ", ".join(rarest))


if __name__ == "__main__":
    main()
