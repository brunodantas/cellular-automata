from PIL import Image

# arithmetic rule implementation

def make_rule(rule_number):
    rule = [int(n) for n in format(rule_number, "08b")]
    rule = list(reversed(rule))  # wolfram style
    # print(rule)
    return rule

def apply_rule(rule, value):
    # print(value)
    return rule[value]

def make_generation(rule, previous_gen):
    gen = []
    indexes = list(range(-(neighborhood_size//2), neighborhood_size//2 + 1))
    neighbors = [previous_gen[x] for x in indexes]
    value = sum([neighbors[i]*pows[i] for i in range(neighborhood_size)])
    index1 = indexes[0]
    last = indexes[-1]
    for _ in range(len(previous_gen)):
        first = previous_gen[index1]*pows[0]
        output = apply_rule(rule, value)
        gen.append(output)
        index1 = (index1+1)%len(previous_gen)
        last = (last+1)%len(previous_gen)
        value = 2*(value - first) + previous_gen[last]
    # print(gen)
    return gen

def render_ca(generations):
    from matplotlib.pyplot import imshow
    from numpy import asarray
    w,h = len(generations[0]), len(generations)
    img = Image.new("RGB", (w,h), (255,255,255))
    pixels = img.load()
    for i in range(len(generations)):
        for j in range(len(generations[0])):
            if generations[i][j] == 1:
                pixels[j,i] = (0,0,0)
    # img.show()
    imshow(asarray(img))

def plot_ca(generations):
    import matplotlib.pyplot as plt
    plt.matshow(generations, cmap=plt.get_cmap("binary"))
    plt.show()

def run_ca(rule_number, inpt, steps):
    rule = make_rule(rule_number)
    generations = [inpt]
    for i in range(steps):
        current = generations[-1]
        generations.append(make_generation(rule, current))
    # render_ca(generations)
    render_ca(generations)


steps = 100
inpt = 100*[0] + [1] + 100*[0]
neighborhood_size = 3
pows = [2**i for i in range(neighborhood_size-1,-1,-1)]
# print(pows)
rule_number = 90
run_ca(rule_number, inpt, steps)
