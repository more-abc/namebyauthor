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
print(na.generate_name(module, author))
# errortools by more_abc

# Generate URL-safe slug
print(na.generate_slug(module, author))
# errortools-by-more-abc

# Generate short unique hash signature
print(na.generate_signature(module, author))
# 7f16a8b2c7e8d910

# Generate full unique ID
print(na.generate_id(module, author))
# errortools-by-more-abc-7f16a8b2
```
```
# metadatas
import namebyauthor as na  

__license__: str = "MIT"
__title__: str = "namebyauthor"
__url__: str = "https://github.com/more-abc/namebyauthor"

__fullname__ = na.generate_name(__title__, __author__)
__slug__ = na.generate_slug(__title__, __author__)
__signature__ = na.generate_signature(__title__, __author__)
__uid__ = na.generate_id(__title__, __author__)
```
