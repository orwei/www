# -*- coding: utf-8 -*-
# @Time : 2017-05-07  0:16
# @Author : Hu Wei

import orm, asyncio, sys
from models import User, Blog, Comment


async def demo(loop):
    await orm.create_pool(loop=loop, user='www-data', password='www-data', db='awesome')

    u = User(name='test20qeqweqweq', email='test20@testqweq.qeqecom', passwd='teqest', image='about:blqeqank')

    await u.save()


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([demo(loop)]))
    loop.close()
    if loop.is_closed():
        sys.exit(0)
