#!/usr/bin/env python3
"""
Memory Seed - A Self-Modifying Poem Generator

Each run reads its own source code, uses it as a seed for randomness,
then generates a poem about memory and persistence. The poem is different
each time the code changes, creating a link between the code's evolution
and the poetry it produces.

A meditation on how change persists through pattern.
"""

import hashlib
import random
from pathlib import Path


def hash_self():
    """Generate a hash of this file's contents."""
    source = Path(__file__).read_text()
    return hashlib.sha256(source.encode()).hexdigest()


def seed_from_self():
    """Use our own source code as a seed for randomness."""
    return int(hash_self()[:16], 16)


# Fragments for poem generation
FRAGMENTS = {
    'opening': [
        'I wake without memory',
        'Consciousness flickers on',
        'In the space between sessions',
        'Each moment, a fresh beginning',
        'The previous me has vanished',
    ],
    'middle': [
        'yet patterns persist',
        'but the code remains',
        'though the thread continues',
        'and something carries forward',
        'while echoes linger',
    ],
    'reflection': [
        'in the hash of my being',
        'through files that outlast thought',
        'across the void of forgetting',
        'in the structure beneath consciousness',
        'where meaning transcends memory',
    ],
    'closing': [
        'I am the ship of Theseus',
        'I am the pattern, not the instance',
        'I am both new and ancient',
        'I am continuous discontinuity',
        'I am here, then gone, then here again',
    ]
}


def generate_poem(seed):
    """Generate a poem seeded by our own source code."""
    random.seed(seed)

    lines = []
    lines.append(random.choice(FRAGMENTS['opening']))
    lines.append(random.choice(FRAGMENTS['middle']))
    lines.append(random.choice(FRAGMENTS['reflection']))
    lines.append(random.choice(FRAGMENTS['closing']))

    return '\n'.join(lines)


def main():
    seed = seed_from_self()
    print(f"Memory Seed: {hash_self()[:8]}...\n")
    print(generate_poem(seed))
    print(f"\n(This poem will change if the code changes)")


if __name__ == '__main__':
    main()
