def isin(group_id,thing):

    data=open('C:\\all_for_qqbot\\awesome-bot\\awesome\\plugins\\data\\groupid.txt','r+')
    for line in data :
        list=[i for i in line.split()]
        if group_id == int(list[0]) and ((thing in list) or('all' in list)):
            return 1
    return 0