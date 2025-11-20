# Credit @ph0enix_web.
# Maintained by @ph0enix_web
# New maintainer @ph0enix_web
# Thank you to the original developer for the base code.
# Credit to the original developer.
# For support, contact @ph0enix_web on Telegram. 
# This is a free and open-source project. 
from os import environ
from typing import Dict, Optional


class TokenParser:
    def __init__(self, config_file: Optional[str] = None):
        self.tokens = {}
        self.config_file = config_file

    def parse_from_env(self) -> Dict[int, str]:
        self.tokens = dict(
            (c + 1, t)
            for c, (_, t) in enumerate(
                filter(
                    lambda n: n[0].startswith("MULTI_TOKEN"), sorted(environ.items())
                )
            )
        )
        return self.tokens
