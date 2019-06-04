# -*- coding: utf-8 -*-
import clipboard
from datetime import *
from dateutil.relativedelta import *
import calendar
import ui
import os

def sc_change(sender):
	update_dp(start=True)
	
def btnpm(sender):
	
	txt_ue = sender.superview['txt_ue']
	
	if sender.name == 'btnp':
		 txt_ue.text = str(int(txt_ue.text) + 1)
	elif sender.name == 'btnm':
		 txt_ue.text = str(int(txt_ue.text) - 1)
	update_dp(start=True)
	
def dp_change(sender):
	if sender.name == 'dp_start':
		update_dp(start=True)
	else:
		update_dp()

def update_dp(start=False):
	global v
	txt_ue = v['txt_ue']
	sc_minutes = v['sc_minutes']
	dp_start = v['dp_start']
	dp_end = v['dp_end']
	minutes_add = int(sc_minutes.segments[sc_minutes.selected_index])
	
	if start:
		dp_end.date = dp_start.date + relativedelta(minutes=(minutes_add*int(txt_ue.text)))
	else:
		dp_start.date = dp_end.date - relativedelta(minutes=(minutes_add*int(txt_ue.text)))
		
def main():
	global v
	sc_minutes = v['sc_minutes']
	sc_minutes.selected_index = 1
	

if __name__ == '__main__':
	v = ui.load_view('uecalc')
	v.present('full_screen', hide_title_bar=True)
	main()
