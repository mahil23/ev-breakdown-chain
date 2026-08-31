from flask import *
from src.dbconnectionnew import *

from flask import Blueprint

api_app = Blueprint('api_app', __name__)

@api_app.route('/login',methods=['post'])
def login():
    print(request.form)
    username=request.form['username']
    password=request.form['password']
    qry="select*from `login` where username=%s and `password`=%s"
    val=(username,password)
    s=selectone(qry,val)

    if s is None:
        return jsonify({'task':'invalid'})
    else:
        id=s['id']
        type=s['type']
        print(type,"ooooooooooooo")
        return jsonify({'task':'valid',"type":s['type'],"lid" : id })



@api_app.route('/m_view_Assigned_work', methods=['post'])
def m_view_Assigned_work():

    lid=request.form['lid']
    print (lid)
    qry="SELECT `assign`.*,`user`.`fname`,`lname`,lid,mobilunitrequest.`latitude`,mobilunitrequest.`longitude` FROM `user` JOIN `mobilunitrequest` ON `user`.`lid`=`mobilunitrequest`.`uid` JOIN`assign` ON `assign`.`request_id`=`mobilunitrequest`.`id` WHERE `assign`.`m_unit_id`=%s AND `assign`.`status`='Assigned'"
    res=selectall2(qry,lid)
    print (res)
    return jsonify(res)

@api_app.route('/REGISTER',methods=['get','post'])
def REGISTER():
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
    return jsonify({'task': 'valid'})

@api_app.route('/REGISTER',methods=['get','post'])
def register_mobile_unit():
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
    return jsonify({'task': 'valid'})


@api_app.route('/send_feedback_mech',methods=['post'])
def send_feedback_mech():
    lid=request.form['lid']
    mid=request.form['mid']
    feedback=request.form['feedback']
    qry="INSERT INTO `feedback` VALUES (NULL,%s,%s,%s,CURDATE())"
    val=(mid,lid,feedback)
    iud(qry,val)
    return jsonify({'task': 'valid'})


@api_app.route('/view_mech', methods=['post'])
def view_mech():
    qry="SELECT * FROM mechanic JOIN `login` ON `login`.`id`=`mechanic`.`lid` WHERE`login`.`type`='mechanic' "
    res=selectall(qry)
    return jsonify(res)





@api_app.route('/send_feedback_ev',methods=['post'])
def send_feedback_ev():
    lid=request.form['lid']
    ev=request.form['ev']
    feedback=request.form['feedback']
    qry="INSERT INTO `feedback` VALUES (NULL,%s,%s,%s,CURDATE())"
    val=(ev,lid,feedback)
    iud(qry,val)
    return jsonify({'task': 'valid'})

@api_app.route('/view_charging_station', methods=['post'])
def view_charging_station():
    qry="select * from charging_station "
    res=selectall(qry)
    return jsonify(res)


@api_app.route('/view_slot', methods=['post'])
def view_slot():
    sid=request.form['sid']

    qry="SELECT * FROM `slot` WHERE `station_id`=%s"
    res=selectall2(qry,sid)
    return jsonify(res)

@api_app.route('/booking',methods=['post'])
def booking():
    lid=request.form['lid']
    slot_id=request.form['slot_id']
    b_time=request.form['b_time']
    b_date=request.form['b_date']
    qry1="SELECT * FROM `booking` WHERE `slotid`=%s AND`booking_time`=%s AND`booking_date`=%s"
    val1 = ( slot_id, b_time, b_date)

    res=selectone(qry1,val1)
    if res is None:
        qry="INSERT INTO `booking` VALUES(NULL,%s,%s,%s,%s,'pending')"
        val=(lid,slot_id,b_time,b_date)
        iud(qry,val)

        return jsonify({'task': 'valid'})
    else:
        return jsonify({'task': 'Not Available Now'})



@api_app.route('/request_for_mobile_unit',methods=['post'])
def request_for_mobile_unit():
    lid=request.form['lid']
    m_u_id=request.form['m_u_id']
    lati=request.form['lati']
    longi=request.form['longi']
    qry="    INSERT INTO `mobilunitrequest` VALUES(NULL,%s,%s,CURDATE(),'pending',%s,%s)"

    val=(lid,m_u_id,lati,longi)
    iud(qry,val)
    return jsonify({'task': 'valid'})

@api_app.route('/request_for_mech',methods=['post'])
def request_for_mech():
    lid=request.form['lid']
    mid=request.form['mid']
    req=request.form['request']

    lati=request.form['lati']
    longi=request.form['longi']

    qry="INSERT INTO `request mechanic` VALUES(NULL,%s,%s,%s,CURDATE(),'pending',%s,%s)"
    val=(lid,mid,req,lati,longi)
    iud(qry,val)
    return jsonify({'task':'valid'})

@api_app.route('/view_requested_mobile_unit', methods=['post'])
def view_requested_mobile_unit():
    sid=request.form['sid']

    qry="SELECT * FROM `slot` WHERE `station_id`=%s"
    res=selectall2(qry,sid)
    return jsonify(res)

@api_app.route('/nearest_mechanic',methods=['post'])
def nearest_mechanic():
    # qry="SELECT * FROM `worker`"
    latitude = request.form['lati']
    longitude = request.form['longi']
    print(latitude,"66666666666666666666666666")
    print(longitude,"66666666666666666666666666")

    # qry="SELECT`user`.*,`location`.*,`worker`.* FROM `worker` JOIN `location` ON `worker`.`lid`=`location`.`lid` JOIN `user` ON `user`.`lid`=`location`.`lid`,(3959 * ACOS (COS (RADIANS('"+ latitude+"'))*COS(RADIANS(`latitude`)) * COS (RADIANS(`longitude`)-RADIANS('"+longitude+"'))+SIN(RADIANS('"+latitude+"'))*SIN (RADIANS(latitude))))AS `user` FROM `worker` HAVING `user``user`<31.068"
    # qry="    SELECT `location`.*,`mechanic`.*, (3959 * ACOS ( COS ( RADIANS(11.973456789) ) * COS( RADIANS( latitude) ) * COS( RADIANS( longitude ) - RADIANS(75.23456786543) ) + SIN ( RADIANS(11.973456789) ) * SIN( RADIANS( latitude ) ))) AS user_distance FROM `location` JOIN `mechanic` ON `mechanic`.`lid`=`location`.`lid` HAVING user_distance  < 31.068"
    qry=" SELECT `mechanic`.*, (3959 * ACOS ( COS ( RADIANS(11.973456789) ) * COS( RADIANS( m_latitude) ) * COS( RADIANS( m_longitude ) - RADIANS(75.23456786543) ) + SIN ( RADIANS(11.973456789) ) * SIN( RADIANS( m_latitude ) ))) AS user_distance FROM  `mechanic`    JOIN `login` ON `login`.`id`=`mechanic`.`lid` WHERE `login`.`type`='mechanic'ORDER BY user_distance "
    # qry="SELECT `mechanic`.*, (3959 * ACOS ( COS ( RADIANS(11.973456789) ) * COS( RADIANS( m_latitude) ) * COS( RADIANS( m_longitude ) - RADIANS(75.23456786543) ) + SIN ( RADIANS(11.973456789) ) * SIN( RADIANS( m_latitude ) ))) AS user_distance FROM  `mechanic`  ORDER BY user_distance"
    s=selectall(qry)
    print (s,'***************')
    return jsonify(s)


@api_app.route('/updatelocation',methods=['post'])
def updatelocation():
    print(request.form)
    lid = request.form['lid']
    lati = request.form['lat']
    longi = request.form['long']
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
    return jsonify(status='send')


@api_app.route('/view_mech_req_status', methods=['post'])
def view_mech_req_status():
    lid = request.form['lid']

    qry="SELECT `request mechanic`.*,`mechanic`.`fname`,`lname` FROM `request mechanic` JOIN `mechanic` ON `mechanic`.`lid`=`request mechanic`.`mid` WHERE `uid`=%s "
    res=selectall2(qry,lid)
    print(res)
    return jsonify(res)


@api_app.route('/nearest_charging_station',methods=['post'])
def nearest_charging_station():
    # qry="SELECT * FROM `worker`"
    latitude = request.form['lati']
    longitude = request.form['longi']

    print(latitude,"166666666666666666666666666")
    print(longitude,"166666666666666666666666666")

    # qry="SELECT`user`.*,`location`.*,`worker`.* FROM `worker` JOIN `location` ON `worker`.`lid`=`location`.`lid` JOIN `user` ON `user`.`lid`=`location`.`lid`,(3959 * ACOS (COS (RADIANS('"+ latitude+"'))*COS(RADIANS(`latitude`)) * COS (RADIANS(`longitude`)-RADIANS('"+longitude+"'))+SIN(RADIANS('"+latitude+"'))*SIN (RADIANS(latitude))))AS `user` FROM `worker` HAVING `user``user`<31.068"
    # qry="      SELECT `location`.*,`charging_station`.*, (3959 * ACOS ( COS ( RADIANS(11.973456789) ) * COS( RADIANS( latitude) ) * COS( RADIANS( longitude ) - RADIANS(75.23456786543) ) + SIN ( RADIANS(11.973456789) ) * SIN( RADIANS( latitude ) ))) AS user_distance FROM `location` JOIN `charging_station` ON `charging_station`.`lid`=`location`.`lid` HAVING user_distance  < 31.068"
    qry="SELECT `charging_station`.*, (3959 * ACOS ( COS ( RADIANS(11.973456789) ) * COS( RADIANS( latitude) ) * COS( RADIANS( longitude ) - RADIANS(75.23456786543) ) + SIN ( RADIANS(11.973456789) ) * SIN( RADIANS( latitude ) ))) AS user_distance FROM  `charging_station`  ORDER BY user_distance"
    s=selectall(qry)
    print (s,'++++++++++++++++++')
    return jsonify(s)

@api_app.route('/view_mobile_unit', methods=['post'])
def view_mobile_unit():
    sid=request.form['sid']

    qry="SELECT * FROM mobile_unit WHERE `station_id`=%s"
    res=selectall2(qry,sid)
    print(res)
    return jsonify(res)


@api_app.route('/view_booking_details', methods=['post'])
def view_booking_details():
    lid=request.form['lid']
    print (lid)
    qry="SELECT `slot`.*,`charging_station`.`name`,`booking`.* FROM `charging_station` JOIN `slot` ON `charging_station`.`lid`=`slot`.`station_id` JOIN `booking` ON `slot`.`slot_id`=`booking`.`slotid` WHERE `booking`.`uid`=%s"

    res=selectall2(qry,lid)
    print(res)
    return jsonify(res)

@api_app.route('/view_request_for_mobile_unit_status', methods=['post'])
def view_request_for_mobile_unit_status():
    lid=request.form['lid']
    print (lid)
    qry="   SELECT `mobile_unit`.*,`charging_station`.`name`,`mobilunitrequest`.*,`location`.* FROM `mobile_unit` JOIN `charging_station` ON `charging_station`.`lid`=`mobile_unit`.`station_id` JOIN `mobilunitrequest` ON `mobilunitrequest`.`m_unitid`=`mobile_unit`.`lid` JOIN `location`ON `location`.`lid`=`mobile_unit`.`lid` WHERE `mobilunitrequest`.`uid`=%s"

    res=selectall2(qry,lid)
    print(res)
    return jsonify(res)


@api_app.route('/update_status',methods=['post'])
def update_status():
    aid=request.form['aid']
    status=request.form['status']
    print(aid)
    print(status)
    qry="UPDATE `assign` SET `status`=%s WHERE `id`=%s"
    val=(status,aid)
    iud(qry,val)
    qry1="UPDATE `mobilunitrequest` SET `status`=%s WHERE `id`=%s "
    val = (status, aid)
    iud(qry1, val)
    return jsonify({'task':'valid'})






