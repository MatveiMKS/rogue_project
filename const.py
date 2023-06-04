##FLOOR##
image_sol = "assets/floor_tiles.jpg"
image_sol_2 = "assets/floor_tiles_2.jpg"
image_sol_3 = "assets/floor_tiles_3.jpg"
image_sol_4 = "assets/floor_tiles_4.jpg"
images_sol = [image_sol, image_sol_2, image_sol_3, image_sol_4]

##HERO##
image_hero = "assets/hero_up.png"

hero_images_f = {
    "z": "assets/hero_up.png",
    "s": "assets/hero_down.png",
    "q": "assets/hero_left.png",
    "d": "assets/hero_right.png"
}

hero_images_e = {
    "w": "assets/hero_up.png",
    "s": "assets/hero_down.png",
    "a": "assets/hero_left.png",
    "d": "assets/hero_right.png"
}

##MONSTERS##
image_monsters = "assets/monster.png"

##DRAGONS##
image_strong_dragon = "assets/dragon_strong.png"
image_weak_dragon = "assets/dragon_weak.png"
image_dragon = "assets/dragon.png"

##BATS##
image_bat = "assets/drone.png"
image_weak_bat = "assets/drone_weak.png"
image_strong_bat = "assets/drone_strong.png"

##BLOBS##
image_strong_blob = "assets/blob_strong.png"
image_weak_blob = "assets/blob_weak.png"
image_blob = "assets/blob.png"

##ORKS##
image_strong_ork = "assets/ork_strong.png"
image_weak_ork = "assets/ork_weak.png"
image_ork = "assets/ork.png"

##GOBLINS##
image_strong_goblin = "assets/goblin_strong.png"
image_weak_goblin = "assets/goblin_weak.png"
image_goblin = "assets/goblin.png"

##ELEMENTS##
image_stairs = "assets/stairs.png"
image_potion = "assets/potion.png"
image_gold = "assets/gold.png"

##WEAPONS##
image_throwing = "assets/bow.png"
image_epee = "assets/epee.png"

image_axe = "assets/axe.png"
image_longsword = "assets/longsword.png"
image_dagger = "assets/dagger.png"


###ARMOR##
image_helmet = "assets/helmet.png"
image_chest = "assets/chest.png"
image_pants = "assets/pants.png"
image_boots = "assets/boots.png"

image_mid_helmet = "assets/mid_helmet.png"
image_mid_chest = "assets/mid_chest.png"
image_mid_pants = "assets/mid_pants.png"
image_mid_boots = "assets/mid_boots.png"

image_rare_helmet = "assets/rare_helmet.png"
image_rare_chest = "assets/rare_chest.png"
image_rare_pants = "assets/rare_pants.png"
image_rare_boots = "assets/rare_boots.png"
image_armure_points = "assets/armure_points.png"


elem_type = {"Goblin" :  image_goblin,
                "Blob" :  image_blob,
                "Bat" :  image_bat,
                "Ork" :  image_ork,
                "Dragon" :  image_dragon,

                "Weak Goblin" :  image_weak_goblin,
                "Weak Blob" :  image_weak_blob,
                "Weak Bat" :  image_weak_bat,
                "Weak Ork" :  image_weak_ork,
                "Weak Dragon" :  image_weak_dragon,
                
                "Strong Goblin" :  image_strong_goblin,
                "Strong Blob" :  image_strong_blob,
                "Strong Bat" :  image_strong_bat,
                "Strong Ork" :  image_strong_ork,
                "Strong Dragon" :  image_strong_dragon,

                "small potion":  image_potion,
                "medium potion":  image_potion,
                "big potion":  image_potion,
                "portoloin":  image_potion,
                "gold":  image_gold,
                "Stairs":  image_stairs,
                "throwing knife":  image_throwing,
                "dagger":  image_dagger,
                "sword":  image_epee,
                "longsword":  image_longsword,
                "axe":  image_axe,
                'leather helmet' : image_helmet,
                'leather chest' : image_chest,
                'leather legs' : image_pants,
                'leather boots' : image_boots,
                'iron helmet' : image_mid_helmet,
                'iron chest' : image_mid_chest,
                'iron legs' : image_mid_pants,
                'iron boots' : image_mid_boots,
                'steel helmet' : image_rare_helmet,
                'steel chest' : image_rare_chest,
                'steel legs' : image_rare_pants,
                'steel boots' : image_rare_boots,
                }


###ARMOR###

# key => protection used to determine type of armor
casques = {
        1 : "assets/casque.png",
        2 : "assets/casque_mid.png",
        3 : "assets/casque_rare.png",
        0 : "assets/casque_vide.png"
}

plastrons = {
        2 : "assets/plastron.png",
        4 : "assets/plastron_mid.png",
        6 : "assets/plastron_rare.png",
        0 : "assets/plastron_vide.png"
}

pantalons = {
        2 : "assets/pantalon.png",
        4 : "assets/pantalon_mid.png",
        6 : "assets/pantalon_rare.png",
        0 : "assets/pantalon_vide.png"
}

bottes = {
        1 : "assets/bottes.png",
        2 : "assets/bottes_mid.png",
        3 : "assets/bottes_rare.png",
        0 : "assets/bottes_vide.png"
}

# key => part of the body for armor
images_armure = {
        "head": casques,
        "chest": plastrons,
        "legs": pantalons,
        "boots": bottes
    }
