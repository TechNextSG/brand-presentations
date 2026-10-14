# -*- coding: utf-8 -*-
"""Build the brand kits (plain HTML pages): python -B _src/build.py. All content is in _src/kit_data.py, the pages come from _src/site.py."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import site_build  # noqa: E402

site_build.main()
