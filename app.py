from requests import get
from bs4 import BeautifulSoup
import urllib.request
import sys

truyen = []

def start():
	print('Nhập thể loại truyện (Không dấu):')
	search = str(input())
	url =  'https://truyenfull.vn/tim-kiem/?tukhoa='+search.replace(' ', '+')
	page = urllib.request.urlopen(url)
	soup = BeautifulSoup(page, 'html.parser')

	lists = soup.find('div', class_='list list-truyen col-xs-12').find_all('div', class_='row')
	if len(lists) == 0:
		print('Không có kết quả cho "'+search+'"')
		start()
	i = 0
	limit = 3
	for light_novel in lists:
		content = light_novel.find('div', class_='col-xs-2 text-info').find('a')
		title = content.get('title')
		link = content.get('href')
		print(str(i)+'. {}'.format(title))
		truyen.append(link)
		if i == limit:
			break
		i += 1

	print('Nhập số thứ tự truyện muốn xem, ví dụ: 0')
	ind = int(input())
	sendLightNovel(ind)

def sendLightNovel(id_t, chapter = 1):

	truyen_url = truyen[id_t]

	link = get(truyen_url+"/chuong-"+str(chapter)+"/")
	soup = BeautifulSoup(link.content, "html.parser")
	title = soup.find("a", class_="truyen-title").text
	body = soup.find("div", class_="chapter-c").text
	nextchap = soup.find('a', class_='btn btn-success btn-chapter-nav').attrs['title']

	print('Tiêu đề: '+title+' | Chap ' + str(chapter)+ '\n')
	print(body.replace('-', '\n-'))
	if nextchap != 'Không hoặc chưa có chương tiếp theo':
		print('Ấn "1" để tiếp tục đọc!, ấn "2" để dừng')
		hoi = int(input())
		if hoi == 1:
			seen(id_t, chapter+1)
		else:
			sys.exit()
	else:
		print('Không hoặc chưa có chương tiếp theo')

start()




