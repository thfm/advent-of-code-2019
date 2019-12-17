def get_layers(image, width, height):
    image = list(str(image))
    layer_size = width * height

    layers = []
    i = 0
    while i * layer_size < len(image):
        layers.append(image[i * layer_size:(i + 1) * layer_size])
        i += 1
    return layers


INPUT_IMAGE = int(open("res/day_eight_inputs.txt").read())
LAYERS = get_layers(INPUT_IMAGE, 25, 6)

ZERO_COUNTS = {}
for layer in LAYERS:
    ZERO_COUNTS[layer.count("0")] = layer

LOWEST_ZEROES = min(list(ZERO_COUNTS.keys()))
TARGET_LAYER = ZERO_COUNTS.get(LOWEST_ZEROES)
print(TARGET_LAYER.count("1") * TARGET_LAYER.count("2"))
