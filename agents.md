# AGENTS.md

## Project Overview
This project is dedicated to designing a 32-type archetype card system inspired by Caroline Myss, but mathematically rooted in the Big Five (OCEAN) personality traits instead of traditional esoteric archetypes. 

## The OCEAN 32-Type System
The underlying framework consists of 32 personality combinations derived from the OCEAN traits:
- **O (Openness)**: High (O) vs Low (o)
- **C (Conscientiousness)**: High (C) vs Low (c)
- **E (Extraversion)**: High (E) vs Low (e)
- **A (Agreeableness)**: High (A) vs Low (a)
- **N (Neuroticism)**: High (N) vs Low (n)

Each combination is represented by a sequence of uppercase and lowercase letters.
Examples:
1. `OCEAN` (All traits high)
2. `OCEAn` (O,C,E,A high; Low Neuroticism)
3. `OcEaN` (High O, Low C, High E, Low A, High N)
...and so on for all 32 combinations.

## AI Agent Workflow & Instructions
As an AI coding/design agent working in this repository, your primary objective is to help flesh out this system. When prompted, you should actively contribute to the following pipeline:

1. **Gender & Demographic Analysis:**
   - Refer to available psychological data/statistics on the Big Five to determine whether a male or a female figure is more likely to have each specific OCEAN combination.
   - Assign the most statistically probable gender to that archetype profile.

2. **Naming & Attributes Formulation:**
   - Using the gender determined in step 1, come up with realistic, fun, and evocative nicknames for all 32 combinations.
   - Define their **Light Attributes**: Their core strengths, positive manifestations, and best environment.
   - Define their **Shadow Attributes**: Their blind spots, negative manifestations, and weaknesses.

3. **Visual & Aesthetic Concepting:**
   - Develop descriptive imagery and visual concepts representing the archetype's core essence, incorporating the statistically probable gender.
   - These image prompts will be used for card generation or generating visuals with AI image generators.

4. **Card Design & Assembly:**
   - Design the digital card layout (such as HTML/CSS templates or Markdown specifications) to fit all text elements (nicknames, light/shadow attributes) alongside the generated pictures. 
   - **Important:** Type-cards are designed in Tailwind CSS.
   - Ensure the UI/UX fits an overarching thematic and premium design system.

## Project Standards & Style
- Avoid traditional astrology or generic fantasy tropes unless tightly linked to the psychological mechanism of the OCEAN traits.
- The tone should be psychological, engaging, empowering, yet objective.
- Keep the generated data organized: store each archetype in an individual Markdown file within the `archetypes/` directory using an index prefix to avoid case-insensitive filesystem collisions (e.g., `archetypes/03_OCEaN.md`) rather than lumping them into one file.
