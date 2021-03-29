from PyQt5 import QtCore, QtGui, QtWidgets
from interface import Ui_MainWindow
import data_query
import sys
import json
import mysql.connector
import pandas as pd

def initialise():
    df_tables = data_query.get_table()
    df_all = data_query.get_all()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # set table1 combo
    for table in df_tables:
        ui.table_combo1.addItem(table)

    # set table2 combo
    ui.table_combo2.addItem("None")
    for table in df_tables:
        ui.table_combo2.addItem(table)

    # set join combo
    ui.join_combo.addItem("LEFT JOIN")
    ui.join_combo.addItem("RIGHT JOIN")
    ui.join_combo.addItem("INNER JOIN")
    ui.join_combo.addItem("OUTER JOIN")

    # set date combo
    for col in df_all.columns:
      ui.time_combo.addItem(col)
    # set filter combo
    ui.filter_combo.addItem("None")
    for col in df_all.columns:
      ui.filter_combo.addItem(col)

    # set operator combo
    ui.operator_combo.addItem("=")
    ui.operator_combo.addItem("!=")
    ui.operator_combo.addItem(">")
    ui.operator_combo.addItem("<")
    ui.operator_combo.addItem(">=")
    ui.operator_combo.addItem("<=")

    # set group by column
    ui.by_col_combo.addItem("None")
    for col in df_all.columns:
      ui.by_col_combo.addItem(col)
    # set aggregate column
    ui.agg_col_combo.addItem("None")
    for col in df_all.columns:
      ui.agg_col_combo.addItem(col)
    # set aggregate function
    ui.agg_func_combo.addItem("None")
    ui.agg_func_combo.addItem("COUNT")
    ui.agg_func_combo.addItem("SUM")
    ui.agg_func_combo.addItem("AVG")
    ui.agg_func_combo.addItem("MAX")
    ui.agg_func_combo.addItem("MIN")

    def add_tables(self):
        table1 = self.table_combo1.currentText()
        table2 = self.table_combo2.currentText()
        if table2 == "None":
            self.table_list.addItem(table1)

    def generates(self):
        table_list = data_query.get_table()

    def add_filters(self):
        oth_filter = self.filter_combo.currentText()
        operator = self.operator_combo.currentText()
        comparison = self.compare_text.toPlainText()
        if oth_filter != "None":
            self.filter_list.addItem(oth_filter + operator + comparison)

    def clear_filters(self):
        self.filter_list.takeItem(self.filter_list.row(self.filter_list.selectedItems()[0]))

    def querys(self):
        date_col = self.time_combo.currentText()
        start_date = self.from_combo.date().toString("yyyy-MM-dd")
        end_date = self.to_combo.date().toString("yyyy-MM-dd")
        groupCol = self.by_col_combo.currentText()
        aggCol = self.agg_col_combo.currentText()
        aggFunc = self.agg_func_combo.currentText()
        filters_count = self.filter_list.count()
        filters_items = [self.filter_list.item(i).text() for i in range(filters_count)]

        filters_clause = " AND ".join(filters_items)

        global df_query

        df_query = data_query.get_filters(filters_clause, filters_count, aggFunc, aggCol, start_date, end_date, groupCol)
        print(df_query)

    def exports(self):
        df_query.to_csv("data.csv")

    def records(self):
        date_col = self.time_combo.currentText()
        start_date = self.from_combo.date().toString("yyyy-MM-dd")
        end_date = self.to_combo.date().toString("yyyy-MM-dd")
        groupCol = self.by_col_combo.currentText()
        aggCol = self.agg_col_combo.currentText()
        aggFunc = self.agg_func_combo.currentText()
        filters_count = self.filter_list.count()
        filters_items = [self.filter_list.item(i).text() for i in range(filters_count)]

        record_dict = {
            "date_col": date_col,
            "start_date": start_date,
            "end_date": end_date,
            "groupCol": groupCol,
            "aggCol": aggCol,
            "aggFunc": aggFunc,
            "filters": filters_items
        }

        with open('record.json', 'w') as json_file:
            json.dump(record_dict, json_file)


    ui.add_table = add_tables.__get__(ui)
    ui.generate = generates.__get__(ui)
    ui.add_filter = add_filters.__get__(ui)
    ui.clear_filter = clear_filters.__get__(ui)
    ui.query = querys.__get__(ui)
    ui.export = exports.__get__(ui)
    ui.record = records.__get__(ui)

    # add_table button
    ui.table_add.clicked.connect(ui.add_table)
    # generate button
    ui.generate_button.clicked.connect(ui.generate)
    # add_filter button
    ui.add_button.clicked.connect(ui.add_filter)
    # clear button
    ui.clear_button.clicked.connect(ui.clear_filter)
    # query button
    ui.query_button.clicked.connect(ui.query)
    # export button
    ui.export_button.clicked.connect(ui.export)
    # record button
    ui.record_button.clicked.connect(ui.record)





    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    initialise()
