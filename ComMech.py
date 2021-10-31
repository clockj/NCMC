#%%
'''
ComMech.py:
    Combine two chemical mechanisms
1. Input: 
    FILE_MECH_1, dominant chemical mechanism (If the same reaction appears in both files, parameters in the dominant one will be kept.)
    FILE_MECH_2, assistant chemical mechanism
    DIR, folder for outfile 
    FILE, output file name
'''
import numpy as np

lowerLetter = [ chr(x) for x in range(ord('a'), ord('z')+1) ]
upperLetter = [ chr(x) for x in range(ord('A'), ord('Z')+1) ]
number = [ str(x) for x in range(2, 10) ]
keyWord = []
keyWord.extend(lowerLetter)
keyWord.extend(upperLetter)
keyWord.extend(number)

'''
Combine elements
'''
def ComEl(FILE_MECH_1, FILE_MECH_2, FILE_OUT):
    '''
    ComEl:
        Combine elements from two different mechanisms
    '''

    # FILE_MECH_1 = 'KM2/KM2.chmech'
    # FILE_MECH_2 = 'Ammonia/mechanism.txt'

    fp_1 = open(FILE_MECH_1, 'r')
    fp_2 = open(FILE_MECH_2, 'r')

    # read first species
    line = fp_1.readline()
    flag = 0
    el_1 = []
    while (line):
        if 'ELEMENTS' in line:   
            flag = 1
        elif flag and 'END' in line:
            break 

        if (flag):
            l = line.split()
            el_1.extend(l)

        line = fp_1.readline()
    el_1 = el_1[1:]    
    fp_1.close()

    # read second species
    line = fp_2.readline()
    flag = 0
    el_2 = []
    while line:
        if 'ELEMENTS' in line:
            flag = 1
        elif flag and 'END' in line:
            break 

        if (flag):
            l = line.split()
            el_2.extend(l)

        line = fp_2.readline()
    el_2 = el_2[1:] 
    fp_2.close()


    '''
    Combine elements
    '''
    el_1_set = set(el_1)
    el_2_set = set(el_2)

    el_total_set = el_1_set | el_2_set
    el_total = list(el_total_set)


    '''
    Print total elements into a file
    '''

    # FILE_OUT = 'Total/NH3_C2H4_NEW_el'

    with open(FILE_OUT, 'w+') as fp:
        line = '    '.join(el_total) + '\n'
        fp.write(line)

'''
Combine species
'''
def ComSp(FILE_MECH_1, FILE_MECH_2, FILE_OUT):
    '''
    ComSp:
        Combine species from two different mechanisms
    '''

    # FILE_MECH_1 = 'KM2/KM2.chmech'
    # FILE_MECH_2 = 'Ammonia/mechanism.txt'

    fp_1 = open(FILE_MECH_1, 'r')
    fp_2 = open(FILE_MECH_2, 'r')

    # read first species
    line = fp_1.readline()
    flag = 0
    sp_1 = []
    while (line):
        if 'SPECIES' in line:   
            flag = 1
        elif flag and 'END' in line:
            break 

        if (flag):
            l = line.split()
            sp_1.extend(l)

        line = fp_1.readline()
    sp_1 = sp_1[1:]    
    fp_1.close()

    # read second species
    line = fp_2.readline()
    flag = 0
    sp_2 = []
    while line:
        if 'SPECIES' in line:
            flag = 1
        elif flag and 'END' in line:
            break 

        if (flag):
            l = line.split()
            sp_2.extend(l)

        line = fp_2.readline()
    sp_2 = sp_2[1:] 
    fp_2.close()


    '''
    Combine species
    '''
    sp_1_set = set(sp_1)
    sp_2_set = set(sp_2)

    sp_total_set = sp_1_set | sp_2_set
    sp_total = list(sp_total_set)


    '''
    Print total species into a file
    '''

    # FILE_OUT = 'Total/NH3_C2H4_NEW_sp'
    num = int(0)
    nSp = len(sp_total)
    nRow = int(nSp / 5) + int( nSp/5 - np.floor(nSp/5) > 0 )
    with open(FILE_OUT, 'w+') as fp:
        for i in range(nRow-1):
            line = '    '.join(sp_total[num: num+5]) + '\n'
            fp.write(line)
            num += 5
        line = '    '.join(sp_total[num: ]) + '\n'
        fp.write(line)

'''
Combine reactions
'''
class Reaction:
    def __init__(self):
        self.Reactant = []
        self.Product = []

        self.Reactant_set = set()
        self.Product_set = set()

        self.nReactant = 0
        self.nProduct = 0

        self.paramRe = []
        self.paramPr = []

        self.nRow = 0
        self.Sign = '<=>'

    '''
    Initialize reaction
    '''
    def addReactant(self, sp):
        '''
        sp: must be a list or array
        '''
        sp = list(sp)
        nSp = len(sp)
        if nSp == 0:
            print('Error in function addReactant: void sp')
            return

        for i in range(nSp):
            if sp[i] in self.Reactant:
                # Assume: repeated species only have parameter 1
                loc = self.Reactant.index(sp[i])
                self.paramRe[loc] += 1
            else:
                # judge whether there exits parameter
                if sp[i][0] in [str(x) for x in range(2,10)]:
                    name = sp[i][1:]
                    self.paramRe.append(int(sp[i][0]))
                else:
                    name = sp[i]
                    self.paramRe.append(1)

                self.Reactant.append(name)
                self.Reactant_set = set(self.Reactant)
                self.nReactant += 1 

    def addProduct(self, sp):
        '''
        sp: must be a list or array
        '''
        sp = list(sp)
        nSp = len(sp)
        if nSp == 0:
            print('Error in function addProduct: void sp')
            return

        for i in range(nSp):
            if sp[i] in self.Product:
                # Assume: repeated species only have parameter 1
                loc = self.Product.index(sp[i])
                self.paramPr[loc] += 1
            else:
                # judge whether there exits parameter
                if sp[i][0] in [str(x) for x in range(2,10)]:
                    name = sp[i][1:]
                    self.paramPr.append(int(sp[i][0]))
                else:
                    name = sp[i]
                    self.paramPr.append(1)

                self.Product.append(name)
                self.Product_set = set(self.Product)
                self.nProduct += 1 

    def addReaction(self, line, row):
        '''
        line: must be reaction
        '''
        # nRow: start from 0
        self.nRow = row
        # SignList = ['=', '<=', '=>', '<=>']
        if '<=>' in line:
            self.Sign = '<=>'
        elif '=>' in line:
            self.Sign = '=>'
        elif '<=' in line:
            self.Sign = '<='
        elif '=' in line:
            self.Sign = '='

        # Split reactions into reactant part and product part
        # print(line) 
        reaction = line.split()[0]
        if len(reaction.split(self.Sign)) != 2:
            print(reaction)
            print(reaction.split(self.Sign))
        reactant, product = reaction.split(self.Sign)

        reactant = reactant.replace('(', '')
        reactant = reactant.replace(')', '')
        product  = product.replace('(', '')
        product  = product.replace(')', '')

        self.addReactant(reactant.split('+'))
        self.addProduct(product.split('+'))


    '''
    Compare reactions
    '''
    def compareNum(self, reaction_n):
        Judge = self.nReactant == reaction_n.nReactant and self.nProduct == reaction_n.nProduct
        Judge_R = self.nReactant == reaction_n.nProduct and self.nProduct == reaction_n.nReactant

        if Judge or Judge_R:
            return 1
        return 0

    def compareRePr(self, reaction_n):
        # Assume both reaction has the same reactants and products
        Judge_Reactant = len(self.Reactant_set & reaction_n.Reactant_set) == self.nReactant

        Judge_Product = len(self.Product_set & reaction_n.Product_set) == self.nProduct

        Judge_Reactant_R = len(self.Reactant_set & reaction_n.Product_set) == self.nReactant

        Judge_Product_R = len(self.Product_set & reaction_n.Reactant_set) == self.nProduct

        if (Judge_Reactant and Judge_Product) or (Judge_Reactant_R and Judge_Product_R):
            return 1
        return 0

    def IsEq(self, reaction_n):
        if self.compareNum(reaction_n):
            if self.compareRePr(reaction_n):
                return 1
                # if self.Sign == reaction_n.Sign:
                    # return 1
        return 0

def GetReaction(FILE_MECH_NAME):
    '''
    Return a list of reactions
    '''
    fp = open(FILE_MECH_NAME, 'r')
    Reaction_collect = []

    flag = 0
    row = -1
    line = fp.readline()
    while line:
        row += 1
        # print('row:', row)
        # Read start and stop
        if line[0] == '!':
            line = fp.readline()
            continue

        if 'REACTIONS' in line:
            startRow = row + 1
            flag = 1
            line = fp.readline()
            continue

        if flag and ('END' in line):
            endRow = row
            break 
        
        if flag:
            # Judge whether it is a reaction
            # if '/' in line:
            #     line = fp.readline()
            #     continue 
            if ('=' in line) and (line[0] in keyWord):
                t = Reaction()
                t.addReaction(line, row)
                # print(t.Reactant)
                Reaction_collect.append(t)
        
        line = fp.readline()

    fp.close()
    return [startRow, endRow, Reaction_collect]

def ComRe(FILE_MECH_1, FILE_MECH_2, FILE_OUT):
    '''
    Combine reactions from two different mechanisms
        1. FILE_MECH_1: master mechanism 
        2. FILE_MECH_2: donor mechanism
    '''

    # FILE_MECH_1 = 'KM2/KM2.chmech'
    # FILE_MECH_2 = 'Ammonia/mechanism.txt'
    # FILE_OUT = 'Total/NH3_C2H4_NEW_Mech.inp'

    lowerLetter = [ chr(x) for x in range(ord('a'), ord('z')+1) ]
    upperLetter = [ chr(x) for x in range(ord('A'), ord('Z')+1) ]
    number = [ str(x) for x in range(2, 10) ]
    keyWord = []
    keyWord.extend(lowerLetter)
    keyWord.extend(upperLetter)
    keyWord.extend(number)


    start_master, end_master, Reaction_collect_master = GetReaction(FILE_MECH_1)
    start_donor,  end_donor,  Reaction_collect_donor = GetReaction(FILE_MECH_2)

    # reaction_row_donor = [Reaction_collect_donor[x].nRow for x in range(len(Reaction_collect_donor))]

    # Find repeated pairs: [row_donor, row_master]
    # Find repeated reaction row and next reaction row
    pairs = []
    endpoints = []

    for i in range(len(Reaction_collect_donor)):
        reaction = Reaction_collect_donor[i]
        flag = 0
        pairs_c = []
        pairs_c.append(reaction.nRow)

        for j in range(len(Reaction_collect_master)):
            if Reaction_collect_master[j].IsEq(reaction):
                flag = 1
                pairs_c.append(Reaction_collect_master[j].nRow)        
        if flag:
            pairs.append(pairs_c)

            if i == len(Reaction_collect_donor) - 1:
                endpoints.append([Reaction_collect_donor[i].nRow, end_donor])
            else:
                endpoints.append([Reaction_collect_donor[i].nRow, Reaction_collect_donor[i+1].nRow])


    # Write into new mechanism file
    fp_master = open(FILE_MECH_1, 'r')
    fp_donor  = open(FILE_MECH_2, 'r')
    fp_out    = open(FILE_OUT, 'w+')

    content_master = fp_master.readlines()[start_master:end_master]
    content_donor = fp_donor.readlines()[start_donor:end_donor]

    for i in range(len(content_master)):
        fp_out.write(content_master[i])
        # fp_out.write('\n')
    fp_out.write('!')
    fp_out.write('\n!Donor Mechanism Starts')
    fp_out.write('\n!\n')

    repeat_row = [pairs[x][0]-start_donor for x in range(len(pairs))]
    flag = 0
    for i in range(len(content_donor)):
        
        if i in repeat_row:
            loc = repeat_row.index(i)
            flag = endpoints[loc][1] - endpoints[loc][0] - 1
            continue

        if flag:
            flag -= 1
            continue
        else:
            fp_out.write(content_donor[i])

    fp_master.close()
    fp_donor.close() 
    fp_out.close()   

'''
Combine total
'''
def ComAll(FILE_MECH_1, FILE_MECH_2, DIR, FILE):
    FILE_El_OUT = DIR + '/' + FILE + '_El'
    FILE_Sp_OUT = DIR + '/' + FILE + '_Sp'
    FILE_Re_OUT = DIR + '/' + FILE + '_Re'
    FILE_All_OUT = DIR + '/' + FILE + '_total.inp'

    ComEl(FILE_MECH_1, FILE_MECH_2, FILE_El_OUT)
    ComSp(FILE_MECH_1, FILE_MECH_2, FILE_Sp_OUT)
    ComRe(FILE_MECH_1, FILE_MECH_2, FILE_Re_OUT)

    fp = open(FILE_All_OUT, 'w+')

    # Write elements
    fp.write('ELEMENTS\n')
    fp_el = open(FILE_El_OUT, 'r')
    content_el = fp_el.readlines()
    for s in content_el:
        fp.write(s)
    fp_el.close()
    fp.write('END\n')

    # Write species 
    fp_sp = open(FILE_Sp_OUT, 'r')
    content_sp = fp_sp.readlines()
    for s in content_sp:
        fp.write(s)
    fp_sp.close()
    fp.write('END\n')

    # Write reactions
    fp_re = open(FILE_Re_OUT, 'r')
    content_re = fp_re.readlines()
    for s in content_re:
        fp.write(s)
    fp_re.close()
    fp.write('END\n')

    fp.close()



# %%
'''
Examples
'''
# ComSp('KM2/KM2.chmech', 'Ammonia/mechanism.txt', 'Total/NH3_C2H4_NEW_sp')
# ComRe('KM2/KM2.chmech', 'Ammonia/mechanism.txt', 'Total/NH3_C2H4_NEW_Mech.inp')
# ComAll('KM2/KM2.chmech', 'Ammonia/mechanism.txt', 'Total', 'NH3_C2H4_NEW')
ComAll('Stanford/TheSoot.chmech', 'SJTU/chem_sjtu.inp', 'Total', 'NH3_C2H4_SFSJ')
# %%
