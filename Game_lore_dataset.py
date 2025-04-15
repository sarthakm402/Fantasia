from datasets import load_dataset
import json
import re
import random 
#first we load dataset 
#then we sort the fantasy ones using keywords  
# dataset = load_dataset("euclaise/writingprompts", split="train")
# fantasy_keywords = [
#     # Locations & Settings
#     "kingdom", "realm", "empire", "enchanted", "dungeon", "forest", "castle", "citadel", "cavern", "ruins",
#     "fortress", "battlefield", "tavern", "village", "tower", "temple", "shrine", "abyss", "underworld",
#     "highlands", "plains", "stronghold", "lair", "hidden city", "haunted", "forbidden", "cursed", "mystical",
#     "ancient", "lost land",

#     # Creatures & Beings
#     "dragon", "elf", "orc", "goblin", "dwarf", "fae", "faerie", "vampire", "necromancer", "warlock",
#     "wizard", "witch", "mage", "seer", "troll", "giant", "lich", "wraith", "spirit", "specter", "demon",
#     "succubus", "banshee", "nymph", "shapeshifter", "werewolf", "centaur", "mermaid", "unicorn", "phoenix",
#     "chimera", "basilisk", "kraken", "hydra",

#     # Magic & Powers
#     "magic", "spell", "sorcery", "alchemy", "ritual", "curse", "prophecy", "enchantment", "illusion",
#     "incantation", "arcane", "sacred", "summon", "portal", "realmwalk", "time travel", "telepathy", "runes",
#     "sigil", "blood magic", "divine power", "astral", "aura", "mana", "relic", "essence", "spirit bond",

#     # Artifacts & Items
#     "sword", "blade", "staff", "amulet", "orb", "crown", "ring", "scroll", "tome", "chalice", "relic", "key",
#     "gauntlet", "armor", "gem", "crystal", "pendant", "talisman", "artifact", "compass", "mirror", "cloak",
#     "map", "banner", "flute",

#     # Roles & Titles
#     "knight", "rogue", "ranger", "bard", "assassin", "warrior", "paladin", "cleric", "druid", "sorcerer",
#     "monarch", "queen", "king", "heir", "squire", "apprentice", "elder", "guardian", "chosen one", "hunter",
#     "champion", "archmage", "outcast", "prophet",

#     # Themes & Tropes
#     "quest", "betrayal", "resurrection", "chosen", "bloodline", "alliance", "rebellion", "heir", "throne",
#     "darkness", "light", "ancient", "legend", "awakening", "banishment", "pact", "war", "destiny", "trial",
#     "exile", "sacrifice", "legacy", "chaos", "order", "fate", "forbidden love", "revenge"
# ]
# limit=1000
# final=[]
# def found(prompt):
#     return any(word in prompt.lower()for word in fantasy_keywords)
# def find_script(dataset,fantasy_keywords):
#     for entry in dataset:
#         prompt = entry.get("prompt", "").strip()
#         story = entry.get("story", "").strip()
#         if not prompt or not story:
#             continue
#         if  not found(prompt):
#             continue
#         first_lines = re.split(r'(?<=[.!?]) +', story)
#         short_story = " ".join(first_lines[:4]).strip()
#         first_sentence = re.split(r'(?<=[.!?]) +', prompt)[0]
#         ans = f"Goal: {first_sentence}\nSetting: {prompt}"
#         final.append({
#          "input": ans,
#          "output": short_story
#         })
#         if len(final)>=limit:
#             break
# with open("fantasy_quests.jsonl", "w") as f:
#     for item in final:
#         json.dump(item, f)
#         f.write("\n")

# print(f" Saved {len(final)} quest entries to fantasy_quests.jsonl")
random.seed(42)
goals = [
    "Retrieve the lost sword", "Rescue the kidnapped prince", "Destroy the cursed amulet",
    "Uncover the secrets of the fallen city", "Seal the demon portal", "Defend the village from raiders",
    "Escort the mystic seer", "Capture the rogue warlock", "Recover the stolen crown",
    "Slay the ancient hydra", "Restore the shattered moonstone", "Negotiate peace between warring kingdoms",
    "Find the lost heir to the throne", "Break the enchantment on the whispering woods",
    "Decipher the cryptic runes of the monolith", "Awaken the slumbering earth giant",
    "Purify the corrupted spring of life", "Navigate the labyrinth of shifting sands",
    "Gather the scattered fragments of the star map", "Silence the chorus of the banshees",
    "Retrieve the stolen artifact of light", "Unmask the disguised demon lord", "Heal the poisoned earth",
    "Locate the hidden sanctuary of the phoenix", "Stop the ritual that summons the void",
    "Protect the last egg of the sky dragons", "Retrieve the memory crystals from the dream realm",
    "Unravel the conspiracy within the merchant guild", "Defeat the spectral armada",
    "Restore the balance of the elemental shrines", "Find the key to the celestial vault",
    "End the reign of the iron tyrant", "Collect the tears of the forgotten gods",
    "Prevent the release of the imprisoned chaos entity", "Restore the lost melody of the world tree",
    "Find the source of the spreading blight", "Retrieve the lost pages of the ancient grimoire",
    "Stop the clockwork heart from shattering", "Capture the elusive shadow thief",
    "Find the hidden path to the celestial forge", "Defeat the living storm",
    "Recover the lost notes of harmony", "Stop the convergence of the shadow realms",
    "Find the dormant seed of the lifebringer tree", "Defeat the corrupted celestial guardian",
    "Retrieve the lost starlight compass", "Stop the summoning of the deep sea leviathan",
    "Find the source of the eternal winter", "Recover the lost voice of the wind spirits",
    "Defeat the living nightmare", "Retrieve the lost fragments of the sunstone",
    "Stop the ritual that darkens the sun", "Find the lost city of the star weavers",
    "Defeat the living shadow", "Retrieve the lost echo of the ancient song",
    "Stop the shattering of the crystal moon", "Find the forgotten shrine of the time keepers"
]

settings = [
    "in the haunted forest", "within the ruins of an ancient castle", "beneath the icy caverns",
    "inside a dragon's lair", "atop the skybound citadel", "through the enchanted swamp",
    "deep inside the shadowlands", "in the cursed tombs of Eldar", "across the sands of time",
    "on the floating islands of Aetheria", "within the clockwork city of Mechanis",
    "among the coral reefs of the sunken kingdom", "in the obsidian peaks of the Firelands",
    "through the shifting dimensions of the Mirror Maze", "in the ethereal planes of the Astral Sea",
    "within the crystalline caves of the Glimmering Depths", "on the desolate plains of the Silent Steppes",
    "in the whispering groves of the Elderwood", "within the ever-changing halls of the Temporal Nexus",
    "among the petrified forests of the Stone Giants", "in the shimmering deserts of the Mirage Realm",
    "within the forgotten libraries of the Mind Weavers", "on the volcanic peaks of the Ashlands",
    "through the bioluminescent jungles of the Night Bloom", "in the inverted towers of the Skyfall City",
    "among the rustling reeds of the Whispering Marsh", "within the shifting sands of the Quicksand Desert",
    "on the cloud-piercing spires of the Highreach Mountains", "through the labyrinthine tunnels of the Underdark",
    "in the frozen wastes of the Frostbite Plains", "among the ruins of the Sunken Citadel",
    "within the shimmering fields of the Aurora Meadows", "on the jagged cliffs of the Storm's Edge",
    "through the echoing caverns of the Crystal Heart", "in the shadowy alleys of the Thieves' Guild",
    "among the ancient trees of the Elderwood Grove", "within the celestial observatory of the Star Seekers",
    "on the windswept mesas of the Painted Desert", "through the twisting paths of the Bramble Maze",
    "in the silent depths of the Obsidian Sea", "among the floating islands of the Sky Archipelago",
    "within the abandoned mines of the Iron Hills", "on the spectral shores of the Ghost Coast",
    "through the living vines of the Entwined Forest", "in the mirrored halls of the Reflection Palace",
    "among the glowing fungi of the Luminescent Caves", "within the shattered remnants of the Fallen Star",
    "on the shifting glaciers of the Icebound Expanse", "through the whispering reeds of the Siren's Lagoon",
    "in the shadow of the monolithic Black Spire", "among the ruins of the Time-Lost Temple",
    "within the shifting mists of the Phantom Moors", "on the crystalline shores of the Starlight Lake",
    "through the ever-changing rooms of the Shifting Manor"
]

intros = [
    "Legends speak of a time when...", "Long ago, in a land torn by magic and war...",
    "Only the chosen one can...", "The prophecy foretold this moment...",
    "In the shadows of the forgotten realm...", "As darkness spreads across the land...",
    "From the depths of ancient slumber, a threat awakens...", "The stars align, and fate's hand is revealed...",
    "Whispers of a forgotten power echo through the ages...", "A veil of mystery shrouds the land, and only you can lift it...",
    "The threads of destiny weave a perilous path...", "Before the dawn breaks, a crucial choice must be made...",
    "The echoes of a lost civilization call out...", "A storm of chaos descends, and only a hero can quell it...",
    "The ancient guardians stir, sensing a looming danger...", "A dark ritual threatens to unravel the fabric of reality...",
    "The balance of power teeters on the edge of destruction...", "A forgotten oath demands fulfillment...",
    "A hidden gate opens, leading to realms beyond comprehension...", "The sands of time shift, altering the course of history...",
    "A chilling wind carries tales of a forgotten evil...", "The constellations whisper secrets of a hidden power...",
    "A forgotten melody stirs, signaling a time of great change...", "The earth trembles, as ancient forces awaken...",
    "A portal shimmers, revealing a path to a forgotten dimension...", "Shadows dance, revealing glimpses of a hidden truth...",
    "A cryptic message arrives, bearing a warning and a quest...", "The moon bleeds, casting an ominous glow upon the land...",
    "A silent vigil begins, as the guardians prepare for a final stand...", "A forgotten language echoes, unlocking the secrets of the past...",
    "The elements clash, signaling a time of great upheaval...", "A dream foretells a journey into the unknown...",
    "A spectral figure appears, bearing a relic of forgotten power...", "The stars fall, heralding a time of chaos and rebirth...",
    "A hidden map reveals a path to a legendary treasure...", "The veil between worlds thins, allowing strange entities to pass...",
    "A forgotten legend resurfaces, speaking of a hero's return...", "The winds carry whispers of a forgotten prophecy...",
    "A mystical artifact pulses, emitting a call to adventure...", "The sun dims, signaling a time of darkness and despair...",
    "A hidden gate opens, inviting the brave to explore its depths...", "The earth groans, as ancient powers stir from their slumber...",
    "A celestial event occurs, altering the course of fate...", "The shadows lengthen, revealing hidden dangers...",
    "A forgotten ritual begins, threatening to unleash untold power...", "The air crackles with magic, signaling a time of great change...",
    "A spectral voice echoes, guiding the lost towards their destiny...", "The constellations align, revealing a hidden path...",
    "A hidden message appears, urging the hero to act before it's too late..."
]

storylines = [
    "You must face fearsome beasts, uncover hidden paths, and resist powerful illusions.",
    "Every step is a trial, and not all who enter return.",
    "Allies and enemies alike hide among the ruins, their loyalties uncertain.",
    "Dark forces will rise if you fail—this quest is not just for glory, but for survival.",
    "A sacred artifact may guide your way, but its power comes at a cost.",
    "Your journey will test your courage, wits, and the strength of your will.",
    "Betrayal lurks in the shadows, and trust is a fragile weapon.",
    "The path ahead is fraught with moral dilemmas, where choices define your legacy.",
    "Ancient riddles and forgotten puzzles guard the way, challenging your intellect.",
    "The elements themselves conspire against you, testing your resilience.",
    "A hidden prophecy reveals a path, but its interpretation is shrouded in mystery.",
    "The fate of entire kingdoms hangs in the balance, resting on your shoulders.",
    "Whispers of forgotten gods and their forgotten powers guide or deceive you.",
    "The journey demands sacrifice, and the price of victory may be steep.",
    "You will encounter beings of pure magic, both benevolent and malevolent.",
    "The very fabric of reality warps around you, testing your perception.",
    "A race against time begins, as the shadows lengthen and the threat grows.",
    "The lines between light and darkness blur, forcing you to question your beliefs.",
    "A forgotten language holds the key to unlocking ancient secrets.",
    "Your actions will ripple through time, altering the course of history.",
    "The path is guarded by ancient traps, testing your agility and cunning.",
    "You must navigate treacherous political alliances to achieve your goal.",
    "The journey reveals hidden truths about yourself and your past.",
    "You will encounter beings from other dimensions, with strange customs and powers.",
    "The quest requires you to master forgotten magical disciplines.",
    "Your choices will determine the fate of entire civilizations.",
    "You must overcome your inner demons to succeed in your quest.",
    "The path is fraught with illusions and deceptions, challenging your perception.",
    "You will encounter guardians of ancient knowledge, who test your worthiness.",
    "The quest requires you to forge alliances with unlikely companions."]
# first I have to use random to randomly choose between the above
""" By doint  range 1000 and random choice"""
# then make a input and output 

dataset=[]
for _ in range(1000):
    goal = random.choice(goals)
    setting = random.choice(settings)
    intro = random.choice(intros)
    plot = random.choice(storylines)
    give=f'Goal:{goal}\nSetting:{setting}'
    take=f'{intro}{goal}.{plot}'
    dataset.append({
        "input":give,
        "output":take
    })

with open("fantasy_quests.jsonl", "w") as f:
    for item in dataset:
        json.dump(item, f)
        f.write("\n")

print(f" Saved {len(dataset)} quest entries to fantasy_quests.jsonl")