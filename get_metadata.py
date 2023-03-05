from pymongo import MongoClient
import datetime
import pandas as pd


def get_metadata(experiment_name, start_datetime, end_datetime, uuid_list):
	''' Return all known metadata from MongoDB at humbug.ac.uk for a certain date range for a list of uuids.
		Example field:
	    db['reports'].find_one()
        returns:
		{'_id': ObjectId('55cb4efa7cdf33532641047d'), 'uuid': 'd323c5c00fd24998', 'datetime_received': datetime.datetime(2015, 8, 12, 14, 49, 46, 982000),
	 'path': '/data/MozzWear/2015-08-10/19/r2015-08-10_19.15.29.wav_u2015-08-12_14.49.46.982279.wav', 'model': 'ONE TOUCH 4015X',
	  'datetime_recorded': datetime.datetime(2015, 8, 10, 19, 15, 29), 'manufacturer': 'Orange'}
	
	input args:
	`experiment_name`: str -> Name of experiment for saving file output
	`start`: datetime.datetime object: Accept recordings uploaded (indexed with "datetime_recorded") from `start`
	`end`: datetime.datetime object: Accept recordings uploaded until `end`
	`uuid_list`: List of `uuids` to include in output
	'''

	client = MongoClient('mongodb://humbug.ac.uk/')
	db = client['backend_upload'] 

	recordings = db['reports']
	# Return query for a certain uuid, with date recorded after ("$gt: greater than") datetime.datetime object
           
	myquery = {"uuid": {"$in": uuid_list}, "datetime_recorded": {"$gt": start_datetime, "$lt": end_datetime}}
	mydoc = recordings.find(myquery)

	df = pd.DataFrame(list(mydoc))

	df.to_csv(experiment_name + '_' + start_datetime.strftime("%Y-%m-%d") + 
			'_to_' + end_datetime.strftime("%Y-%m-%d") + '_metadata.csv', index=False)

if __name__ == "__main__":

#	experiment_name = 'Kivokoni_RCT_2022'
	experiment_name = 'bandundu_incentive'        

#	start_datetime = datetime.datetime(2022, 4, 18, 0, 0, 0, 0)
#	end_datetime = datetime.datetime(2022, 7, 31, 23, 59, 59, 999999)
#2 sites of Bandundu (Caravane and 3 Rivière): 30th June 2022 – 30th October 2022

	start_datetime = datetime.datetime(2022, 6, 30, 0, 0, 0, 0)
	end_datetime = datetime.datetime(2022, 10, 30, 23, 59, 59, 999999)

	uuid_list = ['f4cf4f4a029532bf',
	'a067f65c04d5ed19',
	'fdd3129cd6eaf633',
	'd38b9aacf8b338d2',
	'68a73e84e7090bf4',
	'0ff99f4f4fc74c86',
	'2ce39e7862cb0e51',
	'3b549f0dc93dffbd',
	'37fbb17ef5545621',
	'f781222a831d0294',
	'dae65e2362b77610',
	'5fc138c5153333c2',
	'5a3ef007b030d361',
	'ff604ceeaebf7529',
	'a08376d8189fd308',
	'f4c81b83578febfe',
	'2d4bb501a2d9ce29',
	'a0e9cfa743eec0cc',
	'e30179f8a1e084a7',
	'fc507bdf46bab35e',
	'6b592bb82b7fe563',
	'bbf01b67c5e9e1ea',
	'e827ed7d944b179c',
	'20a872ca52ae80a8',
	'8e0265e5738cf391',
	'2845e16552cb0f8d',
	'b7353c4eb027b108',
	'ed2a53bf3f3d2db8',
	'304d32d925ad8513',
	'5527b7a6428c9080',
	'9e4d1338902f5dd9',
	'288eb0081adf0efa',
	'8b5261b28de8142a',
	'f1e9a5f94e824436',
	'dd7988c6c86d3537',
	'7ec2eb29d9d977e956']
        
	get_metadata(experiment_name, start_datetime, end_datetime, uuid_list)
