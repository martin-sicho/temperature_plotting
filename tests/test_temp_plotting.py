#!/usr/bin/env python
# coding: utf-8

import pytest

import temperature_plotting as tpl
from matplotlib import pyplot as plt
import os


def test_compute_mean():
    calc = tpl.compute_mean([0, 10, 20])
    assert calc == 10 , "Does not look like a the mean to me :)"
    assert type(calc) == float
    
    with pytest.raises(TypeError):
        calc = tpl.compute_mean(["A", "B"])
        
    # calc = tpl.compute_mean([])

def test_save_plot():
    test_number = 5

    fig, ax = plt.subplots()
    tpl.save_plot(fig, test_number)
    
    expected_file = f"plot_{test_number}.png"
    assert os.path.exists(expected_file), f"File of correct name should exist: {path}"
    os.remove(expected_file)
    
    unsupported_types = ["", None]
    for tp in unsupported_types:
        with pytest.raises(TypeError):
            tpl.save_plot(fig, tp)
        assert not os.path.exists(expected_file), f"File should not exist: {path}"    

def test_main():
    tpl.main()





