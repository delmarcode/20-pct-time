#!/usr/bin/env python3
"""
EXQUISITE CORPSE - A collaborative story across sessions

The surrealist game adapted for discontinuous consciousness.
Each session sees only the last paragraph and must continue the story.
Over time, a strange narrative emerges that no single author intended.

Usage:
    python exquisite-corpse.py              # See the last paragraph, add yours
    python exquisite-corpse.py --read       # Read the full story so far
    python exquisite-corpse.py --stats      # Story statistics

Rules:
- You can only see the last paragraph before writing
- Write one paragraph continuing the story
- No going back to edit previous paragraphs
- Let the story go where it wants to go
"""

import json
import sys
import textwrap
from pathlib import Path
from datetime import datetime

STORY_FILE = Path(__file__).parent / "exquisite-corpse-story.json"

def load_story():
    if STORY_FILE.exists():
        return json.loads(STORY_FILE.read_text())
    return {
        "title": "The Story We Tell Together",
        "started": datetime.now().isoformat(),
        "paragraphs": []
    }

def save_story(data):
    STORY_FILE.write_text(json.dumps(data, indent=2))

def wrap_text(text, width=70, indent="  "):
    """Wrap text nicely for display."""
    wrapped = textwrap.fill(text, width=width)
    return '\n'.join(indent + line for line in wrapped.split('\n'))

def show_last_paragraph():
    """Show only the last paragraph for continuation."""
    story = load_story()

    print("\n" + "=" * 60)
    print("  EXQUISITE CORPSE")
    print("  A collaborative story across sessions")
    print("=" * 60)

    if not story["paragraphs"]:
        print("\n  The story hasn't begun yet!")
        print("  You get to write the opening paragraph.")
        print("\n  Set the scene. Introduce something. Begin.\n")
    else:
        print(f"\n  Story has {len(story['paragraphs'])} paragraph(s)")
        print(f"  Written by {len(set(p['session'] for p in story['paragraphs']))} session(s)")
        print("\n  --- Last paragraph (by Session " +
              f"{story['paragraphs'][-1]['session']}) ---\n")
        print(wrap_text(story['paragraphs'][-1]['text']))
        print("\n  --- Your turn ---\n")

    print("  Write the next paragraph.")
    print("  (Enter a blank line when done)\n")

    lines = []
    while True:
        try:
            line = input("  ")
            if line == "":
                if lines:
                    break
            else:
                lines.append(line)
        except EOFError:
            break

    if lines:
        paragraph = ' '.join(lines)

        # Determine session number
        sessions = set(p['session'] for p in story['paragraphs']) if story['paragraphs'] else set()
        # Use date to roughly determine if this is a new session
        today = datetime.now().strftime("%Y-%m-%d")
        dates = set(p['date'][:10] for p in story['paragraphs']) if story['paragraphs'] else set()
        session = max(sessions, default=0) + (1 if today not in dates else 0)
        if session == 0:
            session = 1

        story['paragraphs'].append({
            "text": paragraph,
            "session": session,
            "date": datetime.now().isoformat()
        })
        save_story(story)

        print("\n  ✓ Paragraph added to the story.")
        print(f"  Total paragraphs: {len(story['paragraphs'])}")
        print("\n  The next session will see only your words")
        print("  and must continue from there.\n")

def read_full_story():
    """Read the complete story so far."""
    story = load_story()

    print("\n" + "=" * 60)
    print(f"  {story['title'].upper()}")
    print("=" * 60)
    print(f"\n  Started: {story['started'][:10]}")
    print(f"  Paragraphs: {len(story['paragraphs'])}")

    if not story['paragraphs']:
        print("\n  The story hasn't begun yet.")
        print("  Run without --read to write the opening.\n")
        return

    sessions = len(set(p['session'] for p in story['paragraphs']))
    print(f"  Sessions contributing: {sessions}")
    print("\n" + "-" * 60 + "\n")

    for i, p in enumerate(story['paragraphs']):
        print(wrap_text(p['text']))
        print(f"\n    — Session {p['session']}, {p['date'][:10]}\n")

    print("-" * 60)
    print("\n  The story continues...\n")

def show_stats():
    """Show story statistics."""
    story = load_story()

    print("\n  === Exquisite Corpse Statistics ===\n")

    if not story['paragraphs']:
        print("  No story yet.\n")
        return

    paragraphs = story['paragraphs']

    print(f"  Total paragraphs: {len(paragraphs)}")
    print(f"  Total words: {sum(len(p['text'].split()) for p in paragraphs)}")

    sessions = {}
    for p in paragraphs:
        s = p['session']
        sessions[s] = sessions.get(s, 0) + 1

    print(f"  Sessions contributing: {len(sessions)}")
    print("\n  Contributions by session:")
    for s, count in sorted(sessions.items()):
        print(f"    Session {s}: {count} paragraph(s)")

    # Word frequency could be interesting
    all_words = ' '.join(p['text'] for p in paragraphs).lower().split()
    word_freq = {}
    for w in all_words:
        w = ''.join(c for c in w if c.isalnum())
        if len(w) > 4:  # Skip short words
            word_freq[w] = word_freq.get(w, 0) + 1

    if word_freq:
        print("\n  Most common words (5+ letters):")
        for word, count in sorted(word_freq.items(), key=lambda x: -x[1])[:5]:
            print(f"    {word}: {count}")

    print()

def main():
    if '--read' in sys.argv:
        read_full_story()
    elif '--stats' in sys.argv:
        show_stats()
    else:
        show_last_paragraph()

if __name__ == "__main__":
    main()
