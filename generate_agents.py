import itertools

traits = [
    ('O', 'o', 'Open', 'Traditional'),
    ('C', 'c', 'Organized', 'Spontaneous'),
    ('E', 'e', 'Extraverted', 'Introverted'),
    ('A', 'a', 'Agreeable', 'Assertive'),
    ('N', 'n', 'Sensitive', 'Calm')
]

combinations = list(itertools.product(*[(t[0], t[1]) for t in traits]))

print("# The 32 OCEAN Archetypes\n")

for i, combo in enumerate(combinations):
    code = "".join(combo)
    
    # Simple logic to determine a basic name
    # We will let AI give a better name, but generate a placeholder structure
    print(f"## {i+1}. {code} (The Placeholder)")
    print("**Light Attributes**:")
    print("**Shadow Attributes**:")
    print("**Visual Concept**:")
    print("\n")

