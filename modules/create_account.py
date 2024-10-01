import datetime
from enum import Enum

import xml.etree.ElementTree as ET

class FileLoadXML(Enum):
    NAME_FILE = 'SVAP_NORMAL_Thien_05092024_001_05.xml'
    PREFIX_VC_APPLICATION_NAME = 'APPLCORED'

class Product(Enum):
    TEST = '70000251'

class Account:
    def __init__(self):
        pass


    def create_account(self):
        self.__create_account()

    def __create_account(self):
        try:
            tree = ET.parse(FileLoadXML.NAME_FILE.value)

            previous_application_number = tree.getroot().find('application').find('application_number')
            previous_application_number.text = self.__create_application_number(previous_application_number.text)

            customer_number = tree.getroot().find('application').find('customer').find('customer_number')
            customer_number.text = self.__create_customer_number(customer_number.text)

            product_id = tree.getroot().find('application').find('customer').find('contract').find('product_id')
            product_id.text = self.__create_products()


            fee_fixed_value = (tree.getroot().find('application').find('customer').find('contract').find('service')
                               .find('service_object').find('attribute_fee').find('fee_fixed_value'))
            fee_fixed_value.text = self.__create_fee_fixed_value()

            cycle_start_date = (tree.getroot().find('application').find('customer').find('contract').find('service')
                                .find('service_object').find('attribute_cycle').find('cycle_start_date'))

            cycle_start_date.text = self.__create_cycle_start_date()

            shif_length = (tree.getroot().find('application').find('customer').find('contract').find('service')
                                .find('service_object').find('attribute_cycle').find('shif').find('shift_length'))

            shif_length.text = self.__create_shift_length()


            tree.write(FileLoadXML.NAME_FILE.value)
        except Exception as e:
            print(e)

    @staticmethod
    def __create_application_number(old_application_number: str) -> str:
        prefix = FileLoadXML.PREFIX_VC_APPLICATION_NAME.value
        random_number = prefix + str(int(old_application_number.split(prefix)[1]) + 1)
        return random_number

    @staticmethod
    def __create_customer_number(old_customer_number: str) -> str:
        return str(int(old_customer_number)+1)

    @staticmethod
    def __create_products() -> str:
        print('Enter your product ID')
        print('1. Product test: ' + Product.TEST.value)
        choice_product = input()
        if choice_product == '1':
            return Product.TEST.value
        else:
            return Product.TEST.value

    @staticmethod
    def __create_fee_fixed_value() -> str:
        try:
            user_input = int(input("Enter your fee fixed value: "))
            print("Your value:", user_input)
            return str(user_input)
        except ValueError:
            print("Invalid")

    @staticmethod
    def __create_cycle_start_date() -> str:
        today = datetime.date.today()
        return str(today)


    @staticmethod
    def __create_shift_length() -> str:
        try:
            user_input = int(input("Enter your shif lenght value: "))
            print("Your value:", user_input)
            return str(user_input)
        except ValueError:
            print("Invalid")
