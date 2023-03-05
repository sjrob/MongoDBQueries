from pymongo import MongoClient
import datetime
import pandas as pd
import get_metadata as gm


#2 sites of Bandundu (Caravane and 3 Rivière): 30th June 2022 – 30th October 2022
experiment_name = 'bandundu_incentive'

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

gm.get_metadata(experiment_name, start_datetime, end_datetime, uuid_list)
	
experiment_name = 'bandundu_control'

start_datetime = datetime.datetime(2022, 6, 30, 0, 0, 0, 0)
end_datetime = datetime.datetime(2022, 10, 30, 23, 59, 59, 999999)

uuid_list = [
    'd0bcb535d454253b',
    'd3bd56d1e510799c',
    '52dd5dc4e06c4663',
    'c463bef34130e51b',
    'f266bd017c5e1f27',
    '481b5a0398ab881b',
    '50b27b805d61c130',
    'b9abe8b7a37d1dfa',
    '4c593c6135820966',
    'c1f85eff61e6c0fc',
    'dd30e23326b74227',
    '2ead5e8229887aea',
    'a29506fac292c9eb',
    'a4b6babd9334f5e2',
    '9356e9a55b2acfce',
    'a839e0c6f2f67a93',
    '8db54bb9189e45cb',
    '486d498422278638',
    'c760c3b794b72f62',
    'd7668f520e755fe4',
    '25309b3dd7cf019e',
    '70f645766e9f5f603',
    '5d675cfb0a344e0a',
    '67e1c573005263ae1',
    'd398a760ee2a7516',
    'ba67ef541599f298',
    '62ee991ac2d07ecf',
    '5a7914e25abda450',
    'ae6ee56acc617856',
    'bf7aeb7b55e80e01',
    '7d2485c9caca6a9f',
    '8a2c06c096385d0a',
    'b7c6438d140fbe8a',
    'da8aca2912d9e3fe',
    '7e8e7774e7eebbcf'
]

gm.get_metadata(experiment_name, start_datetime, end_datetime, uuid_list)
	
experiment_name = 'kinshasa_control'

start_datetime = datetime.datetime(2022, 6, 30, 0, 0, 0, 0)
end_datetime = datetime.datetime(2022, 10, 30, 23, 59, 59, 999999)

uuid_list = [
    '1b29d5c8adbab809',
    '1c03c8c26c2e4cad',
    'e83e98940e6b9939',
    'C29bbc8c0c0d793a',
    'e5fc507e12c9cfee',
    'b95a5893d06f6d3a',
    '49a1d402e67430a6',
    'f4223281a48b7cb4',
    '6abdd051105e7ace',
    '116682dfa26aae24',
    '3f5bf8c3b703cbf8',
    '2fbcfaf2cf4d5c66',
    '8e36f69b58455bd3',
    '3dd95d91d2adcebd',
    '3d8b75537a80d5dd',
    '7d25036099b41091',
    '45db7eb36c7ff23b',
    'd31d8059e1ef43f8',
    '5338e47814036fdd',
    '0cb84483d9716a80',
    'ac584e4d9f0fdd60',
    'e1260d9aba96d221',
    '493791f7129926bf',
    '5bdc5177e7c6f5b6',
    '342ae47b1eed2c05',
    '5f2214480b7ce0c9',
    '0061f551a27deefb',
    'e8e8f09fb75a79ed',
    '05ee5a441bcaaa4c',
    '05884ed33d31f340',
    'e3198ee1276cd778',
    'cc1ecf1915c96fe0',
    'b8a0882cefcdf0d3',
    '8bba000e19d4abdd'
]

gm.get_metadata(experiment_name, start_datetime, end_datetime, uuid_list)
	
experiment_name = 'kinshasa_incentive'

start_datetime = datetime.datetime(2022, 6, 30, 0, 0, 0, 0)
end_datetime = datetime.datetime(2022, 10, 30, 23, 59, 59, 999999)

uuid_list = [
    '03d783523b494250',
    'd926be062bec03b2',
    '6a0db05c070473fe',
    '5b877b5a4a47c1fc',
    '484702488240b8bb',
    '57f6be3e2678ff2d',
    '10fbf4b13c671633',
    '13b41fda42f8fa85',
    'b1d6b22d0c4ce91f',
    'c8465237a4362a7b',
    'fc23d8eb1dea2de2',
    '88e3223c9fe809ca',
    'e8f4fb5267a1527c',
    '49ca1dab5601975e',
    '5a610a26bbad4f14',
    '99c4599e66ea233e',
    'f7ddba7798a1c699',
    '69d7f4600329f09e',
    '422054228eb6f5e7',
    '1c03c8c26c2e4cad',
    '2922f8dbebfc4fad',
    '050aab6fc4651530',
    'f4afabece3523bb3',
    'dca1a1e1764efcecb8',
    'dec13370cfa75e87',
    '15830e8d271a6cdb',
    '0c3da0a3ca8e17c4',
    'b1438e08e4867194',
    '94062f72a15b1a4b',
    '4466eac2bc69b460',
    '050aab6fc4651530',
    'c55f8f34cf2e361f',
    '34e297039f74b322',
    '4d3267fd607d95aa',
    '7d524beb5a1dc6d5',
    '4ed245c3a206ea0c'
]

gm.get_metadata(experiment_name, start_datetime, end_datetime, uuid_list)
