from time import sleep
from django.core.urlresolvers import reverse
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver
from blog.models import UserProfile


class SeleniumTests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(SeleniumTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(SeleniumTests, cls).tearDownClass()

    def test_admin_login(self):
        # Create a superuser
        # UserProfile.objects.create(name'superuser', 'superuser@test.com', 'mypassword')

        # let's open the admin login page
        self.selenium.get("{}{}".format(self.live_server_url, reverse('admin:index')))
        sleep(2)

        # let's fill out the form with our superuser's username and password
        username_input = self.selenium.find_element_by_id('id_username')
        sleep(2)

        password_input = self.selenium.find_element_by_id('id_password')
        sleep(1)

        username_input.send_keys('northdacoder')
        password_input.send_keys('hjalmar')
        # username_input.send_keys('n')
        # sleep(.5)
        # username_input.send_keys('o')
        # sleep(.5)
        # username_input.send_keys('r')
        # sleep(.5)
        # username_input.send_keys('t')
        # sleep(.5)
        # username_input.send_keys('h')
        # sleep(.5)
        # username_input.send_keys('d')
        # sleep(.5)
        # username_input.send_keys('a')
        # sleep(.5)
        # username_input.send_keys('c')
        # sleep(.5)
        # username_input.send_keys('o')
        # sleep(.5)
        # username_input.send_keys('d')
        # sleep(.5)
        # username_input.send_keys('e')
        # sleep(.5)
        # username_input.send_keys('r')
        # sleep(.5)
        #
        # password_input.send_keys('h')
        # sleep(.5)
        # password_input.send_keys('j')
        # sleep(.5)
        # password_input.send_keys('a')
        # sleep(.5)
        # password_input.send_keys('l')
        # sleep(.5)
        # password_input.send_keys('m')
        # sleep(.5)
        # password_input.send_keys('a')
        # sleep(.5)
        # password_input.send_keys('r')

        password_input.send_keys(Keys.RETURN)
        sleep(5)

        # password_input = self.selenium.find_element_by_id('id_password')
        # password_input.send_keys('mypassword')

        # Submit the form
        # password_input.send_keys(Keys.RETURN)