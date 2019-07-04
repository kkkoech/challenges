def pizza_slices(cuts):
    return int(1 + cuts * (cuts + 1) / 2)

print(f'1 cuts -> {pizza_slices(1)}')
print(f'2 cuts -> {pizza_slices(2)}')
print(f'3 cuts -> {pizza_slices(3)}')
print(f'4 cuts -> {pizza_slices(4)}')

