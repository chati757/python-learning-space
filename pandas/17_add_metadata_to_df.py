import pandas as pd

# store in hdf5 file format 
storedata = pd.HDFStore('college_data.hdf5') 
  
# data 
storedata.put('data_01', df) 
  
# including metadata 
metadata = {'scale': 0.1, 'offset': 15} 
  
# getting attributes 
storedata.get_storer('data_01').attrs.metadata = metadata 
  
# closing the storedata 
storedata.close() 
  
# getting data 
with pd.HDFStore('college_data.hdf5') as storedata: 
    data = storedata['data_01'] 
    metadata = storedata.get_storer('data_01').attrs.metadata 
  
# display data 
print('\nDataframe:\n', data) 
  
# display stored data 
print('\nStored Data:\n', storedata) 
  
# display metadata 
print('\nMetadata:\n', metadata) 