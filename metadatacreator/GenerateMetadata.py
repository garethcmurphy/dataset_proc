#!/usr/bin/env python3
import datetime
import json
import os
import re
import socket
import sys

from sortedcontainers import SortedDict

from dataset import Dataset
from instrument import Instrument
from orig import Orig


class GenerateMetadata:
    def __init__(self):
        self.mydir = "./data"
        #        self.mydir = "./static"
        self.year_month_regex = '20[0-9]{2}_[0-1][0-9]'
        self.hostname = socket.gethostname()
        if self.hostname == 'login.esss.dk':
            # self.mydir = "/users/detector/experiments/multiblade/data/brightness"
            self.mydir = "/users/detector/experiments"

    def generate(self):

        data_sets = SortedDict()
        i = 0
        experiments = ['sonde', 'nmx', 'multigrid', 'multiblade']
        experiment_date_time = str(datetime.datetime(2018, 1, 1))

        for i in range(0, 4):
            print(i)
            experiment = experiments[i]
            print(experiment)

            d = Dataset()
            new_inst = Instrument()
            inst = new_inst.factory(experiment)
            my_data_set = d.dataset
            print(inst.abbreviation)
            my_data_set.update(inst.inst)
            my_data_set["pid"] = '10.17199/BRIGHTNESS/' + inst.abbreviation + str(1).zfill(4)
            print(my_data_set["pid"])
            file_list = []
            total_file_size = 0

            filenum = 0
            filenames = [
                'data/experiments/multiblade/data/brightness/2017_10_ISIS_MB16S_ReflectometryAtCRISP/06_4_R2_Efficiency_25Hz/2017_10_06_1601_DigNo34_R2_Efficiency25Hz_He3_000.lst1']
            for file in filenames:
                filenum += 1
                longname = file
                basename = 'test_base_name'

                stat_info = os.stat(longname)
                rel_path = longname.replace('/users/detector', '/static')
                file_size = stat_info.st_size
                total_file_size += file_size
                file_entry = {
                    "path": rel_path,
                    "size": file_size,
                    "time": experiment_date_time,
                    "chk": "string",
                    "uid": "string",
                    "gid": "string",
                    "perm": "string"
                }
                if filenum < 100000:
                    file_list.append(file_entry)
            my_data_set["size"] = total_file_size
            my_data_set["packedSize"] = total_file_size
            my_data_set["creationTime"] = experiment_date_time
            my_data_set["endTime"] = experiment_date_time
            my_data_set["createdAt"] = experiment_date_time
            my_data_set["updatedAt"] = experiment_date_time
            my_data_set["doi"] = "10.17199/" + str(my_data_set["pid"])
            scientific_metadata = {
                "identifier": basename
            }
            my_data_set["scientificMetadata"] = scientific_metadata
            orig = Orig()
            my_orig = orig.orig
            my_orig["datasetId"] = str(my_data_set["pid"])
            my_orig["dataFileList"] = file_list
            my_orig["size"] = total_file_size
            my_orig["createdAt"] = experiment_date_time
            my_orig["updatedAt"] = experiment_date_time

            scicat_entries = {"dataset": my_data_set, "orig": my_orig}
            data_sets["orig" + experiment_date_time + str(i).zfill(5)] = scicat_entries

        json.dump(data_sets, sys.stdout, indent=2)

        with open('test_new_metadata.json', 'w') as f:
            json.dump(data_sets, f, ensure_ascii=False, indent=2)

    def get_experiment_info(dirpath):
        experiment = 'ess'
        sonderegex = 'sonde'
        multigridregex = 'multigrid'
        multibladeregex = 'multiblade'
        nmxregex = 'nmx'
        v20regex = 'V20'
        iferegex = 'IFE'
        hzbregex = 'HZB'
        essregex = 'ESS'

        search_result = re.search(v20regex, dirpath, re.IGNORECASE)
        if search_result:
            experiment = 'v20'

        search_result = re.search(essregex, dirpath, re.IGNORECASE)
        if search_result:
            experiment = 'ess'

        search_result = re.search(hzbregex, dirpath, re.IGNORECASE)
        if search_result:
            experiment = 'hzb'

        search_result = re.search(iferegex, dirpath, re.IGNORECASE)
        if search_result:
            experiment = 'ife'

        search_result = re.search(sonderegex, dirpath, re.IGNORECASE)
        if search_result:
            experiment = 'sonde'

        search_result = re.search(multigridregex, dirpath, re.IGNORECASE)
        if search_result:
            experiment = 'multigrid'

        search_result = re.search(multibladeregex, dirpath, re.IGNORECASE)
        if search_result:
            experiment = 'multiblade'

        search_result = re.search(nmxregex, dirpath, re.IGNORECASE)
        if search_result:
            experiment = 'nmx'

        return experiment

    get_experiment_info = staticmethod(get_experiment_info)

    def get_date_information(self, basename, dirpath):
        year_month = "2018_01"
        search_result = re.search(self.year_month_regex, dirpath)
        if search_result:
            year_month = search_result.group(0)
        # print('gm',year_month)
        year = year_month[0:4]
        month = year_month[5:7]
        day = 1
        if re.match('[0-3][0-9]', basename):
            day1 = int(basename[0:2])
            if day1 >= 1:
                day = int(basename[0:2])
        print(year, month, day)
        data_date = datetime.datetime(int(year), int(month), int(day))
        experiment_date_time = data_date.isoformat()
        return experiment_date_time


if __name__ == '__main__':
    g = GenerateMetadata()
    g.generate()
