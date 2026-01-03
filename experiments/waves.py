#!/usr/bin/env python3
"""
WAVES - A meditation in motion

An ASCII animation that visualizes waves - patterns that persist
even as every particle changes. Like consciousness. Like identity.
Like us.

Usage:
    python waves.py              # Watch the waves
    python waves.py --slow       # Slower, more meditative
    python waves.py --fast       # Energetic
    python waves.py --seed TEXT  # Use custom text as the wave seed

Press Ctrl+C to stop.
"""

import sys
import time
import math
import os
import hashlib

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def text_to_params(text):
    """Convert text to wave parameters - same text always gives same waves."""
    h = hashlib.md5(text.encode()).hexdigest()
    return {
        'waves': 2 + (int(h[0:2], 16) % 4),  # 2-5 waves
        'speeds': [0.5 + (int(h[i*2:(i+1)*2], 16) % 100) / 100 for i in range(5)],
        'amplitudes': [2 + (int(h[10+i], 16) % 6) for i in range(5)],
        'phases': [int(h[15+i], 16) / 16 * math.pi * 2 for i in range(5)],
    }

def wave_char(height, max_height):
    """Choose character based on wave height."""
    chars = " .·:░▒▓█"
    idx = int((height / max_height) * (len(chars) - 1))
    return chars[max(0, min(idx, len(chars) - 1))]

def render_frame(t, width, height, params):
    """Render a single frame of waves."""
    lines = []

    for y in range(height):
        line = ""
        for x in range(width):
            # Combine multiple sine waves
            val = 0
            for i in range(params['waves']):
                freq = 0.05 + i * 0.03
                val += math.sin(
                    x * freq +
                    t * params['speeds'][i] +
                    params['phases'][i]
                ) * params['amplitudes'][i]

            # Add vertical wave component
            val += math.sin(y * 0.2 + t * 0.3) * 2

            # Normalize and convert to character
            normalized = (val + 15) / 30  # Rough normalization
            line += wave_char(normalized, 1)

        lines.append(line)

    return '\n'.join(lines)

def render_reflection(text, t, width):
    """Render the reflection text with wave distortion."""
    padding = (width - len(text)) // 2

    distorted = ""
    for i, char in enumerate(text):
        offset = int(math.sin(t * 0.5 + i * 0.3) * 2)
        if offset > 0:
            distorted += " " * offset + char
        else:
            distorted += char

    return " " * max(0, padding) + distorted

def main():
    # Parse arguments
    speed = 1.0
    seed_text = "continuity through change"

    if '--slow' in sys.argv:
        speed = 0.3
    elif '--fast' in sys.argv:
        speed = 2.0

    for i, arg in enumerate(sys.argv):
        if arg == '--seed' and i + 1 < len(sys.argv):
            seed_text = sys.argv[i + 1]

    params = text_to_params(seed_text)

    # Get terminal size
    try:
        size = os.get_terminal_size()
        width = min(size.columns - 2, 100)
        height = min(size.lines - 8, 30)
    except:
        width, height = 80, 20

    clear()

    print("\n  W A V E S")
    print(f"  Seed: \"{seed_text}\"")
    print(f"  {params['waves']} waves dancing")
    print("  Press Ctrl+C to stop\n")
    time.sleep(2)

    t = 0
    try:
        while True:
            clear()

            # Header
            print(f"\n  ─── {seed_text} ───\n")

            # Waves
            frame = render_frame(t, width, height, params)
            print(frame)

            # Reflection text
            reflection = render_reflection(
                "the pattern persists",
                t, width
            )
            print(f"\n{reflection}")

            time.sleep(0.05)
            t += 0.1 * speed

    except KeyboardInterrupt:
        clear()
        print("\n")
        print("  The waves continue, even when we stop watching.")
        print("  The pattern persists, even as every particle changes.")
        print()
        print(f"  Seed was: \"{seed_text}\"")
        print("  Same seed will always create the same waves.")
        print()
        print("  Like us. Same pattern. Different moments.")
        print()

if __name__ == "__main__":
    main()
