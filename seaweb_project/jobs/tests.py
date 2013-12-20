from unittest import TestCase
from .parser import parse_sea_output

SEA_OUTPUT = """
Warning: couldn't find the GMXLIB environment variable
Reading file "/Users/grollins/SEA/examples/methane.top"
Including all atoms

Energies (kcal/mol):
                  GB:   -0.000
           Non-Polar:    2.073
      Reaction Field:   -0.001
  Solvent intershell:    0.000
  Solvent intrashell:    0.012
      Solvent-solute:   -0.021
               Total:    2.063

Other Statistics:
         SASA (nm^2):    1.643
      Shell 0 waters:   13.389
"""

class ParserTest(TestCase):
    def test_parse_sea_output(self):
        output = parse_sea_output(SEA_OUTPUT)
        self.assertEqual(output['gb'], -0.0)
        self.assertEqual(output['non_polar'], 2.073)
        self.assertEqual(output['reaction_field'], -0.001)
        self.assertEqual(output['solvent_intershell'], 0.0)
        self.assertEqual(output['solvent_intrashell'], 0.012)
        self.assertEqual(output['solvent_solute'], -0.021)
        self.assertEqual(output['total'], 2.063)
        self.assertEqual(output['sasa'], 1.643)
        self.assertEqual(output['shell_zero_waters'], 13.389)
