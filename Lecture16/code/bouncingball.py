#!/usr/bin/env python3
import pygame
class BouncingBall:
    acceleration = (0,100)
    minX = 0
    minY = 0
    maxX = 1000
    maxY = 1000;
    def __init__(self, radius, position, velocity):
        self.radius = radius
        self.position = position
        self.velocity = velocity
    def draw(self, screen, colour):
        pygame.draw.circle(screen, colour, self.position, self.radius)
    def setBounds(self, minX, minY, maxX, maxY):
        self.minX = minX + self.radius
        self.maxX = maxX - self.radius
        self.minY = minY + self.radius
        self.maxY = maxY - self.radius
    def update(self, deltaT):
        oldPosition = self.position
        oldVelocity = self.velocity
        newPosition = (oldPosition[0] + deltaT*oldVelocity[0], oldPosition[1] + deltaT*oldVelocity[1])
        newVelocity = (oldVelocity[0] + deltaT*self.acceleration[0], oldVelocity[1] + deltaT*self.acceleration[1])
        self.position = newPosition
        self.velocity = newVelocity
        if newPosition[1] < self.minY or newPosition[1] > self.maxY:
            self.position = oldPosition
            self.velocity = (newVelocity[0], -newVelocity[1]*0.8)
        if self.position[0] < self.minX or self.position[0] > self.maxX:
            self.position = oldPosition
            self.velocity = (-newVelocity[0]*0.8, newVelocity[1])
