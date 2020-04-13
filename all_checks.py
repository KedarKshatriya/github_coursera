#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
import os
import sys


def check_reboot():
    """Returns true if a computer has a pending reboot"""
    return os.path.exists("/run/reboot-required")


def main():
    if check_reboot():
        print("pending reboot.")
        sys.exit(1)
    print("everythin ok")
    sys.exit(0)


main()
