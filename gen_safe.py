import os
import itertools

os.makedirs('archetypes', exist_ok=True)

traits = [('O', 'o'), ('C', 'c'), ('E', 'e'), ('A', 'a'), ('N', 'n')]
combos = list(itertools.product(*traits))

# Gender distribution heuristic based on Big Five research:
# Women typically score higher in Neuroticism and Agreeableness cross-culturally.
# Men typically score lower in both (equivalent to Low a, Low n here).

def get_archetype(i, combo):
    o, c, e, a, n = combo
    code = o+c+e+a+n
    
    # Calculate gender probability
    f_score = 0
    m_score = 0
    
    if a == 'A': f_score += 1
    else: m_score += 1
    
    if n == 'N': f_score += 1
    else: m_score += 1
    
    # Since it's exactly 2 traits we are heavily weighting, it can tie. 
    # If tie, we can alternate or default evenly, let's alternate based on index to ensure 50-50 split. 
    # Actually wait: A=1, N=1 -> F. A=0, N=0 -> M. A=1, N=0 (Tie). A=0, N=1 (Tie).
    # Since there are 32 combos, 16 will be M, 16 will be F exactly if we tie-break perfectly.
    # Tie conditions exist in 16 combinations.
    if f_score > m_score:
        gender = "Female"
    elif m_score > f_score:
        gender = "Male"
    else:
        # Tie break based on index parity to guarantee 50/50 split across the ties
        gender = "Female" if i % 2 == 0 else "Male"
    
    # Nickname placeholder since I will generate them programmatically later
    nickname = f"The {code} Placeholder"
    
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

    figure = "A female figure" if gender == "Female" else "A male figure"
    visual = f"{figure} embodying the combination of {o_light}, {c_light}, and {e_light}."

    content = f"### {code} - {nickname}\n\n"
    content += f"- **Gender Probability:** {gender} (Based on Big 5 statistics for Agreeableness and Neuroticism)\n"
    content += f"- **Light Attributes:** {light}\n"
    content += f"- **Shadow Attributes:** {shadow}\n"
    content += f"- **Visual Concept:** {visual}\n"
    
    # To fix macOS case-insensitive issue, prefix with the index number so OceaN and ocean don't collide
    filename = f"archetypes/{i+1:02d}_{code}.md"
    with open(filename, 'w') as f:
        f.write(content)
        
for i, combo in enumerate(combos):
    get_archetype(i, combo)

print("Safely regenerated 32 files.")
