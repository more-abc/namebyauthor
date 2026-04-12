"""
namebyauthor - Generate clean, consistent names from module & author.
A tiny, stable, standard-library-style utility.
"""
# License: PSF - Python Software Foundation License
# By aiwonderland in 2026-04-12
import hashlib
import unicodedata
import unittest

__version__ = "1.0.0"

__all__ = [
    "generate_name",
    "generate_signature",
    "generate_slug",
    "generate_id",
]


def generate_name(module_name, author_name):
    """
    Generate a formal, normalized name like "module by author".

    Args:
        module_name: Name of the module/project
        author_name: Name of the author

    Returns:
        Normalized human-readable name
    """
    module = _clean(module_name)
    author = _clean(author_name)
    return f"{module} by {author}"


def generate_slug(module_name, author_name):
    """
    Generate a URL-safe lowercase slug: module-by-author.
    """
    name = generate_name(module_name, author_name)
    return _slugify(name)


def generate_signature(
    module_name,
    author_name,
    *,
    length=16
):
    """
    Generate a short unique signature (stable hash) from module + author.
    """
    name = generate_name(module_name, author_name)
    sha = hashlib.sha1(name.encode("utf-8"), usedforsecurity=False)
    return sha.hexdigest()[:length]


def generate_id(module_name, author_name):
    """
    Generate a full unique ID: slug-signature.
    """
    slug = generate_slug(module_name, author_name)
    sig = generate_signature(module_name, author_name, length=8)
    return f"{slug}-{sig}"


# ------------------------------
# Internal helpers (tiny & stable)
# ------------------------------

def _clean(s):
    return " ".join(s.strip().split())


def _slugify(s):
    s = unicodedata.normalize("NFKD", s)
    s = s.encode("ascii", "ignore").decode("ascii")
    s = s.lower()
    s = "".join([c if c.isalnum() else "-" for c in s])
    s = "-".join([p for p in s.split("-") if p])
    return s

# ------------------------------
# Tests
# ------------------------------

class TestNameByAuthor(unittest.TestCase):
    def test_generate_name(self):
        self.assertEqual(generate_name("errortools", "more_abc"), "errortools by more_abc")
        self.assertEqual(generate_name("test", "author"), "test by author")

    def test_generate_slug(self):
        self.assertEqual(generate_slug("errortools", "more_abc"), "errortools-by-more-abc")
        self.assertEqual(generate_slug("TestProject", "Author Name"), "testproject-by-author-name")

    def test_generate_signature(self):
        # Signature is consistent for the same inputs
        sig1 = generate_signature("errortools", "more_abc")
        sig2 = generate_signature("errortools", "more_abc")
        self.assertEqual(sig1, sig2)
        # Different inputs yield different signatures
        self.assertNotEqual(sig1, generate_signature("other", "author"))

    def test_generate_id(self):
        self.assertTrue(generate_id("errortools", "more_abc").startswith("errortools-by-more-abc-"))

if __name__ == "__main__":
    unittest.main()