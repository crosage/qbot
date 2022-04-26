def seq(group_id):
    file=open("C:\\all_for_qqbot\\awesome-bot\\awesome\\plugins\\data\\groupid.txt","r")
    lines=[]
    for line in file :
        list=line.split()
        if (list[1] not in lines )and (int(list[0])==group_id):
            lines.append(list[1])
    return lines