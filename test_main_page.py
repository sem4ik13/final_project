from final_project.pages.login_page import LoginPage
from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
	link = "http://selenium1py.pythonanywhere.com/"
	page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
	page.open()
	login_page = page.go_to_login_page()
	login_page.should_be_login_page()