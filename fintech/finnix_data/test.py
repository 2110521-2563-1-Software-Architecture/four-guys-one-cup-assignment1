import finnix_data
import time 

print('----------------------- start test ohlcv    -------------------------')
##### Class SETData #####

##### Increase Load in Class SETData #####


start_time = time.time()
# if no input in universe list. class will return All stock company 
stock_table_muti_format = finnix_data.SETData("2005-01-01 00:00:00","2020-04-13 10:11:00",['AOT'])
print('Basic use ohlcv ',stock_table_muti_format.start_datetime,stock_table_muti_format.end_datetime , 'with no universe add')
# Query data from Server '5m' '1m'
stock_table_muti_format.fetch_ohlcv(['1d'])

temp_dict_stock = stock_table_muti_format.get_ohlcv()

print('\nTotal Run Time','stock_table_muti_format')
print("\n--- %s seconds ---" % (time.time() - start_time))
print('\nDict. of stock\n',temp_dict_stock)


print('----------------------- end test ohlcv    -------------------------')

'''


print('----------------------- start test fundamental    -------------------------')

print('Basic Use 2004-01-01 09:30:00','2005-01-21 09:30:00 [7UP,AA,ACC,AEC]')
start_time = time.time()
# if no input in universe list. class will return All stock company 
stock_pull = finnix_data.SETData('2004-01-01 09:30:00','2005-01-21 09:30:00',['7UP','AA','ACC','AEC'])

# Query data from Server '5m' '1m'
stock_pull.fetch_fundamental(['epsnumrevfy1c','ltgc'])

temp_dict_stock = stock_pull.get_fundamental()

print('\nTotal Run Time','stock_table_muti_format')
print("\n--- %s seconds ---" % (time.time() - start_time))
print('\nDict. of stock epsnumrevfy1c \n',temp_dict_stock['epsnumrevfy1c'])




print('Test extreme Case 2005-01-04 00:00:00 2020-01-04 00:00:00' )
start_time = time.time()
# if no input in universe list. class will return All stock company 
stock_table_muti_format = finnix_data.SETData('2005-01-04 00:00:00','2020-01-04 00:00:00' )
stock_table_muti_format.fetch_fundamental()
temp_dict_stock = stock_table_muti_format.get_fundamental()

print('\nTotal Run Time','stock_table_muti_format')
print("\n--- %s seconds ---" % (time.time() - start_time))
print('\nDict. of stock Test extreme Case -NO Input in any line  \n',temp_dict_stock)

'''