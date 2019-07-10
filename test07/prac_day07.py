import json


def test01():
    json_data = ''' {
        "name": "rain",
        "age": 19,
        "school": null,
        "address": {
            "city": "上海",
            "area": "浦东"
        },
        "number": [
            1,
            2,
            3
        ],
        "is_man": false
    }'''

    dict_data = json.loads(json_data)
    print(dict_data)
    print('*' * 30)
    dict_data1 = {'name': 'rain', 'age': 19, 'school': None, 'address': {'city': '上海', 'area': '浦东'},
                  'number': [1, 2, 3], 'is_man': False}
    json_data1 = json.dumps(dict_data)
    print(json_data1)


def test02():
    with open('./test_json.json', encoding='utf-8') as f:
        data = json.load(f)
        print(data)

    print('-' * 30)
    dict_data1 = {'name': 'rain', 'age': 19, 'school': None, 'address': {'city': '上海', 'area': '浦东'},
                  'number': [1, 2, 3], 'is_man': False}
    with open('./test_json01.json', 'w', encoding='utf-8') as f:
        json.dump(dict_data1, f)


if __name__ == '__main__':
    test02()
