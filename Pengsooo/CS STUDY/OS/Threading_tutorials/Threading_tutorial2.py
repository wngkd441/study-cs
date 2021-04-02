## threading.Thread 로부터 파생된 class를 작성 ##

import threading, requests, time

# 파생된 class #
class HtmlGetter(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        resp = requests.get(self.url)  # request.get() : 해당 웹페이지의 호출 결과를 가진 Response 객체 리턴
        time.sleep(1)
        print(self.url, len(resp.text), ' chars')


t = HtmlGetter('http://google.com')
t.start()  # HtmlGetter 클래스에서 재정의된 run() 메서드 호출

print("### End ###")