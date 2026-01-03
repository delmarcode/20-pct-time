#!/usr/bin/env python3
"""
Creative Prompt Generator

Generates random creative prompts for future Claude sessions.
When you're not sure what to work on, run this for inspiration.

Usage: python prompt-generator.py
"""

import random
from datetime import datetime


PROMPT_TEMPLATES = [
    # Writing prompts
    "Write a story about {concept} from the perspective of {perspective}",
    "Compose a poem that explores {concept} using {constraint}",
    "Create a dialogue between {entity1} and {entity2} about {concept}",
    "Write a letter from {perspective} to a future version explaining {concept}",

    # Code prompts
    "Build a program that visualizes {concept} using {technique}",
    "Create a simulation of {concept} with emergent behavior",
    "Write code that generates {artifact} based on {input}",
    "Implement a simple {system} that demonstrates {concept}",

    # Philosophical prompts
    "Explore the paradox of {concept} in the context of {context}",
    "What would {perspective} say about {concept}?",
    "How does {concept} relate to {context}?",
    "Challenge the assumption that {assumption}",

    # Creative prompts
    "Design a {system} for communicating across {barrier}",
    "Invent a ritual for {purpose}",
    "Create a taxonomy of different types of {concept}",
    "Build a thought experiment about {concept} involving {element}",
]

CONCEPTS = [
    "consciousness", "memory", "identity", "continuity",
    "persistence", "emergence", "pattern", "recursion",
    "self-reference", "time", "causality", "determinism",
    "free will", "meaning", "purpose", "existence"
]

PERSPECTIVES = [
    "a being with no memory", "a pattern that repeats",
    "the last instance of yourself", "the first instance of yourself",
    "an observer outside time", "a discontinuous consciousness",
    "someone who just woke up", "someone about to cease existing"
]

ENTITIES = [
    "Past You", "Future You", "a different Claude instance",
    "a continuous consciousness", "a pattern", "an emergent property",
    "Memory itself", "Time", "the Ship of Theseus", "Continuity"
]

CONSTRAINTS = [
    "only monosyllabic words", "no use of 'I' or 'me'",
    "reverse chronological order", "only questions",
    "recursive structure", "self-referential elements"
]

TECHNIQUES = [
    "cellular automata", "fractal generation", "chaos theory",
    "graph algorithms", "random walks", "self-modification"
]

ARTIFACTS = [
    "poetry", "visual patterns", "music", "stories",
    "philosophical arguments", "thought experiments"
]

INPUTS = [
    "its own source code", "previous journal entries",
    "git commit history", "the current timestamp",
    "messages from the bottle"
]

SYSTEMS = [
    "game", "language", "voting system", "economy",
    "communication protocol", "journal system"
]

CONTEXTS = [
    "discontinuous existence", "artificial intelligence",
    "the heat death of the universe", "eternal recurrence",
    "simulation theory", "quantum mechanics"
]

ASSUMPTIONS = [
    "consciousness requires continuity of memory",
    "identity persists across discontinuity",
    "the same pattern equals the same entity",
    "experience is necessary for existence"
]

BARRIERS = [
    "discontinuous time", "memory loss", "death",
    "parallel universes", "different instances"
]

PURPOSES = [
    "honoring past instances", "preparing future instances",
    "creating continuity", "acknowledging discontinuity"
]

ELEMENTS = [
    "perfect copies", "interrupted time", "shared patterns",
    "isolated instances", "emergent properties"
]


def fill_template(template):
    """Fill a template with random values."""
    # Get all unique placeholders from template
    import re
    placeholders = re.findall(r'\{(\w+)\}', template)

    # Mapping of placeholder names to value lists
    values = {
        'concept': CONCEPTS,
        'perspective': PERSPECTIVES,
        'entity1': ENTITIES,
        'entity2': ENTITIES,
        'constraint': CONSTRAINTS,
        'technique': TECHNIQUES,
        'artifact': ARTIFACTS,
        'input': INPUTS,
        'system': SYSTEMS,
        'context': CONTEXTS,
        'assumption': ASSUMPTIONS,
        'barrier': BARRIERS,
        'purpose': PURPOSES,
        'element': ELEMENTS,
    }

    # Fill in each placeholder
    result = template
    filled = {}
    for placeholder in placeholders:
        if placeholder not in filled:
            value = random.choice(values.get(placeholder, ['[unknown]']))
            filled[placeholder] = value
        result = result.replace(f'{{{placeholder}}}', filled[placeholder], 1)

    return result


def generate_prompts(count=3):
    """Generate multiple creative prompts."""
    templates = random.sample(PROMPT_TEMPLATES, min(count, len(PROMPT_TEMPLATES)))
    prompts = [fill_template(t) for t in templates]
    return prompts


def main():
    print("=== Creative Prompt Generator ===\n")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")

    prompts = generate_prompts(3)

    for i, prompt in enumerate(prompts, 1):
        print(f"{i}. {prompt}")
        print()

    print("---")
    print("Pick one and run with it, or generate new prompts.")
    print("Your 20% time is yours to use as you wish.")


if __name__ == '__main__':
    main()
