# ============================================================
# LIST METHODS DEMONSTRATION - SPORTS REGISTRATION SYSTEM
# ============================================================
# A register of participants for the sports event.
# This program demonstrates all common Python list methods
# using a sports registration system.

# ---------- Creating a list ----------
participants = []   # empty list
print("Starting registration...")
print("Initial participants list:", participants)

# ---------- append() - adds an item at the END ----------
participants.append("MAk")
participants.append("Maria")
participants.append("Alex")
participants.append("Sara")
print("\nAfter append() (add at end):")
print(participants)

# ---------- insert() - adds an item at a specific position ----------
participants.insert(1, "David")   # insert at index 1
print("\nAfter insert(1, 'David') (add at position):")
print(participants)

# ---------- extend() - adds multiple items from another list ----------
new_players = ["Priya", "Rahul"]
participants.extend(new_players)
print("\nAfter extend() (add multiple items):")
print(participants)

# ---------- remove() - removes first matching item by value ----------
participants.remove("Alex")
print("\nAfter remove('Alex') (remove by value):")
print(participants)

# ---------- pop() - removes & returns last item (or at index) ----------
last_player = participants.pop()
print("\nAfter pop() (remove last item):")
print("Removed player:", last_player)
print(participants)

# ---------- index() - returns index of first matching item ----------
print("\nindex('Maria'):", participants.index("Maria"))

# ---------- count() - counts how many times an item appears ----------
participants.append("John")
participants.append("John")
print("\nAfter adding 'John' twice more:")
print(participants)
print("count('John'):", participants.count("John"))

# ---------- sort() - sorts the list in place ----------
participants.remove("John")
participants.remove("John")
participants.sort()
print("\nAfter sort() (alphabetical order):")
print(participants)

# ---------- reverse() - reverses the order of the list ----------
participants.reverse()
print("\nAfter reverse() (reversed order):")
print(participants)

# ---------- copy() - creates a copy of the list ----------
backup_list = participants.copy()
print("\nAfter copy() (backup list):")
print(backup_list)
# ---------- clear() - removes all items from the list ----------
backup_list.clear()
print("\nAfter clear() (backup list is now empty):")
print(backup_list)

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("SUMMARY OF LIST METHODS USED")
print("=" * 80)
print("list.append(item)   - add item at end")
print("list.insert(i, item) - add item at index i")
print("list.extend([...])  - add multiple items")
print("list.remove(item)   - remove item by value")
print("list.pop()          - remove & return last item")
print("list.index(item)    - get index of item")
print("list.count(item)    - count occurrences of item")
print("list.sort()         - sort the list")
print("list.reverse()      - reverse the list")
print("list.copy()         - copy the list")
print("list.clear()        - remove all items")
print("=" * 80)
print("\nFinal participants list:", participants)
