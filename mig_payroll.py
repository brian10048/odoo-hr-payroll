def migrate_rule_name(rule_id):
    main = env.ref(rule_id)
    old_2017 = env.ref(rule_id.replace('2018', '2017'))
    old_2016 = env.ref(rule_id.replace('2018', '2016'))
    lines = env['hr.payslip.line'].search([('salary_rule_id', 'in', [old_2017.id, old_2016.id,])])
    lines.write({'salary_rule_id': main.id})

rules = [
    'l10n_us_hr_payroll.hr_payroll_rules_fica_emp_ss_wages_2018',
    'l10n_us_hr_payroll.hr_payroll_rules_fica_emp_m_wages_2018',
    'l10n_us_hr_payroll.hr_payroll_rules_fica_emp_m_add_wages_2018',
    'l10n_us_hr_payroll.hr_payroll_rules_fica_emp_ss_2018',
    'l10n_us_hr_payroll.hr_payroll_rules_fica_emp_m_2018',
    'l10n_us_hr_payroll.hr_payroll_rules_fica_emp_m_add_2018',
    'l10n_us_hr_payroll.hr_payroll_rules_fed_inc_withhold_2018_single',
    'l10n_us_hr_payroll.hr_payroll_rules_fed_inc_withhold_2018_married',
    'l10n_us_hr_payroll.hr_payroll_rules_futa_wages_2018',
    'l10n_us_hr_payroll.hr_payroll_rules_futa_2018',
]
for rule_id in rules:
    migrate_rule_name(rule_id)

env.cr.commit()
