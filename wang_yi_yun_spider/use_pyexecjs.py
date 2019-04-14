#Author:xue yi yang
import execjs
def get_mima(data1,data2):
    info =""
    with open("text_CryptoJS_xyy.js","r",encoding="utf-8") as f:
        writ = f.read()
        info =writ
    ctx = execjs.eval( info + """
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b),
        d = CryptoJS.enc.Utf8.parse("0102030405060708"),
        e = CryptoJS.enc.Utf8.parse(a),
        f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    """)
    return ctx
if __name__ == '__main__':
    j = get_mima("x","y")
    print(j)