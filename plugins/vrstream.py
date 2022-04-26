# -*-coding:utf8-*-

import nonebot
from aiocqhttp.exceptions import Error as CQHttpError
from datetime import datetime,date,timedelta
import random
import requests
import json,collections,xml
from lxml import etree
import time

#TODO：Config file, data file.

VR_uid_list=[692437895,3673023]
VR_group_list=[
    [],[367479904]]
VR_name_list=['桃井最中','测试用户']

#我也知道这个配置方式有点蠢，有时间重写一个吧_(:з」∠)_

@nonebot.scheduler.scheduled_job('interval',minutes=1)
async def _():
    bot = nonebot.get_bot()
    for i in range(min(len(VR_uid_list),len(VR_group_list))):
        room_id = get_live_room_id(VR_uid_list[i])
        live_status = GetLiveStatus(room_id)
        if live_status != '':
            for groupnum in VR_group_list[i]:
                await bot.send_group_msg(group_id=groupnum, message=VR_name_list[i] +' 开播啦！！！ ' + live_status)

def get_live_room_id(mid):
    res = requests.get('https://api.bilibili.com/x/space/acc/info?mid='+str(mid)+'&jsonp=jsonp')
    res.encoding = 'utf-8'
    res = res.text
    data = json.loads(res)
    data = data['data']
    roomid = 0
    try:
        roomid = data['live_room']['roomid']
    except:
        pass
    return roomid

def GetLiveStatus(uid):
    res = requests.get('https://api.live.bilibili.com/room/v1/Room/get_info?device=phone&;platform=ios&scale=3&build=10000&room_id=' + str(uid))
    res.encoding = 'utf-8'
    res = res.text
    try:
        with open(str(uid)+'Live','r') as f:
            last_live_str = f.read()
            f.close()
    except Exception as err:
            last_live_str = '0'
            pass
    try:
        live_data = json.loads(res)
        live_data = live_data['data']
        now_live_status = str(live_data['live_status'])
        live_title = live_data['title']
    except:
        now_live_status = '0'
        pass
    f = open(str(uid)+'Live','w')
    f.write(now_live_status)
    f.close()
    if last_live_str != '1':
        if now_live_status == '1':
            return live_title
    return ''

def main():
    print('test')
    room_id = get_live_room_id(423728837)
    print(GetLiveStatus(room_id))

if __name__ == "__main__":
    main()