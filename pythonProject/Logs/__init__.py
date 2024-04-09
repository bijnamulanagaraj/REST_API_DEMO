 terminal_xpath = "//a[@id='toplev1' and text()='Terminal']"
    summary_xpath = "//a[@top='toplev1' and text()='Summary']"
    summaryElements_xpath = "//*[@id='terminalSummary']/table//tr"


    def __init__(self, driver):
        self.driver = driver

    def summaryFindingElemets(self):
        summary_elements= self.driver.find_elements(By.XPATH,self.summary_Elements_xpath)
        return summary_elements