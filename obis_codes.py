import re

# decode obis code
def decode_obis_code(collected_data):

        # A-B:C.D.E*F
        # group	description	examples

        # A	medium	                                1 = electricity, 8 = water
        # B	channel	                                0 = no channel available
        # C	physical unit, depends on A	        power, current, voltage...
        # D	measurement type, depends on A and C	maximum, current value, energy...
        # E	tariff	                                0 = total, 1 = tariff 1, 2 = tariff 2 ...
        # F	separate values defined by A-E	        billing periods, 255 if not used

        export_data = ''

        value  = retreiveValue(collected_data)
        code   = retreiveCode(collected_data)
        factor = retriveBillingPeriod(collected_data)

        if(code != None or collected_data[0] != '!'):

                print(f'Code: ', end='')
                
                # Print codes
                for codes in code:
                        print(f'{codes} ', end='')
                        export_data += f'{codes} '
 
                # Check if code is in OBIS_CODES, if so, print description
                if code[-1] in OBIS_CODES:       
                        codeDesc = (OBIS_CODES[code[-1]]['Desc'])
                        print(f'({codeDesc})', end=' ')
                        export_data += f',{codeDesc},'
                else:
                        print(f'(No code description found for {code[-1]}) ', end='')
                        export_data += f',No code description found for {code[-1]},'

                
                # Check if factor is in data and print it
                if (factor):
                        print(f'{factor[0]} ', end='')
                        export_data += f'{factor[0]},'
                else:
                        export_data += 'n/a,'

                # Print value(s)
                for item in value:
                        print(f'{item} ', end='')
                        export_data += f'{item} '
               
                if code[-1] in OBIS_CODES:
                        codeUnit = (OBIS_CODES[code[-1]]['Unit'])
                        print(codeUnit, end='')
                        export_data += f',{codeUnit}'
                else:
                        export_data += ',n/a'

                print('')
        else:
                if(collected_data[0] != '!'):
                        print(f'No code found for this data : {collected_data}')
        
        return export_data


# Retreive factor from data
def retriveBillingPeriod(collected_data):
        return re.findall("[\*]([0-9]+)", collected_data)

# Retreive value from data
def retreiveValue(collected_data):
        return re.findall("\(([\s:.0-9a-zA-Z^-]+|[\s0-9:]*)\)", collected_data)

# Retreive code from data
def retreiveCode(collected_data):

        # Try to find a code
        typeA = re.search("(^[0-9]+[-][0-9]+)", collected_data)  # X-Y
        typeB = re.findall("^[cC][.][0-9]+[.][0-9]+", collected_data) # C.X.Y
        typeC = re.findall("^[0-9]*[.][0-9]*[.][0-9]*", collected_data) # XX.YY.ZZ

        # Special case of 0-0:F.F.0(00000000) codes
        if (typeA): # XX-YY
                subcode = re.search("[:]([0-9CF]*[.][0-9F]*[.][0-9F]*)", collected_data)
                if (subcode):
                        return [f'{typeA.group(1)}', f'{subcode.group(1)}']
        elif (typeB): # CC.XX.YY
                return typeB

        elif (typeC): # XX.YY.ZZ
                return typeC
        else:
                return None


# Description of OBIS code for IEC 62056 standard protocol
OBIS_CODES    = {

                # Active energy Registers
                '1.8.0': { 'Desc': 'Positive active energy (A+) TOTAL',
                           'Unit': 'kWh'},
                '1.8.1': { 'Desc': 'Positive active energy (A+) T1',
                           'Unit': 'kWh'},
                '1.8.2': { 'Desc': 'Positive active energy (A+) T2',    
                           'Unit': 'kWh'},
                '1.8.3': { 'Desc': 'Positive active energy (A+) T3',
                           'Unit': 'kWh'},
                '1.8.4': { 'Desc': 'Positive active energy (A+) T4',
                           'Unit': 'kWh'},
                '2.8.0': { 'Desc': 'Negative active energy (A-) TOTAL',
                           'Unit': 'kWh'},
                '2.8.1': { 'Desc': 'Negative active energy (A-) T1',    
                           'Unit': 'kWh'},
                '2.8.2': { 'Desc': 'Negative active energy (A-) T2',    
                           'Unit': 'kWh'},
                '2.8.3': { 'Desc': 'Negative active energy (A-) T3',    
                           'Unit': 'kWh'},
                '2.8.4': { 'Desc': 'Negative active energy (A-) T4',    
                           'Unit': 'kWh'},
                '15.8.0': {'Desc': 'Absolute active energy (A+) TOTAL',
                           'Unit': 'kWh'},
                '15.8.1': {'Desc': 'Absolute active energy (A+) T1',
                           'Unit': 'kwh'},
                '15.8.2': {'Desc': 'Absolute active energy (A+) T2',
                           'Unit': 'kwh'},
                '15.8.3': {'Desc': 'Absolute active energy (A+) T3',
                           'Unit': 'kwh'},
                '15.8.4': {'Desc': 'Absolute active energy (A+) T4',
                           'Unit': 'kwh'},
                '16.8.0': {'Desc': 'Sum active energy without reverse blockade ((A+)-(A-)) TOTAL',
                           'Unit': 'kWh'},
                '16.8.':  {'Desc': 'Sum active energy without reverse blockade ((A+)-(A-)) T1',
                           'Unit': 'kWh'},
                '16.8.2': {'Desc': 'Sum active energy without reverse blockade ((A+)-(A-)) T2',
                           'Unit': 'kWh'},
                '16.8.3': {'Desc': 'Sum active energy without reverse blockade ((A+)-(A-)) T3',
                           'Unit': 'kWh'},
                '16.8.4': {'Desc': 'Sum active energy without reverse blockade ((A+)-(A-)) T4',
                           'Unit': 'kWh'},

                # Reactive energy Registers
                '3.8.0': { 'Desc': 'Positive reactive energy (Q+) TOTAL',
                           'Unit': 'kvarh'},
                '3.8.1': { 'Desc': 'Positive reactive energy (Q+) T1',
                           'Unit': 'kvarh'},
                '3.8.2': { 'Desc': 'Positive reactive energy (Q+) T2',
                           'Unit': 'kvarh'},
                '3.8.3': { 'Desc': 'Positive reactive energy (Q+) T3',  
                           'Unit': 'kvarh'},
                '3.8.4': { 'Desc': 'Positive reactive energy (Q+) T4',
                           'Unit': 'kvarh'},
                '4.8.0': { 'Desc': 'Negative reactive energy (Q-) TOTAL',
                           'Unit': 'kvarh'},
                '4.8.1': { 'Desc': 'Negative reactive energy (Q-) T1',
                           'Unit': 'kvarh'},
                '4.8.2': { 'Desc': 'Negative reactive energy (Q-) T2',
                           'Unit': 'kvarh'},
                '4.8.3': { 'Desc': 'Negative reactive energy (Q-) T3',
                           'Unit': 'kvarh'},
                '4.8.4': { 'Desc': 'Negative reactive energy (Q-) T4',
                           'Unit': 'kvarh'},

                # Import and Export Registers
                '5.8.0': { 'Desc': 'Imported inductive reactive energy in 1st quadrant (Q1) TOTAL',
                           'Unit': 'kvarh'},
                '5.8.1': { 'Desc': 'Imported inductive reactive energy in 1st quadrant (Q1) T1',
                           'Unit': 'kvarh'},
                '5.8.2': { 'Desc': 'Imported inductive reactive energy in 1st quadrant (Q1) T2',
                           'Unit': 'kvarh'},
                '5.8.3': { 'Desc': 'Imported inductive reactive energy in 1st quadrant (Q1) T3',
                           'Unit': 'kvarh'},
                '5.8.4': { 'Desc': 'Imported inductive reactive energy in 1st quadrant (Q1) T4',
                           'Unit': 'kvarh'},
                '6.8.0': { 'Desc': 'Imported capacitive reactive energy in 2nd quadrant (Q2) TOTAL',
                           'Unit': 'kvarh'},
                '6.8.1': { 'Desc': 'Imported capacitive reactive energy in 2nd quadrant (Q2) T1',
                           'Unit': 'kvarh'},
                '6.8.2': { 'Desc': 'Imported capacitive reactive energy in 2nd quadrant (Q2) T2',
                           'Unit': 'kvarh'},
                '6.8.3': { 'Desc': 'Imported capacitive reactive energy in 2nd quadrant (Q2) T3',
                           'Unit': 'kvarh'},
                '6.8.4': { 'Desc': 'Imported capacitive reactive energy in 2nd quadrant (Q2) T4',
                           'Unit': 'kvarh'},
                '7.8.0': { 'Desc': 'Exported inductive reactive energy in 3rd quadrant (Q3) TOTAL',
                           'Unit': 'kvarh'},
                '7.8.1': { 'Desc': 'Exported inductive reactive energy in 3rd quadrant (Q3) T1',
                           'Unit': 'kvarh'},
                '7.8.2': { 'Desc': 'Exported inductive reactive energy in 3rd quadrant (Q3) T2',
                           'Unit': 'kvarh'},
                '7.8.3': { 'Desc': 'Exported inductive reactive energy in 3rd quadrant (Q3) T3',                
                           'Unit': 'kvarh'},
                '7.8.4': { 'Desc': 'Exported inductive reactive energy in 3rd quadrant (Q3) T4',
                           'Unit': 'kvarh'},
                '8.8.0': { 'Desc': 'Exported capacitive reactive energy in 4th quadrant (Q4) TOTAL',
                           'Unit': 'kvarh'},
                '8.8.1': { 'Desc': 'Exported capacitive reactive energy in 4th quadrant (Q4) T1',
                           'Unit': 'kvarh'},
                '8.8.2': { 'Desc': 'Exported capacitive reactive energy in 4th quadrant (Q4) T2',
                           'Unit': 'kvarh'},
                '8.8.3': { 'Desc': 'Exported capacitive reactive energy in 4th quadrant (Q4) T3',
                           'Unit': 'kvarh'},
                '8.8.4': { 'Desc': 'Exported capacitive reactive energy in 4th quadrant (Q4) T4',
                           'Unit': 'kvarh'},

                # Apparent energy Registers
                '9.8.0': { 'Desc': 'Absolute apparent energy (S+) TOTAL',
                           'Unit': 'kVAh'},
                '9.8.1': { 'Desc': 'Absolute apparent energy (S+) T1',
                           'Unit': 'kVAh'},
                '9.8.2': { 'Desc': 'Absolute apparent energy (S+) T2',
                           'Unit': 'kVAh'},
                '9.8.3': { 'Desc': 'Absolute apparent energy (S+) T3',
                           'Unit': 'kVAh'},
                '9.8.4': { 'Desc': 'Absolute apparent energy (S+) T4',
                           'Unit': 'kVAh'},

                # Register of active anergy per phases
                '21.8.0': { 'Desc': 'Positive active energy (A+) in phase L1 TOTAL',
                            'Unit': 'kWh'},
                '41.8.0': { 'Desc': 'Positive active energy (A+) in phase L2 TOTAL',
                            'Unit': 'kWh'},
                '61.8.0': { 'Desc': 'Positive active energy (A+) in phase L3 TOTAL',
                            'Unit': 'kWh'},
                '22.8.0': { 'Desc': 'Negative active energy (A-) in phase L1 TOTAL',
                            'Unit': 'kWh'},
                '42.8.0': { 'Desc': 'Negative active energy (A-) in phase L2 TOTAL',
                            'Unit': 'kWh'},
                '62.8.0': { 'Desc': 'Negative active energy (A-) in phase L3 TOTAL',
                            'Unit': 'kWh'},
                '35.8.0': { 'Desc': 'Absolute active energy (|A|) in phase L1 TOTAL',
                            'Unit': 'kWh'},
                '55.8.0': { 'Desc': 'Absolute active energy (|A|) in phase L2 TOTAL',
                            'Unit': 'kWh'},
                '75.8.0': { 'Desc': 'Absolute active energy (|A|) in phase L3 TOTAL',   
                            'Unit': 'kWh'},
                
                # Maximum demand Registers
                '1.6.0': { 'Desc': 'Positive active maximum demand (A+) TOTAL',
                           'Unit': 'kW'},
                '1.6.1': { 'Desc': 'Positive active maximum demand (A+) T1',
                           'Unit': 'kW'},
                '1.6.2': { 'Desc': 'Positive active maximum demand (A+) T2',
                           'Unit': 'kW'},
                '1.6.3': { 'Desc': 'Positive active maximum demand (A+) T3',
                           'Unit': 'kW'},
                '1.6.4': { 'Desc': 'Positive active maximum demand (A+) T4',
                           'Unit': 'kW'},
                '2.6.0': { 'Desc': 'Negative active maximum demand (A-) TOTAL',
                           'Unit': 'kW'},
                '2.6.1': { 'Desc': 'Negative active maximum demand (A-) T1',
                           'Unit': 'kW'},
                '2.6.2': { 'Desc': 'Negative active maximum demand (A-) T2',
                           'Unit': 'kW'},
                '2.6.3': { 'Desc': 'Negative active maximum demand (A-) T3',
                           'Unit': 'kW'},
                '2.6.4': { 'Desc': 'Negative active maximum demand (A-) T4',
                           'Unit': 'kW'},
                '15.6.0':{ 'Desc': 'Absolute active maximum demand (|A|) TOTAL',
                           'Unit': 'kW'},
                '15.6.1':{ 'Desc': 'Absolute active maximum demand (|A|) T1',
                           'Unit': 'kW'},
                '15.6.2':{ 'Desc': 'Absolute active maximum demand (|A|) T2',
                           'Unit': 'kW'},
                '15.6.3':{ 'Desc': 'Absolute active maximum demand (|A|) T3',
                           'Unit': 'kW'},
                '15.6.4':{ 'Desc': 'Absolute active maximum demand (|A|) T4',
                           'Unit': 'kW'},
                '3.6.0': { 'Desc': 'Positive reactive maximum demand (Q+) TOTAL',
                           'Unit': 'kvar'},
                '4.6.0': { 'Desc': 'Negative reactive maximum demand (Q-) TOTAL',       
                           'Unit': 'kvar'},
                '5.6.0': { 'Desc': 'Reactive maximum demand in Q1 (Q1) TOTAL',
                           'Unit': 'kvar'},
                '6.6.0': { 'Desc': 'Reactive maximum demand in Q2 (Q2) TOTAL',
                           'Unit': 'kvar'},
                '7.6.0': { 'Desc': 'Reactive maximum demand in Q3 (Q3) TOTAL',
                           'Unit': 'kvar'},
                '8.6.0': { 'Desc': 'Reactive maximum demand in Q4 (Q4) TOTAL',
                           'Unit': 'kvar'},
                '9.6.0': { 'Desc': 'Apparent maximum demand (S+) TOTAL',
                           'Unit': 'kVA'},

                # Cumulative maximum demand registers
                '1.2.0': { 'Desc': 'Positive active cumulative maximum demand (A+) TOTAL',
                           'Unit': 'kW'},
                '1.2.1': { 'Desc': 'Positive active cumulative maximum demand (A+) T1', 
                           'Unit': 'kW'},
                '1.2.2': { 'Desc': 'Positive active cumulative maximum demand (A+) T2', 
                           'Unit': 'kW'},
                '1.2.3': { 'Desc': 'Positive active cumulative maximum demand (A+) T3', 
                           'Unit': 'kW'},
                '1.2.4': { 'Desc': 'Positive active cumulative maximum demand (A+) T4', 
                           'Unit': 'kW'},
                '2.2.0': { 'Desc': 'Negative active cumulative maximum demand (A-) TOTAL',
                           'Unit': 'kW'},
                '2.2.1': { 'Desc': 'Negative active cumulative maximum demand (A-) T1',
                           'Unit': 'kW'},
                '2.2.2': { 'Desc': 'Negative active cumulative maximum demand (A-) T2',
                           'Unit': 'kW'},
                '2.2.3': { 'Desc': 'Negative active cumulative maximum demand (A-) T3',
                           'Unit': 'kW'},
                '2.2.4': { 'Desc': 'Negative active cumulative maximum demand (A-) T4',
                           'Unit': 'kW'},
                '15.2.0':{ 'Desc': 'Absolute active cumulative maximum demand (|A|) TOTAL',
                           'Unit': 'kW'},
                '15.2.1':{ 'Desc': 'Absolute active cumulative maximum demand (|A|) T1',
                           'Unit': 'kW'},
                '15.2.2':{ 'Desc': 'Absolute active cumulative maximum demand (|A|) T2',
                           'Unit': 'kW'},
                '15.2.3':{ 'Desc': 'Absolute active cumulative maximum demand (|A|) T3',
                           'Unit': 'kW'},
                '15.2.4':{ 'Desc': 'Absolute active cumulative maximum demand (|A|) T4',
                           'Unit': 'kW'},
                '3.2.0': { 'Desc': 'Positive reactive cumulative maximum demand (Q+) TOTAL',
                           'Unit': 'kvar'},
                '4.2.0': { 'Desc': 'Negative reactive cumulative maximum demand (Q-) TOTAL',
                           'Unit': 'kvar'},
                '5.2.0': { 'Desc': 'Reactive cumulative maximum demand in Q1 (Q1) TOTAL',
                           'Unit': 'kvar'},
                '6.2.0': { 'Desc': 'Reactive cumulative maximum demand in Q2 (Q2) TOTAL',
                           'Unit': 'kvar'},
                '7.2.0': { 'Desc': 'Reactive cumulative maximum demand in Q3 (Q3) TOTAL',
                           'Unit': 'kvar'},
                '8.2.0': { 'Desc': 'Reactive cumulative maximum demand in Q4 (Q4) TOTAL',
                           'Unit': 'kvar'},
                '9.2.0': { 'Desc': 'Apparent cumulative maximum demand (S+) TOTAL',
                           'Unit': 'kVA'},
        
                # Demands in a current demand period
                '1.4.0': { 'Desc': 'Positive active demand in a current demand period (A+) TOTAL',
                           'Unit': 'kW'},
                '2.4.0': { 'Desc': 'Negative active demand in a current demand period (A-) TOTAL',
                           'Unit': 'kW'},
                '15.4.0':{ 'Desc': 'Absolute active demand in a current demand period (|A|) TOTAL',
                           'Unit': 'kW'},
                '3.4.0': { 'Desc': 'Positive reactive demand in a current demand period (Q+) TOTAL',
                           'Unit': 'kvar'},
                '4.4.0': { 'Desc': 'Negative reactive demand in a current demand period (Q-) TOTAL',
                           'Unit': 'kvar'},
                '5.4.0': { 'Desc': 'Reactive demand in Q1 in a current demand period (Q1) TOTAL',
                           'Unit': 'kvar'},
                '6.4.0': { 'Desc': 'Reactive demand in Q2 in a current demand period (Q2) TOTAL',
                           'Unit': 'kvar'},
                '7.4.0': { 'Desc': 'Reactive demand in Q3 in a current demand period (Q3) TOTAL',
                           'Unit': 'kvar'},
                '8.4.0': { 'Desc': 'Reactive demand in Q4 in a current demand period (Q4) TOTAL',
                           'Unit': 'kvar'},
                '9.4.0': { 'Desc': 'Apparent demand in a current demand period (S+) TOTAL',
                           'Unit': 'kVA'},

                #Demands in the last completed demand period
                '1.5.0': { 'Desc': 'Positive active demand in the last completed demand period (A+) TOTAL',
                           'Unit': 'kW'},
                '2.5.0': { 'Desc': 'Negative active demand in the last completed demand period (A-) TOTAL',
                           'Unit': 'kW'},
                '15.5.0':{ 'Desc': 'Absolute active demand in the last completed demand period (|A|) TOTAL',
                           'Unit': 'kW'},
                '3.5.0': { 'Desc': 'Positive reactive demand in the last completed demand period (Q+) TOTAL',
                           'Unit': 'kvar'},
                '4.5.0': { 'Desc': 'Negative reactive demand in the last completed demand period (Q-) TOTAL',
                           'Unit': 'kvar'},
                '5.5.0': { 'Desc': 'Reactive demand in Q1 in the last completed demand period (Q1) TOTAL',      
                           'Unit': 'kvar'},
                '6.5.0': { 'Desc': 'Reactive demand in Q2 in the last completed demand period (Q2) TOTAL',
                           'Unit': 'kvar'},
                '7.5.0': { 'Desc': 'Reactive demand in Q3 in the last completed demand period (Q3) TOTAL',
                           'Unit': 'kvar'},
                '8.5.0': { 'Desc': 'Reactive demand in Q4 in the last completed demand period (Q4) TOTAL',
                           'Unit': 'kvar'},
                '9.5.0': { 'Desc': 'Apparent demand in the last completed demand period (S+) TOTAL',
                           'Unit': 'kVA'},
                
                # Instantaneous power registers
                '1.7.0': { 'Desc': 'Positive active instantaneous power (A+) TOTAL',
                           'Unit': 'kW'},
                '21.7.0':{ 'Desc': 'Positive active instantaneous power (A+) in phase L1',
                           'Unit': 'kW'},
                '41.7.0':{ 'Desc': 'Positive active instantaneous power (A+) in phase L2',
                           'Unit': 'kW'},
                '61.7.0':{ 'Desc': 'Positive active instantaneous power (A+) in phase L3',
                           'Unit': 'kW'},
                '2.7.0': { 'Desc': 'Negative active instantaneous power (A-) TOTAL',
                           'Unit': 'kW'},
                '22.7.0':{ 'Desc': 'Negative active instantaneous power (A-) in phase L1',
                           'Unit': 'kW'},
                '42.7.0':{ 'Desc': 'Negative active instantaneous power (A-) in phase L2',
                           'Unit': 'kW'},
                '62.7.0':{ 'Desc': 'Negative active instantaneous power (A-) in phase L3',
                           'Unit': 'kW'},
                '15.7.0':{ 'Desc': 'Absolute active instantaneous power (|A|) TOTAL',
                           'Unit': 'kW'},
                '35.7.0':{ 'Desc': 'Absolute active instantaneous power (|A|) in phase L1',
                           'Unit': 'kW'},
                '55.7.0':{ 'Desc': 'Absolute active instantaneous power (|A|) in phase L2',
                           'Unit': 'kW'}, 
                '75.7.0':{ 'Desc': 'Absolute active instantaneous power (|A|) in phase L3',
                           'Unit': 'kW'}, 
                '16.7.0':{ 'Desc': 'Sum active instantaneous power (A+) -(A-)  TOTAL',
                           'Unit': 'kW'},
                '36.7.0':{ 'Desc': 'Sum active instantaneous power (A+) -(A-) in phase L1',
                           'Unit': 'kW'},
                '56.7.0':{ 'Desc': 'Sum active instantaneous power (A+) -(A-) in phase L2',
                           'Unit': 'kW'},
                '76.7.0':{ 'Desc': 'Sum active instantaneous power (A+) -(A-) in phase L3',
                           'Unit': 'kW'},
                '3.7.0': { 'Desc': 'Positive reactive instantaneous power (Q+) TOTAL',
                           'Unit': 'kvar'},
                '23.7.0':{ 'Desc': 'Positive reactive instantaneous power (Q+) in phase L1',
                           'Unit': 'kvar'},
                '43.7.0':{ 'Desc': 'Positive reactive instantaneous power (Q+) in phase L2',
                           'Unit': 'kvar'},
                '63.7.0':{ 'Desc': 'Positive reactive instantaneous power (Q+) in phase L3',
                           'Unit': 'kvar'},
                '4.7.0': { 'Desc': 'Negative reactive instantaneous power (Q-) TOTAL',
                           'Unit': 'kvar'},        
                '24.7.0':{ 'Desc': 'Negative reactive instantaneous power (Q-) in phase L1',
                           'Unit': 'kvar'},
                '44.7.0':{ 'Desc': 'Negative reactive instantaneous power (Q-) in phase L2',
                           'Unit': 'kvar'},
                '64.7.0':{ 'Desc': 'Negative reactive instantaneous power (Q-) in phase L3',
                           'Unit': 'kvar'},
                '9.7.0': { 'Desc': 'Apparent instantaneous power (S+) TOTAL',
                           'Unit': 'kVA'},
                '29.7.0':{ 'Desc': 'Apparent instantaneous power (S+) in phase L1',
                           'Unit': 'kVA'},
                '49.7.0':{ 'Desc': 'Apparent instantaneous power (S+) in phase L2',
                           'Unit': 'kVA'},
                '69.7.0':{ 'Desc': 'Apparent instantaneous power (S+) in phase L3',
                           'Unit': 'kVA'},

                #  Electricity network quality registers
                '11.7.0':{ 'Desc': 'Instantaneous current (I)',
                           'Unit': 'A'},
                '31.7.0':{ 'Desc': 'Instantaneous current (I) in phase L1',
                           'Unit': 'A'},
                '51.7.0':{ 'Desc': 'Instantaneous current (I) in phase L2',
                           'Unit': 'A'},
                '71.7.0':{ 'Desc': 'Instantaneous current (I) in phase L3',
                           'Unit': 'A'},
                '91.7.0':{ 'Desc': 'Instantaneous current (I) in neutral',
                           'Unit': 'A'},
                '11.6.0':{ 'Desc': 'Maximum current (I max)',
                           'Unit': 'A'},   
                '31.6.0':{ 'Desc': 'Maximum current (I max) in phase L1',
                           'Unit': 'A'},
                '51.6.0':{ 'Desc': 'Maximum current (I max) in phase L2',
                           'Unit': 'A'},
                '71.6.0':{ 'Desc': 'Maximum current (I max) in phase L3',
                           'Unit': 'A'},
                '91.6.0':{ 'Desc': 'Maximum current (I max) in neutral',
                           'Unit': 'A'},
                '12.7.0':{ 'Desc': 'Instantaneous voltage (U)',
                           'Unit': 'V'},
                '32.7.0':{ 'Desc': 'Instantaneous voltage (U) in phase L1',
                           'Unit': 'V'},
                '52.7.0':{ 'Desc': 'Instantaneous voltage (U) in phase L2',
                           'Unit': 'V'},
                '72.7.0':{ 'Desc': 'Instantaneous voltage (U) in phase L3',
                           'Unit': 'V'},
                '13.7.0':{ 'Desc': 'Instantaneous power factor',
                           'Unit': 'cos'},
                '33.7.0':{ 'Desc': 'Instantaneous power factor in phase L1',
                           'Unit': 'cos'},
                '53.7.0':{ 'Desc': 'Instantaneous power factor in phase L2',
                           'Unit': 'cos'},
                '73.7.0':{ 'Desc': 'Instantaneous power factor in phase L3',
                           'Unit': 'cos'},
                '14.7.0':{ 'Desc': 'Instantaneous frequency',
                           'Unit': 'Hz'},
                
                # Tamper registers (energy registers and registers of elapsed time)
                'C.53.1':{ 'Desc': 'Tamper 1 anergy register',
                           'Unit': 'kWh'},
                'C.53.2':{ 'Desc': 'Tamper 2 anergy register',
                           'Unit': 'kWh'}, 
                'C.53.3':{ 'Desc': 'Tamper 3 anergy register',
                           'Unit': 'kWh'},
                'C.53.4':{ 'Desc': 'Tamper 4 anergy register',
                           'Unit': 'kWh'},
                'C.53.11':{'Desc': 'Tamper 5 anergy register',
                           'Unit': 'kWh'},
                'C.53.5':{ 'Desc': 'Tamper 1 time counter register',
                           'Unit': 'h'},
                'C.53.6':{ 'Desc': 'Tamper 2 time counter register',
                           'Unit': 'h'},
                'C.53.7':{ 'Desc': 'Tamper 3 time counter register',
                           'Unit': 'h'},   
                'C.53.8':{ 'Desc': 'Tamper 4 time counter register',
                        'Unit': 'h'},
                'C.53.10':{'Desc': 'Tamper 5 time counter register',
                           'Unit': 'h'},
                
                #  Events registers (counters and time-stamps)
                'C.2.0': { 'Desc': 'Event parameters change - counter',
                           'Unit': 'count'},
                'C.2.1': { 'Desc': 'Event parameters change - time stamp',
                           'Unit': 'date'},
                'C.51.1':{ 'Desc': 'Event terminal cover opened - counter',
                           'Unit': 'count'},
                'C.51.2':{ 'Desc': 'Event terminal cover opened - time stamp',
                           'Unit': 'date'},
                'C.51.3':{ 'Desc': 'Event main cover opened - counter',
                           'Unit': 'count'},
                'C.51.4':{ 'Desc': 'Event main cover opened - time stamp',
                           'Unit': 'date'},
                'C.51.5':{ 'Desc': 'Event magnetic field detection start - counter',
                           'Unit': 'count'},
                'C.51.6':{ 'Desc': 'Event magnetic field detection start - time stamp',
                           'Unit': 'date'},
                'C.51.5':{ 'Desc': 'Event magnetic field detection start - counter',
                           'Unit': 'count'},
                'C.51.6':{ 'Desc': 'Event magnetic field detection start - time stamp',
                           'Unit': 'date'},
                'C.51.7':{ 'Desc': 'Event reverse power flow - counter',
                           'Unit': 'count'},
                'C.51.8':{ 'Desc': 'Event reverse power flow - time stamp',
                           'Unit': 'date'},
                'C.7.0': { 'Desc': 'Event power failure - counter',
                           'Unit': 'count'},
                'C.7.1': { 'Desc': 'Event power failure - time stamp',
                           'Unit': 'date'},
                'C.51.13':{'Desc': 'Event power up - counter',
                           'Unit': 'count'},
                'C.51.14':{'Desc': 'Event power up - time stamp',
                           'Unit': 'date'},
                'C.51.15':{'Desc': 'Event RTC (Real Time Clock) set - counter',
                           'Unit': 'count'},
                'C.51.16':{'Desc': 'Event RTC (Real Time Clock) set - time stamp',
                           'Unit': 'date'},
                'C.51.21':{'Desc': 'Event terminal cover closed - counter',
                           'Unit': 'count'},
                'C.51.22':{'Desc': 'Event terminal cover closed - time stamp',
                           'Unit': 'date'},
                'C.51.23':{'Desc': 'Event main cover closed - counter', 
                           'Unit': 'count'},  
                'C.51.24':{'Desc': 'Event main cover closed - time stamp',
                           'Unit': 'date'},  
                'C.51.25':{'Desc': 'Event log-book 1 erased - counter',      
                           'Unit': 'count'},
                'C.51.26':{'Desc': 'Event log-book 1 erased - time stamp',
                           'Unit': 'date'},
                'C.51.27':{'Desc': 'Event fraud start - counter',
                           'Unit': 'count'},
                'C.51.28':{'Desc': 'Event fraud start - time stamp',
                           'Unit': 'date'},
                'C.51.29':{'Desc': 'Event fraud end - counter', 
                           'Unit': 'count'},
                'C.51.30':{'Desc': 'Event fraud end - time stamp',
                           'Unit': 'date'},
                
                # Miscellaneous registers used in sequences
                '0.9.1':  {'Desc': 'Current time (hh:mm:ss)',
                           'Unit': 'hh:mm:ss'},
                '0.9.2':  {'Desc': 'Current date (dd/mm/yy)',
                           'Unit': 'dd/mm/yy'},
                '0.9.4':  {'Desc': 'Date and Time (YYMMDDhhmmss)',
                           'Unit': 'YYMMDDhhmmss'},
                '0.8.0':  {'Desc': 'Demand period',
                           'Unit': 'min'},
                '0.8.4':  {'Desc': 'Load profile period (option)',
                           'Unit': 'min'},
                '0.0.0':  {'Desc': 'Device address 1',
                           'Unit': 'hex'}, 
                '0.0.1':  {'Desc': 'Device address 2',
                           'Unit': 'hex'},
                '0.1.0':  {'Desc': 'MD reset counter',
                           'Unit': 'count'},
                '0.1.2':  {'Desc': 'MD reset timestamp',
                           'Unit': 'date'},
                '0.2.0':  {'Desc': 'Firmware version',
                           'Unit': 'hex'},
                '0.2.2':  {'Desc': 'Tariff program ID',
                           'Unit': 'hex'},
                'C.1.0':  {'Desc': 'Meter serial number',
                           'Unit': 'hex'},
                'C.1.2':  {'Desc': 'Parameters file code',
                           'Unit': 'hex'},
                'C.1.4':  {'Desc': 'Parameters check sum',
                           'Unit': 'hex'},
                'C.1.5':  {'Desc': 'Firmware built date',
                           'Unit': 'date'},
                'C.1.6':  {'Desc': 'Firmware check sum',
                           'Unit': 'hex'},
                'C.6.0':  {'Desc': 'Power down time counter', 
                           'Unit': 'h'},
                'C.6.1':  {'Desc': 'Battery remaining capacity',
                           'Unit': 'Ah'},
                'F.F.0':  {'Desc': 'Fatal error meter status',
                           'Unit': 'hex'},
                'C.87.0': {'Desc': 'Active tariff',
                           'Unit': 'hex'},
                '0.2.1':  {'Desc': 'Parameters scheme ID',
                           'Unit': 'hex'},
                'C.60.9': {'Desc': 'Fraud flag',
                           'Unit': 'hex'},
                '0.3.0':  {'Desc': 'Active energy meter constant',
                           'Unit': 'hex'},
                '0.4.2':  {'Desc': 'Current transformer ratio',
                           'Unit': 'hex'},
                '0.4.3':  {'Desc': 'Voltage transformer ratio',
                           'Unit': 'hex'},
                } 