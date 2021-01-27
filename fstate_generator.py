import base64
import json
from os import fstat
from pathlib import Path


def _generate_fstate_base64(fstate):
    fstate_json = json.dumps(fstate, ensure_ascii=False)
    fstate_bytes = fstate_json.encode("utf-8")
    return base64.b64encode(fstate_bytes).decode()


def generate_fstate_day(BaoSRQ, cur_sheng, cur_shi, cur_qu, XiangXDZ):
    with open(Path(__file__).resolve().parent.joinpath('fstate_day.json'), encoding='utf8') as f:
        fstate = json.loads(f.read())

    with open(Path(__file__).resolve().parent.joinpath('City.json'), encoding='utf8') as f:
        city_data = json.loads(f.read())

    with open(Path(__file__).resolve().parent.joinpath('District.json'), encoding='utf8') as f:
        district_data = json.loads(f.read())

    if cur_sheng != '上海':
        fstate['p1_ShiFSH']['SelectedValue'] = '否'
        fstate['p1_ddlShi']['F_Items'] = city_data[cur_sheng]
        fstate['p1_ddlXian']['F_Items'] = district_data[cur_shi]

    fstate['p1_BaoSRQ']['Text'] = BaoSRQ
    fstate['p1_XiangXDZ']['Text'] = XiangXDZ
    fstate['p1_ddlSheng']['SelectedValueArray'] = [cur_sheng]
    fstate['p1_ddlShi']['SelectedValueArray'] = [cur_shi]
    fstate['p1_ddlXian']['SelectedValueArray'] = [cur_qu]
    print(fstate)
    fstate_base64 = _generate_fstate_base64(fstate)
    t = len(fstate_base64) // 2
    fstate_base64 = fstate_base64[:t] + 'F_STATE' + fstate_base64[t:]

    return fstate_base64


def generate_fstate_halfday(BaoSRQ):
    with open(Path(__file__).resolve().parent.joinpath('fstate_halfday.json'), encoding='utf8') as f:
        fstate = json.loads(f.read())

    fstate['p1_BaoSRQ']['Text'] = BaoSRQ

    fstate_base64 = _generate_fstate_base64(fstate)

    return fstate_base64


if __name__ == '__main__':
    print(generate_fstate_day("上报日期", "上海", "上海市", "宝山区", "上大路"))
    # print(generate_fstate_halfday())
