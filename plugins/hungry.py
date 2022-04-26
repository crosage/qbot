from nonebot import IntentCommand, on_command,CommandSession
@on_command('饿饿',only_to_me=False)
async def hunger(session:CommandSession):
    answer= await getit()
    await session.send(answer)
async def getit():
    msg='炖猫'
    message=[
        {
            'type':'text',
            'data':{
                'text':msg
            }
        }
    ]
    return (message)