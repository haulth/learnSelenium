from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get('https://vnexpress.net/tin-tuc-24h')


def get_general_info():
    title_news = driver.find_elements(By.XPATH, '//*[@id="automation_TV0"]/div/article')
    #xóa data cũ trong file tin_tuc.txt
    with open('tin_tuc.txt', 'w', encoding='utf-8') as f:
        f.write('')


    for i in range(len(title_news)):
        title_new = title_news[i]
        time = title_new.text.split('\n')[0]
        title = title_new.text.split('\n')[1]
        #lấy link của thẻ a
        element_titles = title_new.find_element(By.XPATH, '//h3/a')
        link = element_titles.get_attribute('href')

        # save to file tin_tuc.txt title, time, link /n, ghi tiếp vào file không ghi đè
        with open('tin_tuc.txt', 'a', encoding='utf-8') as f:
            f.write(title + ',' + time + ',' + link + '\n')
    print('Số bài viết: ', len(title_news))
    print ('done get_general_info')
    return len(title_news)


def get_content(num_of_content_in_list):
    #lấy link từ file tin_tuc.txt với dòng cần lấy là num_of_content_in_list
    with open('tin_tuc.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
        link = lines[num_of_content_in_list].split(',')[2]
        driver.get(link)
        # lấy nội dung từ thẻ a
        elements = driver.find_elements(By.XPATH, '//*[@id="dark_theme"]/section[5]/div/div[2]/article')
        print('time: ' + lines[num_of_content_in_list].split(',')[1])
        print('title: ' + lines[num_of_content_in_list].split(',')[0])
        for element in elements:
            print('content: ', element.text)
        print ('done get_content')
def main():
    length=get_general_info()
    #yêu cầu nhập và kiểm tra số bài viết cần lấy
    quit = True
    while quit:
        print('Nhập -1 để thoát')
        print('Số thứ tự bài viết phải lớn hơn 0 và nhỏ hơn', length+1)
        num_of_content_in_list = int(input('Nhập số thứ tự bài viết cần lấy: '))
        if num_of_content_in_list > 0 and num_of_content_in_list <= length:
            get_content(num_of_content_in_list-1)
        elif num_of_content_in_list == -1:
            quit = False
        else:
            print('Số thứ tự bài viết không hợp lệ')
            print(length)
            

    driver.quit()
if __name__ == '__main__':
    main()