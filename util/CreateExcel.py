import xlsxwriter
from util import ConstantManagement, GetAnalystsTasks

class CreateExcel:

    def __init__(self, sprint_number= None):
        self.sprint_number = sprint_number
        self.book = xlsxwriter.Workbook(ConstantManagement.EXCEL_FILE_NAME)
        self.sheet = self.book.add_worksheet()
        self.header_format = self.book.add_format({'bold': True, 'font_color': '#FFFFFF', 'bg_color': '#0B3861'})
        self.header_format.set_border()
        self.header_format.set_align('center')
        self.basic_format = self.book.add_format({'bold': False, 'font_color': '#000000', 'bg_color': '#FFFFFF'})
        self.basic_format.set_border()
        self.basic_format.set_align('center')
        self.header_format.set_align('vcenter')
        self.header_format.set_text_wrap()
        self.excel_header()
        self.submit_result_values()
        self.book.close()

    def excel_header(self):

        self.sheet.set_column(0, len(ConstantManagement.HEADER_VALUES) - 1, width=40)
        self.sheet.set_row(0, height=60)

        for header in range(0, len(ConstantManagement.HEADER_VALUES)):
            self.sheet.write(0, header, ConstantManagement.HEADER_VALUES[header], self.header_format)

    def submit_result_values(self):
        task_list_creation = GetAnalystsTasks.GetAnalystsTasks(self.sprint_number)
        task_list_creation.collect_data()
        analysts_tasks_list = task_list_creation.get_data_collection()

        for row in range(0, len(analysts_tasks_list)):
            self.sheet.write(row + 1, 0, self.sprint_number, self.basic_format)
            self.sheet.write(row + 1, 1, analysts_tasks_list[row]["analyst_name"], self.basic_format)
            self.sheet.write(row + 1, 2, analysts_tasks_list[row]["enabler_type"], self.basic_format)
            self.sheet.write(row + 1, 3, analysts_tasks_list[row]["user_story_type"], self.basic_format)
            self.sheet.write(row + 1, 4, analysts_tasks_list[row]["bug_type"], self.basic_format)
            self.sheet.write(row + 1, 5, analysts_tasks_list[row]["new_state"], self.basic_format)
            self.sheet.write(row + 1, 6, analysts_tasks_list[row]["active_state"], self.basic_format)
            self.sheet.write(row + 1, 7, analysts_tasks_list[row]["closed_state"], self.basic_format)
            self.sheet.write(row + 1, 8, analysts_tasks_list[row]["impediment_state"], self.basic_format)
            self.sheet.write(row + 1, 9, analysts_tasks_list[row]["engaged_to"], self.basic_format)
            self.sheet.write(row + 1, 10, str(analysts_tasks_list[row]["no_scored"]).strip("[]"), self.basic_format)
            self.sheet.write(row + 1, 11, analysts_tasks_list[row]["pull_data"], self.basic_format)
            self.sheet.write(row + 1, 12, analysts_tasks_list[row]["commit_data"], self.basic_format)

