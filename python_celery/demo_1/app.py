#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : weihuchao
import datetime

if __name__ == '__main__':
    from task import add

    print "start", datetime.datetime.now()
    result = add.delay(2, 3)
    print result
    # print result.ready()        # True
    # print result.get()          # 5
    print "end", datetime.datetime.now()
