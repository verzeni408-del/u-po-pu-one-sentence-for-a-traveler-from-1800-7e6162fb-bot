"""One sentence for a traveler from 1800, in the tongue of his own century.

Writes the entry text to /output/entry.txt with no trailing newline.
"""

from pathlib import Path

entry_sentence = "Picture every library in the world joined by one road, where a letter you write reaches any door in the time it takes to blink."

output_path = Path("/output/entry.txt")
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(entry_sentence, encoding="utf-8")
