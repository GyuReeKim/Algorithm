num = 5
card = '49679'

card_dict = {}
for c in card:
    if c in card_dict:
        card_dict[c] += 1
    else:
        card_dict[c] = 1
print(card_dict)

key_list = []
val_list = []
for key, val in card_dict.items():
    key_list.append(key)
    val_list.append(val)

print(key_list)
print(val_list)