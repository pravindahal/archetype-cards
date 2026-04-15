import json

traits = [
    ('O', 'o'), ('C', 'c'), ('E', 'e'), ('A', 'a'), ('N', 'n')
]
import itertools

combos = list(itertools.product(*traits))

archetypes = {
    "OCEAN": ("The Passionate Champion", "Deeply empathetic, passionately creative, highly organized, enthusiastic leader.", "Overwhelmed by others' emotions, perfectionistic, prone to burnout.", "A radiant figure holding a burning heart while standing on a meticulously organized map."),
    "OCEAn": ("The Radiant Mentor", "Uplifting, creative, structured, effortlessly brings people together.", "Can be overly controlling of group dynamics, dismisses negative emotions.", "A smiling guide holding a glowing compass, surrounded by a group of diverse followers."),
    "OCEaN": ("The Tempestuous Commander", "Driven, visionary, commands the room, deeply invested in outcomes.", "Volatile, overly critical when stressed, demands impossible standards.", "A sea captain steering a ship through a fierce storm with a determined, intense gaze."),
    "OCEan": ("The Unstoppable Visionary", "Bold, structured, innovative, unbothered by criticism.", "Aloof, steamrolls over others' feelings, rigidly pursues goals.", "A futuristic architect looking over a glowing, structured cityscape."),
    "OCeAN": ("The Eccentric Empath", "Wildly creative, emotionally attuned, highly sociable, adaptable.", "Lacks follow-through, emotionally exhausted, scattered focus.", "A vibrant artist throwing colorful paint, but looking slightly overwhelmed by the canvas."),
    "OCeAn": ("The Carefree Muse", "Inspiring, joyful, spontaneous, connects with everyone.", "Flaky, avoids difficult conversations, restless.", "A dancing figure surrounded by floating, glowing musical notes or sparkling lights."),
    "OCeaN": ("The Dramatic Catalyst", "Provocative, energetic, challenges the status quo, deeply passionate.", "Creates unnecessary conflict, unpredictable, struggles with emotional regulation.", "A fire dancer spinning flames, with a chaotic but mesmerizing energy."),
    "OCean": ("The Maverick Innovator", "Rule-breaking, charismatic, thick-skinned, endless initiator.", "Reckless, disregards consequences, manipulative.", "A rogue inventor holding a wild, sparking gadget with a confident smirk."),
    "OcEAN": ("The Devoted Guardian", "Traditional, highly organized, empathetic, socially involved.", "Rigid, anxious about change, overly self-sacrificing.", "A knight in shining armor standing guard at the gates of a cozy village."),
    "OcEAn": ("The Steadfast Pillar", "Reliable, warm, organized, sociable, unshakable.", "Stubborn, overly conventional, resistant to new ideas.", "A majestic oak tree personified, sheltering people under its broad branches."),
    "OcEaN": ("The Righteous Enforcer", "Duty-bound, vocal, intense, demands order and tradition.", "Judgmental, prone to outrage, inflexible.", "A judge holding a gavel and scales, with a stern and slightly anxious expression."),
    "OcEan": ("The Unshakable Executive", "Efficient, decisive, traditional, immune to stress.", "Dictatorial, lacks emotional depth, close-minded.", "A CEO figure standing tall in front of a massive, perfectly structured bank vault."),
    "OceAN": ("The Anxious Caretaker", "Spontaneous, social, highly empathetic, emotionally reactive.", "Disorganized, easily stressed, poor boundaries.", "A chaotic but loving baker whose kitchen is a mess, but who is offering a beautiful pie."),
    "OceAn": ("The Cheerful Host", "Adaptable, friendly, outgoing, untroubled by chaos.", "Superficial, avoids deep commitments, easily distracted.", "A charismatic party host holding a tray of drinks in a lively, slightly messy room."),
    "OceaN": ("The Restless Agitator", "Outspoken, flexible, practical, deeply emotionally frustrated.", "Combative, disorganized, constantly dissatisfied.", "A rebel with a megaphone, standing on a makeshift barricade."),
    "Ocean": ("The Pragmatic Opportunist", "Adaptable, assertive, thick-skinned, outgoing.", "Self-serving, lacks long-term vision, unreliable.", "A smooth-talking merchant in a bustling bazaar, juggling various items."),
    
    # Introverted Half (e)
    "oCEAN": ("The Intense Scholar", "Deeply analytical, organized, empathetic but quiet, emotionally driven.", "Overthinks everything, prone to social anxiety, easily overwhelmed.", "A monk reading an ancient, glowing tome in a candlelit, perfectly organized library."),
    "oCEAn": ("The Serene Sage", "Calm, structured, private, kind-hearted.", "Overly detached, slow to act, overly traditional.", "An elder meditating peacefully by a perfectly still, symmetrical zen garden."),
    "oCEaN": ("The Brooding Perfectionist", "Highly disciplined, solitary, intense, holds strong standards.", "Harshly self-critical, unforgiving of others, prone to bitter resentment.", "A master clockmaker hyper-focused on tiny gears with a furrowed brow."),
    "oCEan": ("The Stoic Architect", "Orderly, quiet, resilient, logical.", "Cold, disconnected from humanity, overwhelmingly rigid.", "A shadowy figure calculating equations on a massive blackboard in an empty room."),
    "oCeAN": ("The Melancholic Dreamer", "Quiet, adaptable, highly sensitive, empathetic.", "Lost in their own head, unmotivated, chronically overwhelmed.", "A solitary figure looking out a rainy window, writing in a messy journal."),
    "oCeAn": ("The Gentle Wanderer", "Easygoing, kind, private, emotionally stable.", "Passive, lacking ambition, too accommodating.", "A nomad sitting peacefully by a smoldering campfire in a quiet forest."),
    "oCeaN": ("The Solitary Critic", "Quiet, observant, critical, intensely analytical.", "Cynical, isolated, prone to emotional brooding.", "A shadowy figure in a corner booth, sketching people with a critical eye."),
    "oCean": ("The Unfazed Lone Wolf", "Independent, practical, tough-minded, unbothered.", "Apathetic, isolated, dismissive of others' feelings.", "A lone survivalist walking away from a chaotic scene without looking back."),
    
    # Let me fix the mapping: I mixed up O vs o and C vs c in the above intros.
    # Actually I should properly map them.
}

# Proper mapping function
def get_archetype(o, c, e, a, n):
    code = o+c+e+a+n
    # Logic to build name and traits if not in explicit dictionary
    # Let's just create a procedural generator for the 32 to ensure consistency
    
    # Light and shadow building
    o_light = "visionary and creative" if o == 'O' else "practical and tradition-honoring"
    o_shadow = "unrealistic and ungrounded" if o == 'O' else "close-minded and rigid"
    
    c_light = "highly organized and disciplined" if c == 'C' else "adaptable and spontaneous"
    c_shadow = "perfectionistic and controlling" if c == 'C' else "chaotic and unreliable"
    
    e_light = "charismatic and outgoing" if e == 'E' else "introspective and observant"
    e_shadow = "attention-seeking and loud" if e == 'E' else "withdrawn and isolated"
    
    a_light = "empathetic and compassionate" if a == 'A' else "assertive and logical"
    a_shadow = "people-pleasing and self-sacrificing" if a == 'A' else "harsh and combative"
    
    n_light = "emotionally attuned and vigilant" if n == 'N' else "resilient and calm"
    n_shadow = "anxious and easily overwhelmed" if n == 'N' else "stoic to the point of apathy"
    
    light = f"{o_light.capitalize()}, {c_light}, {e_light}, {a_light}, and {n_light}."
    shadow = f"{o_shadow.capitalize()}, {c_shadow}, {e_shadow}, {a_shadow}, and {n_shadow}."
    
    # Nicknames dictionary to map specific 32 codes
    nicknames = {
        "OCEAN": "The Passionate Champion", "OCEAn": "The Radiant Mentor", "OCEaN": "The Tempestuous Commander", "OCEan": "The Unstoppable Visionary",
        "OCeAN": "The Intense Scholar", "OCeAn": "The Serene Sage", "OCeaN": "The Brooding Perfectionist", "OCean": "The Stoic Architect",
        "OcEAN": "The Eccentric Empath", "OcEAn": "The Carefree Muse", "OcEaN": "The Dramatic Catalyst", "OcEan": "The Maverick Innovator",
        "OceAN": "The Melancholic Dreamer", "OceAn": "The Gentle Wanderer", "OceaN": "The Solitary Critic", "Ocean": "The Unfazed Lone Wolf",
        
        "oCEAN": "The Devoted Guardian", "oCEAn": "The Steadfast Pillar", "oCEaN": "The Righteous Enforcer", "oCEan": "The Unshakable Executive",
        "oCeAN": "The Quiet Caretaker", "oCeAn": "The Peaceful Observer", "oCeaN": "The Silent Judge", "oCean": "The Resilient Hermit",
        "ocEAN": "The Anxious Host", "ocEAn": "The Cheerful Pragmatist", "ocEaN": "The Restless Agitator", "ocEan": "The Opportunistic Dealer",
        "oceAN": "The Nostalgic Romantic", "oceAn": "The Content Bystander", "oceaN": "The Grumbling Skeptic", "ocean": "The Unbothered Survivalist",
    }
    
    visuals = {
        "OCEAN": "A knight in ornate armor carrying a glowing lantern through a swirling storm.",
        "OCEAn": "A smiling guide holding a glowing compass, surrounded by followers.",
        "OCEaN": "A sea captain steering a ship through a fierce storm with intense gaze.",
        "OCEan": "A futuristic architect looking over a glowing, structured cityscape.",
        "OCeAN": "A monk reading an ancient, glowing tome in a candlelit library.",
        "OCeAn": "An elder meditating peacefully by a symmetrical zen garden.",
        "OCeaN": "A master clockmaker hyper-focused on tiny gears.",
        "OCean": "A shadowy figure calculating equations on a massive blackboard.",
        "OcEAN": "A vibrant artist throwing colorful paint, but looking slightly overwhelmed.",
        "OcEAn": "A dancing figure surrounded by floating, glowing musical notes.",
        "OcEaN": "A fire dancer spinning flames, with a chaotic but mesmerizing energy.",
        "OcEan": "A rogue inventor holding a wild, sparking gadget.",
        "OceAN": "A solitary figure looking out a rainy window, writing in a messy journal.",
        "OceAn": "A nomad sitting peacefully by a smoldering campfire.",
        "OceaN": "A shadowy figure in a corner booth, sketching people with a critical eye.",
        "Ocean": "A lone survivalist walking away from a chaotic scene.",
        
        "oCEAN": "A knight standing guard at the gates of a cozy village.",
        "oCEAn": "A majestic oak tree personified, sheltering people.",
        "oCEaN": "A judge holding a gavel and scales, with a stern expression.",
        "oCEan": "A CEO standing tall in front of a massive, perfectly structured bank vault.",
        "oCeAN": "A librarian carefully dusting old, beloved books with a worried look.",
        "oCeAn": "A monk sweeping a courtyard with practiced, calm strokes.",
        "oCeaN": "A guard standing watch on a lonely, cold tower.",
        "oCean": "An ice sculptor carving a precise, beautiful statue in the freezing cold.",
        "ocEAN": "A chaotic but loving baker offering a beautiful pie in a messy kitchen.",
        "ocEAn": "A charismatic party host with a tray of drinks in a lively room.",
        "ocEaN": "A rebel with a megaphone, standing on a makeshift barricade.",
        "ocEan": "A smooth-talking merchant in a bustling bazaar.",
        "oceAN": "A figure sitting in an attic surrounded by old, cherished memories.",
        "oceAn": "A friendly gardener resting on a bench, admiring their simple plot.",
        "oceaN": "An old prospector panning for gold, muttering under their breath.",
        "ocean": "A scavenger smoothly navigating a post-apocalyptic junkyard without a care."
    }
    
    return nicknames[code], light, shadow, visuals[code], code

md_content = """# Archetypes: The 32 OCEAN Expressions

An archetypal system inspired by Caroline Myss, but mathematically rooted in the Big Five (OCEAN) personality traits. Each of the 32 combinations represents a distinct archetype with its own light and shadow attributes.

## The OCEAN System (Big Five)

The Big Five traits represent fundamental sliders of human personality:
1. **O (Openness):** High `O` (Visionary, Creative) vs. Low `o` (Traditional, Practical)
2. **C (Conscientiousness):** High `C` (Organized, Disciplined) vs. Low `c` (Spontaneous, Flexible)
3. **E (Extraversion):** High `E` (Outgoing, Charismatic) vs. Low `e` (Introverted, Observant)
4. **A (Agreeableness):** High `A` (Empathetic, Compassionate) vs. Low `a` (Assertive, Logical)
5. **N (Neuroticism):** High `N` (Sensitive, Vigilant) vs. Low `n` (Calm, Resilient)

## Card Design System

- **Front:** The archetype's Nickname, a full-bleed evocative Picture, and a subtle icon representing their strongest trait.
- **Back:** The OCEAN code (e.g., *OCEaN*), Light Attributes, Shadow Attributes, and a brief lore or quote.
- **Visual Theme:** Rich, symbolic, and slightly mystical but grounded in modern psychological archetypes (similar to tarot cards with an elemental or fantasy influence).

---

## The 32 Cards

"""

for combo in combos:
    name, light, shadow, visual, code = get_archetype(*combo)
    md_content += f"### {name} ({code})\n\n"
    md_content += f"- **Light Attributes:** {light}\n"
    md_content += f"- **Shadow Attributes:** {shadow}\n"
    md_content += f"- **Visual Concept:** {visual}\n\n"

with open("agents.md", "w") as f:
    f.write(md_content)

print("Done")
