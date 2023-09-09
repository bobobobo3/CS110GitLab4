import main
import io
import sys
import re
import math


def test_main_1():
    n1, n2, n3, mv  = main.main()
    assertval = min(n1, n2, n3)
    assert mv == assertval 
