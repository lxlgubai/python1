import requests
import re
from tqdm import tqdm

url='https://vd6.l.qq.com/proxyhttp'
data={"buid":"vinfoad","vinfoparam":"charge=0&otype=ojson&defnpayver=3&spau=1&spaudio=0&spwm=1&sphls=2&host=v.qq.com&refer=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc00200rblzjix%2Ff0036v9knzd.html&ehost=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc00200rblzjix%2Ff0036v9knzd.html&sphttps=1&encryptVer=8.1&cKey=199DDE2606AA3152539BA769A42EBE05FA9368EDC93AE7DA561B1568DD0F787ECC0D7697C5DBFB52518F5C10897C79DA772E5112834908811E0158D9FC4AAA92948BE0B7DBA12E50891B0F0916B77649326DC5A812072C3BA141B43B975DDBC94A3A57BB7897F7B6CF5B8B0A065C06D3DB18C4434639890839F7CAF0ADB5B9F8703810AD8BEB14C13A4145B130F7CC87998D656041C1439A656BB9B2FC1391FD234DC9DC13EB349B3AA58D312C816D66FF6B158B7720C1CED69D2000CDBA7D9440D36869ADD58BB76FD078D86F1C04389903F26C89663461BCA6F4BCA2C5F0B7D33C32BB4058CC2407DFD8386DBA0BC7&clip=4&guid=bad33cb44f5e41c5&flowid=b620e6291c43c75a456512981ceeb8ad&platform=10201&sdtfrom=v1010&appVer=3.5.57&unid=&auth_from=&auth_ext=&vid=f0036v9knzd&defn=fhd&fhdswitch=0&dtype=3&spsrt=2&tm=1672107020&lang_code=0&logintoken=%7B%22access_token%22%3A%22956891D2553368A08A8B490FBADD0C80%22%2C%22appid%22%3A%22101483052%22%2C%22vusession%22%3A%22ALQu4fEy6884H6auHNIK1g.N%22%2C%22openid%22%3A%229EBA29BC41440AA10A0FFD15E22951C7%22%2C%22vuserid%22%3A%22808783151%22%2C%22video_guid%22%3A%22bad33cb44f5e41c5%22%2C%22main_login%22%3A%22qq%22%7D&spvvpay=1&spadseg=3&spav1=15&spsfrhdr=0&spvideo=0&spm3u8tag=67&spmasterm3u8=3&drm=40","sspAdParam":"{\"ad_scene\":1,\"pre_ad_params\":{\"ad_scene\":1,\"user_type\":1,\"video\":{\"base\":{\"vid\":\"f0036v9knzd\",\"cid\":\"mzc00200rblzjix\"},\"is_live\":false,\"type_id\":1,\"referer\":\"https://v.qq.com/channel/movie\",\"url\":\"https://v.qq.com/x/cover/mzc00200rblzjix/f0036v9knzd.html\",\"flow_id\":\"b620e6291c43c75a456512981ceeb8ad\",\"refresh_id\":\"ac6a56ed4f2010c05904ff27e5cc45dd_1672106996\"},\"platform\":{\"guid\":\"bad33cb44f5e41c5\",\"channel_id\":0,\"site\":\"web\",\"platform\":\"in\",\"from\":0,\"device\":\"pc\",\"play_platform\":10201,\"pv_tag\":\"www_baidu_com|channel\"},\"player\":{\"version\":\"1.13.15\",\"plugin\":\"1.15.22\",\"switch\":1,\"play_type\":\"0\",\"img_type\":\"webp\"},\"token\":{\"type\":1,\"vuid\":808783151,\"vuser_session\":\"ALQu4fEy6884H6auHNIK1g.N\",\"app_id\":\"101483052\",\"open_id\":\"9EBA29BC41440AA10A0FFD15E22951C7\",\"access_token\":\"956891D2553368A08A8B490FBADD0C80\"}}}","adparam":"pf=in&pf_ex=pc&pu=1&pt=0&platform=10201&from=0&flowid=b620e6291c43c75a456512981ceeb8ad&guid=bad33cb44f5e41c5&coverid=mzc00200rblzjix&vid=f0036v9knzd&chid=0&tpid=1&refer=https%3A%2F%2Fv.qq.com%2Fchannel%2Fmovie&url=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc00200rblzjix%2Ff0036v9knzd.html&lt=qq&opid=9EBA29BC41440AA10A0FFD15E22951C7&atkn=956891D2553368A08A8B490FBADD0C80&appid=101483052&uid=808783151&tkn=ALQu4fEy6884H6auHNIK1g.N&rfid=ac6a56ed4f2010c05904ff27e5cc45dd_1672106996&v=1.13.15&vptag=www_baidu_com%7Cchannel&ad_type=LD%7CKB%7CPVL&live=0&appversion=3.2.29&ty=web&adaptor=1&dtype=1&resp_type=json&s_img=webp"}
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
response = requests.post(url=url,json=data, headers=headers).json()
re_data = re.findall('"url":"(.*?)"',response['vinfo'])[6]
yy = requests.get(re_data).text
yy1 = re.sub('#E.*','',yy).split()
for ts in tqdm(yy1):
        tw = 'https://apd-688eca23afe933feb1e34644421b0cc6.v.smtcdns.com/vipts.tc.qq.com/A0AM4EKnvl9B2CcBrX84xdNrL28jyMC-QLM4YeXkdNtg/B_ftKo9qdgiwd-0Vdlq5utAQ/9I0N-IEz_efbwOPHmJBxJx0VO6zZuis1atDMC5etk_uHZYwIgaiYqL_kacD0H3R9K9bthV7vBKdBayLEdFLIvq1nhkLsa3GuqD3lLVWtVzIiyxfGUzGODAD82QgD7eZ1vBcUD5l222G6cas3ZKIxsQhw1lT5XbGOPrrQEjrZyp0/'+ts
        dd = requests.get(url=tw).content
        with open('猫和老鼠.mp4',mode='ab') as f:
             f.write(dd)