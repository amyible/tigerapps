'''
- Mapping of buildings to their info
- Functions that return a list of buildings with certain properties
'''
from pom.menus.scraper import DINING_HALLS
from pom.printers.scraper import PRINTER_BLDGS

BLDG_INFO = {
    'AL099': ('99 Alexander (Forbes College)',(),True),
    'ALEXH': ('Alexander Hall',(),True),
    'ARCHB': ('Architecture Building',(),True),
    'ARCHL': ('Architectural Laboratory',(),True),
    'ARTMU': ('Art Museum',(),True),
    'BENDC': ('Bendheim Center for Finance',(),True),
    'BENDH': ('Bendheim Hall',(),True),
    'BERLT': ('Berlind Theatre',(),True),
    'BLAIR': ('Blair/Buyers Hall',(),True),
    'BOBSH': ('Bobst Hall',(),True),
    'BOWEN': ('Bowen Hall',(),True),
    'BR171': ('Broadmead, 171',(),True),
    'BURRH': ('Aaron Burr Hall',(),True),
    'C1879': ('1879 Hall',('Department of Philosophy', 'Department of Religion', 'Program in Classical Philosophy', 'Program in Political Philosophy',),True),
    'C1915': ('1915 Hall',(),True),
    'CARRS': ('U-Store/Career Services',('Office of Career Services', 'International Internship Program', 'Study Abroad Program',),True),
    'CCAMP': ('Campus Club',(),True),
    'CCAPA': ('Cap and Gown Club',(),True),
    'CCHAR': ('Charter Club',(),True),
    'CCLOI': ('Cloister Club',(),True),
    'CCOLO': ('Colonial Club',(),True),
    'CCOTT': ('Cottage Club',(),True),
    'CENJL': ('Center for Jewish Life',(),True),
    'CFCTR': ('Carl A. Fields Center',(),True),
    'CHANC': ('Chancellor Green',(),True),
    'CLIOH': ('Clio Hall',(),True),
    'COMPU': ('Computer Science Building',('Department of Computer Science',),True),
    'CORWH': ('Corwin Hall',('Department of Politics',),True),
    'CQUAD': ('Quadrangle Club',(),True),
    'CTERR': ('Terrace Club',(),True),
    'CTOWE': ('Tower Club',(),True),
    'DICKH': ('Dickinson Hall',('Department of History', 'Program in History of Science', 'Program in Gender and Sexuality Studies',),True),
    'DILCE': ('Dillon Court East',(),True),
    'DILCW': ('Dillon Court West',(),True),
    'DILLG': ('Dillon Gymnasium',('Stephens Fitness Center', 'Club Sports',),True),
    'ELPLE': ('Elementary Particles Lab East',(),True),
    'ENOHA': ('Eno Hall',(),True),
    'EPYNE': ('East Pyne Building',('Department of Classics', 'Department of Comparative Literature', 'Department of French and Italian', 'Department of German', 'Department of Slavic Languages and Literatures', 'Department of Spanish and Portuguese Languages and Cultures', 'Humanities Resource Center',),True),
    'EQUAA': ('Engineering Quad - A Wing',('Department of Chemical and Biological Engineering', 'Program in Engineering Biology',),True),
    'EQUAB': ('Engineering Quad - B Wing',('Department of Electrical Engineering',),True),
    'EQUAC': ('Engineering Quad - C Wing',('School of Engineering and Applied Science',),True),
    'EQUAD': ('Engineering Quad - D Wing',('Department of Mechanical and Aerospace Engineering',),True),
    'EQUAE': ('Engineering Quad - E Wing',('Department of Civil and Environmental Engineering',),True),
    'EQUAF': ('Engineering Quad - F Wing',(),True),
    'EQUAG': ('Engineering Quad - G Wing',('Energy Research Laboratory',),True),
    'EQUAJ': ('Engineering Quad - J Wing',(),True),
    'FINEH': ('Fine Hall',('Department of Mathematics','Program in Applied and Computational Mathematics',),True),
    'FIRES': ('Firestone Library',(),True),
    'FISHH': ('Fisher Hall',('Department of Economics',),True),
    'FITZO': ('FitzRandolph Observatory',(),True),
    'FORBC': ('Forbes College Main',(),True),
    #'FORRT': ('Forrestal Campus',(),True),
    'FRICK': ('Frick Chemistry Laboratory',('Department of Chemistry',),True),
    'FRIEN': ('Friend Center for Engineering Education',('Engineering Library',),True),
    'FRIST': ('Frist Campus Center',('Cafe Vivian', 'Convenience Store (C-Store)', 'East Asian Library', 'Frist Ticket Office', 'Mailroom and Package Room', 'Program in East Asian Studies', 'Shipping and Packing Agency', 'McGraw Center for Teaching and Learning',),True),
    'GREEN': ('Green Hall',(),True),
    'GUYOT': ('Guyot Hall',('Department of Ecology and Evolutionary Biology', 'Department of Geosciences', 'Princeton Environmental Institute (PEI)', 'Schultz Laboratory', 'Moffett Laboratory',),True),
    'HAMIL': ('Hamilton Hall',(),True),
    'HARGH': ('Whitman College',('Hargadon Hall',),True),
    'HENHO': ('Henry House',(),True),
    'HOLDE': ('Holder Hall',(),True),
    'HOYTL': ('Hoyt Chemical Laboratory',(),True),
    'ICAHN': ('Carl Icahn Laboratory',('Lewis-Sigler Institute for Integrative Genomics',),True),
    'IVY05': ('Ivy Lane, 5',('Center for the Study of Religion',),True),
    'JADWH': ('Jadwin Hall',('Department of Physics', 'Princeton Center for Theoretical Science',),True),
    'JOLIN': ('Joline Hall',(),True),
    'JONES': ('Jones Hall',(),True),
    'LEWLI': ('Lewis Library',(),True),
    'MADIH': ('Madison Hall',(),True),
    'MARXH': ('Marx Hall',('University Center for Human Values',),True),
    'MCCKH': ('McCormick Hall',('Department of Art and Archaeology', 'Marquand Library of Art and Archaeology', 'Art Museum',),True),
    'MCCOH': ('McCosh Health Center',('University Health Services',),True),
    'MCDON': ('James S. McDonnell Hall',(),True),
    'MOFFH': ('Moffett Laboratory',(),True),
    'MUDDL': ('Mudd Manuscript Laboratory',(),True),
    'NA185': ('Nassau Street, 185',(),True),
    'NA201': ('Nassau Street, 201',(),True),
    'ORFES': ('Sherrerd Hall',('Department of Operations Research and Financial Engineering (ORFE)','Center for Information Technology Policy',),True),
    #'PAL01': ('Palmer Square',(),True),
    'PEYTH': ('Peyton Hall: Department of Astrophysical Sciences',(),True),
    'PRO58': ('58 Prospect',(),True),
    'ROBEH': ('Robertson Hall',('Woodrow Wilson School of Public and International Affairs', 'Program in Global Health and Health Policy', 'Program in Law and Public Affairs (LAPA)', 'Center for Arts and Cultural Policy Studies',),True),
    'ROCKL': ('Rock Magnetism Laboratory',(),True),
    'SCCAH': ('Scheide Caldwell House',('Canadian Studies', 'Program in European Cultural Studies', 'Program in Hellenic Studies', 'Program in Judaic Studies', 'Program in Linguistics', 'Program in Medieval Studies', 'Program in the Ancient World', 'Renaissance Studies at Princeton',),True),
    'SCHUL': ('Schultz Laboratory',(),True),
    'STANH': ('Stanhope',(),True),
    'STH91': ('Prospect Avenue, 91',(),True),
    'THOML': ('Thomas Laboratory',('Department of Molecular Biology',),True),
    'VONNH': ('Von Neumann Hall',(),True),
    'WALLB': ('Wallace Hall',('Department of Sociology',),True),
    'WHIGH': ('Whig Hall',(),True),
    'WIL41': ('William Street, 41',(),True),
    'WILCH': ('Wu/Wilcox Hall',('Butler Residential College', 'Wilson Residential College',),True),
    'WOOLC': ('Woolworth Music Center',('Department of Music', 'Program in Musical Performance',),True),
    'WUHAL': ('Wu Hall',(),True),
    
    '106AL': ('106 Alexander',(),True),
    '114NA': ('U-Store/Labyrinth Books',(),True),
    '11UNI': ('11 University Place',(),True),
    '120PR': ('116/120 Prospect Apartments',(),True),
    '126AL': ('120/126 Alexander',(),True),
    '130AL': ('130 Alexander',(),True),
    '136AL': ('132-134/136 Alexander',(),True),
    '144AL': ('138-140/144 Alexander',(),True),
    '169NA': ('169 Nassau',(),True),
    '179NA': ('179 Nassau',(),True),
    '180AL': ('172/180 Alexander',(),True),
    '185NA': ('185 Nassau',(),True),
    '1895F': ('1895 Field',(),True),
    #'1901H': ('1901 Hall',(),True),
    '1938H': ('1938 Hall',(),True),
    '1952S': ('1952 Stadium',(),True),
    '1967H': ('1967 Hall',(),True),
    '200EL': ('200 Elm',(),True),
    '201NA': ('199/201 Nassau',(),True),
    '221NA': ('221 Nassau',(),True),
    '22CHA': ('22 Chambers St.',(),True),
    '23UNI': ('23 University Place',(),True),
    '29EDW': ('27/29 Edwards Place',(),True),
    '31EDW': ('31 Edwards Place',(),True),
    '35UNI': ('35 University Place',(),True),
    '45UNI': ('41/45  University Place',(),True),
    '48UNI': ('48 University Place',(),True),
    '81ALE': ('81 Alexander',(),True),
    'BAKER': ('Baker Rink',(),True),
    'BEDFO': ('Bedford Field',(),True),
    'BLOOM': ('Bloomberg Hall',(),True),
    'BROWN': ('Brown Hall',('Brown Dining Co-op',),True),
    #'BUYER': ('Buyers Hall',(),True),
    'CALDW': ('Caldwell Fieldhouse',(),True),
    'CAMPB': ('Campbell Hall',(),True),
    'CHAPE': ('University Chapel',(),True),
    'CLARK': ('Clarke Field',(),True),
    'COGEN': ('Cogeneration Plant',(),True),
    'CUYLE': ('Cuyler Hall',(),True),
    'DENUN': ('DeNunzio Pool',(),True),
    'DINKY': ('Dinky Station',(),True),
    'DODHA': ('Dod Hall',(),True),
    'EDWAR': ('Edwards Hall',(),True),
    'FEINB': ('Feinburg Hall',(),True),
    'FINNE': ('Finney/Campbell Field',(),True),
    'FISHE': ('Fisher Hall Dorm',(),True),
    'FOULK': ('Foulke Hall',(),True),
    'FRELI': ('Frelinghuysen Field',(),True),
    'GARDE': ('Garden Theater',(),True),
    'GAUSS': ('Gauss Hall',(),True),
    'GRADC': ('Graduate College',(),True),
    'GULIC': ('Gulick Pavilion',(),True),
    'HENRY': ('Henry Hall',(),True),
    'JADWG': ('Jadwin Gym',('Princeton University Athletics',),True),
    'LENZT': ('Lenz Tennis Center',(),True),
    'LITTL': ('Little Hall',(),True),
    'LOCKH': ('Lockhart Hall',(),True),
    'LOWRI': ('Lowrie House',(),True),
    'MACLE': ('Maclean House',(),True),
    'MACMI': ('MacMillan Building',(),True),
    'MCCAR': ('McCarter Theatre',(),True),
    'MCCOS': ('McCosh Hall',('Department of English','Program in American Studies',),True),
    'MURRA': ('Murray Dodge Hall',(),True),
    'NASSH': ('Nassau Hall',('Office of Public Affairs',),True),
    'NEWSO': ('New South Building',(),True),
    'NTHGB': ('North Guard Booth',(),False),
    'PALMH': ('Palmer House',(),True),
    'POEFI': ('Poe/Pardee Field',(),True),
    'POWER': ('Princeton Stadium/Powers Field',(),True),
    'PYNEH': ('Pyne Hall',(),True),
    'ROCKL': ('Rock Magnetism Laboratory',(),True),
    'SCULL': ('Scully Hall',(),True),
    'SEXTO': ('Sexton Field',(),True),
    'SHEAR': ('Shea Rowing Center',(),True),
    'SOUGB': ('South Guard Booth',(),True),
    'SPELM': ('Spelman Halls',(),True),
    'STRUB': ('Strubing Field',(),True),
    'THEWA': ('The Wa',(),True),
    'WALKE': ('Walker Hall',(),True),
    'WESTC': ('West College',('Office of the Registrar', 'Undergraduate Financial Aid', 'Office of Student Employment',),True),
    'WESTG': ('West Garage (Lot 7)',(),True),
    'WITHR': ('Witherspoon Hall',(),True),
    'YOSEL': ('Yoseloff Hall',(),True),
    
    'WILFH': ('Wilf Hall',(),True),
    '1976H': ('1976 Hall',(),True),
    'BOGLE': ('Bogle Hall',(),True),
    'MCDON': ('McDonnell Hall of Physics',(),True),
    'ROBRT': ('Roberts Stadium',('Myslik Field', 'Plummer Field',),True),
    '1939H': ('1939 Hall',(),True),
    'WRGHT': ('Wright Hall',(),True),
    'PATTN': ('Patton Hall',(),True),
    '1903H': ('1903 Hall',(),True),
    '1937H': ('1937 Hall',(),True),
    'CLAPP': ('Dodge-Osborn/1927-Clapp Hall',(),True),
    'LAUGH': ('Laughlin/1901 Hall',(),True),
    '2DICK': ('2 Dickinson Street',('Dickinson Co-op'),True),
    '71UNI': ('71 University Place',('Office of Conference and Event Services', 'Princeton Summer Sports Camps'),True)
    
}

BLDG_CODE = tuple((code, info[0]) for code,info in BLDG_INFO.iteritems())


def getBldgsWithHours():
    return tuple()

def getBldgsWithMenus():
    return tuple(bldg_code for bldg_code in DINING_HALLS.keys())

def getBldgsWithLaundry():
    return ('BLOOM','HARGH', 'SCULL', 'PATTN', 'PYNEH', 'HAMIL', 'JOLIN', 'LOCKH', 'LITTL', 
                'EDWAR', 'FEINB', 'BLAIR', 'CLAPP', 'DODHA', 'BROWN', 'WITHR',  'LAUGH', 
                'C1915', 'HENHO', 'FORBC', 'SPELM', 'HOLDE', '1903H', '1976H', 'YOSEL',)

def getBldgsWithPrinters():
    return tuple(bldg_code for bldg_code in PRINTER_BLDGS.values())

