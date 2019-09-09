import yaml
import requests
from api.sites import search as search_plotnames

config = yaml.load(open("config.yaml", 'r'), Loader=yaml.FullLoader)

"""
Cultivars are the experimental germplasms, using BrAPI's /germplasm endpoint.
"""


def search(season=None, experimentId=None, germplasmId=None, treatmentId=None, pageSize=None, page=None):
    # Default page limit is 1000, but 1134 records existed at time of writing
    url = "%s/germplasm?pageSize=2000" % config["brapi_api"]
    try:
        results = []
        r = requests.get(url).json()['result']['data']

        # Get plot names & filter to distinct
        for germ in r:
            results.append(germ['accessionNumber'])

        results.sort()
        return list(set(results))

    except:
        print("Error fetching sites from BrAPI; using default.")
        return ['PI144134', 'PI145619', 'PI145626', 'PI145633', 'PI146890', 'PI152591', 'PI152651', 'PI152694',
                'PI152727', 'PI152730', 'PI152733', 'PI152771', 'PI152816', 'PI152828', 'PI152860', 'PI152862',
                'PI152923', 'PI152961', 'PI152965', 'PI152966', 'PI152967', 'PI152971', 'PI153877', 'PI154750',
                'PI154844', 'PI154846', 'PI154944', 'PI154987', 'PI154988', 'PI155516', 'PI155760', 'PI155885',
                'PI156178', 'PI156217', 'PI156268', 'PI156326', 'PI156330', 'PI156393', 'PI156463', 'PI156487',
                'PI156871', 'PI156890', 'PI157030', 'PI157035', 'PI157804', 'PI167093', 'PI170787', 'PI175919',
                'PI176766', 'PI179749', 'PI180348', 'PI195754', 'PI196049', 'PI196583', 'PI196586', 'PI196598',
                'PI197542', 'PI19770',  'PI213900', 'PI217691', 'PI218112', 'PI221548', 'PI221651', 'PI22913',
                'PI229841', 'PI251672', 'PI255239', 'PI257599', 'PI257600', 'PI266927', 'PI267573', 'PI273465',
                'PI273969', 'PI276837', 'PI297130', 'PI297155', 'PI297171', 'PI302252', 'PI303658', 'PI329256',
                'PI329286', 'PI329300', 'PI329301', 'PI329310', 'PI329319', 'PI329326', 'PI329333', 'PI329338',
                'PI329351', 'PI329394', 'PI329403', 'PI329435', 'PI329440', 'PI329465', 'PI329466', 'PI329471',
                'PI329473', 'PI329478', 'PI329480', 'PI329501', 'PI329506', 'PI329510', 'PI329511', 'PI329517',
                'PI329518', 'PI329519', 'PI329541', 'PI329545', 'PI329546', 'PI329550', 'PI329570', 'PI329584',
                'PI329585', 'PI329605', 'PI329614', 'PI329618', 'PI329632', 'PI329644', 'PI329645', 'PI329646',
                'PI329665', 'PI329673', 'PI329699', 'PI329702', 'PI329710', 'PI329711', 'PI329841', 'PI329843',
                'PI329864', 'PI329865', 'PI330169', 'PI330181', 'PI330182', 'PI330184', 'PI330185', 'PI330195',
                'PI330196', 'PI330199', 'PI330796', 'PI330803', 'PI330807', 'PI330833', 'PI330858', 'PI337680',
                'PI337689', 'PI35038',  'PI452542', 'PI452619', 'PI452692', 'PI453696', 'PI455217', 'PI455221',
                'PI455280', 'PI455301', 'PI455307', 'PI505717', 'PI505722', 'PI505735', 'PI506030', 'PI506069',
                'PI506114', 'PI506122', 'PI510757', 'PI511355', 'PI513898', 'PI514456', 'PI521019', 'PI521152',
                'PI521280', 'PI521290', 'PI524475', 'PI525049', 'PI52606',  'PI526905', 'PI527045', 'PI533902',
                'PI533998', 'PI534120', 'PI534165', 'PI535785', 'PI535792', 'PI535794', 'PI535795', 'PI535796',
                'PI540518', 'PI561840', 'PI562730', 'PI562732', 'PI562781', 'PI562897', 'PI562970', 'PI562971',
                'PI562981', 'PI562982', 'PI562985', 'PI562990', 'PI562991', 'PI562994', 'PI562997', 'PI562998',
                'PI563002', 'PI563006', 'PI563009', 'PI563020', 'PI563021', 'PI563022', 'PI563032', 'PI563196',
                'PI563222', 'PI563295', 'PI563329', 'PI563330', 'PI563331', 'PI563332', 'PI563338', 'PI563350',
                'PI563355', 'PI564163', 'PI566819', 'PI569090', 'PI569097', 'PI569148', 'PI569244', 'PI569264',
                'PI569418', 'PI569419', 'PI569420', 'PI569421', 'PI569422', 'PI569423', 'PI569427', 'PI569443',
                'PI569444', 'PI569445', 'PI569447', 'PI569452', 'PI569453', 'PI569455', 'PI569457', 'PI569458',
                'PI569460', 'PI569462', 'PI569465', 'PI569886', 'PI570031', 'PI570038', 'PI570042', 'PI570071',
                'PI570073', 'PI570074', 'PI570075', 'PI570076', 'PI570085', 'PI570087', 'PI570090', 'PI570091',
                'PI570096', 'PI570106', 'PI570109', 'PI570110', 'PI570114', 'PI570145', 'PI570254', 'PI570373',
                'PI570388', 'PI570400', 'PI570431', 'PI573193', 'PI576399', 'PI576401', 'PI583832', 'PI585406',
                'PI585452', 'PI585454', 'PI585461', 'PI585467', 'PI585577', 'PI585608', 'PI585954', 'PI585961',
                'PI585966', 'PI586435', 'PI586541', 'PI593916', 'PI619807', 'PI619838', 'PI620072', 'PI620157',
                'PI63715',  'PI641807', 'PI641810', 'PI641815', 'PI641817', 'PI641821', 'PI641824', 'PI641825',
                'PI641829', 'PI641830', 'PI641835', 'PI641836', 'PI641850', 'PI641860', 'PI641862', 'PI641892',
                'PI641909', 'PI642998', 'PI643008', 'PI643016', 'PI646242', 'PI646251', 'PI646266', 'PI651491',
                'PI651495', 'PI651496', 'PI651497', 'PI653616', 'PI653617', 'PI655972', 'PI655978', 'PI655983',
                'PI656015', 'PI656026', 'PI656035', 'PI656065', 'PI92270', 'SP1516']

def get(season=None, experimentId=None, germplasmId=None, treatmentId=None, pageSize=None, page=None):
    return "Not implemented."

# Get all sites for given cultivar, optionally filtered by season
def get_sites_by_cultivar(cultivar, season=None):
    results = []
    try:
        # First, get cultivar ID from name
        url = "%s/germplasm?germplasmName=%s" % (config["brapi_api"], cultivar)
        r = requests.get(url).json()['result']['data']
        for germ in r:
            # Then, use that ID + season name to get list of plot names
            germ_id = germ['germplasmDbId']
            results += search_plotnames(season, germplasmId=germ_id)
        return results
    except:
        print("Error getting sites for cultivar %s" % cultivar)

    return results

