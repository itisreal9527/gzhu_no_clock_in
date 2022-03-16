from login_new import login_new
from clock_in import clock_in
import os

stu_id = str(os.env['STUID'])
pwd = str(os.env['STUPWD'])

login_new(stu_id, pwd)
clock_in(stu_id)
