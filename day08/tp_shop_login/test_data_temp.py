import json
import sys


def get_data():
    with open('./test_tp_shop_data.json', encoding='utf-8') as f:
        data = json.load(f)
        data_list = []
        data_list1 = []
        for i in data.values():
            data_list.append(list(i.values()))
            data_list1.append(i.values())
        print(data_list)
        print(data_list1)
        print('data_list:', sys.getsizeof(data_list))
        print('data_list1:', sys.getsizeof(data_list1))
        return data_list


if __name__ == '__main__':
    get_data()
