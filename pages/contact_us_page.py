from pages.base_page import BasePage


class ContactUs(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.name = page.get_by_placeholder("Name")
        self.email = page.get_by_placeholder("Email").first
        self.subject = page.get_by_placeholder("Subject")
        self.msg = page.get_by_placeholder("Your Message Here")
        self.attached_file = page.locator("input[name='upload_file']")
        self.submit = page.locator("input[name='submit']")

    def contract_us_form(self, name, email, subject, message, file_path):
        self.name.fill(name)
        self.email.fill(email)
        self.subject.fill(subject)
        self.msg.fill(message)
        self.attached_file.set_input_files(file_path)
        self.submit.click()
