from time import sleep
from random import randint
from math import floor
from perlin_noise import PerlinNoise
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

World_Type = input("World_Type:")

app = Ursina()

block_p = 1

Name = Text(text="MCKraft1.2 The 1.2 Update", x=-0.85, y=0.45)

Sky_texture = load_texture("Sky.png")
Grass_Block_texture = load_texture("Grass_Block.png")
Grassy_Stone_Block_texture = load_texture("Grassy_Stone.png")
Grassy_Brick_Block_texture = load_texture("Grassy_Brick.png")
Glass_Block_texture = load_texture("Glass_Block.png")
Leaves1_Block_texture = load_texture("Leaves1.png")
Leaves2_Block_texture = load_texture("Leaves2.png")
Leaves3_Block_texture = load_texture("Leaves3.png")
Tree_Log1_Block_texture = load_texture("Tree_Log1.png")
Poopy_Grass_Block_texture = load_texture("Poopy_Grass.png")
Mushroom_Dirt_Block_texture = load_texture("Mushroom_Dirt.png")
Snow_Block_texture = load_texture("Snow_Block.png")
Tree_Log2_Block_texture = load_texture("Tree_Log2.png")
Tree_Log3_Block_texture = load_texture("Tree_Log3.png")
Shroom_Block_texture = load_texture("Shroom_Block.png")
Froglight1_Block_texture = load_texture("Froglight1_Block.png")
Froglight2_Block_texture = load_texture("Froglight2_Block.png")
Froglight3_Block_texture = load_texture("Froglight3_Block.png")
Mud_Block_texture = load_texture("Mud_Block.png")
Dirt_Path_Block_texture = load_texture("Dirt_Path_Block.png")
Snowy_Grass_Block_texture = load_texture("Snowy_Grass_Block.png")
Sand_Block_texture = load_texture("Sand_Block.png")
Gravel_Block_texture = load_texture("Gravel_Block.png")
Netherrack_Block_texture = load_texture("Netherrack.png")
Tree_Log1_Block_Sapling_Block_texture = load_texture("Tree_Log1_Block_Sapling_Block.png")
Tree_Log2_Block_Sapling_Block_texture = load_texture("Tree_Log2_Block_Sapling_Block.png")
Tree_Log3_Block_Sapling_Block_texture = load_texture("Tree_Log3_Block_Sapling_Block.png")
Not_A_Real_Block_texture = load_texture("Not_A_Real_Block.png")
Goldish_Blackstone_Block_texture = load_texture("Goldish_Blackstone_Block.png")

def update():
    global block_p
    if held_keys["left arrow"]:
        sleep(0.1)
        block_p = block_p - 1
    if held_keys["right arrow"]:
        sleep(0.1)
        block_p = block_p + 1
    if block_p < 1:
        block_p = 1
    elif block_p > 27:
        block_p = 27

grass_block = 64
grassy_stone = 64
grassy_brick = 64
glass_block = 64
leaves1_block = 64
leaves2_block = 64
leaves3_block = 64
tree_log1_block = 64
poopy_grass_block = 64
mushroom_dirt_block = 64
snow_block = 64
tree_log2_block = 64
tree_log3_block = 64
shroom_block = 64
froglight1_block = 64
froglight2_block = 64
froglight3_block = 64
mud_block = 64
dirt_path_block = 64
snowy_grass_block = 64
sand_block = 64
gravel_block = 64
netherrack_block = 64
tree_log1_block_sapling_block = 64
tree_log2_block_sapling_block = 64
tree_log3_block_sapling_block = 64
goldish_blackstone_block = 64

seed = PerlinNoise(octaves=3, seed=randint(1, 1000))

Item = Text(text=f"{block_p}. Grass_Block {grass_block}", x=-0.85, y=0.37)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model="sphere",
            texture=Sky_texture,
            scale = 5000,
            double_sided = True)

class Grass_Block(Button):
    def __init__(self, position, texture = Grass_Block_texture, gravity = 0):
        super().__init__(
            parent=scene,
            position=position,
            model="cube",
            origin_y=0.5,
            texture=texture,
            color=color.white,
            colision="mesh",
            double_sided=True,
            gravity=0)
    def input(self, key):
        global block_p, grass_block, grassy_stone, grassy_brick, glass_block, leaves1_block, leaves2_block, leaves3_block, tree_log1_block, poopy_grass_block, mushroom_dirt_block, snow_block, tree_log2_block, tree_log3_block, shroom_block, froglight1_block, froglight2_block, froglight3_block, mud_block, dirt_path_block, snowy_grass_block, sand_block, gravel_block, netherrack_block, tree_log1_block_sapling_block, tree_log2_block_sapling_block, tree_log3_block_sapling_block, goldish_blackstone_block
        if self.hovered:
            if key == "p":
                if self.texture == Grass_Block_texture:
                    block_p = 1
                    Item.text=f"{block_p}. Grass_Block {grass_block}"
                if self.texture == Grassy_Stone_Block_texture:
                    block_p = 2
                    Item.text=f"{block_p}. Grassy_Stone_Block {grassy_stone}"
                if self.texture == Grassy_Brick_Block_texture:
                    block_p = 3
                    Item.text=f"{block_p}. Grassy_Brick_Block {grassy_brick}"
                if self.texture == Glass_Block_texture:
                    block_p = 4
                    Item.text=f"{block_p}. Glass_Block {glass_block}"
                if self.texture == Leaves1_Block_texture:
                    block_p = 5
                    Item.text=f"{block_p}. Leaves1_Block {leaves1_block}"
                if self.texture == Leaves2_Block_texture:
                    block_p = 6
                    Item.text=f"{block_p}. Leaves2_Block {leaves2_block}"
                if self.texture == Leaves3_Block_texture:
                    block_p = 7
                    Item.text=f"{block_p}. Leaves3_Block {leaves3_block}"
                if self.texture == Tree_Log1_Block_texture:
                    block_p = 8
                    Item.text=f"{block_p}. Tree_Log1_Block {tree_log1_block}"
                if self.texture == Poopy_Grass_Block_texture:
                    block_p = 9
                    Item.text=f"{block_p}. Poopy_Grass_Block {poopy_grass_block}"
                if self.texture == Mushroom_Dirt_Block_texture:
                    block_p = 10
                    Item.text=f"{block_p}. Mushroom_Dirt_Block {mushroom_dirt_block}"
                if self.texture == Snow_Block_texture:
                    block_p = 11
                    Item.text=f"{block_p}. Snow_Block {snow_block}"
                if self.texture == Tree_Log2_Block_texture:
                    block_p = 12
                    Item.text=f"{block_p}. Tree_Log2_Block {tree_log2_block}"
                if self.texture == Tree_Log3_Block_texture:
                    block_p = 13
                    Item.text=f"{block_p}. Tree_Log3_Block {tree_log3_block}"
                if self.texture == Shroom_Block_texture:
                    block_p = 14
                    Item.text=f"{block_p}. Shroom_Block {shroom_block}"
                if self.texture == Froglight1_Block_texture:
                    block_p = 15
                    Item.text=f"{block_p}. Froglight1_Block {froglight1_block}"
                if self.texture == Froglight2_Block_texture:
                    block_p = 16
                    Item.text=f"{block_p}. Froglight2_Block {froglight2_block}"
                if self.texture == Froglight3_Block_texture:
                    block_p = 17
                    Item.text=f"{block_p}. Froglight3_Block {froglight3_block}"
                if self.texture == Mud_Block_texture:
                    block_p = 18
                    Item.text=f"{block_p}. Mud_Block {mud_block}"
                if self.texture == Dirt_Path_Block_texture:
                    block_p = 19
                    Item.text=f"{block_p}. Dirt_Path_Block {dirt_path_block}"
                if self.texture == Snowy_Grass_Block_texture:
                    block_p = 20
                    Item.text=f"{block_p}. Snowy_Grass_Block {snowy_grass_block}"
                if self.texture == Sand_Block_texture:
                    block_p = 21
                    Item.text=f"{block_p}. Sand_Block {sand_block}"
                if self.texture == Gravel_Block_texture:
                    block_p = 22
                    Item.text=f"{block_p}. Gravel_Block {gravel_block}"
                if self.texture == Netherrack_Block_texture:
                    block_p = 23
                    Item.text=f"{block_p}. Netherrack_Block {netherrack_block}"
                if self.texture == Tree_Log1_Block_Sapling_Block_texture:
                    block_p = 24
                    Item.text=f"{block_p}. Tree_Log1_Block_Sapling_Block {tree_log1_block_sapling_block}"
                if self.texture == Tree_Log2_Block_Sapling_Block_texture:
                    block_p = 25
                    Item.text=f"{block_p}. Tree_Log2_Block_Sapling_Block {tree_log2_block_sapling_block}"
                if self.texture == Tree_Log3_Block_Sapling_Block_texture:
                    block_p = 26
                    Item.text=f"{block_p}. Tree_Log3_Block_Sapling_Block {tree_log3_block_sapling_block}"
                if self.texture == Goldish_Blackstone_Block_texture:
                    block_p = 27
                    Item.text=f"{block_p}. Goldish_Blackstone_Block {goldish_blackstone_block}"
            if World_Type.lower() != "debug":
                if block_p == 1:
                    if grass_block > 0:
                        Item.text=f"{block_p}. Grass_Block {grass_block}"
                        if key == "left mouse down":
                            place_block = Grass_Block(position = self.position + mouse.normal, texture = Grass_Block_texture)
                            grass_block = grass_block - 1
                            Item.text=f"{block_p}. Grass_Block {grass_block}"
                if block_p == 2:
                    if grassy_stone > 0:
                        Item.text=f"{block_p}. Grassy_Stone_Block {grassy_stone}"
                        if key == "left mouse down":
                            place_block = Grass_Block(position = self.position + mouse.normal, texture = Grassy_Stone_Block_texture)
                            grassy_stone = grassy_stone - 1
                            Item.text=f"{block_p}. Grassy_Stone_Block {grassy_stone}"
                if block_p == 3:
                    if grassy_brick > 0:
                        Item.text=f"{block_p}. Grassy_Brick_Block {grassy_brick}"
                        if key == "left mouse down":
                            place_block = Grass_Block(position = self.position + mouse.normal, texture = Grassy_Brick_Block_texture)
                            grassy_brick = grassy_brick - 1
                            Item.text=f"{block_p}. Grassy_Brick_Block {grassy_brick}"
                if block_p == 4:
                    if glass_block > 0:
                        Item.text=f"{block_p}. Glass_Block {glass_block}"
                        if key == "left mouse down":
                            place_block = Grass_Block(position = self.position + mouse.normal, texture = Glass_Block_texture)
                            glass_block = glass_block - 1
                            Item.text=f"{block_p}. Glass_Block {glass_block}"
                if block_p == 5:
                    if leaves1_block > 0:
                        Item.text=f"{block_p}. Leaves1_Block {leaves1_block}"
                        if key == "left mouse down":
                            sapling_gen = randint(1, 12)
                            place_block = Grass_Block(position = self.position + mouse.normal, texture = Leaves1_Block_texture)
                            leaves1_block = leaves1_block - 1
                            Item.text=f"{block_p}. Leaves1_Block {leaves1_block}"
                            if sapling_gen == 12:
                                sapling_1 = Grass_Block(position = self.position + mouse.normal, texture = Tree_Log1_Block_Sapling_Block_texture)
                if block_p == 6:
                    if leaves2_block > 0:
                        Item.text=f"{block_p}. Leaves2_Block {leaves2_block}"
                        if key == "left mouse down":
                            sapling_gen = randint(1, 12)
                            place_block = Grass_Block(position = self.position + mouse.normal, texture = Leaves2_Block_texture)
                            leaves2_block = leaves2_block - 1
                            Item.text=f"{block_p}. Leaves2_Block {leaves2_block}"
                            if sapling_gen == 12:
                                sapling_1 = Grass_Block(position = self.position + mouse.normal, texture = Tree_Log2_Block_Sapling_Block_texture)
                if block_p == 7:
                    if leaves3_block > 0:
                        Item.text=f"{block_p}. Leaves3_Block {leaves3_block}"
                        if key == "left mouse down":
                            sapling_gen = randint(1, 12)
                            place_block = Grass_Block(position = self.position + mouse.normal, texture = Leaves3_Block_texture)
                            leaves3_block = leaves3_block - 1
                            Item.text=f"{block_p}. Leaves3_Block {leaves3_block}"
                            if sapling_gen == 12:
                                sapling_1 = Grass_Block(position = self.position + mouse.normal, texture = Tree_Log3_Block_Sapling_Block_texture)
                if block_p == 8:
                    if tree_log1_block > 0:
                        Item.text=f"{block_p}. Tree_Log1_Block {tree_log1_block}"
                        if key == "left mouse down":
                            place_block = Grass_Block(position = self.position + mouse.normal, texture = Tree_Log1_Block_texture)
                            tree_log1_block = tree_log1_block - 1
                            Item.text=f"{block_p}. Tree_Log1_Block {tree_log1_block}"
                if block_p == 9:
                    if poopy_grass_block > 0:
                        Item.text=f"{block_p}. Poopy_Grass_Block {poopy_grass_block}"
                        if key == "left mouse down":
                            place_block = Grass_Block(position = self.position + mouse.normal, texture = Poopy_Grass_Block_texture)
                            poopy_grass_block = poopy_grass_block - 1
                            Item.text=f"{block_p}. Poopy_Grass_Block {poopy_grass_block}"
                if block_p == 10:
                    if mushroom_dirt_block > 0:
                        Item.text=f"{block_p}. Mushroom_Dirt_Block {mushroom_dirt_block}"
                        if key == "left mouse down":
                            place_block = Grass_Block(position = self.position + mouse.normal, texture = Mushroom_Dirt_Block_texture)
                            mushroom_dirt_block = mushroom_dirt_block - 1
                            Item.text=f"{block_p}. Mushroom_Dirt_Block {mushroom_dirt_block}"
                if block_p == 11:
                    if snow_block > 0:
                        Item.text=f"{block_p}. Snow_Block {snow_block}"
                        if key == "left mouse down":
                            place_block = Grass_Block(position = self.position + mouse.normal, texture = Snow_Block_texture)
                            snow_block = snow_block - 1
                            Item.text=f"{block_p}. Snow_Block {snow_block}"
                if block_p == 12:
                    if tree_log2_block > 0:
                        Item.text=f"{block_p}. Tree_Log2_Block {tree_log2_block}"
                        if key == "left mouse down":
                            place_block = Grass_Block(position = self.position + mouse.normal, texture = Tree_Log2_Block_texture)
                            tree_log2_block = tree_log2_block - 1
                            Item.text=f"{block_p}. Tree_Log2_Block {tree_log2_block}"
                if block_p == 13:
                    if tree_log3_block > 0:
                        Item.text=f"{block_p}. Tree_Log3_Block {tree_log3_block}"
                        if key == "left mouse down":
                            place_block = Grass_Block(position = self.position + mouse.normal, texture = Tree_Log3_Block_texture)
                            tree_log3_block = tree_log3_block - 1
                            Item.text=f"{block_p}. Tree_Log3_Block {tree_log3_block}"
                if block_p == 14:
                    if shroom_block > 0:
                        Item.text=f"{block_p}. Shroom_Block {shroom_block}"
                        if key == "left mouse down":
                            place_block = Grass_Block(position = self.position + mouse.normal, texture = Shroom_Block_texture)
                            shroom_block = shroom_block - 1
                            Item.text=f"{block_p}. Shroom_Block {shroom_block}"
                if block_p == 15:
                    if froglight1_block > 0:
                        Item.text=f"{block_p}. Froglight1_Block {froglight1_block}"
                        if key == "left mouse down":
                            place_block = Grass_Block(position = self.position + mouse.normal, texture = Froglight1_Block_texture)
                            froglight1_block = froglight1_block - 1
                            Item.text=f"{block_p}. Froglight1_Block {froglight1_block}"
                if block_p == 16:
                    if froglight2_block > 0:
                        Item.text=f"{block_p}. Froglight2_Block {froglight2_block}"
                        if key == "left mouse down":
                            place_block = Grass_Block(position = self.position + mouse.normal, texture = Froglight2_Block_texture)
                            froglight2_block = froglight2_block - 1
                            Item.text=f"{block_p}. Froglight2_Block {froglight2_block}"
                if block_p == 17:
                    if froglight3_block > 0:
                        Item.text=f"{block_p}. Froglight3_Block {froglight3_block}"
                        if key == "left mouse down":
                            place_block = Grass_Block(position = self.position + mouse.normal, texture = Froglight3_Block_texture)
                            froglight3_block = froglight3_block - 1
                            Item.text=f"{block_p}. Froglight3_Block {froglight3_block}"
                if block_p == 18:
                    if mud_block > 0:
                        Item.text=f"{block_p}. Mud_Block {mud_block}"
                        if key == "left mouse down":
                            place_block = Grass_Block(position = self.position + mouse.normal, texture = Mud_Block_texture)
                            mud_block = mud_block - 1
                            Item.text=f"{block_p}. Mud_Block {mud_block}"
                if block_p == 19:
                    if dirt_path_block > 0:
                        Item.text=f"{block_p}. Dirt_Path_Block {dirt_path_block}"
                        if key == "left mouse down":
                            place_block = Grass_Block(position = self.position + mouse.normal, texture = Dirt_Path_Block_texture)
                            dirt_path_block = dirt_path_block - 1
                            Item.text=f"{block_p}. Dirt_Path_Block {dirt_path_block}"
                if block_p == 20:
                    if snowy_grass_block > 0:
                        Item.text=f"{block_p}. Snowy_Grass_Block {snowy_grass_block}"
                        if key == "left mouse down":
                            place_block = Grass_Block(position = self.position + mouse.normal, texture = Snowy_Grass_Block_texture)
                            snowy_grass_block = snowy_grass_block - 1
                            Item.text=f"{block_p}. Snowy_Grass_Block {snowy_grass_block}"
                if block_p == 21:
                    if sand_block > 0:
                        Item.text=f"{block_p}. Sand_Block {sand_block}"
                        if key == "left mouse down":
                            place_block = Grass_Block(position = self.position + mouse.normal, texture = Sand_Block_texture)
                            sand_block = sand_block - 1
                            Item.text=f"{block_p}. Sand_Block {sand_block}"
                if block_p == 22:
                    if gravel_block > 0:
                        Item.text=f"{block_p}. Gravel_Block {gravel_block}"
                        if key == "left mouse down":
                            place_block = Grass_Block(position = self.position + mouse.normal, texture = Gravel_Block_texture)
                            gravel_block = gravel_block - 1
                            Item.text=f"{block_p}. Gravel_Block {gravel_block}"
                if block_p == 23:
                    if netherrack_block > 0:
                        Item.text=f"{block_p}. Netherrack_Block {netherrack_block}"
                        if key == "left mouse down":
                            place_block = Grass_Block(position = self.position + mouse.normal, texture = Netherrack_Block_texture)
                            netherrack_block = netherrack_block - 1
                            Item.text=f"{block_p}. Netherrack_Block {netherrack_block}"
                if block_p == 24:
                    if tree_log1_block_sapling_block > 0:
                        Item.text=f"{block_p}. Tree_Log1_Block_Sapling_Block {tree_log1_block_sapling_block}"
                        if self.texture == Grass_Block_texture or self.texture == Not_A_Real_Block_texture:
                            if key == "left mouse down":
                                place_block = Grass_Block(position = self.position + mouse.normal, texture = Tree_Log1_Block_Sapling_Block_texture)
                                tree_log1_block_sapling_block = tree_log1_block_sapling_block - 1
                                Item.text=f"{block_p}. Tree_Log1_Block_Sapling_Block {tree_log1_block_sapling_block}"
                                destroy(place_block)
                                grow_tree = Grass_Block(position = self.position + mouse.normal, texture = Tree_Log1_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (0, 1, 0) + mouse.normal, texture = Tree_Log1_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (0, 2, 0) + mouse.normal, texture = Tree_Log1_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (0, 3, 0) + mouse.normal, texture = Tree_Log1_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (0, 4, 0) + mouse.normal, texture = Leaves1_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (1, 3, 0) + mouse.normal, texture = Leaves1_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (-1, 3, 0) + mouse.normal, texture = Leaves1_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (0, 3, 1) + mouse.normal, texture = Leaves1_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (0, 3, -1) + mouse.normal, texture = Leaves1_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (0, 2, 1) + mouse.normal, texture = Leaves1_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (0, 2, 2) + mouse.normal, texture = Leaves1_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (1, 2, 1) + mouse.normal, texture = Leaves1_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (1, 2, 2) + mouse.normal, texture = Leaves1_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (-1, 2, 1) + mouse.normal, texture = Leaves1_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (-1, 2, 2) + mouse.normal, texture = Leaves1_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (0, 2, -1) + mouse.normal, texture = Leaves1_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (0, 2, -2) + mouse.normal, texture = Leaves1_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (1, 2, -2) + mouse.normal, texture = Leaves1_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (1, 2, -1) + mouse.normal, texture = Leaves1_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (-1, 2, -1) + mouse.normal, texture = Leaves1_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (-1, 2, -2) + mouse.normal, texture = Leaves1_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (1, 2, 0) + mouse.normal, texture = Leaves1_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (-1, 2, 0) + mouse.normal, texture = Leaves1_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (2, 2, 0) + mouse.normal, texture = Leaves1_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (-2, 2, 0) + mouse.normal, texture = Leaves1_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (2, 2, 1) + mouse.normal, texture = Leaves1_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (-2, 2, 1) + mouse.normal, texture = Leaves1_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (2, 2, -1) + mouse.normal, texture = Leaves1_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (-2, 2, -1) + mouse.normal, texture = Leaves1_Block_texture)
                if block_p == 25:
                    if tree_log2_block_sapling_block > 0:
                        Item.text=f"{block_p}. Tree_Log2_Block_Sapling_Block {tree_log2_block_sapling_block}"
                        if self.texture == Grass_Block_texture or self.texture == Not_A_Real_Block_texture:
                            if key == "left mouse down":
                                place_block = Grass_Block(position = self.position + mouse.normal, texture = Tree_Log2_Block_Sapling_Block_texture)
                                tree_log2_block_sapling_block = tree_log2_block_sapling_block - 1
                                Item.text=f"{block_p}. Tree_Log2_Block_Sapling_Block {tree_log2_block_sapling_block}"
                                destroy(place_block)
                                grow_tree = Grass_Block(position = self.position + mouse.normal, texture = Tree_Log2_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (0, 1, 0) + mouse.normal, texture = Tree_Log2_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (0, 2, 0) + mouse.normal, texture = Tree_Log2_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (0, 3, 0) + mouse.normal, texture = Tree_Log2_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (0, 4, 0) + mouse.normal, texture = Leaves2_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (1, 3, 0) + mouse.normal, texture = Leaves2_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (-1, 3, 0) + mouse.normal, texture = Leaves2_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (0, 3, 1) + mouse.normal, texture = Leaves2_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (0, 3, -1) + mouse.normal, texture = Leaves2_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (0, 2, 1) + mouse.normal, texture = Leaves2_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (0, 2, 2) + mouse.normal, texture = Leaves2_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (1, 2, 1) + mouse.normal, texture = Leaves2_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (1, 2, 2) + mouse.normal, texture = Leaves2_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (-1, 2, 1) + mouse.normal, texture = Leaves2_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (-1, 2, 2) + mouse.normal, texture = Leaves2_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (0, 2, -1) + mouse.normal, texture = Leaves2_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (0, 2, -2) + mouse.normal, texture = Leaves2_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (1, 2, -2) + mouse.normal, texture = Leaves2_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (1, 2, -1) + mouse.normal, texture = Leaves2_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (-1, 2, -1) + mouse.normal, texture = Leaves2_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (-1, 2, -2) + mouse.normal, texture = Leaves2_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (1, 2, 0) + mouse.normal, texture = Leaves2_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (-1, 2, 0) + mouse.normal, texture = Leaves2_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (2, 2, 0) + mouse.normal, texture = Leaves2_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (-2, 2, 0) + mouse.normal, texture = Leaves2_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (2, 2, 1) + mouse.normal, texture = Leaves2_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (-2, 2, 1) + mouse.normal, texture = Leaves2_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (2, 2, -1) + mouse.normal, texture = Leaves2_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (-2, 2, -1) + mouse.normal, texture = Leaves2_Block_texture)
                if block_p == 26:
                    if tree_log3_block_sapling_block > 0:
                        Item.text=f"{block_p}. Tree_Log3_Block_Sapling_Block {tree_log3_block_sapling_block}"
                        if self.texture == Grass_Block_texture or self.texture == Not_A_Real_Block_texture:
                            if key == "left mouse down":
                                place_block = Grass_Block(position = self.position + mouse.normal, texture = Tree_Log3_Block_Sapling_Block_texture)
                                tree_log3_block_sapling_block = tree_log3_block_sapling_block - 1
                                Item.text=f"{block_p}. Tree_Log3_Block_Sapling_Block {tree_log3_block_sapling_block}"
                                destroy(place_block)
                                grow_tree = Grass_Block(position = self.position + mouse.normal, texture = Tree_Log3_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (0, 1, 0) + mouse.normal, texture = Tree_Log3_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (0, 2, 0) + mouse.normal, texture = Tree_Log3_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (0, 3, 0) + mouse.normal, texture = Tree_Log3_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (0, 4, 0) + mouse.normal, texture = Leaves3_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (1, 3, 0) + mouse.normal, texture = Leaves3_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (-1, 3, 0) + mouse.normal, texture = Leaves3_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (0, 3, 1) + mouse.normal, texture = Leaves3_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (0, 3, -1) + mouse.normal, texture = Leaves3_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (0, 2, 1) + mouse.normal, texture = Leaves3_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (0, 2, 2) + mouse.normal, texture = Leaves3_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (1, 2, 1) + mouse.normal, texture = Leaves3_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (1, 2, 2) + mouse.normal, texture = Leaves3_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (-1, 2, 1) + mouse.normal, texture = Leaves3_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (-1, 2, 2) + mouse.normal, texture = Leaves3_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (0, 2, -1) + mouse.normal, texture = Leaves3_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (0, 2, -2) + mouse.normal, texture = Leaves3_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (1, 2, -2) + mouse.normal, texture = Leaves3_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (1, 2, -1) + mouse.normal, texture = Leaves3_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (-1, 2, -1) + mouse.normal, texture = Leaves3_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (-1, 2, -2) + mouse.normal, texture = Leaves3_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (1, 2, 0) + mouse.normal, texture = Leaves3_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (-1, 2, 0) + mouse.normal, texture = Leaves3_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (2, 2, 0) + mouse.normal, texture = Leaves3_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (-2, 2, 0) + mouse.normal, texture = Leaves3_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (2, 2, 1) + mouse.normal, texture = Leaves3_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (-2, 2, 1) + mouse.normal, texture = Leaves3_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (2, 2, -1) + mouse.normal, texture = Leaves3_Block_texture)
                                grow_tree = Grass_Block(position = self.position + (-2, 2, -1) + mouse.normal, texture = Leaves3_Block_texture)
                if block_p == 27:
                    if goldish_blackstone_block > 0:
                        Item.text=f"{block_p}. Goldish_Blackstone_Block {goldish_blackstone_block}"
                        if key == "left mouse down":
                            place_block = Grass_Block(position = self.position + mouse.normal, texture = Goldish_Blackstone_Block_texture)
                            goldish_blackstone_block = goldish_blackstone_block - 1
                            Item.text=f"{block_p}. Goldish_Blackstone_Block {goldish_blackstone_block}"
            if World_Type.lower() != "debug":
                if key == "right mouse down" or key == "backspace":
                    if self.texture == Grass_Block_texture:
                        grass_block = grass_block + 1
                    if self.texture == Grassy_Stone_Block_texture:
                        grassy_stone = grassy_stone + 1
                    if self.texture == Grassy_Brick_Block_texture:
                        grassy_brick = grassy_brick + 1
                    if self.texture == Glass_Block_texture:
                        glass_block = glass_block + 1
                    if self.texture == Leaves1_Block_texture:
                        leaves1_block = leaves1_block + 1
                    if self.texture == Leaves2_Block_texture:
                        leaves2_block = leaves2_block + 1
                    if self.texture == Leaves3_Block_texture:
                        leaves3_block = leaves3_block + 1
                    if self.texture == Tree_Log1_Block_texture:
                        tree_log1_block = tree_log1_block + 1
                    if self.texture == Poopy_Grass_Block_texture:
                        poopy_grass_block = poopy_grass_block + 1
                    if self.texture == Mushroom_Dirt_Block_texture:
                        mushroom_dirt_block = mushroom_dirt_block + 1
                    if self.texture == Snow_Block_texture:
                        snow_block = snow_block + 1
                    if self.texture == Tree_Log2_Block_texture:
                        tree_log2_block = tree_log2_block + 1
                    if self.texture == Tree_Log3_Block_texture:
                        tree_log3_block = tree_log3_block + 1
                    if self.texture == Shroom_Block_texture:
                        shroom_block = shroom_block + 1
                    if self.texture == Froglight1_Block_texture:
                        froglight1_block = froglight1_block + 1
                    if self.texture == Froglight2_Block_texture:
                        froglight2_block = froglight2_block + 1
                    if self.texture == Froglight3_Block_texture:
                        froglight3_block = froglight3_block + 1
                    if self.texture == Mud_Block_texture:
                        mud_block = mud_block + 1
                    if self.texture == Dirt_Path_Block_texture:
                        dirt_path_block = dirt_path_block + 1
                    if self.texture == Snowy_Grass_Block_texture:
                        snowy_grass_block = snowy_grass_block + 1
                    if self.texture == Sand_Block_texture:
                        sand_block = sand_block + 1
                    if self.texture == Gravel_Block_texture:
                        gravel_block = gravel_block + 1
                    if self.texture == Netherrack_Block_texture:
                        netherrack_block = netherrack_block + 1
                    if self.texture == Tree_Log1_Block_Sapling_Block_texture:
                        tree_log1_block_sapling_block = tree_log1_block_sapling_block + 1
                    if self.texture == Tree_Log2_Block_Sapling_Block_texture:
                        tree_log2_block_sapling_block = tree_log2_block_sapling_block + 1
                    if self.texture == Tree_Log3_Block_Sapling_Block_texture:
                        tree_log3_block_sapling_block = tree_log3_block_sapling_block + 1
                    if self.texture != Not_A_Real_Block_texture:
                        destroy(self)
                    if self.texture == Goldish_Blackstone_Block_texture:
                        goldish_blackstone_block = goldish_blackstone_block + 1

min_y = -2

if World_Type.lower() == "normal":
    for z in range(30):
        for x in range(30):
            y_fl = seed([z * 0.02, x * 0.02])
            y_fl = floor(y_fl * 5)
            for y in range(y_fl, min_y - 1, -1):
                Blocks = Grass_Block(position=(z, y + min_y, x))
elif World_Type.lower() == "flat" or World_Type.lower() == "mogswamp":
    for z in range(30):
        for x in range(30):
            y_fl = seed([z * 0.02, x * 0.02])
            y_fl = floor(y_fl * 0)
            for y in range(y_fl, min_y - 1, -1):
                Blocks = Grass_Block(position=(z, y + min_y, x))
elif World_Type.lower() == "blocks" or World_Type.lower() == "debug":
    for z in range(30):
        for x in range(30):
            y_fl = seed([z * 0.02, x * 0.02])
            y_fl = floor(y_fl * 0)
            for y in range(y_fl, min_y - 1, -1):
                Blocks = Grass_Block(position=(z, y + min_y, x))
    Grass_Block(position=(0, 0, 29), texture=Grass_Block_texture)
    Grass_Block(position=(1, 0, 29), texture=Grassy_Stone_Block_texture)
    Grass_Block(position=(2, 0, 29), texture=Grassy_Brick_Block_texture)
    Grass_Block(position=(3, 0, 29), texture=Glass_Block_texture)
    Grass_Block(position=(4, 0, 29), texture=Leaves1_Block_texture)
    Grass_Block(position=(5, 0, 29), texture=Leaves2_Block_texture)
    Grass_Block(position=(6, 0, 29), texture=Leaves3_Block_texture)
    Grass_Block(position=(7, 0, 29), texture=Tree_Log1_Block_texture)
    Grass_Block(position=(8, 0, 29), texture=Poopy_Grass_Block_texture)
    Grass_Block(position=(9, 0, 29), texture=Mushroom_Dirt_Block_texture)
    Grass_Block(position=(10, 0, 29), texture=Snow_Block_texture)
    Grass_Block(position=(11, 0, 29), texture=Tree_Log2_Block_texture)
    Grass_Block(position=(12, 0, 29), texture=Tree_Log3_Block_texture)
    Grass_Block(position=(13, 0, 29), texture=Shroom_Block_texture)
    Grass_Block(position=(14, 0, 29), texture=Froglight1_Block_texture)
    Grass_Block(position=(15, 0, 29), texture=Froglight2_Block_texture)
    Grass_Block(position=(16, 0, 29), texture=Froglight3_Block_texture)
    Grass_Block(position=(17, 0, 29), texture=Mud_Block_texture)
    Grass_Block(position=(18, 0, 29), texture=Dirt_Path_Block_texture)
    Grass_Block(position=(19, 0, 29), texture=Snowy_Grass_Block_texture)
    Grass_Block(position=(20, 0, 29), texture=Sand_Block_texture)
    Grass_Block(position=(21, 0, 29), texture=Gravel_Block_texture)
    Grass_Block(position=(22, 0, 29), texture=Netherrack_Block_texture)
    Grass_Block(position=(23, 0, 29), texture=Tree_Log1_Block_Sapling_Block_texture)
    Grass_Block(position=(24, 0, 29), texture=Tree_Log2_Block_Sapling_Block_texture)
    Grass_Block(position=(25, 0, 29), texture=Tree_Log3_Block_Sapling_Block_texture)
    Grass_Block(position=(23, -1, 29), texture=Not_A_Real_Block_texture)
    Grass_Block(position=(24, -1, 29), texture=Not_A_Real_Block_texture)
    Grass_Block(position=(25, -1, 29), texture=Not_A_Real_Block_texture)
    Grass_Block(position=(26, 0, 29), texture=Not_A_Real_Block_texture)
    Grass_Block(position=(27, 0, 29), texture=Goldish_Blackstone_Block_texture)

elif World_Type.lower() == "snowy_normal":
    for z in range(30):
        for x in range(30):
            y_fl = seed([z * 0.02, x * 0.02])
            y_fl = floor(y_fl * 5)
            for y in range(y_fl, min_y - 1, -1):
                Blocks = Grass_Block(position=(z, y + min_y, x), texture=Snow_Block_texture)
elif World_Type.lower() == "snowy_flat" or World_Type.lower() == "snowy_mogswamp":
    for z in range(30):
        for x in range(30):
            y_fl = seed([z * 0.02, x * 0.02])
            y_fl = floor(y_fl * 0)
            for y in range(y_fl, min_y - 1, -1):
                Blocks = Grass_Block(position=(z, y + min_y, x), texture=Snow_Block_texture)
elif World_Type.lower() == "normal_swamp":
    for z in range(30):
        for x in range(30):
            y_fl = seed([z * 0.02, x * 0.02])
            y_fl = floor(y_fl * 5)
            for y in range(y_fl, min_y - 1, -1):
                Blocks = Grass_Block(position=(z, y + min_y, x), texture=Mud_Block_texture)
elif World_Type.lower() == "flat_swamp" or World_Type.lower() == "mogswamp_swamp":
    for z in range(30):
        for x in range(30):
            y_fl = seed([z * 0.02, x * 0.02])
            y_fl = floor(y_fl * 0)
            for y in range(y_fl, min_y - 1, -1):
                Blocks = Grass_Block(position=(z, y + min_y, x), texture=Mud_Block_texture)
else:
    for z in range(30):
        for x in range(30):
            y_fl = seed([z * 0.02, x * 0.02])
            y_fl = floor(y_fl * 3)
            for y in range(y_fl, min_y - 1, -1):
                Blocks = Grass_Block(position=(z, y + min_y, x))

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.controller = FirstPersonController(
            mouse_sensitivity = Vec2(100, 100),
            player = self,
            origin_y = 0.5,
            gravity = 0.3
        )

player = Player()
sky = Sky()

def input(key):
    if key == "escape":
        exit()

app.run()