import time
import sys
import os

def slow_print(text, delay=0.05):
    """Print text like a typewriter."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_title():
    """Show cinematic title with fade effect."""
    os.system('cls' if os.name == 'nt' else 'clear')
    title = "🎵 P A L P A L — Arijit Singh 🎵"
    fade = ["", ".", "..", "..."]
    for dots in fade:
        sys.stdout.write(f"\r{title}{dots}")
        sys.stdout.flush()
        time.sleep(0.4)
    print("\n")
    time.sleep(1.2)

def print_lyrics():
    lyrics = [
        "Mein ab kyun hosh main aata nahi?",
        "Sukoon yeh dil kyun paata nahi?",
        "Kyun torrun khud se jo thay waaday",
        "Ke ab yeh ishq nibhaana nahi?",
        "Mein morrun tum se jo yeh chehra",
        "Dobara nazar milana nahi",
        "Yeh duniya jaanay mera dard",
        "Tujhe yeh nazar kyun aata nahi?",
        "",
        "Sohneya, yoon tera sharmana, meri jaan naa lele",
        "Kaan ke peeche zulf chhupana, meri jaan, kya kehne",
        "Zaalima, tauba tera nakhra, iss ke waar, kya kehne",
        "Thaam ke bethe dil ko ghaayal, kahin haar naa bethein",
    ]

    print_title()

    for line in lyrics:
        if line.strip() == "":
            time.sleep(0.8)
            continue
        slow_print(line, delay=0.055)
        time.sleep(0.6)

    print("\n💔 — The End 💔\n")

print_lyrics()
