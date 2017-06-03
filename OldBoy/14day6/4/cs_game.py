#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = "Sigai"


class Role(object):

    def __init__(self, name, role, weapon, life_value=100, money=15000):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money
        print(self.name,"生成了")

    def shot(self):
        print("shooting...")

    def got_shot(self):
        print("%s:ah...,I got shot..." % self.name)

    def buy_gun(self, gun_name):
        print("just bought %s" % gun_name)


r1 = Role('Alex', 'police', 'AK47')  # 实例化类生成一个对象，并保存到一个变量里。
r2 = Role('Jack', 'terrorist', 'B22')  # 生成一个角色
Role.shot(r2)
# r1.buy_gun("b43")
# r1.got_shot()
# r2.got_shot()