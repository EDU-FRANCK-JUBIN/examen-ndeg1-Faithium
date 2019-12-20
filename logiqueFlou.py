# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 11:02:31 2019

@author: ilias
"""

from skfuzzy import control as ctrl
import skfuzzy as fuzz
import numpy as np

error = ctrl.Antecedent(np.arange(-4, 5, 1), 'error')
error_dot = ctrl.Antecedent(np.arange(-10, 11, 1), 'error_dot')
percent_output = ctrl.Consequent(np.arange(-100, 101, 1), 'percent_output')

error_names = ['TooHot', 'JustRight', 'TooCold']
error_dot_names = ['GettingHot', 'NoChange', 'GettingCold']

error.automf(names=error_names)
error_dot.automf(names=error_dot_names)

error.view()
error_dot.view()

percent_output['cool'] = fuzz.trimf(percent_output.universe, [-100, -50, 0])
percent_output['do_nothing'] = fuzz.trimf(percent_output.universe, [-50, 0, 50])
percent_output['heat'] = fuzz.trimf(percent_output.universe, [0, 50, 100])

percent_output.view()

rule1 = ctrl.Rule(error['TooHot'] & error_dot['GettingHot'], percent_output['cool'])
rule2 = ctrl.Rule(error['TooHot'] & error_dot['NoChange'], percent_output['cool'])
rule3 = ctrl.Rule(error['TooHot'] & error_dot['GettingCold'], percent_output['cool'])
rule4 = ctrl.Rule(error['JustRight'] & error_dot['GettingHot'], percent_output['cool'])
rule5 = ctrl.Rule(error['JustRight'] & error_dot['NoChange'], percent_output['do_nothing'])
rule6 = ctrl.Rule(error['JustRight'] & error_dot['GettingCold'], percent_output['heat'])
rule7 = ctrl.Rule(error['TooCold'] & error_dot['GettingHot'], percent_output['heat'])
rule8 = ctrl.Rule(error['TooCold'] & error_dot['NoChange'], percent_output['heat'])
rule9 = ctrl.Rule(error['TooCold'] & error_dot['GettingCold'], percent_output['heat'])

outputing_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
outputing = ctrl.ControlSystemSimulation(outputing_ctrl)

outputing.input['error'] = -1
outputing.input['error_dot'] = -4

outputing.compute()

percent_output.view(sim=outputing)

outputing.input['error'] = -1.5
outputing.input['error_dot'] = -1

outputing.compute()

percent_output.view(sim=outputing)

outputing.input['error'] = 0.5
outputing.input['error_dot'] = 1

outputing.compute()

percent_output.view(sim=outputing)

outputing.input['error'] = 0.5
outputing.input['error_dot'] = 4

outputing.compute()

percent_output.view(sim=outputing)