from email.headerregistry import Group
from nonebot import on_notice,NoticeSession
import random
from nonebot import IntentCommand, on_command,CommandSession
#on_command将函数声明为命令处理器
import datetime,time
from nonebot import on_natural_language,NLPSession
from .ingroup import isin

@on_command('早',only_to_me=False)
async def morning(session:CommandSession):#监听相关字段
    if isin(session.event.group_id,'morning')==0 :
        return     
    if session.event.user_id ==3147892066 :
        return 
    answer=await getit(session.event.group_id,session.event.user_id)
    await session.send(answer)
async def getit(group_id,user_id):
#    return f'哈哈'
    i =datetime.datetime.now()
    minute=f'{i.minute}' if i.minute>=10 else f'0{i.minute}'
    second=f'{i.second}' if i.second>=10 else f'0{i.second}'
    greetings=['早安','早喵','早上好','早上花']
#    if 1:
    if i.hour>=4 and i.hour <14 :
        data=open('C:\\all_for_qqbot\\awesome-bot\\awesome\\plugins\\data\\morning.txt','r+')
        tot=1
        for line in data :
            list=[int(i) for i in line.split()]
            if user_id==list[2] and list[0]==i.day and list[1]==group_id:
                second=f'{list[6]}' if list[6]>=10 else f'0{list[6]}'
                return f'{greetings[random.randint(0,3)]}，你是群里第{list[3]}个起床的人，起床时间是{list[4]}:{list[5]}:{second}'
            if list[0]==i.day and list[1]==group_id:
                tot=tot+1 
        s=f'{i.day} {group_id} {user_id} {tot} {i.hour} {i.minute} {i.second}\n'
        data.write(s)
        return f'{greetings[random.randint(0,3)]}，现在是{i.hour}:{minute}:{second}，你是群里第{tot}个起床的哦'
    else :
        return f'早喵早喵～(慵懒)'

@on_natural_language(keywords={'早上好'},only_to_me=False)
async def _(session:NLPSession):
    return IntentCommand(90,'早')
@on_natural_language(keywords={'早啊'},only_to_me=False)
async def _(session:NLPSession):
    return IntentCommand(90,'早')
@on_natural_language(keywords={'早上花'},only_to_me=False)
async def _(session:NLPSession):
    return IntentCommand(90,'早')
@on_natural_language(keywords={'早安'},only_to_me=False)
async def _(session:NLPSession):
    return IntentCommand(90,'早')