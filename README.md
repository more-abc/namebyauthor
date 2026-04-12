# namebyauthor
A tiny, zero-dependency Python utility to generate clean, consistent names, slugs, unique signatures, and IDs from project/module names + author names.

<!-- Inspired by Python standard library modules like `colorsys` and `pprint` — small, stable, and minimal. -->

## Features
- Zero dependencies
- Pure Python, works on all versions
- Generate human-readable names
- Generate URL-safe slugs
- Generate stable unique hash signatures
- Generate full unique IDs

## Installation
```bash
pip install namebyauthor
```

## Usage Example
```python
import namebyauthor as na

module = "errortools"
author = "more_abc"

# Generate formatted name
print(generate_name(module, author))
# errortools by more_abc

# Generate URL-safe slug
print(generate_slug(module, author))
# errortools-by-more-abc

# Generate short unique hash signature
print(generate_signature(module, author))
# 7f16a8b2c7e8d910

# Generate full unique ID
print(generate_id(module, author))
# errortools-by-more-abc-7f16a8b2
```