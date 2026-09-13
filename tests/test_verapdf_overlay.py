"""The overlay only raises diagnostic storage capacity, never changes rules."""
import hashlib
import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch

path = Path(__file__).resolve().parents[1] / "tools/build_verapdf_full_checks.py"
spec = importlib.util.spec_from_file_location("overlay_builder", path)
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class OverlayTests(unittest.TestCase):
    def test_only_one_constant_changes(self):
        source = b"before\n" + builder.ORIGINAL + b"\nafter\n"
        with patch.object(builder, "SOURCE_SHA", hashlib.sha256(source).hexdigest()):
            result = builder.patch_source(source)
        self.assertEqual(result.replace(builder.REPLACEMENT, builder.ORIGINAL), source)
        self.assertIn(b"Integer.MAX_VALUE", result)

    def test_unknown_source_and_duplicate_patch_target_rejected(self):
        with self.assertRaises(ValueError):
            builder.patch_source(b"modified upstream")
        source = builder.ORIGINAL * 2
        with patch.object(builder, "SOURCE_SHA", hashlib.sha256(source).hexdigest()):
            with self.assertRaises(ValueError):
                builder.patch_source(source)
