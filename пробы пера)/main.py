import Azertag_az
import time

#
# ojr = [['Kennedinin', 'əlaqədar'], ['bilməməsi'], ['k']]
# # parsing()
# print(moderator.parsing(data_master_scan_in = ojr, data_time=int(time.time() - 24*60*60*50)))

# print('\n\n\n\n\n\n', '-'*40)
#
# ojr = [['mənim', 'bilmədən'], ['bilməməsi'], ['k']]
# print(parsing(data_master_scan_in = ojr, data_time=int(time.time() - 24*60*60*50)))
#
# print('\n\n\n\n\n\n', '-'*40)
#
ojr = [['intellektual', 'enerjisistem'], ['qərargah'], ['helikopterlər']]
print(Azertag_az.parsing(data_master_scan_in = ojr, data_time=int(time.time() - 24*60*60*50)))

# print(parsing(data_master_scan_in = [['azərbaycanda'], []], data_time=int(time.time() - 24*60*60*50)))