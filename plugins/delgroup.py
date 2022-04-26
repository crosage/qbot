from nonebot import IntentCommand, on_command,CommandSession
#on_command将函数声明为命令处理器
import datetime
from .seqcoms import seq
import os 
from nonebot import on_natural_language,NLPSession

@on_command('del',only_to_me=False)
async def night(session:CommandSession):
#    if session.event.user_id!=2051252420 :
#        return 
    thing=session.current_arg_text.split()
    print(thing)
    data=(open('C:\\all_for_qqbot\\awesome-bot\\awesome\\plugins\\data\\groupid.txt','r+'))
    line=''
    for lines in data:
        ok=1
        for coms in thing :
            list=lines.split()
            print(session.event.group_id!=int(list[0]),session.event.group_id,int(list[0]),coms !=list[1],str(list[1]),coms)
            if session.event.group_id==int(list[0]) and coms ==list[1]:
                ok=0
        print(ok)
        if ok==1:
            line=line+lines
    data.close()
    tmp=open('C:\\all_for_qqbot\\awesome-bot\\awesome\\plugins\\data\\groupid_tmp.txt','w')
    tmp.writelines(line)
    tmp.close()
    os.remove('C:\\all_for_qqbot\\awesome-bot\\awesome\\plugins\\data\\groupid.txt')
    os.rename('C:\\all_for_qqbot\\awesome-bot\\awesome\\plugins\\data\\groupid_tmp.txt','C:\\all_for_qqbot\\awesome-bot\\awesome\\plugins\\data\\groupid.txt')
    answer=await getit(session.event.group_id,session.event.user_id,thing);
    await session.send(answer)
async def getit(group_id,user_id,thing) :
    ok=1
    for i in thing :
        if i in seq(group_id) :
            ok=0
    if ok==1 :
        message=[
            {
                'type':'text',
                'data':{
                    "text":'Sussess!'
                }
            }
        ]
    else :
        message=[
            {
                'type':'text',
                'data':{
                    "text":'Fail'
                }
            }
        ]
    return message