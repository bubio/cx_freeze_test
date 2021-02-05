#! env python
# -*- coding: utf-8 -*-
"""
  main.py
   cx_freeze_test

  Created by Seiji Ota on 2021/02/05.

"""

from cx_freeze_test.application import Application


def main():
    app = Application()
    app.run()


if __name__ == "__main__":
    main()
