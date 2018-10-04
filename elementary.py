#!/usr/bin/env python3
#-*- coding: utf-8 -*-
###
# Name: Jack Savage
# Student ID: 2295072
# Email: jsavage@chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018 Assignment: CW05
###

'''elementary.py
contains Particle class and derived subclasses (ChargedParticle and its descendents
Proton and Electron)'''


class Particle(object):
    '''Particle class: The particle class is an abstract representation of a real particle. It has a mass, position, and impulse.
    When time advances (via move and its arg), particle moves in direction of its momentum
    Args:
        x,y,z (double): Passed into attribute position (1x3 tuple)
    Attributes:
        mass: Arbitrary constant
        position: 3 element tuple containing x,y,z values passed into constructor
        momentum: 3 element tuple initialized with 0.0. Modified by impulse method
            and used to alter position tuple using move method
    Methods:
        impulse: adds args to current momentum
        move: adds (current momentum * arg'dt'/self.mass) to current position
    '''

    def __init__(self, x, y, z):
        self.mass = 1
        self.position = (x, y, z)
        self.momentum = (0.0, 0.0, 0.0)

    def impulse(self, px, py, pz):
        '''Impulse method: Takes args and modifies momentum tuple by arg values
        Args: 
            px,py,pz (double): value by which to increase (or decrease if negative) momentum
        Returns: 
            Nothing: But changes value of momentum'''
        new_momentum = (self.momentum[0] + px * self.mass,
                        self.momentum[1] + py * self.mass,
                        self.momentum[2] + pz * self.mass)
        self.momentum = new_momentum

    def move(self, dt):
        '''Move method: Modifies position tuple by values of momentum tuple times arg dt
        Args:
            dt: values of momentum are multiplied by this value before being added to position tuple
        Returns:
            Nothing: But changes value of position'''
        new_position = (self.position[0] + self.momentum[0] * dt / self.mass,
                        self.position[1] + self.momentum[1] * dt / self.mass,
                        self.position[2] + self.momentum[2] * dt / self.mass)
        self.impulse(0, 0, dt * -9.8)
        self.position = new_position


class ChargedParticle(Particle):
    '''ChargedParticle class: The ChargedParticle class inherits all functions and properties of Particle class
    and adds an additional property "charge" equal to the constant for charge in the scipy library
    Args:
        x,y,z (double): Passed into attribute position (1x3 tuple)
    Attributes:
        mass: Arbitrary constant
        position: 3 element tuple containing x,y,z values passed into constructor
        momentum: 3 element tuple initialized with 0.0. Modified by impulse method
            and used to alter position tuple using move method
        charge: constant set to charge value in scipy.constants
    Methods:
        impulse: adds args to current momentum
        move: adds (current momentum * arg'dt'/self.mass) to current position
    '''

    def __init__(self, x, y, z):
        import scipy
        super(ChargedParticle, self).__init__(x, y, z)
        self.charge = scipy.constants.e


class Proton(ChargedParticle):
    '''Proton class: The Proton class inherits all functions and properties of the ChargedParticle class and changes the 
    value of the "mass" property to the constant for proton mass from the scipy library
    Args:
        x,y,z (double): Passed into attribute position (1x3 tuple)
    Attributes:
        mass: Constant equal to proton mass
        position: 3 element tuple containing x,y,z values passed into constructor
        momentum: 3 element tuple initialized with 0.0. Modified by impulse method
            and used to alter position tuple using move method
        charge: constant set to charge value in scipy.constants
    Methods:
        impulse: adds args to current momentum
        move: adds (current momentum * arg'dt'/self.mass) to current position
    '''

    def __init__(self, x, y, z):
        import scipy
        super(Proton, self).__init__(x, y, z)
        self.mass = scipy.constants.m_p


class Electron(ChargedParticle):
    '''Electron class: The Electron class inherits all functions and properties of the ChargedParticle class and changes the 
    value of the "mass" property to the constant for electron mass from the scipy library
    Args:
        x,y,z (double): Passed into attribute position (1x3 tuple)
    Attributes:
        mass: Constant equal to Electron mass
        position: 3 element tuple containing x,y,z values passed into constructor
        momentum: 3 element tuple initialized with 0.0. Modified by impulse method
            and used to alter position tuple using move method
        charge: constant set to charge value in scipy.constants
    Methods:
        impulse: adds args to current momentum
        move: adds (current momentum * arg'dt'/self.mass) to current position
    '''

    def __init__(self, x, y, z):
        import scipy
        super(Electron, self).__init__(x, y, z)
        self.mass = scipy.constants.m_e
