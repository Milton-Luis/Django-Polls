import os
import sys
from pathlib import Path

import dynaconf

BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.append(os.path.join(BASE_DIR, "apps"))


settings = dynaconf.DjangoDynaconf(__name__)
