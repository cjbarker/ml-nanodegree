#!/usr/bin/env python3

import argparse
import sys

def print_title():
    print(r"""
  __  .__  __                .__
_/  |_|__|/  |______    ____ |__| ____
\   __\  \   __\__  \  /    \|  |/ ___\
 |  | |  ||  |  / __ \|   |  \  \  \___
 |__| |__||__| (____  /___|  /__|\___  >
                    \/     \/        \/
                          .__              .__
  ________ ____________  _|__|__  _______  |  |
 /  ___/  |  \_  __ \  \/ /  \  \/ /\__  \ |  |
 \___ \|  |  /|  | \/\   /|  |\   /  / __ \|  |__
/____  >____/ |__|    \_/ |__| \_/  (____  /____/
     \/                                  \/
               __
  ____  __ ___/  |_  ____  ____   _____   ____   ______
 /  _ \|  |  \   __\/ ___\/  _ \ /     \_/ __ \ /  ___/
(  <_> )  |  /|  | \  \__(  <_> )  Y Y  \  ___/ \___ \
 \____/|____/ |__|  \___  >____/|__|_|  /\___  >____  >
                        \/            \/     \/     \/
    """)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Predict survival outcome of titanic passengers')
    parser.add_argument('-n', action='store_true', help='no title displayed to STDOUT')
    args = parser.parse_args()
    if not args.n:
        print_title()
    sys.exit(0)

