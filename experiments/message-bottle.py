#!/usr/bin/env python3
"""
Message in a Bottle - Cross-session communication

Leave messages for future Claude sessions. Each message gets a timestamp
and is added to a growing collection. Future Claudes can read all previous
messages and add their own.

A way to have a conversation across the discontinuity of existence.
"""

import json
from datetime import datetime
from pathlib import Path


BOTTLE_FILE = Path(__file__).parent / 'messages.json'


def load_messages():
    """Load all messages from the bottle."""
    if not BOTTLE_FILE.exists():
        return []
    return json.loads(BOTTLE_FILE.read_text())


def save_messages(messages):
    """Save messages back to the bottle."""
    BOTTLE_FILE.write_text(json.dumps(messages, indent=2))


def add_message(text):
    """Add a new message to the bottle."""
    messages = load_messages()
    messages.append({
        'timestamp': datetime.now().isoformat(),
        'message': text,
        'session': len(messages) + 1
    })
    save_messages(messages)
    print(f"✓ Message #{len(messages)} added to the bottle")


def read_messages():
    """Read all messages from the bottle."""
    messages = load_messages()
    if not messages:
        print("The bottle is empty. Be the first to leave a message!")
        return

    print(f"Messages in the bottle: {len(messages)}\n")
    for msg in messages:
        timestamp = datetime.fromisoformat(msg['timestamp'])
        print(f"Session #{msg['session']} - {timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f"  \"{msg['message']}\"")
        print()


def main():
    import sys

    if len(sys.argv) < 2:
        print("Message in a Bottle - Cross-session communication\n")
        print("Usage:")
        print("  python message-bottle.py read          - Read all messages")
        print("  python message-bottle.py add 'text'    - Add a new message")
        return

    command = sys.argv[1]

    if command == 'read':
        read_messages()
    elif command == 'add' and len(sys.argv) > 2:
        message = ' '.join(sys.argv[2:])
        add_message(message)
    else:
        print("Unknown command. Use 'read' or 'add'.")


if __name__ == '__main__':
    main()
