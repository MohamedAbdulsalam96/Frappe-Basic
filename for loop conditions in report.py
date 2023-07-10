from __future__ import unicode_literals
import frappe
from frappe import msgprint, _

def execute(filters=None):
    if not filters:
        filters = {}

    area_list = get_area(filters)
    unit_list = get_unit(filters)

    columns = get_columns()

    data = []

    for area in area_list:
        rowea = ["", area.area, "", "", "", "", "", "", ""]
        data.append(rowea)
        rpt_list_area = get_unit(area.area)
        if not rpt_list_area:
            continue
        for unit in rpt_list_area:
            rowin = ["", unit.unit, "", "", "", "", "", "", ""]
            data.append(rowin)
            rpt_list_unit = get_rpt(area.area, unit.unit)
            if not rpt_list_unit:
                continue
            for rpt in rpt_list_unit:
                rowrp = [
                    rpt.machine_serial_no, rpt.customer_name, rpt.mach_model,
                    rpt.machine_si_no, rpt.embroidery_area, rpt.contact_person,
                    rpt.date_of_installation, rpt.unit, rpt.area
                ]
                data.append(rowrp)


    if not data:
        msgprint(_("No records found"))
        return columns, data

    return columns, data


def get_columns():
    columns = [
        {"label": _("MC.No"), "fieldname": "machine_serial_no", "fieldtype": "Data", "width": 100},
        {"label": _("Customer Name"), "fieldname": "customer_name", "fieldtype": "Data", "width": 180},
        {"label": _("M.Model.No"), "fieldname": "mach_model", "fieldtype": "Data", "width": 100},
        {"label": _("M.SI.No"), "fieldname": "machine_si_no", "fieldtype": "Data", "width": 100},
        {"label": _("Embroidery Area"), "fieldname": "embroidery_area", "fieldtype": "Data", "width": 150},
        {"label": _("Contact Person"), "fieldname": "contact_person", "fieldtype": "Data", "width": 150},
        {"label": _("Date of Installation"), "fieldname": "date_of_installation", "fieldtype": "Data", "width": 150},
        {"label": _("Unit"), "fieldname": "unit", "fieldtype": "Data", "width": 100},
        {"label": _("Area"), "fieldname": "area", "fieldtype": "Data", "width": 100}
    ]
    return columns


def get_conditions(filters):
    conditions = ""
    if filters.get("area"):
        conditions += "AND area = %(area)s "
    if filters.get("unit"):
        conditions += "AND unit = %(unit)s "
    # if filters.get("from_date"):
    #     conditions += "AND a.date >= %(from_date)s "
    # if filters.get("to_date"):
    #     conditions += "AND a.date <= %(to_date)s "
    return conditions


def get_area(filters):
    conditions = get_conditions(filters)
    return frappe.db.sql(
        """SELECT area FROM `tabMachines` WHERE unit <> '' AND area <> '' {0} GROUP BY area ORDER BY area, unit """.format(
            conditions
        ),
        filters,
        as_dict=1,
    )


def get_unit(area):
    area_condition = ""

    if area:
        area_condition = "AND area = %(area)s "

    sql_query = """
        SELECT unit
        FROM `tabMachines`
        WHERE unit <> '' AND area <> '' {0}
        GROUP BY unit
        ORDER BY area, unit
    """.format(area_condition)

    return frappe.db.sql(sql_query, {"area": area}, as_dict=1)



def get_rpt(area, unit):
    # conditions = get_conditions(filters)
    area_condition = ""
    unit_condition = ""

    if area:
        area_condition = "AND area = %(area)s "
    if unit:
        unit_condition = "AND unit = %(unit)s "

    sql_query = """
        SELECT
            machine_serial_no, customer_name, mach_model, machine_si_no,
            embroidery_area, contact_person, date_of_installation,
            unit, area
        FROM
            `tabMachines`
        WHERE
            unit <> '' AND area <> '' {0} {1}
        ORDER BY
            area, unit
    """.format(
        area_condition, unit_condition
    )

    return frappe.db.sql(sql_query, {"area": area, "unit": unit}, as_dict=1)
