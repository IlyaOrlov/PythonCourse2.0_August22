import os
import qrcode
import re


def txt_to_qrcode(txt, qr_filepath, qr_filetype='JPEG'):
    qr = qrcode.QRCode(version=1, box_size=2, border=4)
    qr.add_data(txt)
    qr.make(fit=True)
    img = qr.make_image()
    img_file = open(qr_filepath, 'wb')
    img.save(img_file, qr_filetype)
    img_file.close()


if __name__ == '__main__':
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    path_to_qr = os.path.join(cur_dir, 'qr_output.jpg')

    with open('реквизиты.txt', encoding='utf-8') as file:
        txt = file.read()
    lst = txt.split("\n\n\n")

    lst1 = []
    lst2 = []
    for i in lst[1].split("\n"):
        lst1.append(re.sub(r'.+: *', '', i))
    for i in lst[2].split("\n"):
        lst2.append(re.sub(r'.+: *', '', i).strip("'"))
    d = dict(zip(lst2, lst1))

    lst0 = re.sub(r"' \\\n +'", '', lst[0])
    pat = lst0.replace("pattern = ", "").strip("'|").split('|')
    for i in range(len(pat)):
        if pat[i].find('=') != -1:
            n = pat[i].split("=")
            if n[1] in d:
                n[1] = d.get(n[1])
            pat[i] = n[0] + '=' + n[1]
        else:
            n = pat[i].split('_')
            for j, k in enumerate(n):
                val = "_" + k
                if val in d:
                    n[j] = d.get(val)
            pat[i] = "".join(n)

    pattern = ""
    for i in pat:
        pattern += (i + "|")

    txt_to_qrcode(pattern, path_to_qr)
    print(path_to_qr)