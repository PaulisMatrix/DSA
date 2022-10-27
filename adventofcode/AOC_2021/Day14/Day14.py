steps = 10
'''
chain = 'NNCB'
rules = {'CH': 'B', 'HH': 'N', 'CB': 'H', 'NH': 'C', 'HB': 'C', 
'HC': 'B', 'HN': 'C', 'NN': 'C', 'BH': 'H', 'NC': 'B', 'NB': 'B',
'BN': 'B', 'BB': 'N', 'BC': 'B', 'CC': 'N', 'CN': 'C'}
'''
chain = ''
rules = {}


input = open('input','r').read()[:-1].split('\n')
chain = chain+input[0]
for rule in input[2:]:
    #print(rule)
    key,val = rule.split('->')
    #print(key.strip(),val.strip())
    rules[key.strip()] = val.strip()


while steps:
    temp = ''
    #print(temp)
    for i in range(len(chain)-1):
        v = rules[chain[i:i+2]]
        if i==0:
            temp+=chain[i] + v + chain[i+1]
        else:
            temp+=v+chain[i+1]
    chain = temp
    temp = ''
    steps-=1

from collections import Counter
count = Counter(chain)
print(count)


'''

{'VO': 'C', 'VV': 'S', 'HK': 'H', 'FC': 'C', 'VB': 'V', 'NO': 'H', 'BN': 'B', 'FP': 'K', 'CS': 'C',
'HC': 'S', 'FS': 'K', 'KH': 'V', 'CH': 'H', 'BP': 'K', 'OF': 'K', 'SS': 'F', 'SP': 'C', 'PN': 'O', 
'CK': 'K', 'KS': 'H', 'HO': 'K', 'FV': 'F', 'SN': 'P', 'HN': 'O', 'KK': 'H', 'KP': 'O', 'CN': 'N',
'BO': 'C', 'CC': 'H', 'PB': 'F', 'PV': 'K', 'BV': 'K', 'PP': 'H', 'KB': 'F', 'NC': 'F', 'PC': 'V', 
'FN': 'N', 'NH': 'B', 'CF': 'V', 'PO': 'F', 'KC': 'S', 'VP': 'P', 'HH': 'N', 'OB': 'O', 'KN': 'O',
'PS': 'N', 'SF': 'V', 'VK': 'F', 'CO': 'N', 'KF': 'B', 'VC': 'C', 'SH': 'S', 'HV': 'V', 'FK': 'O',
'NV': 'N', 'SC': 'O', 'BK': 'F', 'BB': 'K', 'HF': 'K', 'OC': 'O', 'KO': 'V', 'OS': 'P', 'FF': 'O', 
'PH': 'F', 'FB': 'O', 'NN': 'C', 'NK': 'C', 'HP': 'B', 'PF': 'H', 'PK': 'C', 'NP': 'O', 'NS': 'V',
'CV': 'O', 'VH': 'C', 'OP': 'N', 'SO': 'O', 'SK': 'H', 'SV': 'O', 'NF': 'H', 'BS': 'K', 'BH': 'O', 
'VN': 'S', 'HB': 'O', 'OH': 'K', 'CB': 'B', 'BC': 'S', 'OV': 'F', 'BF': 'P', 'OO': 'F', 'HS': 'H',
'ON': 'P', 'NB': 'F', 'CP': 'S', 'SB': 'V', 'VF': 'C', 'OK': 'O', 'FH': 'H', 'KV': 'S', 'FO': 'C', 'VS': 'B'}

'''


















