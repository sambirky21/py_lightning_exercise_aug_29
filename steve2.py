eye_colors = [
  {
    "color": "brown"
  },
  {
    "color": "green"
  },
  {
    "color": "amber"
  },
  {
    "color": "blue"
  },
  {
    "color": "amber"
  },
  {
    "color": "amber"
  },
  {
    "color": "brown"
  },
  {
    "color": "amber"
  },
  {
    "color": "brown"
  },
  {
    "color": "brown"
  },
  {
    "color": "purple"
  },
  {
    "color": "purple"
  },
  {
    "color": "blue"
  },
  {
    "color": "blue"
  },
  {
    "color": "brown"
  },
  {
    "color": "amber"
  },
  {
    "color": "amber"
  },
  {
    "color": "green"
  },
  {
    "color": "green"
  },
  {
    "color": "green"
  },
  {
    "color": "brown"
  },
  {
    "color": "amber"
  },
  {
    "color": "brown"
  },
  {
    "color": "amber"
  },
  {
    "color": "blue"
  },
  {
    "color": "blue"
  },
  {
    "color": "green"
  },
  {
    "color": "green"
  }
]

# 2. Create a new collection that stores the unique color names AND how many times each one is in the list

# unique_colors = set()

# for color_dict in eye_colors:
#     current_color = color_dict["color"]
#     unique_colors.add(current_color)

# print(unique_colors)

# hashtable lookup
color_table = {}

for color_dict in eye_colors:
    current_color = color_dict["color"]

    if current_color not in color_dict:
        color_table[current_color] = 1
    else:
        color_table[current_color] += 1