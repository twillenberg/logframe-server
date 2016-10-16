import logicalframework
import output
import indicator
import assumption
import constants

import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)+"/templates"))
APP_NAME          = 'Logframe Server'
DATE_TIME         = 'Sunday, 16th October, 2016'
URL_CSS           = 'css/default.css'
URL_IMG           = 'img/logo.neocapita.png'

class Welcome(webapp2.RequestHandler):
    def get(self):
        # Define the HTTP headers.
        self.response.headers['Content-Type'] = 'text/html'

        # Obtain the template from the Jinja environment.
        env = JINJA_ENVIRONMENT
        template = env.get_template('default.html')
        app_name = 'Logframe Server'
        date_time = 'Sunday, 16th October 2016'
        url = '/css/default.css'
        output = template.render(app_name=app_name, date_time=date_time, url=url)
        
        # Output the rendered template.
        self.response.write(output)        

'''
class Controller:
    lf = LogicalFramework()

    def __init__(self, lf):
        self.lf = lf

    def set_impact(self, impact_statement):
        self.lf.set_impact(impact_statement)

    def add_impact_indicator(self, ind):
        self.lf.add_impact_indicator(ind)

    def set_outcome(self, outcome_statement):
        self.lf.set_outcome(outcome_statement)
    def add_outcome_indicator(self,ind):
        self.lf.add_outcome_indicator(ind)

    def add_impact_assumption(self,assumption):
        self.lf.impact.add_assumption(assumption)

    def add_outcome_assumption(self,assumption):
        self.lf.outcome.add_assumption(assumption)

    def set_outputs():
        """ Builds the logical framework object heirarchy. """

        # Creating output 1 ######################################################
        output1 = Output(1, 'Macro-fiscal analysis is comprehensive in scope and is communicated in a timely manner to senior management.', 2)

        indicator1_1 = Indicator(1.1,
                                "Comprehensiveness of Medium-Term Fiscal Framework document.",
                                "Medium-Term Fiscal Framework is updated 1-2 times each year. It is not comprehensive and does not include a relevant sensitivity analysis.",
                                "Medium-Term Fiscal Framework updated and improved to inform 'soft ceilings' prior to Budget Circular 1.")
        output1.add_indicator(indicator1_1)

        indicator1_2 = Indicator(1.2,
                                "Availability of fiscal information to internal and external stakeholders.",
                                "Fiscal reports are produced on a monthly, quarterly and annual basis. Policy briefs are provided on an ad hoc basis.",
                                "(i) Fiscal Policy Department  website improved to include downloadable tables of key fiscal data (see note 4); and (ii) Fiscal Policy Department produces 2 thematic presentations and policy notes relevant to Budget Circular 1 (see note 5).")
        output1.add_indicator(indicator1_2)

        assumption1_1 = Assumption(assumption_level.OUTPUT, 1, "Availability of data from donors and Resolute Support Mission")
        assumption1_2 = Assumption(assumption_level.OUTPUT, 2, "Willingness of Fiscal Policy Department staff to engage with Ministry of Finance leadership on key issues")
        assumption1_3 = Assumption(assumption_level.OUTPUT, 3, "Operations & Maintenance data is available to Fiscal Policy Department")
        assumption1_4 = Assumption(assumption_level.OUTPUT, 4, "Engagement of pilot line ministries in Operations & Maintenance work")
        assumption1_5 = Assumption(assumption_level.OUTPUT, 5, "Reform minded counterparts retained by Ministry of Finance.")
        assumption1_6 = Assumption(assumption_level.OUTPUT, 6, "Fiscal Policy Department is adequately staff resourced to ensure core functions can be carried out.")
        assumption1_7 = Assumption(assumption_level.OUTPUT, 7, "Willingness of Ministry of Finance leadership to engage Fiscal Policy Department on key issues.")
        assumption1_8 = Assumption(assumption_level.OUTPUT, 8, "Ministry of Finance leadership maintains its leadership on the issue of 'soft' and 'hard' ceilings.")
        output1.add_assumption(assumption1_1)
        output1.add_assumption(assumption1_2)
        output1.add_assumption(assumption1_3)
        output1.add_assumption(assumption1_4)
        output1.add_assumption(assumption1_5)
        output1.add_assumption(assumption1_6)
        output1.add_assumption(assumption1_7)
        output1.add_assumption(assumption1_8)
        lf.add_output(output1)

        # Creating output 2 ######################################################
        output2 = Output(2, 'Key reforms are implemented in the Budget Department allowing allocation of resources in line with the Government priorities and effective service delivery.', 5)
        indicator2_1 = Indicator(2.1,
                                "Capacity of selected budgetary unit program managers to implement the revised program budgeting guidance on applying program budgeting processes and systems (including its application to O&M and at the provincial level).",
                                "The program budgeting guidance has not been revised.",
                                "(i)  The Directorate Geenral Budget's PFMR-II provincial budgeting implementation targets are achieved; and(ii) Program budgeting training strategy is being implemented.")

        indicator2_2 = Indicator(2.2,
                                "Ministries implement the 'Performance Criteria' defined in the GIRoA's O&M policy.",
                                "Ministry of Education (schools) and Ministry of Public Health (central hospitals only) calculated Operations & Maintenance cost based on norms and integrated it into their Budget Circular 2 budget submission.",
                                "Health and Education sectors medium-term Operations & Maintenance requirements estimated and included in Budget Circular 1 'soft ceilings' (see note 1 & 5).")

        indicator2_3 = Indicator(2.3,
                                "Directorate General of Budget and budgetary unit capacity to facilitate Budget Committee to undertake the annual budget hearing based on national development plan priorities and program performance information.",
                                "Baseline will be established on the activation date of this log frame, using the 'Structured Interview between the Strengthening Afghanistan's Budget II and the Directorate General Budget' tool.",
                                "Directorate General of Budget has access to one additional key tool the (Budgetary Unit Budget Committee template tool) for justification of capital pipeline requests.")

        indicator2_4 = Indicator(2.4,
                                "Capacity of selected budgetary unit program managers to implement the revised program budgeting guidance on applying program budgeting processes and systems (including its application to O&M and at the provincial level).",
                                "The program budgeting guidance has not been revised.",
                                "(i)  The Directorate Geenral Budget's PFMR-II provincial budgeting implementation targets are achieved; and(ii) Program budgeting training strategy is being implemented.")

        indicator2_5 = Indicator(2.5,
                                "Capacity of selected budgetary unit program managers to implement the revised program budgeting guidance on applying program budgeting processes and systems (including its application to O&M and at the provincial level).",
                                "The program budgeting guidance has not been revised.",
                                "(i)  The Directorate Geenral Budget's PFMR-II provincial budgeting implementation targets are achieved; and(ii) Program budgeting training strategy is being implemented.")
        output2.add_indicator(indicator2_1)
        output2.add_indicator(indicator2_2)
        output2.add_indicator(indicator2_3)
        output2.add_indicator(indicator2_4)
        output2.add_indicator(indicator2_5)

        assumption2_1 = Assumption(assumption_level.OUTPUT, 1, "Common and integrated approach to implementing the program budgeting reform")
        assumption2_2 = Assumption(assumption_level.OUTPUT, 2, "That the Ministry of Finance led capacity-building program leads to Budgetary Units successfully adopting budget reforms")
        assumption2_3 = Assumption(assumption_level.OUTPUT, 3, "That Directorate General of Budget and Budgetary Units have the resources to implement the budget reforms")
        assumption2_4 = Assumption(assumption_level.OUTPUT, 4, "That budget reforms will be actively supported by Ministry of Finance and Budget Unit senior management")
        assumption2_5 = Assumption(assumption_level.OUTPUT, 5, "That the creation of capacity in Ministry of Finance and Budgetary Units is not lost through staff attrition")
        assumption2_6 = Assumption(assumption_level.OUTPUT, 6, "That willing and reform- minded donor partners exist")
        assumption2_7 = Assumption(assumption_level.OUTPUT, 7, "That Ministry of Finance will actively hold Budgetary Units to account to implement the reforms")
        assumption2_8 = Assumption(assumption_level.OUTPUT, 8, "Willingness of the Budget Committee to consider new processes for conduct of the budget hearings")
        assumption2_9 = Assumption(assumption_level.OUTPUT, 9, "Program Budgeting Roadmap endorsed and included in the Public Financial Management Roadmap II")
        assumption2_10 = Assumption(assumption_level.OUTPUT, 10, "Provincial budget policy and program budgeting policy endorsed by the Cabinet")
        assumption2_11 = Assumption(assumption_level.OUTPUT, 11, "Operations & Maintenance Policy is endorsed by the Cabinet")
        assumption2_12 = Assumption(assumption_level.OUTPUT, 12, "Sufficient funding is provided to Budget Units under the Afghanistan Reconstruction Trust Fund Incentive Program in order to enable the rollout of the Operations & Maintenance Policy")
        assumption2_13 = Assumption(assumption_level.OUTPUT, 13, "Implementation of the Operations & Maintenance Policy is included in the Public Financial Management Roadmap II")
        assumption2_14 = Assumption(assumption_level.OUTPUT, 14, "Directorate General Budget and Budget Units have sufficient resourcing to implement the Operations & Maintenance Policy")
        assumption2_15 = Assumption(assumption_level.OUTPUT, 15, "Provincial Budgeting Policy approved by Cabinet")
        assumption2_16 = Assumption(assumption_level.OUTPUT, 16, "Government is committed to the development and implementation of the Public Financial Management Roadmap II")

        output2.add_assumption(assumption2_1)
        output2.add_assumption(assumption2_2)
        output2.add_assumption(assumption2_3)
        output2.add_assumption(assumption2_4)
        output2.add_assumption(assumption2_5)
        output2.add_assumption(assumption2_6)
        output2.add_assumption(assumption2_7)
        output2.add_assumption(assumption2_8)
        output2.add_assumption(assumption2_9)
        output2.add_assumption(assumption2_10)
        output2.add_assumption(assumption2_11)
        output2.add_assumption(assumption2_12)
        output2.add_assumption(assumption2_13)
        output2.add_assumption(assumption2_14)
        output2.add_assumption(assumption2_15)
        output2.add_assumption(assumption2_16)
        lf.add_output(output2)

        # Creating output 3 ######################################################
        output3 = Output(3, 'Strengthened institutional tools, systems and processes for better management of budget execution and cash management.', 2)
        indicator3_1 = Indicator(3.1,
                                "Capacity of selected budgetary unit program managers to implement the revised program budgeting guidance on applying program budgeting processes and systems (including its application to O&M and at the provincial level).",
                                "The program budgeting guidance has not been revised.",
                                "(i)  The Directorate Geenral Budget's PFMR-II provincial budgeting implementation targets are achieved; and(ii) Program budgeting training strategy is being implemented.")
        indicator3_2 = Indicator(3.2,
                                "Capacity of selected budgetary unit program managers to implement the revised program budgeting guidance on applying program budgeting processes and systems (including its application to O&M and at the provincial level).",
                                "The program budgeting guidance has not been revised.",
                                "(i)  The Directorate Geenral Budget's PFMR-II provincial budgeting implementation targets are achieved; and(ii) Program budgeting training strategy is being implemented.")
        output3.add_indicator(indicator3_1)
        output3.add_indicator(indicator3_2)
        lf.add_output(output3)

        # Creating output 4 ######################################################
        output4 = Output(4, 'Increased capacity of GIRoA to manage aid effectively and efficiently.', 2)
        lf.add_output(output4)

        # Creating output 5 ######################################################
        output5 = Output(5, 'Government planning and performance monitoring systems strengthened to enable improved national budget efficiency and effectiveness.', 2)
        assumption3_1 = Assumption(assumption_level.OUTPUT, 1, "Assuming that DFID support is sustained.")
        output3.add_assumption(assumption3_1)
        lf.add_output(output5)


    def display_lower():
        lf.number_of_outputs()
        lf.display_outputs()


    def display():
        # Clear the terminal output.
        os.system('cls' if os.name == 'nt' else 'clear')

        # Display the high-level statements for the log frame.
        self.lf.display_version()

        self.lf.display_impact()
        self.lf.impact.number_of_assumptions()
        self.lf.impact.display_assumptions()
        self.lf.separate()

        self.lf.display_outcome()
        self.lf.outcome.number_of_assumptions()
        self.lf.outcome.display_assumptions()
        self.lf.separate()

        set_outputs()
        display_lower()

class Create(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Reading Logframe...')

        # Create the log frame object.
        lf = LogicalFramework("Strengthening Afghanistan's Budget II", 5.03)
        ctrler = Controller(lf)

        # Set the high-level statements for the logframe.
        ctrler.set_impact("The GIRoA can effectively manage resources in support of economic growth and to improve the lives of the Afghan people.")
        ctrler.set_outcome("Transparent and well functioning GIRoA budget process.")

        # Create and add high-level indicators for the logframe.
        imp_ind = Indicator(1, "GDP Growth", 0, 5)
        ctrler.add_impact_indicator(imp_ind)
        oc_ind = Indicator(2, "Transparency Index", 21, 27)
        ctrler.add_outcome_indicator(oc_ind)

        # Add assumptions for the logframe.
        impact_assumption1 = Assumption(assumption_level.IMPACT, 1, "Assuming the Government wishes to make public financial management reforms")
        outcome_assumption1 = Assumption(assumption_level.OUTCOME, 1, "Assuming the Government assigns qualified staff to the team")
        ctrler.add_impact_assumption(impact_assumption1)
        ctrler.add_outcome_assumption(outcome_assumption1)

        ctrler.display
'''

app = webapp2.WSGIApplication([
    ('/', Welcome),
    ('/welcome', Welcome)
], debug=True)
