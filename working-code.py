


# Command function to run GTAPv11 based on your GTAP INVEST 

default_erwin_style_cmf_dict = {
            'auxiliary files': 'gtapv11',   # changed this from v7 in your code
            'check-on-read elements': 'warn',
            'cpu': 'yes',
            'start with MMNZ': '500000000',
            'File GTAPSETS': '\"<^data_dir^>\SETS.har\"', 
            'File GTAPDATA': '\"<^data_dir^>\Basedata.har\"',
            'File GTAPPARM': '\"<^data_dir^>\Default.prm\"',
            # 'File GTAPSUPP': '\"<^data_dir^>\Basedata.har\"',
            'File GTAPSUPP': '\"<^data_dir^>\MapFile.har\"',
            'Updated File GTAPDATA': '\"<^output_dir^>\<^experiment_name^>.UPD\"',
            'File GTAPVOL': '\"<^output_dir^>\<^experiment_name^>-VOL.har\"',
            'File WELVIEW': '\"<^output_dir^>\<^experiment_name^>-WEL.har\"',
            'File GTAPSUM': '\"<^output_dir^>\<^experiment_name^>-SUM.har\"',
            'Solution File': '\"<^output_dir^>\<^experiment_name^>.sl4\"',
            'log file': '\"<^output_dir^>\<^experiment_name^>.log\"',
            'Method': 'Gragg',
            'Steps': '2 4 6',
            'Exogenous': [
                'pop',
                'psaveslack' ,
                'pfactwld',
                'profitslack',
                'incomeslack ',
                'endwslack',
                'cgdslack',
                'tradslack',
                'ams' ,
                'atm',
                'atf',
                'ats',
                'atd',
                'aosec',
                'aoreg',
                'avasec',
                'avareg',
                'aintsec',
                'aintreg',
                'aintall',
                'afcom',
                'afsec',
                'afreg',
                'afecom',
                'afesec',
                'afereg',
                'aoall',
                'afall',
                'afeall',
                'au',
                'dppriv',
                'dpgov',
                'dpsave',
                'to',
                'tinc',
                'tpreg',
                'tm',
                'tms',
                'tx',
                'txs',
                'qe',
                'qesf',
            ], # DONT FORGET REST ENDOGENOUS STATMENT 
            
            # (For our case I'm not sure wha to put here yet?)
            'Verbal Description': 'verbal_description_default_text',
            'xSets': {'AGCOM': ['Agri commodities', '(pdr, wht, gro, v_f, osd, c_b, pfb, ocr, ctl, oap, rmk, wol)'],
                      'AGCOM_SM' : ['smaller agri commodities', '(pdr, wht, gro)'],       
                      },
            # SUGGESTED CHANGE: Use xSet [name of set] read elements from file [file path] header "FOUR LETTER HEADER";
            'xSubsets': ['AGCOM is subset of COMM', 'AGCOM is subset of ACTS', 'AGCOM_SM is subset of COMM', 'AGCOM_SM is subset of ACTS'],
            # xSubset now will be defined based on the same xset file.
            
            # Here we can define the tariffs that we want to use for the trade and environment paper?? I have changed this to an example that I think would work for our paper

            'Shock': {'name': 'tariff on imports 80pc',
                      'shortname': 'ti80pc',
                      'shock_string': 'Shock afall(TRAD_COMM, PROD_COMM, reg) = uniform 80;'}
                
    }