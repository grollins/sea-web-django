from parse import search

def parse_sea_output(output_str):
    output = {}
    output['gb'] = search('GB:   {:g}', output_str)[0]
    output['non_polar'] = search('Non-Polar:   {:g}', output_str)[0]
    output['reaction_field'] = search('Reaction Field:   {:g}', output_str)[0]
    output['solvent_intershell'] = search('Solvent intershell:   {:g}', output_str)[0]
    output['solvent_intrashell'] = search('Solvent intrashell:   {:g}', output_str)[0]
    output['solvent_solute'] = search('Solvent-solute:   {:g}', output_str)[0]
    output['total'] = search('Total:   {:g}', output_str)[0]
    output['sasa'] = search('SASA (nm^2):   {:g}', output_str)[0]
    output['shell_zero_waters'] = search('Shell 0 waters:   {:g}', output_str)[0]
    return output
