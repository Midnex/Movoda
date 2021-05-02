import csv
from os import name
from dearpygui.core import *
from dearpygui.simple import *
import sys

ver = 0.2

def convertFile(directory, file):
    with open(f"{directory}\\_conv{file.upper()}", "w") as w:
        w.write("ref,split,sku,qty,status,transType,shipTo,customer\n")
        with open(f"{directory}\\{file}", "r") as f:
            for line in csv.DictReader(f):
                if 'AllocationStatus' in line.keys():
                    orgRef = line['ReferenceNum'].split('-')[0]
                    split = line['ReferenceNum']
                    status = line['AllocationStatus']
                    skuList = line['SkuAndQty']
                    transType = 'Order'
                    shipTo = line['ShipToCompany']
                    customer = ''
                elif 'StatusEnum' in line.keys():
                    orgRef = line['ReferenceNum']
                    split = ''
                    status = line['StatusEnum']
                    skuList = line['Skus']
                    transType = 'Receipt'
                    shipTo = 'OISI'
                    customer = line['Customer']
                else:
                    print(f"{file} does not contain AllocationStatus or StatusEnum fields\nField(s) are required to process.")
                    break
                if orgRef == "" or status == 'No Line Items' or status == 'Canceled':
                    pass
                else:
                    for item in skuList.split(","):
                        sku = item.split("(")[0]
                        qty = item.split("(")[1].replace(")","")
                        w.write(f"{orgRef},{split},{sku},{qty},{status},{transType},{shipTo},{customer}\n")
    sys.exit()

def file(sender, data):
    open_file_dialog(callback=apply_selected_file, extensions=".csv")

def apply_selected_file(sender, data):
    directory = data[0]
    filename = data[1]
    set_value("file", filename)
    convertFile(directory, filename)

def main():
    set_main_window_size(600, 650)
    set_main_window_resizable(False)
    set_main_window_title(f"OrderGridExport Split v{ver}")
    with window("main"):
        file("main",None)
        add_text("File: ")
        add_same_line()
        add_label_text("##file", source="file", color=[255, 0, 0])
    start_dearpygui(primary_window="main")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file = sys.argv[1]
        convertFile(file)
    else:
        main()