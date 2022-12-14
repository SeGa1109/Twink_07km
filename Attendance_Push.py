from Env import *

def AttendancePushLay():
    datalist=[[ms.Text("Emp. Code",justification= 'center',size=(10,1),relief= 'raised',font=fstylehd),
               ms.Text("Name",justification= 'center',relief= 'raised',size=(32,1),font=fstylehd),
               ms.Text("F/S Name",justification= 'center',relief= 'raised',size=(32,1),font=fstylehd),
               ms.Text("Shift_AT",justification= 'center',relief= 'raised',size=(20,1),font=fstylehd),
               ms.Text("OT Hr",justification= 'center',relief= 'raised',size=(6,1),font=fstylehd),
               ms.Text("Expense",justification= 'center',relief= 'raised', size=(8, 1), font=fstylehd),
               ms.Text("Department", justification='center', relief='raised', size=(14, 1), font=fstylehd),
              ]]
    datalistnp = [[ms.Text("Emp. Code",justification= 'center',size=(10,1),relief= 'raised',font=fstylehd),
               ms.Text("Name",justification= 'center',relief= 'raised',size=(32,1),font=fstylehd),
               ms.Text("F/S Name",justification= 'center',relief= 'raised',size=(32,1),font=fstylehd),
               ms.Text("Shift_AT",justification= 'center',relief= 'raised',size=(20,1),font=fstylehd),
               ms.Text("OT Hr",justification= 'center',relief= 'raised',size=(6,1),font=fstylehd),
               ms.Text("Expense",justification= 'center',relief= 'raised', size=(8, 1), font=fstylehd),
               ms.Text("Department", justification='center', relief='raised', size=(14, 1), font=fstylehd),
              ]]

    mycursor.execute('select UID,emp_code,employee_name,f_sp_name from register where active_status = "Y" and '
                     'ET = "PF" and shift_work = "Yes"')
    globals()['emplistpy']=[list(x) for x in mycursor.fetchall()]

    for i in range (len(emplistpy)):
        sub1=ms.Column([[
              ms.Input(emplistpy[i][1],font=fstyle,key='atpecsy'+str(i),size=(10,1),disabled=True,justification='center',
                       disabled_readonly_background_color=ms.theme_background_color(),border_width= 0),ms.Sizer(5,0),
              ms.Text(emplistpy[i][2],font=fstyle,size=(35,1),key='atpnsy'+str(i),justification='center'),ms.Sizer(2,0),
              ms.Text(emplistpy[i][3], font=fstyle, size=(35, 1) ,key='atpfssy'+str(i),justification='center'),ms.Sizer(20,0),
              ms.Radio("1", font=fstyle, key='atp1ssy' + str(i), group_id='atpsdsy' + str(i)),
              ms.Radio("2",font=fstyle,key='atp2ssy'+str(i),group_id='atpsdsy'+str(i)),
              ms.Radio("3",font=fstyle,key='atp3ssy'+str(i),group_id='atpsdsy'+str(i)),
              ms.Radio("A", font=fstyle, key='atpassy' + str(i), group_id='atpsdsy' + str(i)),
              ms.Sizer(25,0),
              ms.Spin(values=[0,1,2,3,4],initial_value=0,font=fstyle,size=(4,1),key='atpotsy'+str(i),),ms.Sizer(7,0),
              ms.Input("0.0",font=fstyle,key='atpxpsy'+str(i),size=(8,1)),ms.Sizer(7,0),
              ms.Combo(values=dep_list,font=fstyle,key='atpdpsy'+str(i),size=(14,1))
        ],[ms.HSeparator()] ],visible= True,key='atpsy'+str(i))
        datalist.append([sub1])

    mycursor.execute('select UID,emp_code,employee_name,f_sp_name from register where active_status = "Y" and ET = "PF" and shift_work = "No"')
    globals()['emplistpn']=[list(x) for x in mycursor.fetchall()]

    for i in range (len(emplistpn)):
        sub1=ms.Column([
             [ms.Input(emplistpn[i][1],font=fstyle,key='atpecsn'+str(i),size=(10,1),disabled=True,justification='center',
                       disabled_readonly_background_color=ms.theme_background_color(),border_width= 0),ms.Sizer(5,0),
              ms.Text(emplistpn[i][2],font=fstyle,size=(35,1),key='atpnsn'+str(i),justification='center'),ms.Sizer(2,0),
              ms.Text(emplistpn[i][3], font=fstyle, size=(35, 1) ,key='atpfssn'+str(i),justification='center'),ms.Sizer(20,0),
              ms.Radio("P", font=fstyle, key='atp1ssn' + str(i), group_id='atpsdsn' + str(i)),
              ms.Radio("A",font=fstyle,key='atp2ssn'+str(i),group_id='atpsdsn'+str(i)),
                         ms.Sizer(122,0),
              ms.Spin(values=[0,1,2,3,4],initial_value=0,font=fstyle,size=(4,1),key='atpotsn'+str(i),),ms.Sizer(7,0),
              ms.Input("0.0",font=fstyle,key='atpxpsn'+str(i),size=(8,1)),
              ms.Sizer(7, 0),
              ms.Combo(values=dep_list, font=fstyle, key='atpdpsn' + str(i), size=(14, 1))
              ],[ms.HSeparator()] ],visible= True,key='atpsn'+str(i))
        datalist.append([sub1])

#---------------------------------------------------------------------

    mycursor.execute(
        'select UID,emp_code,employee_name,f_sp_name from register where active_status = "Y" and ET = "NON PF" and shift_work = "Yes"')
    globals()['emplistny'] = [list(x) for x in mycursor.fetchall()]

    for i in range(len(emplistny)):
        sub1 = ms.Column([[
                           ms.Input(emplistny[i][1], font=fstyle, key='atpecnsy' + str(i), size=(10, 1), disabled=True,
                                    justification='center',
                                    disabled_readonly_background_color=ms.theme_background_color(), border_width=0),
                           ms.Sizer(5, 0),
                           ms.Text(emplistny[i][2], font=fstyle, size=(35, 1), key='atpnnsy' + str(i),
                                   justification='center'), ms.Sizer(2, 0),
                           ms.Text(emplistny[i][3], font=fstyle, size=(35, 1), key='atpfsnsy' + str(i),
                                   justification='center'), ms.Sizer(15, 0),
                           ms.Radio("1", font=fstyle, key='atp1snsy' + str(i), group_id='atpsdnsy' + str(i)),
                           ms.Radio("2", font=fstyle, key='atp2snsy' + str(i), group_id='atpsdnsy' + str(i)),
                           ms.Radio("3", font=fstyle, key='atp3snsy' + str(i), group_id='atpsdnsy' + str(i)),
                           ms.Radio("A", font=fstyle, key='atpasnsy' + str(i), group_id='atpsdsy' + str(i)),
                           ms.Sizer(25, 0),
                           ms.Spin(values=[0, 1, 2, 3, 4], initial_value=0, font=fstyle, size=(4, 1),
                                   key='atpotnsy' + str(i), ), ms.Sizer(7, 0),
                           ms.Input("0.0", font=fstyle, key='atpxpnsy' + str(i), size=(8, 1)),
                          ms.Combo(values=dep_list, font=fstyle, key='atpdpnsy' + str(i), size=(14, 1))
                           ], [ms.HSeparator()]], visible=True, key='atpnsy' + str(i))
        datalistnp.append([sub1])

    mycursor.execute(
        'select UID,emp_code,employee_name,f_sp_name from register where active_status = "Y" and ET = "NON PF" and shift_work = "No"')
    globals()['emplistnn'] = [list(x) for x in mycursor.fetchall()]

    for i in range(len(emplistnn)):
        sub1 = ms.Column([[ms.Input(emplistnn[i][1], font=fstyle, key='atpecnsn' + str(i), size=(10, 1), disabled=True,
                                    justification='center',
                                    disabled_readonly_background_color=ms.theme_background_color(), border_width=0),
                           ms.Sizer(5, 0),
                           ms.Text(emplistnn[i][2], font=fstyle, size=(35, 1), key='atpnnsn' + str(i),
                                   justification='center'), ms.Sizer(2, 0),
                           ms.Text(emplistnn[i][3], font=fstyle, size=(35, 1), key='atpfsnsn' + str(i),
                                   justification='center'), ms.Sizer(20, 0),
                           ms.Radio("P", font=fstyle, key='atp1snsn' + str(i), group_id='atpsdnsn' + str(i)),
                           ms.Radio("A", font=fstyle, key='atp2snsn' + str(i), group_id='atpsdnsn' + str(i)),
                           ms.Sizer(122, 0),
                           ms.Spin(values=[0, 1, 2, 3, 4], initial_value=0, font=fstyle, size=(4, 1),
                                   key='atpotnsn' + str(i), ), ms.Sizer(7, 0),
                           ms.Input("0.0", font=fstyle, key='atpxpnsn' + str(i), size=(8, 1)),
                           ms.Sizer(7, 0),
                           ms.Combo(values=dep_list, font=fstyle, key='atpdpnsn' + str(i), size=(14, 1))
                           ], [ms.HSeparator()]], visible=True, key='atpnsn' + str(i))
        datalistnp.append([sub1])

#----------------------

    layout=[
        [ms.Text("Attendance Register",font=fstylehd)],
        [ms.Text("Entry Person",font=fstyle,size=(12,1)),ms.Combo(values=user_name(),font=fstyle,size=(20,1),key='atpers'),ms.Sizer(swi-650,0),
         ms.Text("Date",font=fstyle,size=(5,1)),ms.InputText("",size=(15,1),font=fstyle,key="atpdate"),
         ms.CalendarButton(todatenf,target='atpdate',image_data=chse, format="%d-%m-%Y",location=(1250,100))],
        [ms.Frame("Entry",layout= [[ms.Column(datalist,scrollable=True,vertical_scroll_only= True,visible=True,size=(swi-70,shi-220),key='atppf'),
                                   ms.Column(datalistnp,scrollable=True,visible=False,vertical_scroll_only=True,size=(swi-70,shi-220),key='atpnpf')],
                                   [ms.Checkbox("Non Pf",key='atpswap',enable_events= True,font=fstyle)]],
                  font=fstyle,size=(swi-50,shi-150))],
         [ms.Input(default_text= "",size=(15,1),font=fstyle,password_char="*",key='atppw',tooltip="Please enter the Password to proceed .!")],
        [ms.Button("Update",font=fstyle,key='atpupdate',tooltip="Please enter the Password to proceed .!")
         ]]
    return layout

'''
TestMenu = ms.Window("Attendance Push",layout,location=(0,0),size=(swi,shi),element_justification='center')
while True:
    event,values=TestMenu.read()
    if event == ms.WIN_CLOSED:
        TestMenu.close()
        break
'''

def AttendancePushFn(Menu,event,values):
    if event == 'atpswap':
        if Menu['atpswap'].get() == False:
            Menu['atppf'].update(visible=True)
            Menu['atpnpf'].update(visible=False)
        else:
            Menu['atppf'].update(visible=False)
            Menu['atpnpf'].update(visible=True)

    if event == 'atpupdate':
       #print(values['atpers'])
       #print("ckecking", user_pass(values['atpers'])[0][0])
       if values['atppw']==user_pass(values['atpers'])[0][0]:
           pushdate = list(values['atpdate'].split("-"))
           DB_Creation(values['atpdate'])
           mycursor.execute("select `%s` from %s_%s where empcode = 'counter'" % (pushdate[0], pushdate[1], pushdate[2]))
           counter = mycursor.fetchall()[0][0]
           mycursor.execute("INSERT INTO `twink_06ma`.`attendance_log`(`gen_date`,`person`,`pushdate`,`status`) values ('%s','%s','%s','%s')" \
               % (todate.strftime("%Y/%m/%d %H:%M:%S"), values["atpers"][0], datetime.strptime(values['atpdate'], "%d-%m-%Y").strftime("%Y-%m-%d"), "C"))
           mydb.commit()
           mycursor.execute("select Description,UID from dep_list")
           db_data=mycursor.fetchall()
           dplist={x[0]: (x[1]) for x in db_data}
           if counter != None:
               chk1 = ms.popup_get_text(
                   "Attendance Already Created in the specified Date\n---\nPlease click yes to Update with a Master password",
                   font=fstyle, no_titlebar=True)
               if chk1 == MasterPass:
                   mydb.rollback()
                   sql="INSERT INTO `twink_06ma`.`attendance_log`(`gen_date`,`person`,`pushdate`,`status`) values ('%s','%s','%s','%s')" \
                       % (todate.strftime("%Y/%m/%d %H:%M:%S"), values["atpers"],
                          datetime.strptime(values['atpdate'], "%d-%m-%Y").strftime("%Y-%m-%d"), "U")
                   #print(sql)
                   mycursor.execute(sql)
                   mydb.commit()

                   atndata = []
                   for i in range(len(emplistpy)):
                       data = []
                       data.append(values['atpecsy' + str(i)])
                       if values['atp1ssy' + str(i)] == True:
                           indata = '1'
                       elif values['atp2ssy' + str(i)] == True:
                           indata = '2'
                       elif values['atp3ssy' + str(i)] == True:
                           indata = '3'
                       elif values['atpassy' + str(i)] == True:
                           indata = 'A'
                       else:
                           continue
                       indata += ","
                       indata += str(values['atpotsy' + str(i)])
                       indata += ","
                       indata += str(values['atpxpsy' + str(i)])
                       indata += ","
                       indata += str(dplist.get(values['atpdpsy' + str(i)]))
                       data.append(indata)
                       atndata.append(data)
                   for i in range(len(emplistpn)):
                       data = []
                       data.append(values['atpecsn' + str(i)])
                       if values['atp1ssn' + str(i)] == True:
                           indata = 'P'
                       elif values['atp2ssn' + str(i)] == True:
                           indata = 'A'
                       else:
                           continue
                       indata += ","
                       indata += str(values['atpotsn' + str(i)])
                       indata += ","
                       indata += str(values['atpxpsn' + str(i)])
                       indata += ","
                       indata += str(dplist.get(values['atpdpsn' + str(i)]))
                       data.append(indata)
                       atndata.append(data)
                   for i in range(len(emplistny)):
                       data = []
                       data.append(values['atpecnsy' + str(i)])
                       if values['atp1snsy' + str(i)] == True:
                           indata = '1'
                       elif values['atp2snsy' + str(i)] == True:
                           indata = '2'
                       elif values['atp3snsy' + str(i)] == True:
                           indata = '3'
                       elif values['atpasnsy' + str(i)] == True:
                           indata = 'A'
                       else:
                           continue
                       indata += ","
                       indata += str(values['atpotnsy' + str(i)])
                       indata += ","
                       indata += str(values['atpxpnsy' + str(i)])
                       indata += ","
                       indata += str(dplist.get(values['atpdpnsy' + str(i)]))
                       data.append(indata)
                       atndata.append(data)
                   for i in range(len(emplistnn)):
                       data = []
                       data.append(values['atpecnsn' + str(i)])
                       if values['atp1snsn' + str(i)] == True:
                           indata = 'P'
                       elif values['atp2snsn' + str(i)] == True:
                           indata = 'A'
                       else:
                           continue
                       indata += ","
                       indata += str(values['atpotnsn' + str(i)])
                       indata += ","
                       indata += str(values['atpxpnsn' + str(i)])
                       indata += ","
                       indata += str(dplist.get(values['atpdpnsn' + str(i)]))
                       data.append(indata)
                       atndata.append(data)
                   #print(pushdate, atndata)
                   for x in range(len(atndata)):
                       sql = "update %s_%s set `%s` = '%s' where empcode = '%s'" % \
                             (pushdate[1], pushdate[2], pushdate[0], atndata[x][1], atndata[x][0])
                       #print(sql)
                       mycursor.execute(sql)

                   sql = "update %s_%s set `%s` = 'v' where empcode = 'counter'" % \
                         (pushdate[1], pushdate[2], pushdate[0],)
                   mycursor.execute(sql)
                   mydb.commit()

               else:
                   ms.popup_auto_close("Wrong Password", auto_close_duration=1)
                   return
           else:
               atndata = []
               for i in range(len(emplistpy)):
                   data = []
                   data.append(values['atpecsy' + str(i)])
                   if values['atp1ssy' + str(i)] == True:
                       indata = '1'
                   elif values['atp2ssy' + str(i)] == True:
                       indata = '2'
                   elif values['atp3ssy' + str(i)] == True:
                       indata = '3'
                   elif values['atpassy' + str(i)] == True:
                       indata = 'A'
                   else:
                       indata = 'e'
                   indata += ","
                   indata += str(values['atpotsy' + str(i)])
                   indata += ","
                   indata += str(values['atpxpsy' + str(i)])
                   indata += ","
                   indata += str(dplist.get(values['atpdpsy'+ str(i)]))
                   data.append(indata)
                   atndata.append(data)
               for i in range(len(emplistpn)):
                   data = []
                   data.append(values['atpecsn' + str(i)])
                   if values['atp1ssn' + str(i)] == True:
                       indata = 'P'
                   elif values['atp2ssn' + str(i)] == True:
                       indata = 'A'
                   else:
                       indata = 'e'
                   indata += ","
                   indata += str(values['atpotsn' + str(i)])
                   indata += ","
                   indata += str(values['atpxpsn' + str(i)])
                   indata += ","
                   indata += str(dplist.get(values['atpdpsn'+ str(i)]))
                   data.append(indata)
                   atndata.append(data)
               for i in range(len(emplistny)):
                   data = []
                   data.append(values['atpecnsy' + str(i)])
                   if values['atp1snsy' + str(i)] == True:
                       indata = '1'
                   elif values['atp2snsy' + str(i)] == True:
                       indata = '2'
                   elif values['atp3snsy' + str(i)] == True:
                       indata = '3'
                   elif values['atpasnsy' + str(i)] == True:
                       indata = 'A'
                   else:
                       indata = 'e'
                   indata += ","
                   indata += str(values['atpotnsy' + str(i)])
                   indata += ","
                   indata += str(values['atpxpnsy' + str(i)])
                   indata += ","
                   indata += str(dplist.get(values['atpdpnsy'+ str(i)]))
                   data.append(indata)
                   atndata.append(data)
               for i in range(len(emplistnn)):
                   data = []
                   data.append(values['atpecnsn' + str(i)])
                   if values['atp1snsn' + str(i)] == True:
                       indata = 'P'
                   elif values['atp2snsn' + str(i)] == True:
                       indata = 'A'
                   else:
                       indata = 'e'
                   indata += ","
                   indata += str(values['atpotnsn' + str(i)])
                   indata += ","
                   indata += str(values['atpxpnsn' + str(i)])
                   indata += ","
                   indata += str(dplist.get(values['atpdpnsn'+ str(i)]))
                   data.append(indata)
                   atndata.append(data)
               #print(pushdate, atndata)
               for x in range(len(atndata)):
                   sql = "update %s_%s set `%s` = '%s' where empcode = '%s'" % \
                         (pushdate[1], pushdate[2], pushdate[0], atndata[x][1], atndata[x][0])
                   #print(sql)
                   mycursor.execute(sql)

               sql = "update %s_%s set `%s` = 'v' where empcode = 'counter'" % \
                     (pushdate[1], pushdate[2], pushdate[0],)
               mycursor.execute(sql)
               mydb.commit()
       else:
           ms.popup_auto_close("Wrong Password", auto_close_duration=1)

#v6.0