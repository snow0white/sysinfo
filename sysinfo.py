#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test1.py
#  
#  Copyright 2019 snowwhite <snowwhite@debian>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


from requests import get 
import os
import time
import platform 
import socket 
import psutil


print('********System utility *********')
print('1. OS version') 
print('2. Battery life')
print('3. Disk IO counters')
print('4. Disk usage')
print('5. User')
print('6. IP address')
print('7. net stats')
print('8. net info')
print('9. Disk partitions')
print('10. Python pin, Python Compiler')
print('11. Add something later')
print('12. Net Connections')
print('********Thank you for usinig this system utility***********')
choice = raw_input('What info do you want:')
choice = int(choice)
if choice == 1: 
		print'System:', platform.system()
		print'Node :', platform.node()
		print'Release:', platform.release()
		print'Version:', platform.version()
		print'Machine:', platform.machine()
		print'Processor:', platform.processor()
		print'Users:', psutil.users()
elif choice == 2:
		battery = psutil.sensors_battery() 
		battery
		print battery  
elif choice == 3:
		print(psutil.disk_io_counters(perdisk=True))
elif choice == 4:
		print(psutil.disk_usage('/'))
elif choice == 5: 
		print(psutil.users())
elif choice == 6:
				s = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
				s.connect(("1.1.1.1" , 80))
				ip = get ('https://ifconfig.co/ip').text
				print 'My public IP address is:', ip
				print 'My private IP address is:', (s.getsockname() [0])
				s.close()
elif choice == 7:
		print(psutil.net_if_stats())
elif choice == 8:
	#def psutil.net_if_addrs():
		#z = psutil.net_if_addrs():
		#for z in conn:
			#print conn
		print(psutil.net_if_addrs())
elif choice == 9:
	def disksinfo(self):
		values = []
		disk_partitions = psutil.disk_partitions(all=True)
		for partition in disk_partitions:
			usage = psutil.disk_usage(partition.mountpoint)
			device = {
				'device': partition.device,
				'mountpoint': partition.mountpoint, 
				'fstype': partition.opts,
				'total': usage.total,
				'used': usage.used,
				'free': usage.used, 
				'percent': usage.percent
				}
		values.append(device)
		values = sorted(values, key=lambda device: device['device'])
		print disksinfo

elif choice == 10:
		p = psutil.Process()
		with p.oneshot():
			p.name()
			p.cpu_times()
			p.cpu_percent()
			p.ppid()
			p.status()
		print p
elif choice == 11:
		print(platform.machine())
elif choice == 12: 
	def print_conns_by_proc_name(addr):
		system_conns = psutil.net_connections()
		for i in system_connsm:
			if conn.pid == pid:
				print i
print('Thank you')
