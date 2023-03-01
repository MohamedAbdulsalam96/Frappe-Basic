# Copyright (c) 2013, Regent Info Solution and contributors
# For license information, please see license.txt



from __future__ import unicode_literals
from dateutil.parser._parser import ParserError
import re, datetime, math, time
from dateutil import parser
import frappe
from datetime import timedelta
# from datetime import datetime
from frappe import msgprint, _

TIME_FORMAT = "%H:%M"

def execute(filters=None):
    if not filters: filters = {}


    emp_list = get_emp_dtls(filters)


    columns = get_columns()

    if not emp_list:
        msgprint(_("No record found"))
        return columns, emp_list

    data = []



    for emp in emp_list:

        conditions = ""

        row = [emp.name,emp.first_name,emp.designation,emp.department,emp.category]

        # if filters.get("employee"):
        filters.update({"employee": emp.name})
        conditions += "and employee = %(employee)s"

        if filters.get("from_date"):
            conditions += "and time >= %(from_date)s"
        if filters.get("from_date"):
            conditions += " and time <(DATE_ADD(%(from_date)s, INTERVAL 1 DAY))"



        att_dtls = frappe.db.sql("""select  etime as result from Employee_loginQ\
            where 0=0 %s group by etime,location order by etime""" % conditions, filters, as_dict=1)
        i=0
        a=''
        b=''
        c=''
        t=''
        e=''
        f=''
        g=''
        h=''
        w=''
        x=''
        y=''
        z=''
        for d in att_dtls:
            i+=1
            if i==1:
                a=d.result
                # msgprint(_(a))
            if i==2:
                b=d.result
                # msgprint(_(b))
            if i==3:
                c=d.result
                # msgprint(_(c))
            if i==4:
                t=d.result
                # msgprint(_(t))
            if i==5:
                e=d.result
                # msgprint(_(e))
            if i==6:
                f=d.result
                # msgprint(_(f))
            if i==7:
                g=d.result
                # msgprint(_(g))
            if i==8:
                h=d.result
                # msgprint(_(h))
            if i==9:
                w=d.result
                # msgprint(_(w))
            if i==10:
                x=d.result
                # msgprint(_(x))
            if i==11:
                y=d.result
                # msgprint(_(y))
            if i==12:
                z=d.result
                # msgprint(_(z))
            
            value=d.result

            row.append(value)
        if c:
            ac = c.split(':')[0]
            cd = c.split(':')[1]
            acd = (int(ac)*60) +int(cd)
            ab = b.split(':')[0]
            bd = b.split(':')[1]
            abd = (int(ab)*60) +int(bd)
            abcd = (acd-abd)
            # msgprint(_(str(round(abcd, 2))))
            # msgprint(_(str(int(str(abcd).split('.')[1])/60)))
        else:
            abcd = 0
        # msgprint(_(str(acd)))
        # msgprint(_(str(abd)))
        # msgprint(_(str(round(abcd, 2))))
        # -----
        if e:
            be = e.split(':')[0]
            ed = e.split(':')[1]
            bed = (int(be)*60) +int(ed)
            bt = t.split(':')[0]
            td = t.split(':')[1]
            btd = (int(bt)*60) +int(td)
            betd = (bed-btd)
        else:
            betd = 0
        # msgprint(_(str(bed)))
        # msgprint(_(str(btd)))
        # msgprint(_(str(round(betd, 2))))
        # -------
        if g:
            cg = g.split(':')[0]
            gd = g.split(':')[1]
            cgd = (int(cg)*60) +int(gd)
            cf = f.split(':')[0]
            fd = f.split(':')[1]
            cfd = (int(cf)*60) +int(fd)
            cgfd = (cgd-cfd)
        else:
            cgfd = 0
        # msgprint(_(str(cgd)))
        # msgprint(_(str(cfd)))
        # msgprint(_(str(round(cgfd, 2))))
        # -------
        if w:
            aw = w.split(':')[0]
            wd = w.split(':')[1]
            awd = (int(aw)*60) +int(wd)
            ah = h.split(':')[0]
            hd = h.split(':')[1]
            ahd = (int(ah)*60) +int(hd)
            awhd = (awd-ahd)
        else:
            awhd = 0
        # msgprint(_(str(awd)))
        # msgprint(_(str(ahd)))
        # msgprint(_(str(round(awhd, 2))))
        # ------
        if y:
            ay = y.split(':')[0]
            yd = y.split(':')[1]
            ayd = (int(ay)*60) +int(yd)
            ax = x.split(':')[0]
            xd = x.split(':')[1]
            axd = (int(ax)*60) +int(xd)
            ayxd = (ayd-axd)
        else:
            ayxd = 0
        # msgprint(_(str(ayd)))
        # msgprint(_(str(axd)))
        # msgprint(_(str(round(ayxd, 2))))
        total_break = str(round(betd, 2) + round(abcd, 2)+ round(cgfd, 2)+ round(awhd, 2)+ round(ayxd, 2))
        total_break_time = str(datetime.timedelta(minutes = int(total_break)))
        
        # msgprint(_(total_break))
        
        # msgprint(_(datetime.datetime.strptime(c, '%H:%M')))
        # msgprint(_(c-b))
        if i<12:
            j=0
            for j in range(12-i):
                row.append("0")

        log_dtls = frappe.db.sql("""select  cast(min(time) as time) as login,cast(max(time) as time) as logout,TIMEDIFF(max(time), min(time) ) as total_hr from `tabEmployee Checkin`\
            where docstatus=0 %s order by time""" % conditions, filters, as_dict=1)

        for d in log_dtls:
            # frappe.msgprint(_('{},{},{}'.format(d.login,d.logout,d.total_hr)))
            row.append(d.login)
            row.append(d.logout)
            row.append(d.total_hr)
            row.append(total_break_time)
            if d.total_hr:
                jjj = str(d.total_hr)
                z = jjj.split(':')[0]
                zz = jjj.split(':')[1]
                zzz = jjj.split(':')[2]
                zzzz = (int(z)*60) +int(zz)
                net_work_time =  str(round(zzzz, 2))
                # msgprint(_(total_break))
                # msgprint(_(net_work_time))
                net_work_time1 = str((datetime.timedelta(minutes = (int(net_work_time)-int(total_break)))) )
                row.append(net_work_time1)
            else:
                row.append('')
            # msgprint(_(d.total_hr))
            # net_work_time = str(datetime.timedelta(minutes = int(total_break)))
            # row.append(net_work_time)
            
            # if d.total_hr:
                # xyz = (str(d.total_hr)).split(':')
                # delta = timedelta(hours=int(xyz[0]), minutes=int(xyz[1]), seconds=int(xyz[2]))
                # total_seconds = delta.total_seconds()
                # xyz=str(datetime.timedelta(minutes = int(d.total_hr)))
                # work_hour = str(int(total_seconds) - int(total_break))
            # else:
                # work_hour = str(0)
            # row.append(work_hour)
        data.append(row)
    return columns, data


def get_columns():
    columns = [
        _("Emp Code") + ":Data:100",
        _("Emp Name") + ":Data:120",
        _("Designation") + ":Data:120",
        _("Department") + ":Data:120",
        _("Category") + ":Data:120",
        _("In1") + ":Data:60",
        _("Out1") + ":Data:60",
        _("In2") + ":Data:60",
        _("Out2") + ":Data:60",
        _("In3") + ":Data:60",
        _("Out3") + ":Data:60",
        _("In4") + ":Data:60",
        _("Out4") + ":Data:60",
        _("In5") + ":Data:60",
        _("Out5") + ":Data:60",
        _("In6") + ":Data:60",
        _("Out6") + ":Data:60",
        # _("Test Brk") + ":Data:60",        
        _("Login") + ":Data:100",
        _("Logout") + ":Data:100",
        _("Total Hours") + ":Data:100",
        _("Total Break") + ":Data:100",
        # _("Net Work") + ":Data:100",
        _("Net Working Hour") + ":Data:150",

    ]


    return columns


def get_conditions(filters):
    conditions = ""

    if filters.get("employee"):
        conditions += "and employee = %(employee)s"
    # if filters.get("from_date"):
        # conditions += "and date >= %(from_date)s"
    # if filters.get("to_date"):
        # conditions += " and date <= %(to_date)s"

    return conditions

def get_init_conditions(filters):
    conditions = ""

    if filters.get("employee"):
        conditions += "and name = %(employee)s"
    if filters.get("grade"):
        conditions += "and shift_timing_emp = %(grade)s"
    if filters.get("dept"):
        conditions += "and department = %(dept)s"
    if filters.get("desig"):
        conditions += "and designation = %(desig)s"
    # if filters.get("category"):
        # conditions += "and category = %(category)s"


    return conditions


def get_emp_dtls(filters):

    conditions = get_init_conditions(filters)

    entries = frappe.db.sql("""
        SELECT
             name, first_name,designation, department, category
        FROM
            `tabEmployee` tm
        where  name = '52722' and docstatus<2 %s order by department,name desc""" %
        conditions, filters, as_dict=1)
    return entries
# shift_timing_emp ='MOBILE USERS'status='Active' and
