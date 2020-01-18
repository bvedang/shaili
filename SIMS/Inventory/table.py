from flask_table import Table,Col
class LS_Stage_1_Table(Table):

    classes = ['table']
    fda_batch_no = Col('FDA Batch No')
    starting_date = Col('Starting Date')
    salicylic_acid = Col('Salicylic Acid')
    dms = Col('DMS')
    caustic_soda_flakes = Col('Caustic Soda Flakes')
    hcl = Col('HCL')
    water = Col('Water')
    wet_cake = Col('Wet Cake')
    dry_output = Col('Dry Output')
    p_yeild = Col('Yeild')
    complete_date = Col('Complete Date')

class LS_Stage_2_Table(Table):
    classes = ['table']
    fdb_batch_no = Col('FDB Batch Number')
    starting_date = Col('Starting Date')
    fda = Col('FDA')
    fda_batch_no = Col('FDA Batch Number')
    chlorosulphonic_acid = Col('Chlorosulphuric Acid')
    thionyl_cholride = Col('Thionyl Chloride')
    liq_amonia = Col('Liquid Ammonia')
    sulphuric_acid = Col('Sulphuric Acid')
    wet_cake_after_csa_reaction = Col('Wet-cake after CSA Reaction')
    wet_cake = Col('Wet-Cake')
    dry_output = Col('Dry Output')
    factor = Col('Factor')

class Livo_Ester(Table):
    classes = ['table']
    fdc_batch_no = Col('FDC Batch Number')
    starting_date = Col('Starting Date')
    fdb = Col('FDB')
    fdb_batch_no = Col('FDB Batch Number')
    ok_fresh = Col('OK')
    ok_recovered = Col('OK Recoverd')
    ok_cf_ml = Col('OK CF ML')
    sulphuric_acid = Col('Sulphuric Acid')
    part_A_wet_cake = Col('Part A wet Cake')
    dmf_fresh = Col('DMF Fresh')
    dmf_recovered = Col('DMF Recoverd')
    cmf_ml_dmf = Col('CMF ML DMF')
    soda_ash = Col('Soda Ash')
    charcoal = Col('Charcoal')
    final_wet_cake = Col('Final Wet Cake')
    dry_output = Col('Dry Output')
    factor = Col('Factor')
    remarks = Col('Remarks')




