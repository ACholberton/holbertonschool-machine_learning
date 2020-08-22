#!/usr/bin/env python3.6
"""Function that returns two placeholdres, x and y, for neural network"""


import tensorflow as tf


def create_placeholders(nx, classes):

    x = tf.placeholder(tf.float32, (name, nx), name="x")
    y = tf.placeholder(tf.float32, (name, classes), name="y")

    return (x, y)

