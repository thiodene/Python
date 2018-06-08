from flask import jsonify, Blueprint, request
from util.config import logger, db, PAGE_SIZE, SORT_FIELD, SORT_ORDER
from sqlalchemy import text
from util.query_parser import QueryParser
import time
import mysql.connector
from model.user import User
from model.sensor import Sensor
from model.company import Company
from model.equipment import Equipment
from model.setting import Setting
from model.sample import Sample
from util.tasks import store_samples

class MigrateBlueprint(object):
    def __init__(self):
        self.blueprint = Blueprint('migrate',
                                   'migrate',
                                   url_prefix='/migrate' )

        #self.host = 'sims.scentroid.com'
        self.host = '167.114.10.49'
        self.username = 'root'
        #self.password = 'salam9080'
        self.password = 'GAhftYwxCvw93L5e'
        self.database = 'sims'

        @self.blueprint.route('/user', methods=['GET'])
        def migrate_user():
            try:
                cnx = mysql.connector.connect(host=self.host, user=self.username, password=self.password, database=self.database, )
                cursor = cnx.cursor()
                query = "SELECT * FROM user"
                cursor.execute(query)

                for (id, email, tel, username, name, family, image, company, birthdate, gender, location, roles,
                     extra, password, createdat, expireat) in cursor:
                    u = User()
                    u.id = id
                    u.first_name = name
                    u.last_name = family
                    u.password = password
                    u.email = email
                    u.roles = roles
                    u.created_by = 10
                    u.created_on = createdat
                    db.session.add(u)
                    db.session.commit()
                cursor.close()
                cnx.close()
                return "done"
            except Exception as e:
                return str(e),500

        @self.blueprint.route('/company', methods=['GET'])
        def migrate_company():
            try:
                cnx = mysql.connector.connect(host=self.host, user=self.username, password=self.password, database=self.database, )
                cursor = cnx.cursor()
                query = "SELECT * FROM company"
                cursor.execute(query)

                for (id, name, city, timezone, alarm_email, address, tel, logo, manager, extra, creator, createdat ) in cursor:
                    u = Company()
                    u.id = id
                    u.name = name
                    u.city = city
                    u.timezone = timezone
                    u.alarm_email = alarm_email
                    u.address = address
                    u.telephone = tel
                    u.logo = logo
                    if manager in [0,-1]:
                        manager = 10
                    u.manager = manager
                    u.extra = extra
                    u.created_by = 10
                    u.created_on = createdat
                    db.session.add(u)
                    db.session.commit()
                cursor.close()
                cnx.close()
                return "done"
            except Exception as e:
                return str(e),500



        @self.blueprint.route('/equipment', methods=['GET'])
        def migrate_equipment():
            try:
                cnx = mysql.connector.connect(host=self.host, user=self.username, password=self.password, database=self.database, )
                cursor = cnx.cursor()
                query = "SELECT * FROM equipement"
                cursor.execute(query)

                for (id, name, status, sn, secret, extra, company, category, notification, calibrated, createdat, creator) in cursor:
                    u = Equipment()
                    u.id = id
                    u.category = category
                    u.name = name
                    u.notification_on = notification
                    u.status = status
                    u.serial_number = sn
                    u.secret = secret
                    u.extra = extra
                    u.company = company
                    u.calibrated_on = calibrated
                    u.created_by = 10
                    u.created_on = createdat
                    db.session.add(u)
                    db.session.commit()
                cursor.close()
                cnx.close()
                return "done"
            except Exception as e:
                return str(e),500



        @self.blueprint.route('/sensor', methods=['GET'])
        def migrate_sensor():
            try:
                cnx = mysql.connector.connect(host=self.host, user=self.username, password=self.password, database=self.database, )
                cursor = cnx.cursor()
                query = "SELECT * FROM sensor"
                cursor.execute(query)

                for (id, name, packet_id, equipment, type, dataunit, calibrationfactors, alarm_max_value,
                     alarm_value_total, alarm_value_num, extra, creator, createdat ) in cursor:
                    if equipment in [0,22,28]:
                        continue
                    u = Sensor()
                    u.id = id
                    u.name = name
                    u.packet_id = packet_id
                    u.equipment = equipment
                    u.type = type
                    u.unit = dataunit
                    u.calibration_factors = calibrationfactors
                    #alarm_max_value = db.Column(db.Float(), nullable=False)
                    #alarm_value_total = db.Column(db.Integer, nullable=False)
                    #alarm_value_number = db.Column(db.Integer, nullable=False)
                    u.extra = extra
                    u.created_by = 10
                    u.created_on = createdat
                    db.session.add(u)
                    db.session.commit()
                cursor.close()
                cnx.close()
                return "done"
            except Exception as e:
                return str(e),500


        @self.blueprint.route('/setting', methods=['GET'])
        def migrate_setting():
            try:
                cnx = mysql.connector.connect(host=self.host, user=self.username, password=self.password, database=self.database, )
                cursor = cnx.cursor()
                query = "SELECT * FROM setting"
                cursor.execute(query)

                for (id, category, name, value, updatedby, updatedat ) in cursor:
                    u = Setting()
                    u.id = id
                    u.category = category
                    u.name = name
                    u.value = value
                    u.updated_by = updatedby
                    u.updated_on = updatedat
                    db.session.add(u)
                    db.session.commit()
                cursor.close()
                cnx.close()
                return "done"
            except Exception as e:
                return str(e),500


        @self.blueprint.route('/sample', methods=['GET'])
        def migrate_sample():
            try:
                start = int(request.args.get("start",0))
                page_size = 2000
                company_for_equipement={}
                equipments = {}
                sensors = {}
                cnx = mysql.connector.connect(host=self.host, user=self.username, password=self.password, database=self.database, )
                cursor = cnx.cursor()

                while start < 25000000:
                    start += page_size

                    query = "SELECT * FROM sample  LIMIT %d,%d" %( start, page_size)
                    cursor.execute(query)
                    batch = []
                    for (id,equipement,sensor,type,value,lat,lon,state,sampledat,createdat) in cursor:
                        try:
                            if value == 'nan' or value == 'inf':
                                continue
                            u = {}
                            if equipement not in company_for_equipement:
                                e = Equipment.query.filter_by(id=equipement).first()
                                if not e:
                                    continue
                                else:
                                    equipments[equipement] = e
                                    c = Company.query.filter_by(id=e.company).first()
                                    if c:
                                        company_for_equipement[equipement] = c.id
                                    else:
                                        company_for_equipement[equipement] = None


                            company = company_for_equipement[equipement]
                            if company:
                                u['company'] = long(company)
                            else:
                                continue

                            if equipement:
                                u['equipment'] = long(equipement)
                            else:
                                continue

                            if sensor not in sensors:
                                s = Sensor.query.filter_by(id=sensor).first()
                                if s and s.packet_id:
                                    sensors[sensor] = s
                                else:
                                    continue

                            u['doc_id'] = str(equipments[equipement].serial_number)+":" + \
                                          str(sensors[sensor].packet_id)+":" + \
                                          str(long(sampledat)*1000)
                            u['sensor'] = long(sensor)
                            u['type'] = str(type)
                            u['value'] = float(value)
                            u['location'] = {}
                            u['location']['lat'] = float(lat)
                            u['location']['lon'] = float(lon)
                            u['state'] = str(state)
                            u['sampled_on']= long(sampledat)*1000
                            batch.append(u)
                        except KeyError as e:
                            logger.error("id %s ,equipement %s ,sensor %s" % (str(id),str(equipement),str(sensor)))
                            logger.exception(e)
                            return str(e),500
                        except Exception as e:
                            logger.exception(e)
                    cursor.close()
                    cnx.close()
                    store_samples(batch)
            except Exception as e:
                logger.exception(e)
                return str(e),500

    def get(self):
        return self.blueprint

