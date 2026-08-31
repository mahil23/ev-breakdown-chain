from flask import *
from src.dbconnectionnew import *

from flask import Blueprint

web_app = Blueprint('web_app', __name__)

import functools

import requests
import re

from datetime import datetime

def login_required(func):
    @functools.wraps(func)
    def secure_function():
        if "lid" not in session:
            return render_template('index.html')
        return func()

    return secure_function


@web_app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@web_app.route('/')
def home():
    return render_template("/Home.html")

@web_app.route('/login')
def login():
    return render_template("/index.html")

@web_app.route('/logincode',methods=['get','post'])
def logincode():
    username=request.form['textfield']
    password=request.form['textfield2']
    qry="select*from login where username=%s and password=%s"
    val=(username,password)
    res=selectone(qry,val)
    if res is None:
        return''' <script>alert("invalid");window.location='/' </script>'''
    elif res['type']=='admin':
        session['lid'] = res['id']
        return '''<script>alert("valid");window.location='/ADMIN_HOME'</script>'''
    elif res['type'] == 'mechanic':
        session['lid'] = res['id']
        return '''<script>alert("valid");window.location='/MECHANIC_HOME'</script>'''
    elif res['type'] == 'station':
         session['lid'] = res['id']
         return '''<script>alert("valid");window.location='/ev_station_HOME'</script>'''
    elif res['type'] == 'user':
         session['lid'] = res['id']
         return '''<script>alert("valid");window.location='/userhome'</script>'''
    elif res['type'] == 'm_unit':
         session['lid'] = res['id']
         return '''<script>alert("valid");window.location='/m_unit_home'</script>'''
    else:
         return '''<script>alert("invalid");window.location='/'</script>'''


# @web_app.route('/add_petrol_pump')
# def add_petrol_pump():
#     return render_template("/ADMIN/addpetrolpump.html")
#
# @web_app.route('/add_petrol_pump1',methods=['get','post'])
# def add_petrol_pump1():
#     name=request.form['textfield']
#     place=request.form['textfield2']
#     phone=request.form['textfield3']
#     email=request.form['textfield4']
#     latitude=request.form['textfield5']
#     longtitude=request.form['textfield6']
#
#     import random
#     pswd = random.randint(0000,9999)
#
#     qry1="INSERT INTO `login` VALUES(NULL,%s,%s,%s)"
#     res =iud(qry1,(email,pswd,'pump'))
#
#     qry="INSERT INTO `petrol pump` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s)"
#     iud(qry,(res,name,place,phone,email,latitude,longtitude))
#     return ''' <script>alert("Inserted");window.location='/' </script>'''


@web_app.route('/ADMIN_HOME')
@login_required
def ADMIN_HOME():
    return render_template("/ADMIN/ADMIN HOME.html")





@web_app.route('/add_and_manage_station')

def add_and_manage_station():
    return render_template("ev_reg_index.html")


@web_app.route('/add_and_manage_station1',methods=['post'])

def add_and_manage_station1():
    name = request.form['textfield']
    place=request.form['textfield2']
    phone=request.form['textfield3']
    email=request.form['textfield4']
    latitude=request.form['textfield5']
    longtitude=request.form['textfield6']
    username=request.form['textfield7']
    password=request.form['textfield8']
    qry1 = "INSERT INTO `login` VALUES(NULL,%s,%s,'pending')"
    val=(username,password)
    id=iud(qry1,val)
    qry="INSERT INTO `charging_station` VALUES (NULL,%s,%s,%s,%s,%s,%s,%s)"
    val1=(str(id),name,place,phone,email,latitude,longtitude)
    iud(qry,val1)
    return ''' <script>alert("Registed");window.location='/manage_ev' </script>'''

@web_app.route('/edit_station')
@login_required

def edit_station():
    id=request.args.get('id')
    session['ES_id']=id
    qry="select * from charging_station where  `lid`=%s"
    res=selectone(qry,id)
    return render_template("/ADMIN/edit_station.html",val=res)


@web_app.route('/edit_station1',methods=['post'])
def edit_station1():
    name = request.form['textfield']
    place=request.form['textfield2']
    phone=request.form['textfield3']
    email=request.form['textfield4']
    latitude=request.form['textfield5']
    longtitude=request.form['textfield6']

    qry="UPDATE `charging_station` SET `name`=%s,`place`=%s,`phone`=%s,`email`=%s,`latitude`=%s,`longitude`=%s WHERE `lid`=%s"
    val1=(name,place,phone,email,latitude,longtitude,session['ES_id'])
    iud(qry,val1)
    return ''' <script>alert("edited");window.location='/manage_ev' </script>'''
@web_app.route('/delete_station')
@login_required

def delete_station():
    id=request.args.get('id')
    qry="delete from charging_station WHERE `lid`=%s"
    iud(qry,id)
    qry = "delete from login WHERE `id`=%s"
    iud(qry, id)
    return ''' <script>alert("deleted");window.location='/manage_ev' </script>'''



@web_app.route('/manage_ev')
@login_required

def manage_ev():
    qry=" SELECT * FROM `charging_station`"
    res=selectall(qry)
    return render_template("/ADMIN/manage_ev.html",val=res)



@web_app.route('/verify_mechanic')
@login_required

def verify_mechanic():
    qry="SELECT `login`.*,mechanic.*FROM login JOIN mechanic ON mechanic.lid=login.id"
    res=selectall(qry)
    return render_template("/ADMIN/verify mechanic.html",val=res)


@web_app.route('/Accept_mechanic')
@login_required

def Accept_mechanic():
    id=request.args.get('id')
    qry="update login set type='mechanic' WHERE `id`=%s"
    iud(qry,id)
    return ''' <script>alert("Accepted");window.location='/verify_mechanic' </script>'''



@web_app.route('/reject_mechanic')
@login_required

def reject_mechanic():
    id=request.args.get('id')
    qry="update login set type='reject' WHERE `id`=%s"
    iud(qry,id)
    return ''' <script>alert("Rejected");window.location='/verify_mechanic' </script>'''

@web_app.route('/verify_ev')
@login_required

def verify_ev():
    qry="   SELECT `login`.*,charging_station.*FROM login JOIN `charging_station`  ON `charging_station`.lid=login.id"
    res=selectall(qry)
    return render_template("/ADMIN/verify ev.html",val=res)



@web_app.route('/Accept_ev')
@login_required

def Accept_ev():
    id=request.args.get('id')
    qry="update login set type='station' WHERE `id`=%s"
    iud(qry,id)
    return ''' <script>alert("Accepted");window.location='/verify_ev' </script>'''



@web_app.route('/reject_ev')
@login_required

def reject_ev():
    id=request.args.get('id')
    qry="update login set type='reject' WHERE `id`=%s"
    iud(qry,id)
    return ''' <script>alert("Rejected");window.location='/verify_ev' </script>'''



@web_app.route('/VIEW__FEEDBACK')
@login_required

def VIEW__FEEDBACK():
    return render_template("/ADMIN/VIEW FEEDBACK.html")




@web_app.route('/VIEW__FEEDBACK1',methods=['post'])
@login_required

def VIEW__FEEDBACK1():
    type=request.form['select']
    if type== 'mech' :
        qry="SELECT `user`.`fname`,`user`.`lname` ,`feedback`.*,`mechanic`.`fname`AS fn  FROM `user` JOIN `feedback` ON `feedback`.`uid`=`user`.`lid` JOIN `mechanic` ON `mechanic`.`lid`=`feedback`.`lid`"
        res=selectall(qry)
        return render_template("/ADMIN/VIEW FEEDBACK.html",val=res)

    else:

        qry="SELECT `user`.`fname`,`user`.`lname` ,`feedback`.*,`charging_station`.`name` AS fn  FROM `user` JOIN `feedback` ON `feedback`.`uid`=`user`.`lid` JOIN `charging_station` ON `charging_station`.`lid`=`feedback`.`lid`"
        res=selectall(qry)
        return render_template("/ADMIN/VIEW FEEDBACK.html",val=res)



@web_app.route('/REGISTER')

def REGISTER():
    return render_template("/mech_reg_index.html")


@web_app.route('/REGISTER1',methods=['get','post'])
def REGISTER1():
    FIRSTNAME=request.form['textfield']
    LASTNAME=request.form['textfield2']
    EMAIL=request.form['textfield3']
    PHONE=request.form['textfield4']
    LATITUDE=request.form['textfield5']
    LONGITUDE=request.form['textfield6']
    username = request.form['textfield7']
    password = request.form['textfield8']
    qry1 = "INSERT INTO `login` VALUES(NULL,%s,%s,'pending')"
    val = (username, password)
    id = iud(qry1, val)
    qry = "INSERT INTO `mechanic` VALUES (NULL,%s,%s,%s,%s,%s,%s,%s)"
    val1 = (str(id), FIRSTNAME,LASTNAME,PHONE,EMAIL,LATITUDE,LONGITUDE)
    iud(qry, val1)
    return ''' <script>alert("Registered");window.location='/' </script>'''

@web_app.route('/MECHANIC_HOME')
@login_required

def MECHANIC_HOME():
    return render_template("/MECHANIC/MECHANIC HOME.html")




@web_app.route('/STATUS')
@login_required

def STATUS():
    return render_template("/MECHANIC/STATUS.html")

@web_app.route('/view_profile')
def view_profile():
    qry="SELECT * FROM `mechanic` WHERE `lid`=%s "
    res=selectone(qry,session['lid'])
    return render_template("/MECHANIC/view_profile.html",val=res)

@web_app.route('/update_profile',methods=['post','get','put'])
def update_profile():
    fname = request.form['textfield']
    lname = request.form['textfield2']
    email = request.form['textfield3']
    phone = request.form['textfield4']
    qry="UPDATE `mechanic` SET `fname`=%s,`lname`=%s,`phone`=%s,`email`=%s WHERE `lid`=%s"
    val=(fname,lname,phone,email,session['lid'])
    iud(qry, val)
    return ''' <script>alert("Updated");window.location='/view_profile' </script>'''

@web_app.route('/VIEW_FEEDBACK')
@login_required

def VIEW_FEEDBACK():
    qry = "SELECT `user`.*,`feedback`.* FROM `feedback` JOIN `user` ON `user`.`Lid`=`feedback`.`uid` WHERE `feedback`.`lid`=%s"
    res = selectall2(qry, session['lid'])
    return render_template("/MECHANIC/VIEW_FEEDBACK.html",val=res)


# @web_app.route('/VIEW_REQUEST_AND_UPDATE')
# def VIEW_REQUEST_AND_UPDATE():
#     return render_template("/MECHANIC/VIEW_REQUEST_AND_UPDATE.html")
@web_app.route('/VIEW_REQUEST_AND_UPDATE')
@login_required

def VIEW_REQUEST_AND_UPDATE():
    qry="   SELECT `request mechanic`.*,`user`.`Fname`,`Lname`,`location`.`latitude`AS lat ,`location`.`longitude` AS longi FROM `request mechanic` JOIN `user` ON `request mechanic`.`uid`=`user`.`lid` JOIN `location` ON `location`.`lid`=`user`.`lid` WHERE `request mechanic`.`mid`=%s AND `request mechanic`.status='pending'"
    # qry="SELECT `request mechanic`.*,`user`.`Fname`,`Lname` FROM `request mechanic` JOIN `user` ON `request mechanic`.`uid`=`user`.`Lid` WHERE `request mechanic`.`mid`=%s and `request mechanic`.status='pending'"
    res=selectall2(qry,session['lid'])
    return render_template("/MECHANIC/VIEW_REQUEST_AND_UPDATE.html",val=res)

@web_app.route('/accept_request')
@login_required

def accept_request():
    id=request.args.get('id')
    qry="UPDATE `request mechanic` SET `status`='Accepted' WHERE `id`=%s"
    iud(qry,id)
    return '''<script>alert("ACCEPTED");window.location='/VIEW_REQUEST_AND_UPDATE'</script>'''


@web_app.route('/reject_request')
@login_required

def reject_request():
    id=request.args.get('id')
    qry="UPDATE `request mechanic` SET `status`='reject' WHERE `id`=%s"
    iud(qry,id)
    return '''<script>alert("REJECTED");window.location='/VIEW_REQUEST_AND_UPDATE'</script>'''

# /////////////////////////////////////////////////////////////////////////EV/////////////////////////////////////

@web_app.route('/VIEW_PRO')
@login_required

def VIEW_PRO():
    qry="SELECT * FROM `charging_station` WHERE `lid`=%s"
    res=selectone(qry,session['lid'])
    print(res)
    return render_template("/ev station/VIEW_PROFILE_EV.html",val=res)

@web_app.route('/update_ev_profile',methods=['post'])
@login_required

def update_ev_profile():
    name = request.form['textfield']
    place = request.form['textfield2']
    phone = request.form['textfield3']
    email = request.form['textfield4']
    latitude = request.form['textfield5']
    longtitude = request.form['textfield6']
    qry="UPDATE `charging_station` SET `name`=%s,`place`=%s,`phone`=%s,`email`=%s,`latitude`=%s,`longitude`=%s WHERE `lid`=%s"


    val1 = ( name, place, phone, email, latitude, longtitude,session['lid'])
    iud(qry, val1)
    return ''' <script>alert("Updated");window.location='/VIEW_PRO' </script>'''



@web_app.route('/manage_mu')
@login_required

def manage_mu():
    qry="SELECT * FROM `mobile_unit` WHERE `station_id`=%s"
    res=selectall2(qry,session['lid'])
    return render_template("/ev station/manage_mu.html",val=res)

@web_app.route('/add_mobile_unit',methods=['post'])
@login_required

def add_mobile_unit():
    return render_template("/ev station/add_mobile_unit.html")

@web_app.route('/add_mobile_unit1',methods=['post'])
@login_required

def add_mobile_unit1():
    dname = request.form['textfield']
    vehicle=request.form['textfield2']
    capacity=request.form['textfield3']

    username=request.form['textfield4']
    password=request.form['textfield5']
    qry1 = "INSERT INTO `login` VALUES(NULL,%s,%s,'m_unit')"
    val=(username,password)
    id=iud(qry1,val)
    qry="INSERT INTO `mobile_unit` VALUES (NULL,%s,%s,%s,%s,%s)"
    val1=(str(id),dname,vehicle,session['lid'],capacity)
    iud(qry,val1)
    return ''' <script>alert("Added");window.location='/manage_mu' </script>'''


@web_app.route('/edit_mobile_unit',methods=['post','get'])
@login_required

def edit_mobile_unit():
    id = request.args.get('id')
    session['Emu_id'] = id
    qry = "select * from mobile_unit where  `lid`=%s"
    res = selectone(qry, id)
    return render_template("/ev station/edit_mobile_unit.html",val=res)

@web_app.route('/edit_mobile_unit1',methods=['post'])
def edit_mobile_unit1():
    dname = request.form['textfield']
    vehicle=request.form['textfield2']
    capacity=request.form['textfield3']


    qry="UPDATE `mobile_unit` SET `driver`=%s,`vehicle_num`=%s,capacity=%s  WHERE `lid`=%s"
    val1=(dname,vehicle,capacity,session['Emu_id'])
    iud(qry,val1)
    return ''' <script>alert("updated");window.location='/manage_mu' </script>'''

@web_app.route('/delete_mu')
@login_required

def delete_mu():
    id=request.args.get('id')
    qry="delete from mobile_unit WHERE `lid`=%s"
    iud(qry,id)
    qry = "delete from login WHERE `id`=%s"
    iud(qry, id)
    return ''' <script>alert("deleted");window.location='/manage_mu' </script>'''

@web_app.route('/manage_slot')
@login_required

def manage_slot():
    qry="SELECT * FROM `slot` WHERE `station_id`=%s"
    res=selectall2(qry,session['lid'])
    return render_template("/ev station/manage_slot.html",val=res)

@web_app.route('/add_slot',methods=['post'])
@login_required

def add_slot():
    return render_template("/ev station/add_slot.html")

@web_app.route('/add_slot1',methods=['post'])
def add_slot1():
    details = request.form['textfield']
    slotno = request.form['textfield2']
    slot_type = request.form['select']

    qry = "INSERT INTO `slot` VALUES(NULL,%s,%s,%s,%s)"
    val1 = (session['lid'],slot_type, slotno,details)

    iud(qry, val1)
    return ''' <script>alert("Added");window.location='/manage_slot' </script>'''

@web_app.route('/edit_slot')
@login_required

def edit_slot():
    id = request.args.get('id')
    session['Esl_id'] = id
    qry = "select * from slot where  `slot_id`=%s"
    res = selectone(qry, id)

    return render_template("/ev station/edit_slot.html",val=res)

@web_app.route('/edit_slot1',methods=['post'])
def edit_slot1():
    time = request.form['select']
    slotno = request.form['textfield2']
    details = request.form['textfield3']

    qry="    UPDATE `slot` SET `type`=%s,`slot_number`=%s ,details=%sWHERE `slot_id`=%s"
    val1 = (time, slotno,details, session['Esl_id'])


    iud(qry, val1)
    return ''' <script>alert("Edited");window.location='/manage_slot' </script>'''


@web_app.route('/delete_slot')
@login_required

def delete_slot():
    id = request.args.get('id')
    qry="delete from slot  WHERE `slot_id`=%s"
    iud(qry, id)
    return ''' <script>alert("Deleted");window.location='/manage_slot' </script>'''


@web_app.route('/assigm_mobunit')
@login_required

def assigm_mobunit():
    qry="SELECT * FROM `mobile_unit` WHERE `station_id`=%s"
    res=selectall2(qry,session['lid'])
    qry1="  SELECT `mobilunitrequest`.`date`,`mobilunitrequest`.`id` ,`user`.`fname`,`lname`FROM `mobilunitrequest` JOIN `mobile_unit`ON `mobile_unit`.`lid`=`mobilunitrequest`.`m_unitid`JOIN  `charging_station` ON `mobile_unit`.`station_id`=`charging_station`.`lid` JOIN `user`ON `user`.`lid`=`mobilunitrequest`.`uid` WHERE `charging_station`.`lid`=%s AND `mobilunitrequest`.`status`!='completed'"
    res1=selectall2(qry1,session['lid'])
    return render_template("/ev station/assigm_mobunit.html",val=res,val1=res1)

@web_app.route('/assigm_mobunit1',methods=['post'])
def assigm_mobunit1():
    unit=request.form['select']
    o_id=request.form['select2']
    qry="INSERT INTO `assign` VALUES(NULL,%s,%s,CURDATE(),'Assigned')"
    val=(unit,o_id)
    iud(qry,val)
    return ''' <script>alert("Assigned");window.location='/assigm_mobunit' </script>'''





@web_app.route('/view_charge_request')
@login_required

def view_charge_request():
    return render_template("/ev station/view_charge_request.html")



@web_app.route('/view_charging_station')
@login_required

def view_charging_station():
    return render_template("/ev station/view_charging_station.html")



@web_app.route('/view_mobile_unit')
@login_required

def view_mobile_unit():
     return render_template("/ev station/view_mobile_unit.html")

@web_app.route('/view_mu_work_status')
@login_required

def view_mu_work_status():
    qry="SELECT * FROM `mobile_unit` JOIN `mobilunitrequest` ON `mobilunitrequest`.`m_unitid`=`mobile_unit`.`lid` WHERE `mobile_unit`.`station_id`=%s"
    res=selectall2(qry,session['lid'])
    return render_template("/ev station/view_mu_work_status.html",val=res)



@web_app.route('/view_mobilestation_request')
@login_required

def view_mobilestation_request():
    return render_template("/ev station/view_mobilestation_request.html")


@web_app.route('/ev_station_HOME')
@login_required

def ev_station_HOME():

    return render_template("/ev station/EV HOME.html")

# @web_app.route('/VIEW_FEEDBACK_ev')
# @login_required

# def VIEW_FEEDBACK_ev():
#     qry = "SELECT `user`.*,`feedback`.* FROM `feedback` JOIN `user` ON `user`.`Lid`=`feedback`.`uid` WHERE `feedback`.`lid`=%s"
#     print(qry)
#     res = selectall2(qry, session['lid'])
#     print (res)

#     return render_template("/ev station/VIEW_FEEDBACK.html",val=res)

@web_app.route('/view_Booking')
@login_required

def view_Booking():
    qry="SELECT `user`.`fname`,`lname` ,`slot`.`slot_number` ,`booking`.* FROM `user` JOIN `booking` ON `user`.`lid`=`booking`.`uid` JOIN `slot` ON `booking`.`slotid`=`slot`.`slot_id` WHERE `slot`.`station_id`=%s"
    res=selectall2(qry,session['lid'])
    return render_template("/ev station/view_Booking.html",val=res)


@web_app.route('/accept_user_request')
@login_required

def accept_user_request():
    id=request.args.get('id')
    qry="UPDATE `booking` SET `status`='Accepted' WHERE `bid`=%s"
    iud(qry,id)
    return '''<script>alert("ACEEPTED");window.location='/view_Booking'</script>'''


@web_app.route('/reject_user_request')
@login_required

def reject_user_request():
    id=request.args.get('id')
    qry="UPDATE `booking` SET `status`='Reject' WHERE `bid`=%s"
    iud(qry,id)
    return '''<script>alert("REJECTED");window.location='/view_Booking'</script>'''


@web_app.route('/userhome')
@login_required

def userHome():

    return render_template("/user/userhome.html")

# Mobile Unit Section

@web_app.route('/view_assigned', methods=['get','post'])
@login_required

def View_Assigned():
    lid=session['lid']
    qry="SELECT `assign`.*,`user`.`fname`,`lname`,lid,mobilunitrequest.`latitude`,mobilunitrequest.`longitude` FROM `user` JOIN `mobilunitrequest` ON `user`.`lid`=`mobilunitrequest`.`uid` JOIN`assign` ON `assign`.`request_id`=`mobilunitrequest`.`id` WHERE `assign`.`m_unit_id`=%s"
    res=selectall2(qry,lid)
    print (res)
    return render_template("/M_UNIT/view_assigned.html", val = res)

@web_app.route('/m_unit_home')
@login_required

def MOBILE_UNIT_HOME():
    return render_template("/M_UNIT/m_unit_home.html")

@web_app.route('/manage_work')
@login_required

def Manage_Work():
    lid=session['lid']
    qry="SELECT `assign`.*,`user`.`fname`,`lname`,lid,mobilunitrequest.`id`,mobilunitrequest.`latitude`,mobilunitrequest.`longitude` FROM `user` JOIN `mobilunitrequest` ON `user`.`lid`=`mobilunitrequest`.`uid` JOIN`assign` ON `assign`.`request_id`=`mobilunitrequest`.`id` WHERE `assign`.`m_unit_id`=%s"
    res=selectall2(qry,lid)
    print (res)
    
    return render_template("/M_UNIT/manage_work.html", val=res)



@web_app.route('/update_status',methods=['post'])
def update_status():
    aid=session['lid']
    status=request.form['status']
    request_id = request.form['request_id']
    print(request_id)
    
    print(status)
    qry="UPDATE `assign` SET `status`=%s WHERE `request_id`=%s"
    val=(status,request_id)
    iud(qry,val)
    qry1="UPDATE `mobilunitrequest` SET `status`=%s WHERE `id`=%s "
    val = (status, request_id)
    iud(qry1, val)
    return '''<script>alert("UPDATED");window.location='/manage_work'</script>'''



@web_app.route('/updatelocation',methods=['post'])
def updatelocation():
    print(request.form)
    lid = session['lid']
    lati = request.form['lat']
    longi = request.form['longi']
    qry="SELECT * FROM `location` WHERE `lid`=%s"
    res=selectone(qry,lid)
    if res is None:
        qry="INSERT INTO `location` VALUES(NULL,%s,%s,%s)"
        val=(lid,lati,longi)
        iud(qry,val)
    else:
        qry="UPDATE `location` SET `latitude`=%s,`longitude`=%s WHERE `lid`=%s"
        val=(lati,longi,lid)
        iud(qry,val)
    return '''<script>alert("UPDATED");window.location='/manage_work'</script>'''

@web_app.route('/view_user_register')

def viewUserRegisterPage():
    return render_template("user_reg_index.html")

@web_app.route('/registeruser',methods=['get','post'])
def RegisterUser():
    FIRSTNAME=request.form['fname']
    LASTNAME=request.form['lname']
    PLACE = request.form['place']
    PIN = request.form['pin']
    POST = request.form['post']
    EMAIL=request.form['email']
    PHONE=request.form['phone']
    username = request.form['uname']
    password = request.form['password']
    qry1 = "INSERT INTO `login` VALUES(NULL,%s,%s,'user')"
    val = (username, password)
    id = iud(qry1, val)
    qry = "INSERT INTO `USER` VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1 = (str(id), FIRSTNAME,LASTNAME,PLACE,PIN,POST,EMAIL,PHONE)
    iud(qry, val1)
    return '''<script>alert("User Registered");window.location='/'</script>'''

@web_app.route('/view_mech', methods=['get'])
def view_mech():
    return render_template('/user/manage_mechanic.html')

def get_lat_long_from_google_maps_link(map_url):
    try:
        # Expand the short URL (Google redirects to a full URL)
        response = requests.get(map_url, allow_redirects=True, verify=False)
        final_url = response.url  # The redirected URL
        print(final_url)

        # Extract latitude and longitude from the URL
        match = re.search(r'@(-?\d+\.\d+),(-?\d+\.\d+)', final_url)
        print(match)
        if match:
            latitude, longitude = match.groups()
            print(float(latitude))
            return float(latitude), float(longitude)
        else:
            return None, None
    except Exception as e:
        print("Error:", e)
        return None, None
    
def is_blocked():
    try:
        maps = requests.get("https://maps.google.com", timeout=5)
        print(f"Maps accessible: {maps.status_code == 200}")
    except:
        print("Maps blocked")

@web_app.route('/nearest_mechanic',methods=['post'])
def nearest_mechanic():
    hello = is_blocked()
    print(hello)
    print("hello")
    latitude = request.form['lati']
    longitude = request.form['longi']
    # maplink = request.form['maplink']
    # print(maplink)
    # if maplink is None:
    #     return "No link"
    # latitude, longitude = get_lat_long_from_google_maps_link(maplink)

    # if latitude is None or longitude is None:
    #     return "Invalid Google Maps link. Please enter a valid link."
    
    print(latitude,"66666666666666666666666666")
    print(longitude,"66666666666666666666666666")
    lid = session['lid']
    qry="SELECT * FROM `location` WHERE `lid`=%s"
    res=selectone(qry,lid)
    if res is None:
        qry="INSERT INTO `location` VALUES(NULL,%s,%s,%s)"
        val=(lid,latitude,longitude)
        iud(qry,val)
    else:
        qry="UPDATE `location` SET `latitude`=%s,`longitude`=%s WHERE `lid`=%s"
        val=(latitude,longitude,lid)
        iud(qry,val)
    qry = "SELECT `mechanic`.*, (3959 * ACOS(COS(RADIANS(%s)) * COS(RADIANS(m_latitude)) * COS(RADIANS(m_longitude) - RADIANS(%s)) + SIN(RADIANS(%s)) * SIN(RADIANS(m_latitude)))) AS user_distance FROM `mechanic`    JOIN `login` ON `login`.`id` = `mechanic`.`lid` WHERE `login`.`type` = 'mechanic' HAVING user_distance < 20 ORDER BY user_distance"
    params = (latitude, longitude, latitude)
    s=selectall2(qry, params)
    print (s,'***************')
    return render_template('/user/manage_mechanic.html', mechanics = s)

@web_app.route('/request_for_mech',methods=['post'])
def request_for_mech():
    lid=session['lid']
    mid=request.form['lid']
    req=request.form['request']
    latitude = request.form['lati']
    longitude = request.form['longi']
    # maplink = request.form['maplink']
    # print(maplink)
    # if maplink is None:
    #     return "No link"
    # latitude, longitude = get_lat_long_from_google_maps_link(maplink)

    # if latitude is None or longitude is None:
    #     return "Invalid Google Maps link. Please enter a valid link."


    qry="""INSERT INTO `request mechanic` (id, uid, mid, request, date, status, latitude, longitude) 
             VALUES (NULL, %s, %s, %s, CURDATE(), 'pending', %s,%s)"""
    val=(lid,mid,req,latitude,longitude)
    iud(qry,val)
    return '''<script>alert("Booked");window.location='/view_mech'</script>'''

@web_app.route('/view_mech_req_status', methods=['get'])
def view_mech_req_status():
    lid = session['lid']
    qry="SELECT `request mechanic`.*,`mechanic`.`fname`,`lname`,`phone` FROM `request mechanic` JOIN `mechanic` ON `mechanic`.`lid`=`request mechanic`.`mid` WHERE `uid`=%s "
    res=selectall2(qry,lid)
    return render_template('/user/mechanic_status.html', val = res)


@web_app.route('/view_evstation', methods=['get'])
def view_evstation():
    return render_template('/user/manage_charging_station.html')

@web_app.route('/nearest_charging_station', methods=['post'])
def nearest_charging_station():
    print("hello")
    latitude = request.form['lati']
    longitude = request.form['longi']
    # maplink = request.form['maplink']
    # print(maplink)
    # if maplink is None:
    #     return "No link"
    # latitude, longitude = get_lat_long_from_google_maps_link(maplink)

    # if latitude is None or longitude is None:
    #     return "Invalid Google Maps link. Please enter a valid link."

    print(latitude, "166666666666666666666666666")
    print(longitude, "166666666666666666666666666")

    # Query to find nearest charging stations using Haversine formula
    qry = """SELECT `charging_station`.*, 
                    (3959 * ACOS( 
                        COS(RADIANS(%s)) * COS(RADIANS(latitude)) * 
                        COS(RADIANS(longitude) - RADIANS(%s)) + 
                        SIN(RADIANS(%s)) * SIN(RADIANS(latitude))
                    )) AS user_distance 
             FROM `charging_station` 
             HAVING user_distance < 20 ORDER BY user_distance"""

    
    params = (latitude, longitude, latitude)
    s = selectall2(qry, params)

    print(s, '++++++++++++++++++')
    return render_template('/user/manage_charging_station.html', val = s)
@web_app.route('/nearest_m_unit', methods=['post','get'])
def nearest_m_unit():
    print("hello")
    latitude = request.form['lati']
    longitude = request.form['longi']
    # maplink = request.form['maplink']
    # print(maplink)
    # if maplink is None:
    #     return "No link"
    # latitude, longitude = get_lat_long_from_google_maps_link(maplink)

    # if latitude is None or longitude is None:
    #     return "Invalid Google Maps link. Please enter a valid link."

    # print(latitude, "166666666666666666666666666")
    # print(longitude, "166666666666666666666666666")

    # Query to find nearest charging stations using Haversine formula
    
    qry = """SELECT `charging_station`.*, 
                (3959 * ACOS( 
                    COS(RADIANS(%s)) * COS(RADIANS(latitude)) * 
                    COS(RADIANS(longitude) - RADIANS(%s)) + 
                    SIN(RADIANS(%s)) * SIN(RADIANS(latitude))
                )) AS user_distance 
            FROM `charging_station` 
            HAVING user_distance < 20 ORDER BY user_distance"""
    
    params = (latitude, longitude, latitude)
    s = selectall2(qry, params)

    print(s, '++++++++++++++++++')
    return render_template('/user/manage_m_unit.html', val = s)

@web_app.route('/view_booking_form', methods=['post','get'])
def view_booking_form():
    station_id = request.form['station_id']
    qry = "SELECT * FROM  `slot` WHERE `station_id`=%s"
    slots = selectall2(qry,station_id)
    return render_template('/user/book_station.html', val = slots)

@web_app.route('/ev_station_status', methods=['get'])
def ev_station_status():
    lid = session['lid']
    qry = """
    SELECT booking.*, charging_station.name 
    FROM booking 
    JOIN charging_station ON booking.station_id = charging_station.lid
    WHERE booking.uid = %s
    """
    bookings = selectall2(qry,lid)
    return render_template('/user/ev_station_status.html', val = bookings)

@web_app.route('/booking', methods=['post'])
def booking():
    lid = session['lid']
    slot_id = request.form['slot_id']
    b_time = request.form['b_time']
    b_date = request.form['b_date']

    # Fetch station_id from the slot table
    qry_station = "SELECT station_id FROM slot WHERE slot_id=%s"
    val_station = (slot_id,)
    station_res = selectone(qry_station, val_station)

    if station_res:
        station_id = station_res['station_id']  # Extract station_id

        # Check if the slot is already booked
        qry1 = "SELECT * FROM `booking` WHERE `slotid`=%s AND `booking_time`=%s AND `booking_date`=%s"
        val1 = (slot_id, b_time, b_date)
        res = selectone(qry1, val1)

        if res is None:
            qry = "INSERT INTO `booking` VALUES(NULL, %s, %s, %s, %s, %s, 'pending')"
            val = (lid, station_id, slot_id, b_time, b_date)
            iud(qry, val)

            return '''<script>alert("Booked");window.location='/ev_station_status'</script>'''
        else:
            return '''<script>alert("Slot not available. Try another");window.location='/view_booking_form'</script>'''
    else:
        return '''<script>alert("Invalid Slot ID");window.location='/view_booking_form'</script>'''
    

@web_app.route('/view_mobileunit', methods=['get'])
def view_mobileunit():
    return render_template('/user/manage_m_unit.html')

@web_app.route('/m_unit_status', methods=['get'])
def m_unit_status():
    lid = session['lid']
    qry = "SELECT * FROM  `mobilunitrequest` WHERE `uid`=%s"
    bookings = selectall2(qry,lid)
    return render_template('/user/m_unit_status.html', val = bookings)

@web_app.route('/m_unit_booking',methods=['post'])
def m_unit_booking():
    uid=session['lid']
    latitude = request.form['lati']
    longitude = request.form['longi']
    # maplink = request.form['maplink']
    # print(maplink)
    # if maplink is None:
    #     return "No link"
    # latitude, longitude = get_lat_long_from_google_maps_link(maplink)

    # if latitude is None or longitude is None:
    #     return "Invalid Google Maps link. Please enter a valid link."

    print(latitude, "166666666666666666666666666")
    print(longitude, "166666666666666666666666666")
    status = "Not assigned"
    m_unitid = None
    date = datetime.now().strftime('%d-%m-%Y')

    qry = "INSERT INTO `mobilunitrequest` VALUES(NULL, %s, %s, %s, %s, %s, %s)"
    val = (uid, m_unitid, date, status, latitude, longitude)  # ✅ Matches the placeholders
    iud(qry, val)

    return '''<script>alert("Booked");window.location='/m_unit_status'</script>'''


@web_app.route('/send_feedback_mech',methods=['post'])
def send_feedback_mech():
    uid=session['lid']
    lid=request.form['mid']
    feedback=request.form['feedback']
    type = 'mechanic'
    qry = "INSERT INTO `feedback` (`id`, `lid`, `uid`, `feedback`, `date`, `type`) VALUES (NULL, %s, %s, %s, CURDATE(), %s)"
    val=(lid,uid,feedback,type)
    iud(qry,val)
    return '''<script>alert("feedback send");window.location='/view_mech_req_status'</script>'''


@web_app.route('/send_feedback_ev',methods=['post'])
def send_feedback_ev():
    uid=session['lid']
    bid=request.form['mid']
    type = 'ev'
    feedback=request.form['feedback']
    qry = "INSERT INTO `feedback` (`id`, `lid`, `uid`, `feedback`, `date`, `type`) VALUES (NULL, %s, %s, %s, CURDATE(), %s)"
    val=(bid,uid,feedback,type)
    iud(qry,val)
    return '''<script>alert("feedback send");window.location='/ev_station_status'</script>'''


@web_app.route('/view_feedback_mech',methods=['get'])
def view_feedback_mech():
    print("hii")
    uid=session['lid']
    print(uid)
    qry="""
    SELECT feedback.*, user.fname 
    FROM feedback 
    JOIN user ON feedback.uid = user.lid 
    WHERE feedback.lid = %s AND feedback.type = 'MECHANIC';
"""
    val=(uid)
    feedbacks = selectall2(qry,val)
    print(feedbacks)
    return render_template('MECHANIC/VIEW_FEEDBACK.html',context=feedbacks)


@web_app.route('/view_feedback_ev', methods=['GET'])
def view_feedback_ev():
    print("hii")
    station_id = session['lid']  # Assuming this is the station ID
    print(station_id)
    print("helooooooooooooo")

    if not station_id:
        return "Station ID not found in session", 400

    qry = """
    SELECT feedback.*, user.fname 
    FROM feedback 
    JOIN user ON feedback.uid = user.lid  -- Fetch user's name using uid
    WHERE feedback.lid = %s AND feedback.type = 'ev';
    """
    val = (station_id,)  # Corrected tuple format

    feedbacks = selectall2(qry, val)
    print(feedbacks)

    return render_template('ev station/VIEW_FEEDBACK.html', context=feedbacks)

@web_app.route('/view_feedback_admin', methods=['GET'])
def view_feedback_admin():
    print("hii")

    qry = """
    SELECT feedback.*, 
           user.fname AS user_name, 
           login.username AS service_provider_name
    FROM feedback 
    JOIN user ON feedback.uid = user.lid 
    JOIN login ON feedback.lid = login.id;
    """

    feedbacks = selectall(qry)
    print(feedbacks)

    return render_template('ADMIN/VIEW FEEDBACK.html', context=feedbacks)
    