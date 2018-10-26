#coding=utf-8

"""主要用来测试：对接口API进行改造，同时兼容老接口。通过新接口、老接口对同一环境的请求，对比请求结果，验证接口层"""


def onlevel_message(current_dict="..."):
    mes = "{"+current_dict+"}"
    return mes
# x,y 分别是要对比的两个dict
# meslist是要输出的对比结果中不一致的项，目前输出没有体现层级，查看不直观，待优化
def diff_dict(x, y, meslist=[],current_dict="..."):
    mes = ""
    onlevel_mes = ""
    if(type(x)==dict and type(y)==dict):
        ykeys = set(y.keys())
        xkeys = set(x.keys())

        if current_dict!="...":
            onlevel_mes = onlevel_message(current_dict)
        if list(xkeys.difference(ykeys)) !=[]:
            mes = "The x's keys not in y's keys，that: %s,%s not in y's" % (onlevel_mes,list(xkeys.difference(ykeys)))
            meslist.append(mes)
        if list(ykeys.difference(xkeys)) != []:
            mes = "The y's keys not in x's keys，that: %s,%s not in x's" % (onlevel_mes,list(ykeys.difference(xkeys)))
            meslist.append(mes)
        keys = xkeys & ykeys
        for k in keys:
            xvalue = x[k]
            yvalue = y[k]
            if type(xvalue) == type(yvalue) == list:
                l = len(xvalue)
                if (len(xvalue) > len(yvalue)):
                    l = len(yvalue)
                    mes = "The key's items count difference ,x's bigger than y's,that:%s,key is %s,%s not in y's" \
                          % (onlevel_mes,k,xvalue[(l-1):])
                    meslist.append(mes)
                elif (len(xvalue) < len(yvalue)):
                    l = len(xvalue)
                    mes = "The key's items count difference, y's bigger than x's,that:%s, key is %s,%s not in x's" \
                          % (onlevel_mes,k,yvalue[(l-1):-1])
                    meslist.append(mes)
                for i in range(l):
                    if(type(xvalue[i]) != dict and type(xvalue[i]) != list):
                        if xvalue[i] == yvalue[i]:
                            pass
                        else:
                            mes = "One of list element value is difference, that:%s,list[%d], x's value:%s,y's value:%s " \
                                  % (onlevel_mes,i,xvalue,yvalue[i])
                            meslist.append(mes)
                    else:
                        diff_dict(xvalue[i],yvalue[i],meslist)
            elif((type(xvalue) != dict and type(yvalue) != list) and (type(yvalue) !=dict and type(yvalue) != list)):
                if xvalue == yvalue:
                    pass
                else:
                    mes = "The key's value is differentce,that:%s, key is '%s',x's value:%s, y's value:%s "\
                          % (onlevel_mes,k,xvalue,yvalue)
                    meslist.append(mes)
            elif(type(xvalue)==dict and type(yvalue)==dict):
                current_dict = "'%s':{...}" % k
                diff_dict(xvalue,yvalue,meslist,current_dict)
    else:
        raise "The x or y type is not dict!"
    return meslist

def display_meslist(meslist):
    print "The diff result is:\r\n"
    for i in range(len(meslist)):
        print "(%s. %s\r\n" % (i+1,meslist[i])

