#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymongo


def database():
    conn = pymongo.Connection("localhost", 27017)
    mydb = conn.stickyNote

    myusr = mydb.stickyNote
    # a = myusr.find()
    # # print(a)
    # for mya in a:
    #     print(mya)


# def write():