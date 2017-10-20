import cisco
with open("running-config.cfg",'r') as current:
	change_line=current_read()
current.closed()

rel_f=re.sub("ip address 172./",change_line)

with open("running-config.cfg",'r') as update:
        change_line=update_read()
update.closed


